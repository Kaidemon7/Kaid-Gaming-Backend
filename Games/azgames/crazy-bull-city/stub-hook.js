(function () {
  try {
    var hosts = /(azgame\.io|api\.azgames\.io|cdnwave\.com|gamemonetize\.com|imasdk\.googleapis\.com|stpd\.cloud|pagead2\.googlesyndication\.com|securepubads\.g\.doubleclick\.net|adsterra\.com|wgplayer\.com|adplay\.tv|trendgames\.io|ghcatcher\.com|shaperush\.io|silvergames\.com|coolmathgames\.com|gamesnacks\.com|lagged\.com|readyplayer1\.xyz|game-cdn\.poki\.com|poki\.com|gamedistribution\.com|dtsaf\.com|withdesk\.com|pushnami\.com|popads\.net|propellerads\.com|onclckdn\.com|alphagames\.com)/i;
    var stubFile = 'stub-rm.js';
    var stopper = function (url) {
      if (!url || typeof url !== 'string') return url;
      if (hosts.test(url)) return stubFile;
      return url;
    };
    var des = document.createElement;
    document.createElement = function (tag) {
      var el = des.call(document, tag);
      if (String(tag).toLowerCase() === 'script') {
        try {
          Object.defineProperty(el, 'src', {
            get: function () { return el.getAttribute('src'); },
            set: function (v) { el.setAttribute('src', stopper(v)); },
            configurable: true
          });
        } catch (e) {}
      }
      return el;
    };
    try {
      var desc = Object.getOwnPropertyDescriptor(HTMLScriptElement.prototype, 'src');
      var origViaSet = desc && desc.set;
      Object.defineProperty(HTMLScriptElement.prototype, 'src', {
        configurable: true,
        get: function () { return this.getAttribute('src'); },
        set: function (v) {
          var nv = stopper(v);
          if (nv === stubFile) {
            this.setAttribute('src', nv);
            this.setAttribute('data-adstub', '1');
          } else if (origViaSet) { origViaSet.call(this, v); } else { this.setAttribute('src', v); }
        }
      });
    } catch (e) {}
    var fetch0 = window.fetch;
    if (typeof fetch0 === 'function') {
      window.fetch = function () {
        var u = arguments[0];
        var s = (u && u.url) ? u.url : String(u);
        if (hosts.test(s)) return Promise.resolve(new Response('', { status: 200, statusText: 'OK' }));
        return fetch0.apply(this, arguments);
      };
    }
    var XHRopen = XMLHttpRequest.prototype.open;
    var XHRsend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.open = function (m, u) {
      u = typeof u === 'string' ? u : String(u);
      if (hosts.test(u)) { this._adstubbed = true; }
      return XHRopen.apply(this, arguments);
    };
    XMLHttpRequest.prototype.send = function () {
      var self = this;
      if (this._adstubbed) {
        try {
          Object.defineProperty(self, 'readyState', { configurable: true, get: function () { return 4; } });
          Object.defineProperty(self, 'status', { configurable: true, get: function () { return 200; } });
          Object.defineProperty(self, 'responseText', { configurable: true, get: function () { return ''; } });
          if (typeof self.response === 'undefined') Object.defineProperty(self, 'response', { configurable: true, get: function () { return ''; } });
          var ev = function (t) { try { self.dispatchEvent(new Event(t)); } catch (e) {} };
          ev('readystatechange'); ev('load'); ev('loadend');
          if (typeof self.onload === 'function') { try { self.onload(); } catch (e) {} }
          if (typeof self.onreadystatechange === 'function') { try { self.onreadystatechange(); } catch (e) {} }
        } catch (e) {}
        return;
      }
      return XHRsend.apply(this, arguments);
    };
  } catch (e) {}
})();
