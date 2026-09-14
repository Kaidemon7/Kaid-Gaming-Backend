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
  window.GMSOFT_SDKTYPE = 'gm';
  window.GMSOFT_SIGNED = '';
  window.GMSOFT_GAME_INFO = {};
  window.gamemonetize = window.GameMonetize = make();
  window.PokiSDK = window.Poki = make();
  window.googletag = window.googletag || { cmd: [], pubads: function () { return { refresh: function(){}, defineSlot: function(){ return {}; }, enableServices: function(){}, addService: function(){} }; } };
  try {
    window.dispatchEvent(new CustomEvent('gmsoftSdkReady', {}));
    window.dispatchEvent(new CustomEvent('gmadsSdkReady', {}));
  } catch (e) {}
})();
