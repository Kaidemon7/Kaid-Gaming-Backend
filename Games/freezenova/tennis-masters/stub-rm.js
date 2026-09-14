(function () {
  if (typeof window === 'undefined') return;
  function make() {
    var f = function () {
      var a = arguments;
      if (typeof a[a.length - 1] === 'function') { setTimeout(function () { try { a[a.length - 1](); } catch (e) {} }, 1); }
      return f;
    };
    f.then = function (ok, bad) { if (typeof ok === 'function') { setTimeout(function () { try { ok({}); } catch (e) {} }, 1); } return f; };
    f['catch'] = function (bad) { if (typeof bad === 'function') { setTimeout(function () { try { bad({}); } catch (e) {} }, 1); } return f; };
    f['finally'] = function (cb) { if (typeof cb === 'function') { setTimeout(function () { try { cb(); } catch (e) {} }, 1); } return f; };
    return new Proxy(f, {
      get: function (t, prop, r) { if (typeof prop === 'symbol') return undefined; if (prop in t) return t[prop]; return f; },
      set: function () { return true; },
      apply: function () { return f; }
    });
  }
  window.GMGameSDK = make();
  window.GameMonetize = window.gamemonetize = make();
  window.mgAds = window.AdInPlay = window.AdBreak = window.adBreak = make();
  try {
    var el = document.getElementById && document.getElementById('content');
    var evt = function (name) {
      var e;
      try { e = new Event(name); } catch (x) { e = document.createEvent('Event'); e.initEvent(name, true, true); }
      var t = el || document.body || document;
      t.dispatchEvent(e);
    };
    evt('SDK_READY');
    evt('SDK_GAME_START');
  } catch (e) {}
})();
