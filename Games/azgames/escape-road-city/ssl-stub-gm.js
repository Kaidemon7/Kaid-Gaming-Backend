(function () {
  if (typeof window === 'undefined') return;
  var noop = function () { return window.GMGameSDK || noop; };
  var sdk = {
    init: noop, setVersion: noop, trackEvent: noop, trackEventParams: noop,
    gameReady: noop, gameplayStart: noop, gameplayStop: noop, showRewarded: noop,
    showInterstitial: noop, preloadAd: noop, hideAds: noop, showAds: noop,
    oauthComplete: noop, logoutComplete: noop, on: noop, off: noop
  };
  window.GMGameSDK = sdk;
  window.GMSOFT_SDKTYPE = 'gm';
})();
