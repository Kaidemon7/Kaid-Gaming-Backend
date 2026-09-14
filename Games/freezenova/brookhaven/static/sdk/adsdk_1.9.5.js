<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,minimum-scale=1,initial-scale=1"><link rel="shortcut icon" href=https://static.hippoobox.com/h5web/static/assets/LOGO-256.png><meta name=copyright content=www.hippoobox.com><meta name=theme-color content=#FF6422><meta name=keywords content="html5 games,online html5 games,mobile games,free mobile games,free online games,hippoo games,best online games"><meta name=description content="hippoo games, Play the Best free online games! We have the best online games website, free html5 games, html5 games, and much more... Choose a game to play for free and have fun with us now!"><meta property=og:type content=website><meta property=og:image content=http://www.hippoobox.com/static/assets/logo-push.png itemprop=image><meta property=og:title content="Ready For Some Gaming Adventure?"><meta property=og:url content=http://www.hippoobox.com><meta property=og:site_name content="hippoo games"><meta property=og:description content="Play the most addictive games on Hippoo Games center."><meta name=twitter:card content=games><meta name=twitter:title content="Ready For Some Gaming Adventure? "><meta name=twitter:description content="Play the most addictive games on Hippoo Games center."><meta property=fb:app_id content=278397626105459><meta name=google-signin-client_id content=580151408688-7e9mg6epdncegksd0na3uljb08ok0u8t.apps.googleusercontent.com><link rel=manifest href=./manifest.json><title>Hippoo Games</title><link href=/static/css/app.4a3fb57b5e9ecf5aea0b8da3a980afc7.css rel=stylesheet></head><body><div id=app></div><noscript><h1>Hippoo Games</h1>this is a website for:<br>html5 games,online html5 games,mobile games,free mobile games,free online games,hippoogames,best online games<br>hippoogames, Play the Best free online games! We have the best online games website, free html5 games, html5 games, and much more... Choose a game to play for free and have fun with us now!<br><hr><em><strong>You should start javascript to function properly !!!</strong></em></noscript><script type=text/javascript src=/static/js/manifest.42e5a14fb139cc9931a2.js></script><script type=text/javascript src=/static/js/vendor.cd4a21d19fa33318a5ec.js></script><script type=text/javascript src=/static/js/app.369817249fb8a0c64284.js></script></body><script>if (location.hash !== "#nopv") {
      window.fbAsyncInit = function() {
        FB.init({
          appId: "278397626105459",
          autoLogAppEvents: true,
          cookie: true,
          xfbml: false,
          version: "v3.1"
        });
      };
      // 针对aha登录的问题的临时方案
      window.ahaToken = "";
      function setAhaLoginToken(token) {
        window.ahaToken = token;
        localStorage.setItem("ahaToken", token);
        var eObj = {
          t: token
        };
        window.fireCustomEvent("ahaLogin", eObj);
      }
      function fireCustomEvent(name, eventObj) {
        var cusEvent = new CustomEvent(name, {
          detail: eventObj
        });
        if (window.dispatchEvent) {
          window.dispatchEvent(cusEvent);
        } else {
          window.fireEvent(cusEvent);
        }
      }
      function addAsyncScript(src, id) {
        var fjs = document.getElementsByTagName("script")[0];
        var js = document.createElement("script");
        if (id) {
          if (document.getElementById(id)) {
            return;
          }
          js.id = id;
        }
        js.async = true;
        js.src = src;
        fjs.parentNode.insertBefore(js, fjs);
      }
      // addAsyncScript(
      //   "//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"
      // );
      // addAsyncScript("https://tads.mobadvent.com/tsax.js");
      addAsyncScript("//www.googletagmanager.com/gtag/js?id=" + window.GAId);
      addAsyncScript("//apis.google.com/js/api:client.js");
      // addAsyncScript("https://connect.facebook.net/en_US/fbadnw60-tag.js");
      addAsyncScript("//static.ssp.transsion.com/webapi/sp.js");

      window.dataLayer = window.dataLayer || [];
      var dataLayer = window.dataLayer;

      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", window.GAId);

      // mockAjax()
      /* test gtag 跨网域 2019/5/8 SZ */
    }
    // (function(w,d, s, id) {w.webpushr=w.webpushr||function(){(w.webpushr.q=w.webpushr.q||[]).push(arguments)};var js, fjs = d.getElementsByTagName(s)[0];js = d.createElement(s); js.id = id;js.src = "https://cdn.webpushr.com/app.min.js";fjs.parentNode.appendChild(js);}(window,document, 'script', 'webpushr-jssdk'));webpushr('init',window.PushId);  // 2020-02-10暂时去掉webpushr功能</script><script>if (
      window.location.host !== "www.hippoobox.com" &&
      window.location.host !== "ind-www.hippoobox.com"
    ) {
      window.da_setting = {
        env: "test"
      };
    }</script></html>