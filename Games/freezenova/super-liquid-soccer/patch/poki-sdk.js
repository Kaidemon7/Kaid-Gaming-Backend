(function () {
  if (typeof window === 'undefined') return;
  function PokiSDK() {}
  PokiSDK.init = PokiSDK.setDebug = PokiSDK.setLogLevel = PokiSDK.gameLoadingStart =
  PokiSDK.gameLoadingFinished = PokiSDK.gameplayStart = PokiSDK.gameplayStop =
  PokiSDK.commercialBreak = PokiSDK.rewardedBreak = PokiSDK.displayAd = PokiSDK.catalog =
  PokiSDK.catalogItem = PokiSDK.isAdBlocked = PokiSDK.openDocument = PokiSDK.shareableURL =
  function () { return new Promise(function (res) { try { res(null); } catch (e) {} }); };
  PokiSDK.getURLParam = function () { return null; };
  window.PokiSDK = PokiSDK;
  window.Poki = PokiSDK;
})();
