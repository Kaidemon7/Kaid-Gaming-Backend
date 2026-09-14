/*!
 * Unity 6 WebGL — Audio/Focus Guard with Google IMA hooks (v4)
 * - Hooks WebAudio + HTMLMedia
 * - Listens for Google IMA ad lifecycle if present (CONTENT_PAUSE/RESUME)
 * - Detects ad containers (google_sdk_container / google-ima / adsbygoogle iframes) as fallback
 * - Notifies Unity ServerManager.JS_SetFocus("true"/"false")
 * Place BEFORE Build/<name>.loader.js
 */
(function () {
  // -------------------- Track AudioContexts (Unity + any created later) --------------------
  const trackedContexts = new Set();
  function wrapCtor(name) {
    const Native = self[name];
    if (typeof Native !== "function") return;
    function Patched(...args) { const ctx = new Native(...args); try { trackedContexts.add(ctx); } catch {} return ctx; }
    Object.defineProperty(Patched, "name", { value: name });
    Patched.prototype = Native.prototype;
    for (const k of Object.getOwnPropertyNames(Native)) {
      if (!(k in Patched)) { try { Object.defineProperty(Patched, k, Object.getOwnPropertyDescriptor(Native, k)); } catch {} }
    }
    self[name] = Patched;
  }
  wrapCtor("AudioContext"); wrapCtor("webkitAudioContext");

  // -------------------- Track <audio>/<video> too --------------------
  const mediaEls = new Set();
  function collectMedia() { document.querySelectorAll("audio,video").forEach(el => mediaEls.add(el)); }
  new MutationObserver(muts => {
    for (const m of muts) for (const n of m.addedNodes || []) {
      if (n && n.nodeType === 1) {
        if (n.matches && n.matches("audio,video")) mediaEls.add(n);
        n.querySelectorAll && n.querySelectorAll("audio,video").forEach(el => mediaEls.add(el));
      }
    }
  }).observe(document.documentElement, { childList: true, subtree: true });

  // -------------------- Suspend / Resume helpers --------------------
  let suspendedByGuard = false;
  async function suspendAll() {
    let touched = false;
    for (const ctx of trackedContexts) {
      try { if (ctx && (ctx.state === "running" || ctx.state === "interrupted")) { await ctx.suspend(); touched = true; } } catch {}
    }
    for (const el of mediaEls) {
      try {
        if (!el.paused) el.pause();
        el.__bg_prevMuted = el.muted; el.__bg_prevVol = el.volume;
        el.muted = true; el.volume = 0; touched = true;
      } catch {}
    }
    suspendedByGuard = touched;
  }
  async function resumeAll() {
    for (const ctx of trackedContexts) { try { if (ctx && ctx.state === "suspended") await ctx.resume(); } catch {} }
    for (const el of mediaEls) {
      try {
        if (typeof el.__bg_prevMuted === "boolean") el.muted = el.__bg_prevMuted;
        if (typeof el.__bg_prevVol === "number") el.volume = el.__bg_prevVol;
      } catch {}
    }
  }

  // -------------------- Unity bridge to ServerManager --------------------
  function notifyFocus(hasFocus) {
    if (self.unityInstance && self.unityInstance.SendMessage) {
      try { self.unityInstance.SendMessage("ServerManager", "JS_SetFocus", hasFocus ? "true" : "false"); } catch {}
    }
  }
  // capture unityInstance ASAP
  const originalCreate = self.createUnityInstance;
  if (typeof originalCreate === "function") {
    self.createUnityInstance = function(canvas, config) {
      return originalCreate(canvas, config).then(inst => { self.unityInstance = inst; return inst; });
    };
  }

  // -------------------- Ad-awareness (Google IMA + DOM fallback) --------------------
  let adActive = false;

  async function enterAd() {
    if (adActive) return;
    adActive = true;
    await suspendAll();
    notifyFocus(false); // -> OnApplicationFocus(false)
  }
  async function exitAd() {
    adActive = false;
    // Only resume if page is visible (e.g., user didn’t lock screen during ad)
    if (document.visibilityState === "visible") {
      if (suspendedByGuard) { await resumeAll(); suspendedByGuard = false; }
      notifyFocus(true);  // -> OnApplicationFocus(true)
    }
  }

  // Hook IMA if available: CONTENT_PAUSE_REQUESTED & CONTENT_RESUME_REQUESTED cover pre/mid/post-rolls
  function hookIMA() {
    if (!self.google || !google.ima) return false;
    try {
      const AdsLoaderProto = google.ima.AdsLoader && google.ima.AdsLoader.prototype;
      if (!AdsLoaderProto || AdsLoaderProto.__bg_hooked) return !!AdsLoaderProto;

      const origAddEvent = EventTarget.prototype.addEventListener;
      // We’ll hook AdsManager instances when they’re created
      const origGetAdsManager = google.ima.AdsManagerLoadedEvent && google.ima.AdsManagerLoadedEvent.prototype.getAdsManager;

      if (origGetAdsManager && !google.ima.AdsManagerLoadedEvent.prototype.__bg_wrapped) {
        google.ima.AdsManagerLoadedEvent.prototype.__bg_wrapped = true;
        google.ima.AdsManagerLoadedEvent.prototype.getAdsManager = function () {
          const mgr = origGetAdsManager.apply(this, arguments);
          try {
            mgr.addEventListener(google.ima.AdEvent.Type.CONTENT_PAUSE_REQUESTED, enterAd);
            mgr.addEventListener(google.ima.AdEvent.Type.STARTED, enterAd);
            mgr.addEventListener(google.ima.AdEvent.Type.PAUSED, enterAd);
            mgr.addEventListener(google.ima.AdEvent.Type.RESUMED, () => { /* still ad */ });
            mgr.addEventListener(google.ima.AdEvent.Type.CONTENT_RESUME_REQUESTED, exitAd);
            mgr.addEventListener(google.ima.AdEvent.Type.ALL_ADS_COMPLETED, exitAd);
            mgr.addEventListener(google.ima.AdEvent.Type.COMPLETE, exitAd);
            mgr.addEventListener(google.ima.AdEvent.Type.SKIPPED, exitAd);
            mgr.addEventListener(google.ima.AdEvent.Type.AD_ERROR, exitAd);
          } catch {}
          return mgr;
        };
      }

      AdsLoaderProto.__bg_hooked = true;
      return true;
    } catch { return false; }
  }

  // Fallback detection: DOM containers used by IMA/AdSense
  function isAdDomPresent() {
    // Common IMA container ids/classes + google iframes
    const maybe = document.querySelector(
      '#google_sdk_container, .google-ima, .ima-container, .ima-ad-container, iframe[src*="doubleclick"], iframe[src*="google"], .adsbygoogle'
    );
    if (!maybe) return false;
    // Check visibility quickly
    const el = maybe;
    const visible = !!(el.offsetParent || (el.getClientRects && el.getClientRects().length));
    return visible;
  }

  // Observe DOM for ad-insertion/removal
  const adObserver = new MutationObserver(() => {
    if (isAdDomPresent()) enterAd();
    else if (adActive) exitAd();
  });

  // -------------------- Background / Foreground (screen lock/app switch) --------------------
  async function toBackground() { collectMedia(); await suspendAll(); notifyFocus(false); }
  async function toForeground() {
    if (adActive) { /* still in ad, do not resume yet */ return; }
    if (suspendedByGuard) { await resumeAll(); suspendedByGuard = false; }
    notifyFocus(true);
  }

  function onVisibility() { (document.visibilityState === "hidden") ? toBackground() : toForeground(); }
  function onPageHide() { toBackground(); }
  function onPageShow() { toForeground(); }
  function onFreeze()   { toBackground(); }

  // -------------------- Init --------------------
  function init() {
    collectMedia();
    // lifecycle
    document.addEventListener("visibilitychange", onVisibility, { passive: true });
    addEventListener("pagehide", onPageHide, { passive: true });
    addEventListener("pageshow", onPageShow, { passive: true });
    document.addEventListener("freeze", onFreeze, { passive: true });

    // IMA hooks (retry a bit in case IMA loads late)
    let tries = 0;
    const t = setInterval(() => { tries++; const ok = hookIMA(); if (ok || tries > 40) clearInterval(t); }, 125);

    // DOM ad detection
    adObserver.observe(document.documentElement, { childList: true, subtree: true, attributes: true });

    // If page is already hidden (e.g., opened in background)
    if (document.visibilityState === "hidden") toBackground();

    // Debug
    self.UnityAudioBackgroundGuard = {
      getContexts: () => Array.from(trackedContexts),
      suspend: toBackground, resume: toForeground,
      _adActive: () => adActive
    };
  }

  if (document.readyState === "complete" || document.readyState === "interactive") init();
  else document.addEventListener("DOMContentLoaded", init, { once: true });
})();
