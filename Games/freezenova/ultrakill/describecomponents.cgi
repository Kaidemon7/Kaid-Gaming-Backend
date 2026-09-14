<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
<meta property="og:type" content="website">
<meta property="og:title" content="
  Components for Firefox">

    

    <meta name="viewport"
          content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="color-scheme" content="dark light">
    <meta name="generator" content=" 20260908.1">
    <meta name="bugzilla-global" content="dummy"
        id="bugzilla-global" data-bugzilla="{&quot;api_token&quot;:&quot;&quot;,&quot;config&quot;:{&quot;basepath&quot;:&quot;\/&quot;,&quot;cookie_consent_enabled&quot;:true,&quot;cookie_consent_required&quot;:false,&quot;essential_cookies&quot;:[&quot;bugzilla&quot;,&quot;Bugzilla_login&quot;,&quot;Bugzilla_logincookie&quot;,&quot;Bugzilla_login_request_cookie&quot;,&quot;github_state&quot;,&quot;github_token&quot;,&quot;mfa_verification_token&quot;,&quot;moz-consent-pref&quot;,&quot;sudo&quot;],&quot;urlbase&quot;:&quot;https:\/\/bugzilla.mozilla.org\/&quot;},&quot;constant&quot;:{&quot;CGI_URI_LIMIT&quot;:8000,&quot;COMMENT_COLS&quot;:80},&quot;param&quot;:{&quot;allow_attachment_display&quot;:true,&quot;maxattachmentsize&quot;:&quot;10240&quot;,&quot;maxusermatches&quot;:&quot;50&quot;,&quot;splinter_base&quot;:&quot;\/page.cgi?id=splinter.html&amp;ignore=\/&quot;,&quot;use_markdown&quot;:true},&quot;string&quot;:{&quot;bug&quot;:&quot;&quot;,&quot;bug_type_required&quot;:&quot;You must select a Type for this &quot;,&quot;component_required&quot;:&quot;You must select a Component for this &quot;,&quot;description_required&quot;:&quot;You must enter a Description for this &quot;,&quot;short_desc_required&quot;:&quot;You must enter a Summary for this &quot;,&quot;version_required&quot;:&quot;You must select a Version for this &quot;},&quot;user&quot;:{&quot;cookie_consent&quot;:&quot;&quot;,&quot;is_new&quot;:true,&quot;login&quot;:&quot;&quot;}}">
    <meta name="google-site-verification" content="JYXIuR9cAlV7fLmglSrc_4UaJS6Wzh5Mdxiorqu5AQc" />
    <title>
  Components for Firefox</title>

<link rel="Top" href="/">

<link href="/static/v20260908.1/skins/standard/global.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/describecomponents.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-structure-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-theme-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/lib/prism.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/consent.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/Review/web/styles/badge.css" rel="stylesheet" type="text/css">



    
<script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/jquery/jquery-min.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/jquery/ui/jquery-ui-min.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/jquery/plugins/devbridgeAutocomplete/devbridgeAutocomplete-min.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/global.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/util.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/widgets.js"></script>

      <script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD">BUGZILLA.value_descs = JSON.parse('{\"bug_status\":{},\"resolution\":{\"\":\"---\"}}');

      </script>
<script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/extensions/ComponentWatching/web/js/overlay.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/lib/prism.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/consent.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/cookie-helper.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/js/lib/md5.min.js"></script><script nonce="GIvvAiAsYi7rTux9m8IjKIYqYmWoUh3lJGC57jig19aHBzHD" src="/static/v20260908.1/extensions/Review/web/js/badge.js"></script>

    

    
    <link href="/static/v20260908.1/skins/lib/fontawesome.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-brands.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-solid.min.css" rel="stylesheet" type="text/css">

    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla@Mozilla" href="/search_plugin.cgi"><link rel="shortcut icon" href="/extensions/BMO/web/images/favicon.ico">
<link rel="icon" type="image/svg+xml" href="/extensions/BMO/web/images/favicon.svg"><meta name="robots" content="noarchive">
  </head>



  <body
        class="bugzilla-mozilla-org
               skin-standard">



<div id="wrapper">

<header id="header" role="banner" aria-label="Global Header">
  <div class="inner" role="none">
    <button type="button" class="iconic ghost" id="open-menu-drawer" aria-label="Open Site Menu">
      <span class="icon" aria-hidden="true" data-icon="menu"></span>
    </button><div id="header-external-links" class="dropdown" role="none">
  <button type="button" id="header-external-menu-button" class="dropdown-button minor"
          aria-label="Show Mozilla Menu" aria-expanded="false" aria-haspopup="true"
          aria-controls="header-external-menu">
    <img src="/static/v20260908.1/extensions/BMO/web/images/moz-fav-one-color-white-rgb.svg"
         width="32" height="32" alt="">
  </button>
  <ul class="dropdown-content right" id="header-external-menu" role="menu" aria-label="Mozilla Menu"
      style="display:none;">
    <li role="none">
      <a href="https://www.mozilla.org/" role="menuitem">
        <span class="label" role="none">Mozilla Home</span>
      </a>
    </li>
    <li role="separator"></li>
    <li role="none">
      <a href="https://www.mozilla.org/privacy/websites/" role="menuitem">
        <span class="label" role="none">Privacy</span>
      </a>
    </li>
    <li role="none">
      <a href="https://www.mozilla.org/privacy/websites/#cookies" role="menuitem">
        <span class="label" role="none">Cookies</span>
      </a>
    </li>
    <li role="none">
      <a href="https://www.mozilla.org/about/legal/" role="menuitem">
        <span class="label" role="none">Legal</span>
      </a>
    </li>
  </ul>
</div>
    <h1 id="header-title" class="title" role="none">
      <a class="header-button" href="https://bugzilla.mozilla.org/home" title="Go to home page">
        <span aria-label="Go to Bugzilla Home Page">Bugzilla</span>
      </a>
    </h1>
    <form id="header-search" class="quicksearch" action="/buglist.cgi"
          data-no-csrf role="search" aria-label="Search Bugs">
      <button type="button" class="iconic ghost" id="show-searchbox"
              aria-label="Search Bugs">
        <span class="icon" aria-hidden="true" data-icon="search"></span>
      </button>
      <div class="searchbox-outer dropdown" role="combobox" aria-label="Quick Search"
           aria-haspopup="listbox" aria-owns="header-search-dropdown" aria-expanded="false">
        <span class="icon" aria-hidden="true" data-icon="search"></span>
        <input id="quicksearch_top" class="dropdown-button" name="quicksearch" autocomplete="off"
               value="" accesskey="s"
               placeholder="Search Bugs"
               title="Enter a bug number or some search terms"
               role="searchbox" aria-controls="header-search-dropdown" aria-label="Search Terms"><div id="header-search-dropdown" class="dropdown-content dropdown-panel right" role="listbox"
     style="display: none;">
  <div id="header-search-dropdown-wrapper" role="none">
    <section id="header-search-dropdown-help" role="group" aria-label="Help">
      <footer role="none">
        <a href="/page.cgi?id=quicksearch.html">Quick Search Tips</a>
        <a href="/query.cgi?format=advanced">Advanced Search</a>
      </footer>
    </section>
  </div>
</div>
      </div>
    </form>
    <nav id="header-nav" role="menubar" aria-label="Site Links">
      <ul class="links" role="none"><li role="none">
    <a class="header-button" href="/describecomponents.cgi"
       title="Browse bugs by component" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="category"></span>
      <span class="label" role="none">Browse</span>
    </a>
  </li>
  <li role="none">
    <a class="header-button" href="/query.cgi?format=advanced"
       title="Search bugs using various criteria" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="pageview"></span>
      <span class="label" role="none">Advanced Search</span>
    </a>
  </li>
  <li role="none">
    <a class="header-button" href="/enter_bug.cgi"
       title="File a new bug" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="add_box"></span>
      <span class="label" role="none">New Bug</span>
    </a>
  </li>
      </ul>
      <div class="dropdown" role="none">
        <button type="button" id="header-tools-menu-button"
                class="header-button dropdown-button minor" title="More tools…"
                role="menuitem" aria-label="Show More Tools Menu" aria-expanded="false"
                aria-haspopup="true" aria-controls="header-tools-menu">
          <span class="icon" aria-hidden="true" data-icon="more_horiz"></span>
        </button>
        <ul class="dropdown-content left" id="header-tools-menu" role="menu"
            aria-label="More Tools Menu" style="display:none;"><li role="none">
    <a href="/report.cgi" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="analytics"></span>
      <span class="label" role="none">Reports</span>
    </a>
  </li>
    <li role="separator"></li>
    <li role="none">
      <a href="https://bmo.readthedocs.io/en/latest/" target="_blank" role="menuitem">
        <span class="icon" aria-hidden="true" data-icon="help"></span>
        <span class="label" role="none">Documentation</span>
      </a>
    </li>
        </ul>
      </div>
    </nav>
      <ul id="header-login" class="links" role="none"><li id="mini_login_container_top" role="none">
  <a id="login_link_top" href="/index.cgi?GoAheadAndLogIn=1"
     class='show_mini_login_form header-button' data-qs-suffix="_top"
     role="button">
    <span class="icon" aria-hidden="true" data-icon="login"></span>
    <span class="label" role="none">Log In</span>
  </a>

  <div id="mini_login_top" class="mini-popup mini_login bz_default_hidden">

<form method="post" action="/github.cgi">
    <input type="hidden" name="github_token" value="W5Bo0rESncnQ6FOhsSGwKLpymladH9l7zKYgquG5RmfDrazozZipdxBPWh5pPwySBtELu81kOKh0nWZUp3DsVLnV1wwvn8zUEFtVBCOYjxFRHHiBUPCm9ykvnVxCCPiXvpbCJynarNkVoFkFllb2yhExokdpxb5TedKdq7ziEs8opgrNgBqecFeMwuYXGB3qF7R5K6GJbz3NodzAI7MEl3ozkF8hmoBsFsLOL83xuWEcIbe6a4RzuxzHz4a9hBlD">
    <input type="hidden" name="target_uri" value="https://bugzilla.mozilla.org/describecomponents.cgi">
    <button type="submit">
      <i class="fab fa-github"></i> Log In with GitHub
    </button>
  </form>

    <div class="method-separator">or</div>

  <form action="/describecomponents.cgi?product=Firefox" method="POST"
        data-qs-suffix="_top">

    <input id="Bugzilla_login_top"
           class="bz_login"
           name="Bugzilla_login"
           title="Login"
           placeholder="Email"
           aria-label="Email"
           type="email"
           required
    >
    <input class="bz_password"
           id="Bugzilla_password_top"
           name="Bugzilla_password"
           type="password"
           title="Password"
           placeholder="Password"
           aria-label="Password"
           required
    >
    <input class="bz_password bz_default_hidden bz_mini_login_help" type="text"
           id="Bugzilla_password_dummy_top" value="password"
           title="Password"
    >
      <span class="remember-outer">
        <input type="checkbox" id="Bugzilla_remember_top"
               name="Bugzilla_remember" value="on" class="bz_remember"
               checked>
        <label for="Bugzilla_remember_top">Remember me</label>
      </span>
    <input type="hidden" name="Bugzilla_login_token"
           value="1789095061-M7OguGmT4BIAZKdZFyZuVIewfoded8CjVtf15P3DkCQ">
    <input type="submit" name="GoAheadAndLogIn" value="Log In" id="log_in_top"
           class="check_mini_login_fields" data-qs-suffix="_top">
    <a href="#" id="hide_mini_login_top" aria-label="Close"
       class="close-button hide_mini_login_form" data-qs-suffix="_top">
      <span class="icon" aria-hidden="true"></span>
    </a>
  </form>
  <div class="footer">
      <a href="/createaccount.cgi">Create an Account</a>
    &middot;
    <a id="forgot_link_top" href="/index.cgi?GoAheadAndLogIn=1#forgot"
       class='show_forgot_form'
       data-qs-suffix="_top">Forgot Password</a>
  </div>
  </div>

  <div id="forgot_form_top" class="mini-popup mini_forgot bz_default_hidden">
  <form action="/token.cgi" method="post">
    <input type="email" name="loginname" size="20" placeholder="Email" aria-label="Email" required>
    <input id="forgot_button_top" value="Reset Password"
           type="submit">
    <input type="hidden" name="a" value="reqpw">
    <input type="hidden" id="token_top" name="token" value="1789095061-vccf7ZEF0z_WDtXbZQi6B4JFjuEo4Fj0lo25P_i6xI4">
    <a href="#" class="close-button hide_forgot_form" aria-label="Close" data-qs-suffix="_top">
      <span class="icon" aria-hidden="true"></span>
    </a>
  </form>
  </div>
</li>
      </ul>
  </div>
  <dialog id="menu-drawer" inert aria-label="Site Menu">
    <div class="drawer-inner" role="none">
      <div class="header" role="none">
        <button type="button" class="iconic ghost" id="close-menu-drawer"
                aria-label="Close Site Menu">
          <span class="icon" aria-hidden="true" data-icon="close"></span>
        </button>
      </div>
      <ul role="menu" aria-label="Site Links"><li role="none">
    <a class="header-button" href="/describecomponents.cgi"
       title="Browse bugs by component" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="category"></span>
      <span class="label" role="none">Browse</span>
    </a>
  </li>
  <li role="none">
    <a class="header-button" href="/query.cgi?format=advanced"
       title="Search bugs using various criteria" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="pageview"></span>
      <span class="label" role="none">Advanced Search</span>
    </a>
  </li>
  <li role="none">
    <a class="header-button" href="/enter_bug.cgi"
       title="File a new bug" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="add_box"></span>
      <span class="label" role="none">New Bug</span>
    </a>
  </li><li role="none">
    <a href="/report.cgi" role="menuitem">
      <span class="icon" aria-hidden="true" data-icon="analytics"></span>
      <span class="label" role="none">Reports</span>
    </a>
  </li>
    <li role="separator"></li>
    <li role="none">
      <a href="https://bmo.readthedocs.io/en/latest/" target="_blank" role="menuitem">
        <span class="icon" aria-hidden="true" data-icon="help"></span>
        <span class="label" role="none">Documentation</span>
      </a>
    </li>
      </ul>
    </div>
  </dialog>
</header> 


<main id="bugzilla-body" tabindex="-1">

<aside id="message-container" role="complementary">
  <noscript>
    <div class="noscript">
      <div class="inner">
        <p>Please enable JavaScript in your browser to use all the features on this site.</p>
      </div>
    </div>
  </noscript>
  
</aside>

<div id="main-inner">

<section class="product">
  <header>
    <h1>Firefox</h1>
    <p>For bugs in  Firefox Desktop, the Mozilla Foundation's web browser. For Firefox user interface issues in menus, bookmarks, location bar, and preferences. Many Firefox bugs will either be filed here or in the <a href="https://bugzilla.mozilla.org/describecomponents.cgi?product=Core">Core</a> product. Bugs for developer tools (F12) should be filed in the <a href="https://bugzilla.mozilla.org/describecomponents.cgi?product=DevTools">DevTools</a> product.  (<a href="https://wiki.mozilla.org/Modules/All#Firefox">more info</a>)</p><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-source="Component Description">Watch</button>
  </header>
  <div class="instructions">
    <p>Select a component to see open bugs in that component:</p>
  </div>
  <div class="list"><section id="about:logins" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=about%3Alogins&amp;resolution=---">about:logins</a></h2>
    </header>
    <div>
      <p class="description">Issues with the <a href="https://wiki.mozilla.org/Toolkit:Password_Manager/about:logins">Firefox Lockwise 'Logins and Passwords' management page</a>. Issues with filling and saving passwords on websites belong in <a href="https://wiki.mozilla.org/Toolkit:Password_Manager">Toolkit::Password Manager</a>.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="about:logins" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Address Bar" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Address%20Bar&amp;resolution=---">Address Bar</a></h2>
    </header>
    <div>
      <p class="description">For bugs in the Firefox "Smart Location Bar" (aka Awesome Bar) UI element, including the bookmark and history autocomplete matching behavior.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Address Bar" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Bookmarks &amp; History" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Bookmarks%20%26%20History&amp;resolution=---">Bookmarks &amp; History</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox bookmarks & history. This includes the bookmarks menu, add and modify bookmarks dialogs and the bookmarks manager.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Bookmarks &amp; History" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Containers" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Containers&amp;resolution=---">Containers</a></h2>
    </header>
    <div>
      <p class="description">Bugs related to the Containers / Contextual Identities feature (container tabs, identity management, related UI)</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Containers" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Data Loss Prevention" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Data%20Loss%20Prevention&amp;resolution=---">Data Loss Prevention</a></h2>
    </header>
    <div>
      <p class="description">For bugs in Firefox's support of DLP (Data Loss Prevention) products and the Content Analysis SDK including DLP-related prompts, warnings, and performance.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Data Loss Prevention" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Disability Access" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Disability%20Access&amp;resolution=---">Disability Access</a></h2>
    </header>
    <div>
      <p class="description">Accessibility-related bugs in Firefox: screen readers, support for magnifier tools, user interface bugs affecting the experience of people with disabilities, compliance with national and international accessibility standards.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Disability Access" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Distributions" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Distributions&amp;resolution=---">Distributions</a></h2>
    </header>
    <div>
      <p class="description">Bugs related to the creation of desktop distributions (distribution.ini)</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Distributions" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Downloads Panel" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Downloads%20Panel&amp;resolution=---">Downloads Panel</a></h2>
    </header>
    <div>
      <p class="description">For issues with the Downloads Panel, the new download manager of Firefox that lives in the navigation toolbar.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Downloads Panel" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Enterprise Policies" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Enterprise%20Policies&amp;resolution=---">Enterprise Policies</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests related to specific policies implemented in Firefox, or to the policy engine itself. Bugs about Group Policy Object (GPO) should be reported in this component.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Enterprise Policies" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Extension Compatibility" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Extension%20Compatibility&amp;resolution=---">Extension Compatibility</a></h2>
    </header>
    <div>
      <p class="description">Version level or extension problems or Gecko problems that cause extensions not to work. Also home to INVALID bugs where a malfunctioning extension has broken Firefox.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Extension Compatibility" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="File Handling" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=File%20Handling&amp;resolution=---">File Handling</a></h2>
    </header>
    <div>
      <p class="description">For issues dealing with helper applications, and guessing Content Types when they aren't specified/known (ftp:, file:, jar:, but generally not http:). This component does not cover: backend networking issues, such as those covered by Networking: FTP or Networking: File, nor does it cover the Download Manager which has its own component in the Toolkit product.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="File Handling" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Firefox Accounts" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Firefox%20Accounts&amp;resolution=---">Firefox Accounts</a></h2>
    </header>
    <div>
      <p class="description">For bugs in shared services/fxaccounts code related to Firefox accounts</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Firefox Accounts" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Firefox Monitor" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Firefox%20Monitor&amp;resolution=---">Firefox Monitor</a></h2>
    </header>
    <div>
      <p class="description">Bugs related to the Firefox Monitor (a.k.a Breach Alerts) feature within the Firefox UI.
For issues with the website, please file an issue on <a href="https://github.com/mozilla/blurts-server">GitHub</a>.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Firefox Monitor" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Firefox View" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Firefox%20View&amp;resolution=---">Firefox View</a></h2>
    </header>
    <div>
      <p class="description">Bugs relating to the Firefox View page, toolbar button and integration</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Firefox View" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Foxfooding" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Foxfooding&amp;resolution=---">Foxfooding</a></h2>
    </header>
    <div>
      <p class="description">Bugs found through the foxfooding program will be filed in this component to be later triaged to the appropriate buckets.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Foxfooding" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="General" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=General&amp;resolution=---">General</a></h2>
    </header>
    <div>
      <p class="description">For bugs in Firefox which do not fit into other more specific Firefox components</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="General" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Headless" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Headless&amp;resolution=---">Headless</a></h2>
    </header>
    <div>
      <p class="description">For bugs related to headless browsing mode where Firefox is a web browser without a Graphical User Interface (GUI).</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Headless" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Installer" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Installer&amp;resolution=---">Installer</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for the Firefox application install wizard.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Installer" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="IP Protection" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=IP%20Protection&amp;resolution=---">IP Protection</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for IP Protection in Firefox</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="IP Protection" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Keyboard Navigation" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Keyboard%20Navigation&amp;resolution=---">Keyboard Navigation</a></h2>
    </header>
    <div>
      <p class="description">Keyboard shortcut navigation in Firefox's user interface</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Keyboard Navigation" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Launcher Process" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Launcher%20Process&amp;resolution=---">Launcher Process</a></h2>
    </header>
    <div>
      <p class="description">Bugs relating to the Launcher Process for Windows builds</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Launcher Process" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Menus" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Menus&amp;resolution=---">Menus</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox menus. This includes toplevel and context menus.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Menus" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Messaging System" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Messaging%20System&amp;resolution=---">Messaging System</a></h2>
    </header>
    <div>
      <p class="description">For bugs that involve user interrupting messages, badging and notifications in Firefox. This includes Contextual Feature Recommender (CFR), Onboarding Tour, Feature Callouts, Menu/Toolbar badges and door-hangers.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Messaging System" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Migration" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Migration&amp;resolution=---">Migration</a></h2>
    </header>
    <div>
      <p class="description">Firefox Profile Migration from other browsers.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Migration" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="New Tab Page" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=New%20Tab%20Page&amp;resolution=---">New Tab Page</a></h2>
    </header>
    <div>
      <p class="description">The page displayed when a new tab is opened (about:newtab).</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="New Tab Page" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Nimbus Desktop Client" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Nimbus%20Desktop%20Client&amp;resolution=---">Nimbus Desktop Client</a></h2>
    </header>
    <div>
      <p class="description">All bugs related to Nimbus experimentation client code in Firefox Desktop</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Nimbus Desktop Client" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Normandy Client" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Normandy%20Client&amp;resolution=---">Normandy Client</a></h2>
    </header>
    <div>
      <p class="description">In-browser component that validates and executes actions in a sandbox</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Normandy Client" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Normandy Server" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Normandy%20Server&amp;resolution=---">Normandy Server</a></h2>
    </header>
    <div>
      <p class="description">Web service to store and serve recipes</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Normandy Server" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Page Info Window" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Page%20Info%20Window&amp;resolution=---">Page Info Window</a></h2>
    </header>
    <div>
      <p class="description">For issues with the Page Info window.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Page Info Window" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="PDF Viewer" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=PDF%20Viewer&amp;resolution=---">PDF Viewer</a></h2>
    </header>
    <div>
      <p class="description">For bugs related to Firefox's built-in PDF viewing capabilities (also known as pdf.js).</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="PDF Viewer" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Performance" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Performance&amp;resolution=---">Performance</a></h2>
    </header>
    <div>
      <p class="description">Issues related to the performance of the browser front-end.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Performance" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Pocket" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Pocket&amp;resolution=---">Pocket</a></h2>
    </header>
    <div>
      <p class="description">Bugs involving the integration with Pocket and Firefox.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Pocket" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Private Browsing" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Private%20Browsing&amp;resolution=---">Private Browsing</a></h2>
    </header>
    <div>
      <p class="description">For bugs and feature requests in Firefox's Private Browsing implementation.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Private Browsing" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Profile Backup" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Profile%20Backup&amp;resolution=---">Profile Backup</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for profile backup in Firefox</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Profile Backup" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Protections UI" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Protections%20UI&amp;resolution=---">Protections UI</a></h2>
    </header>
    <div>
      <p class="description">For bugs and feature requests in Firefox’s Anti-Tracking Protections UI such as the Protection Panel and the Protection Report.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Protections UI" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Remote Settings Client" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Remote%20Settings%20Client&amp;resolution=---">Remote Settings Client</a></h2>
    </header>
    <div>
      <p class="description">Module in charge of fetching and keeping remote settings in sync with Mozilla servers.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Remote Settings Client" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Report Broken Site" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Report%20Broken%20Site&amp;resolution=---">Report Broken Site</a></h2>
    </header>
    <div>
      <p class="description">For issues with the "Report Broken Site" tool.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Report Broken Site" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Screenshots" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Screenshots&amp;resolution=---">Screenshots</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox Screenshots</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Screenshots" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Search" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Search&amp;resolution=---">Search</a></h2>
    </header>
    <div>
      <p class="description">Web search UI, default search engines and Toolkit's search service. Find-in-page bugs belong in Toolkit::Find Toolbar instead.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Search" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Security" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Security&amp;resolution=---">Security</a></h2>
    </header>
    <div>
      <p class="description">For app-level security bugs.
<p>
If the problem relates to underlying components (PSM, NSS, Core, Toolkit) then please file it in the appropriate product instead of here.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Security" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Session Restore" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Session%20Restore&amp;resolution=---">Session Restore</a></h2>
    </header>
    <div>
      <p class="description">For bugs in Firefox's session restore functionality, including the undo close tab  feature.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Session Restore" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Settings UI" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Settings%20UI&amp;resolution=---">Settings UI</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox Settings. This is specific to the Tools-&gt;Settings UI - for issues with other types of settings (e.g. permissions, settings internal to websites, OS settings, ...), requests to change default settings values, bugs where internal values of settings have no effect, etc., file bugs in components related to those features/settings instead.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Settings UI" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Sharing" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Sharing&amp;resolution=---">Sharing</a></h2>
    </header>
    <div>
      <p class="description">For bugs or feature work relating to content sharing in Firefox</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Sharing" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Shell Integration" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Shell%20Integration&amp;resolution=---">Shell Integration</a></h2>
    </header>
    <div>
      <p class="description">This component is responsible for determining if Firefox is the default browser, setting Firefox as the default browser, and setting the desktop background.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Shell Integration" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Sidebar" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Sidebar&amp;resolution=---">Sidebar</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox Sidebar</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Sidebar" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Site Identity" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Site%20Identity&amp;resolution=---">Site Identity</a></h2>
    </header>
    <div>
      <p class="description">For bugs and feature requests in the UI that signals site identity and connection security, such as the lock icon and the corresponding “identity panel”.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Site Identity" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Site Permissions" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Site%20Permissions&amp;resolution=---">Site Permissions</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for the Firefox UI to give or revoke web page permissions to access device functionality such as camera, microphone, geolocation or notifications.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Site Permissions" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Sync" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Sync&amp;resolution=---">Sync</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Sync in Firefox Desktop.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Sync" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="System Add-ons: Off-train Deployment" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=System%20Add-ons%3A%20Off-train%20Deployment&amp;resolution=---">System Add-ons: Off-train Deployment</a></h2>
    </header>
    <div>
      <p class="description">Requests to ship a system add-on off-train through Go Faster (Balrog) (<a href="https://wiki.mozilla.org/Firefox/Go_Faster/System_Add-ons/Process">more info</a>).</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="System Add-ons: Off-train Deployment" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Tabbed Browser" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Tabbed%20Browser&amp;resolution=---">Tabbed Browser</a></h2>
    </header>
    <div>
      <p class="description">For problems in the browser tab features or problems with the  widget itself.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Tabbed Browser" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Tabbed Browser: Split View" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Tabbed%20Browser%3A%20Split%20View&amp;resolution=---">Tabbed Browser: Split View</a></h2>
    </header>
    <div>
      <p class="description">For bugs or feature work relating to splitview-specific tab and content behavior.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Tabbed Browser: Split View" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Tabbed Browser: Tab Groups" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Tabbed%20Browser%3A%20Tab%20Groups&amp;resolution=---">Tabbed Browser: Tab Groups</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests related to tab groups in the tab strip and other places that tabs live.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Tabbed Browser: Tab Groups" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Theme" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Theme&amp;resolution=---">Theme</a></h2>
    </header>
    <div>
      <p class="description">General user interface, user experience, and visual design for the default theme used in Firefox.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Theme" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Toolbars and Customization" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Toolbars%20and%20Customization&amp;resolution=---">Toolbars and Customization</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox toolbars. This includes
toolbar customization.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Toolbars and Customization" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Top Sites" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Top%20Sites&amp;resolution=---">Top Sites</a></h2>
    </header>
    <div>
      <p class="description">Bugs related to top sites on the new tab page and in the address bar</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Top Sites" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Tours" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Tours&amp;resolution=---">Tours</a></h2>
    </header>
    <div>
      <p class="description">UITour, firstrun and whatsnew Firefox bugs.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Tours" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Translations" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Translations&amp;resolution=---">Translations</a></h2>
    </header>
    <div>
      <p class="description">Instant translation and language detection in Firefox.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Translations" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Untriaged" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Untriaged&amp;resolution=---">Untriaged</a></h2>
    </header>
    <div>
      <p class="description">For newly filed bugs that need some help finding the right place to go.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Untriaged" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Web Apps" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Web%20Apps&amp;resolution=---">Web Apps</a></h2>
    </header>
    <div>
      <p class="description">This component is responsible for web apps for Firefox.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Web Apps" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="WebPayments UI" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=WebPayments%20UI&amp;resolution=---">Web<wbr>Payments UI</a></h2>
    </header>
    <div>
      <p class="description">User Interface for the WebPayments <a href="https://w3c.github.io/browser-payment-api/">Payment Request API</a> and <a href="https://w3c.github.io/payment-handler/">Payment Handler API</a>.</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="WebPayments UI" data-source="Component Description">Watch</button>
    </footer>
  </section><section id="Widgets" class="component">
    <header>
      <h2><a href="/buglist.cgi?product=Firefox&amp;component=Widgets&amp;resolution=---">Widgets</a></h2>
    </header>
    <div>
      <p class="description">Bugs and feature requests for Firefox Widgets</p>
    </div>
    <footer><button disabled type="button" class="secondary component-watching" data-product="Firefox"
        data-component="Widgets" data-source="Component Description">Watch</button>
    </footer>
  </section>
  </div>
</section>
</div> 
</main> 
</div> 


</body>
</html>