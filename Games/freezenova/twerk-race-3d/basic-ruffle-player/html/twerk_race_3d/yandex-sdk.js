(function () {
  if (typeof window === 'undefined') return;
  window.YaGames = { init: function () { return Promise.resolve({ features: { LoadingAPI: { ready: function(){}, setProgress: function(){}, hideLoading: function(){} }, GameplayAPI: { start: function(){}, stop: function(){} }, Advert: { show: function(){ return Promise.resolve(); }, showFullscreenAdv: function(){ return Promise.resolve(); }, showRewardedVideo: function(){ return Promise.resolve(false); } } } }); } };
  window.YaGamesInit = function() {};
})();
