/**
 * Ducky Game API SDK
 * Include this script in your game to communicate with the Ducky parent window.
 *
 * Usage:
 *   <script src="ducky.js"></script>
 *   <script>
 *     const user = await DuckyAPI.getUser();
 *     const balance = await DuckyAPI.getBalance();
 *     const items = await DuckyAPI.getItems();
 *     const result = await DuckyAPI.spendDaboons(50, 'power_up');
 *     const time   = await DuckyAPI.getServerTime();
 *     // → { success: true, data: { ms: <unix epoch ms>, iso: '2026-04-25T...' } }
 *   </script>
 */
const DuckyAPI = {
  _pending: new Map(),
  _timeout: 5000,

  // Read the routing id the parent injected into this iframe. The parent
  // sets it two ways depending on its render mode:
  //   • direct iframe (src is a full game URL)  → appended as `?i=<id>`
  //   • about:blank + document.write             → injected as `<meta name="i">`
  // We read whichever is populated, cache it, and echo it on every
  // postMessage. If neither is present (older parent shell), `_i` stays
  // empty — messages omit the field, and the parent falls back to its
  // legacy "process every message" path so older deployments keep working.
  _readI() {
    try {
      if (typeof document !== "undefined") {
        const m = document.querySelector('meta[name="i"]');
        if (m) {
          const v = m.getAttribute("content");
          if (v) return v;
        }
      }
      if (typeof location !== "undefined" && location.search) {
        const v = new URLSearchParams(location.search).get("i");
        if (v) return v;
      }
    } catch (e) { /* document/location unavailable — fall through */ }
    return "";
  },
  get _i() {
    if (this._iCache == null) this._iCache = this._readI();
    return this._iCache;
  },
  _iCache: null,

  // Per-action token bucket. 60 calls/min sustained, burst of 10.
  // Separate buckets per action so e.g. rapid save_progress can't starve get_user.
  // Refill rate = _rateLimit.perMin / 60 tokens per second.
  //   maxWaitMs: any call that would have to wait longer than this rejects
  //   immediately — bounds the queue depth (~30 queued per action at 1/sec).
  _rateLimit: { perMin: 60, burst: 10, maxWaitMs: 30000 },
  // Per-action overrides, applied on top of _rateLimit. Used for actions
  // that should be much stricter than the default — anti-cheat hooks,
  // expensive backend calls, etc.
  _actionRateLimit: {
    // Daily-claim anti-cheat: only used to figure out the calendar day,
    // so 1 network fetch per HOUR is plenty (SDK getServerTime cache
    // serves anything faster). 1/60 per minute = 1 per hour, burst 1.
    // maxWaitMs:0 means bypass attempts (e.g. clearing the cache from
    // devtools) get rejected immediately rather than queuing.
    'get_server_time': { perMin: 1/60, burst: 1, maxWaitMs: 0 },
  },
  _buckets: new Map(),

  _takeToken(action) {
    const cfg   = (this._actionRateLimit && this._actionRateLimit[action]) || this._rateLimit;
    const now   = Date.now();
    const rate  = cfg.perMin / 60; // tokens/sec
    const burst = cfg.burst;
    let b = this._buckets.get(action);
    if (!b) { b = { tokens: burst, last: now }; this._buckets.set(action, b); }
    b.tokens = Math.min(burst, b.tokens + ((now - b.last) / 1000) * rate);
    b.last = now;
    if (b.tokens >= 1) { b.tokens -= 1; return 0; }
    const waitMs = Math.ceil(((1 - b.tokens) / rate) * 1000);
    if (waitMs > cfg.maxWaitMs) return -1; // queue full — don't consume a token
    b.tokens -= 1; // may go negative; queued callers wait proportionally longer
    return waitMs;
  },

  async _send(action, payload) {
    const waitMs = this._takeToken(action);
    if (waitMs < 0) {
      throw new Error("Ducky API rate-limit queue full for action: " + action);
    }
    if (waitMs > 0) {
      await new Promise(r => setTimeout(r, waitMs));
    }
    return new Promise((resolve, reject) => {
      const requestId = crypto.randomUUID();
      const timeout = setTimeout(() => {
        this._pending.delete(requestId);
        reject(new Error("Ducky API timeout - is the game running inside Ducky?"));
      }, this._timeout);
      this._pending.set(requestId, { resolve, timeout });
      // `i` echoes the routing id the parent injected (see _readI).
      // Empty string means no id was injected — the parent's handler
      // treats `i: ""` the same as missing and falls back to its legacy
      // routing, so old shells keep working.
      const msg = { type: "DUCKY_API_REQUEST", requestId, action, payload };
      const i = this._i;
      if (i) msg.i = i;
      (window.top || window.parent).postMessage(msg, "*");
    });
  },

  _handleResponse(event) {
    if (event.data?.type !== "DUCKY_API_RESPONSE") return;
    const pending = DuckyAPI._pending.get(event.data.requestId);
    if (!pending) return;
    clearTimeout(pending.timeout);
    DuckyAPI._pending.delete(event.data.requestId);
    pending.resolve(event.data);
  },

  getUser()    { return this._send("get_user"); },
  getBalance() { return this._send("get_balance"); },
  getItems()   { return this._send("get_items"); },

  // Authoritative wall-clock time from the Ducky backend (e.g. Supabase
  // `now()`). Use this instead of `Date.now()` for anything a client could
  // exploit by changing the OS clock — daily-claim windows, cooldowns,
  // anti-rate-limit checks. Expected response:
  //   { success: true, data: { ms: <epoch ms>, iso: <ISO 8601 string> } }
  //
  // Cached for _timeCacheTtlMs (1 hour by default — this is only used for
  // calendar-day checks, so hour-level drift is fine). On cache hit we
  // extrapolate the current ms by adding the monotonic performance.now()
  // delta since the anchor; performance.now() is immune to OS clock
  // changes, so the cached value can't be exploited by jumping the system
  // clock forward between calls. The per-action rate limit above (1/hour)
  // is a defense-in-depth backstop for cache-bypass attempts.
  _timeCache: { mono: 0, ms: 0 },
  _timeCacheTtlMs: 60 * 60 * 1000,   // 1 hour
  async getServerTime() {
    const nowMono = performance.now();
    const c = this._timeCache;
    if (c.ms && (nowMono - c.mono) < this._timeCacheTtlMs) {
      const ms = c.ms + (nowMono - c.mono);
      return { success: true, cached: true, data: { ms, iso: new Date(ms).toISOString() } };
    }
    const res = await this._send("get_server_time");
    if (res && res.success && res.data && typeof res.data.ms === 'number') {
      c.mono = nowMono;
      c.ms   = res.data.ms;
    }
    return res;
  },

  spendDaboons(amount, reason) {
    return this._send("spend_daboons", { amount, reason });
  },
  spendDabloons(amount, reason) {
    return this._send("spend_dabloons", { amount, reason });
  },

  saveProgress(data) {
    return this._send("save_progress", { json: JSON.stringify(data) });
  },

  getProgress() {
    return this._send("get_progress");
  },

  mergeProgress(local, cloud) {
    if (!cloud) return { ...local };
    const merged = { ...local };
    for (const key in cloud) {
      if (typeof cloud[key] === "number" && typeof merged[key] === "number") {
        merged[key] = Math.max(merged[key], cloud[key]);
      } else if (Array.isArray(cloud[key]) && Array.isArray(merged[key])) {
        merged[key] = [...new Set([...merged[key], ...cloud[key]])];
      }
    }
    return merged;
  },
};

window.addEventListener("message", (e) => DuckyAPI._handleResponse(e));
