<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
<meta property="og:type" content="website">
<meta property="og:title" content="1670675 - Brotli compression does not work (at least on http://localhost/ ?)">
<meta property="og:url" content="https://bugzilla.mozilla.org/show_bug.cgi?id=1670675">
<meta property="og:description"
      content="RESOLVED (valentin.gosu) in Core - DOM: Networking. Last updated 2020-10-22.">
<meta name="twitter:label1" value="Type">
<meta name="twitter:data1" value="defect">
<meta name="twitter:label2" value="Priority">
<meta name="twitter:data2" value="P3">

    

    <meta name="viewport"
          content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="color-scheme" content="dark light">
    <meta name="generator" content="Bugzilla 20260908.1">
    <meta name="bugzilla-global" content="dummy"
        id="bugzilla-global" data-bugzilla="{&quot;api_token&quot;:&quot;&quot;,&quot;config&quot;:{&quot;basepath&quot;:&quot;\/&quot;,&quot;cookie_consent_enabled&quot;:true,&quot;cookie_consent_required&quot;:false,&quot;essential_cookies&quot;:[&quot;bugzilla&quot;,&quot;Bugzilla_login&quot;,&quot;Bugzilla_logincookie&quot;,&quot;Bugzilla_login_request_cookie&quot;,&quot;github_state&quot;,&quot;github_token&quot;,&quot;mfa_verification_token&quot;,&quot;moz-consent-pref&quot;,&quot;sudo&quot;],&quot;urlbase&quot;:&quot;https:\/\/bugzilla.mozilla.org\/&quot;},&quot;constant&quot;:{&quot;CGI_URI_LIMIT&quot;:8000,&quot;COMMENT_COLS&quot;:80},&quot;param&quot;:{&quot;allow_attachment_display&quot;:true,&quot;maxattachmentsize&quot;:&quot;10240&quot;,&quot;maxusermatches&quot;:&quot;50&quot;,&quot;splinter_base&quot;:&quot;\/page.cgi?id=splinter.html&amp;ignore=\/&quot;,&quot;use_markdown&quot;:true},&quot;string&quot;:{&quot;TextEditor&quot;:{&quot;command_bold&quot;:&quot;Bold&quot;,&quot;command_bulleted_list&quot;:&quot;Bulleted list&quot;,&quot;command_code&quot;:&quot;Code&quot;,&quot;command_heading&quot;:&quot;Heading&quot;,&quot;command_italic&quot;:&quot;Italic&quot;,&quot;command_link&quot;:&quot;Link&quot;,&quot;command_numbered_list&quot;:&quot;Numbered list&quot;,&quot;command_quote&quot;:&quot;Quote&quot;,&quot;comment_editor&quot;:&quot;Comment Editor&quot;,&quot;edit&quot;:&quot;Edit&quot;,&quot;etiquette_link&quot;:{&quot;href&quot;:&quot;page.cgi?id=etiquette.html&quot;,&quot;text&quot;:&quot;Etiquette&quot;},&quot;guidelines_link&quot;:{&quot;href&quot;:&quot;page.cgi?id=bug-writing.html&quot;,&quot;text&quot;:&quot;Bug Writing Guidelines&quot;},&quot;loading&quot;:&quot;Loading…&quot;,&quot;markdown_link&quot;:{&quot;href&quot;:&quot;https:\/\/guides.github.com\/features\/mastering-markdown\/&quot;,&quot;text&quot;:&quot;Markdown supported&quot;},&quot;preview&quot;:&quot;Preview&quot;,&quot;preview_error&quot;:&quot;Preview could not be loaded. Please try again later.&quot;,&quot;text_editor&quot;:&quot;Text Editor&quot;,&quot;toolbar_label&quot;:&quot;Markdown text-formatting toolbar&quot;},&quot;bug&quot;:&quot;bug&quot;,&quot;bug_type_required&quot;:&quot;You must select a Type for this bug&quot;,&quot;component_required&quot;:&quot;You must select a Component for this bug&quot;,&quot;description_required&quot;:&quot;You must enter a Description for this bug&quot;,&quot;short_desc_required&quot;:&quot;You must enter a Summary for this bug&quot;,&quot;version_required&quot;:&quot;You must select a Version for this bug&quot;},&quot;user&quot;:{&quot;cookie_consent&quot;:&quot;&quot;,&quot;is_new&quot;:true,&quot;login&quot;:&quot;&quot;}}">
    <meta name="google-site-verification" content="JYXIuR9cAlV7fLmglSrc_4UaJS6Wzh5Mdxiorqu5AQc" />
    <title>1670675 - Brotli compression does not work (at least on http://localhost/ ?)</title>

<link rel="Top" href="/">

  


  
    <link rel="Show" title="Dependency Tree"
          href="/showdependencytree.cgi?id=1670675&amp;hide_resolved=1">
    <link rel="Show" title="Dependency Graph"
          href="/showdependencygraph.cgi?id=1670675">
    <link rel="Show" title="Bug Activity"
          href="/show_activity.cgi?id=1670675">

<link href="/static/v20260908.1/skins/standard/global.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/BugModal/web/bug_modal.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/plugins/contextMenu/contextMenu.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/BMO/web/styles/bug_modal.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/EditComments/web/styles/inline-comment-editor.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-structure-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-theme-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/lib/prism.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/consent.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/Needinfo/web/styles/needinfo.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/Review/web/styles/badge.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/Review/web/styles/review.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/text-editor.css" rel="stylesheet" type="text/css">



    
<script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/jquery/jquery-min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/jquery/ui/jquery-ui-min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/jquery/plugins/contextMenu/contextMenu-min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/jquery/plugins/devbridgeAutocomplete/devbridgeAutocomplete-min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/global.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/util.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/widgets.js"></script>

      <script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB">BUGZILLA.value_descs = JSON.parse('{\"bug_status\":{},\"resolution\":{\"\":\"---\"}}');

  
    var tracking_flags_str = "{\"flags\":{\"tracking\":{\"cf_status_thunderbird_esr140\":\"---\",\"cf_tracking_firefox157\":\"---\",\"cf_status_firefox158\":\"---\",\"cf_status_firefox_esr140\":\"---\",\"cf_tracking_thunderbird_esr115\":\"---\",\"cf_tracking_firefox_esr153\":\"---\",\"cf_status_thunderbird_esr115\":\"---\",\"cf_status_firefox157\":\"---\",\"cf_status_firefox_esr153\":\"---\",\"cf_tracking_firefox156\":\"---\",\"cf_tracking_firefox_esr140\":\"---\",\"cf_status_firefox84\":\"fixed\",\"cf_status_firefox_esr115\":\"---\",\"cf_tracking_firefox158\":\"---\",\"cf_status_thunderbird_esr153\":\"---\",\"cf_tracking_firefox_relnote\":\"---\",\"cf_tracking_thunderbird_esr153\":\"---\",\"cf_status_firefox156\":\"---\",\"cf_tracking_firefox_esr115\":\"---\",\"cf_tracking_thunderbird_esr140\":\"---\"},\"project\":{\"cf_a11y_review_project_flag\":\"---\",\"cf_accessibility_severity\":\"---\",\"cf_size_estimate\":\"---\",\"cf_webcompat_score\":\"---\",\"cf_performance_impact\":\"---\",\"cf_webcompat_priority\":\"---\"}},\"comments\":{\"cf_a11y_review_project_flag\":{\"requested\":\"Description:\\nPlease provide an explanation of the feature or change. Include a description of the user scenario in which it would be used and how the user would complete the task(s).\\nScreenshots and visual UI specs are welcome, but please include sufficient accompanying explanation so that blind members of the accessibility team are able to understand the feature\/change.\\n\\nHow do we test this?\\nIf there is an implementation to test, please provide instructions for testing it; e.g. setting preferences, other preparation, how to trigger the UI, etc.\\n\\nWhen will this ship?\\nTracking bug\/issue:\\nDesign documents (e.g. Product Requirements Document, UI spec):\\nEngineering lead:\\nProduct manager:\\n\\nThe accessibility team has developed the Mozilla Accessibility Release Guidelines which outline what is needed to make user interfaces accessible:\\nhttps:\/\/wiki.mozilla.org\/Accessibility\/Guidelines\\nPlease describe the accessibility guidelines you considered and what steps you\'ve taken to address them:\\n\\nDescribe any areas of concern to which you want the accessibility team to give special attention:\"},\"cf_tracking_firefox_esr153\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox_esr115\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox156\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox_esr140\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox158\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox157\":{\"?\":\"[Tracking Requested - why for this release]:\"},\"cf_tracking_firefox_relnote\":{\"?\":\"Release Note Request (optional, but appreciated)\\n[Why is this notable]:\\n[Affects Firefox for Android]:\\n[Suggested wording]:\\n[Links (documentation, blog post, etc)]:\"}},\"types\":[\"tracking\"]}";
    var TrackingFlags = $.parseJSON(tracking_flags_str);

  
    BUGZILLA.bug_id = 1670675;
    BUGZILLA.bug_title = '1670675 - Brotli compression does not work (at least on http:\/\/localhost\/ ?)';
    BUGZILLA.bug_summary = 'Brotli compression does not work (at least on http:\/\/localhost\/ ?)';
    BUGZILLA.bug_url = 'https:\/\/bugzilla.mozilla.org\/show_bug.cgi?id=1670675';
    BUGZILLA.bug_keywords = '',
    BUGZILLA.bug_secure = false;
    

  BUGZILLA.user = {
    id: 0,
    login: '',
    is_insider: false,
    is_timetracker: false,
    can_tag: false,
    can_triage: false,
    timezone: 'America\/Los_Angeles',
    settings: {
      quote_replies: 'quoted_reply',
      comment_box_position: 'after_comments',
      comment_sort_order: 'oldest_to_newest',
      zoom_textareas: true,
      remember_collapsed: true,
      inline_attachments: true,
      autosize_comments: false
    },
    cookie_consent: false
  };
  review_suggestions = {
    _mentors: [
    ],


      
      'DOM: Networking': [
      ],

    
    _end: 1
  };

    static_component = 'DOM: Networking';
      </script>
<script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/text-editor.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/BugModal/web/autosize.min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/ProdCompSearch/web/js/prod_comp_search.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/BugModal/web/attachments_overlay.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/BugModal/web/bug_modal.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/BugModal/web/comments.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/ComponentWatching/web/js/overlay.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/bugzilla-readable-status-min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/field.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/comments.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/TrackingFlags/web/js/flags.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/BMO/web/js/firefox-crash-table.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/MozChangeField/web/js/severity-s1-priority-p1.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/MozChangeField/web/js/clear-tracking-priority-s1.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/MozChangeField/web/js/set-tracking-severity-s1.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/lib/prism.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/consent.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/cookie-helper.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/js/lib/md5.min.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/Review/web/js/badge.js"></script><script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/Review/web/js/review.js"></script>

    

    
    <link href="/static/v20260908.1/skins/lib/fontawesome.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-brands.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-solid.min.css" rel="stylesheet" type="text/css">

    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla@Mozilla" href="/search_plugin.cgi"><link rel="shortcut icon" href="/extensions/BMO/web/images/favicon.ico">
<link rel="icon" type="image/svg+xml" href="/extensions/BMO/web/images/favicon.svg">
<link rel="canonical" href="https://bugzilla.mozilla.org/show_bug.cgi?id=1670675">
<link rel="shorturl" href="https://bugzilla.mozilla.org/1670675"><meta name="robots" content="noarchive">
  </head>



  <body
        class="bugzilla-mozilla-org
               skin-standard bug_modal">



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
    <input type="hidden" name="github_token" value="YE4ms4rye8cy9mOdAziEY3QZb3Fc31tnFWWfxSxnA30Bsxw71PpkN9w0SQtsLOk3z0hRd5TdFIMzEQdRtZET9ka2Twbm6GsOby9uHOB6esL9CTlCyONYinCjhxAaPIUbm3AV6RotD010KxKcEoOOYmC2mje3k03FsxWPXdelNTS4CWoUjcqfm8pVNP0hVgiVoX4o7yZ3nTdULwfxfrfSJINv061omUg0224abBQPubEUL5erc68JNymKx1DtOnIg">
    <input type="hidden" name="target_uri" value="https://bugzilla.mozilla.org/show_bug.cgi">
    <button type="submit">
      <i class="fab fa-github"></i> Log In with GitHub
    </button>
  </form>

    <div class="method-separator">or</div>

  <form action="/show_bug.cgi?id=1670675" method="POST"
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
           value="1789172180-a7bovCdMCPR4A1Zh1cuKdXLnb-a3nF4umAVrAJpsp2I">
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
    <input type="hidden" id="token_top" name="token" value="1789172180-I9P431BnqiTtS6GOk0JrPwpB2XseiL5cgW9IDqbGrXU">
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




<div role="toolbar" id="page-toolbar">
  <div role="group" class="buttons">
    <button type="button" id="copy-summary" class="secondary separate-dropdown-button-main"
      title="Copy bug number and summary to your clipboard">Copy Summary</button
    ><div id="copy-menu-dropdown" class="dropdown"><button type="button" id="copy-menu-btn" aria-haspopup="true" aria-label="View"
      aria-expanded="false" aria-controls="copy-menu" class="dropdown-button secondary separate-dropdown-button-arrow"
      title="More options for copy">&#9662;</button>
      <ul class="dropdown-content left" id="copy-menu" role="menu" style="display:none;">
        <li role="presentation">
          <a id="copy-markdown-summary" role="menuitem" tabindex="-1">Markdown</a>
        </li>
        <li role="presentation">
          <a id="copy-markdown-bug-number" role="menuitem" tabindex="-1">Markdown (bug number)</a>
        </li>
        <li role="presentation">
          <a id="copy-text-summary" role="menuitem" tabindex="-1">Plain Text</a>
        </li>
        <li role="presentation">
          <a id="copy-html-summary" role="menuitem" tabindex="-1">HTML</a>
        </li>
      </ul>
    </div>
    <div class="dropdown">
      <button type="button" id="action-menu-btn" aria-haspopup="true" aria-label="View"
        aria-expanded="false" aria-controls="action-menu" class="dropdown-button secondary">View &#9662;</button>
      <ul class="dropdown-content left" id="action-menu" role="menu" style="display:none;">
        <li role="presentation">
          <a id="action-reset" role="menuitem" tabindex="-1">Reset Sections</a>
        </li>
        <li role="presentation">
          <a id="action-expand-all" role="menuitem" tabindex="-1">Expand All Sections</a>
        </li>
        <li role="presentation">
          <a id="action-collapse-all" role="menuitem" tabindex="-1">Collapse All Sections</a>
        </li>
        <li role="separator"></li>
        <li role="presentation">
          <a id="action-history" role="menuitem" tabindex="-1">History</a>
        </li>
        <li role="separator"></li>
        <li role="presentation">
          <a href="/rest/bug/1670675" role="menuitem" tabindex="-1">JSON</a>
        </li>
        <li role="presentation">
          <a href="/show_bug.cgi?ctype=xml&amp;id=1670675" role="menuitem" tabindex="-1">XML</a>
        </li>
      </ul>
    </div>
  </div>
</div>



<div role="status" id="io-error" style="display:none"></div>
<section class="module"
>
  <div class="module-content"
  >
  <div id="summary-container">
    <div class="field bug_modal indent"
    id="field-status_summary"
>



  
    <div class=" container">
        <span id="field-value-status_summary">
      <span class="bug-status-label text" data-status="closed">Closed</span>
      <span id="field-value-bug_id">
        <a href="/show_bug.cgi?id=1670675">Bug 1670675</a>
      </span>
      <span class="bug-time-labels">
        <span class="bug-time-label">Opened <span class="rel-time" title="2020-10-12 06:56 PDT" data-time="1602510963">5 years ago</span></span>
          <span class="bug-time-label">Closed <span class="rel-time" title="2020-10-22 08:02 PDT" data-time="1603378978">5 years ago</span></span>
      </span>
        </span>
    </div>

  
</div>
<div class="field bug_modal indent edit-hide"
>



  
    <div class=" container">
      

      <h1 id="field-value-short_desc">Brotli compression does not work (at least on <a target="_blank" rel="nofollow noreferrer" href="http://localhost/">http://localhost/</a> ?)</h1>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-short_desc" style="display:none"
>
    <div class="name">
      
        <span class="required_star edit-show" style="display:none" aria-label="Required Field">*</span> 
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#short_desc" id="short_desc-help-link" class="help">Summary:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-short_desc">
            Brotli compression does not work (at least on http://localhost/ ?)

        </span>
    </div>

  
</div>
  </div>
  </div>
</section>


<section class="module" id="module-categories"
>
    <header id="module-categories-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Categories section"
           data-label-collapsed="Expand Categories section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-categories-content"
             aria-expanded="true"
             aria-labeledby="module-categories-title"
             aria-describedby="module-categories-subtitle"></div>
        <h2 class="module-title" id="module-categories-title">Categories</h2>
          <h3 class="module-subtitle" id="module-categories-subtitle">
            (Core :: DOM: Networking, defect, P3)
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-categories-content"
  ><div class="fields-lhs">

    <div class="field bug_modal"
    id="field-product"
>
    <div class="name">
      
        <a href="/describecomponents.cgi?product=Core" id="product-help-link" class="help">Product:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-product">
      <div class="name-info-outer dropdown">
        <span id="product-name" class="dropdown-button" tabindex="0" role="button"
             aria-haspopup="menu" aria-controls="product-info">Core
          <span class="icon" aria-hidden="true">&#x25BE;</span>
        </span>
        <aside id="product-info" class="name-info-popup dropdown-content right hover-display" hidden role="menu"
               aria-label="Product description and actions">
          <header>
            <div class="title">Core</div>
            <div class="description">Shared components used by Firefox and other Mozilla software, including handling of Web content; Gecko, HTML, CSS, layout, DOM, scripts, images, networking, etc. Issues with web page layout probably go here, while Firefox user interface issues belong in the <a href="https://bugzilla.mozilla.org/describecomponents.cgi?product=Firefox">Firefox</a> product. (<a href="https://wiki.mozilla.org/Modules/All#Core">More info</a>)</div>
          </header>
          <li role="separator"></li>
          <div class="actions">
            <div><a href="/buglist.cgi?product=Core&amp;bug_status=__open__"
                    target="_blank" role="menuitem" tabindex="-1">See Open Bugs in This Product</a></div>
            <div><a href="/enter_bug.cgi?product=Core"
                    target="_blank" role="menuitem" tabindex="-1">File New Bug in This Product</a></div>
            <div><button disabled type="button" class="secondary component-watching" role="menuitem" tabindex="-1"
                         data-product="Core"
                         data-label-watch="Watch This Product" data-label-unwatch="Unwatch This Product"
                         data-source="BugModal">Watch This Product</button></div>
          </div>
        </aside>
      </div>
        </span>
    </div>

  
</div>

    <div class="field bug_modal"
    id="field-component"
>
    <div class="name">
      
        <a href="/describecomponents.cgi?product=Core&component=DOM%3A%20Networking#DOM%3A%20Networking" id="component-help-link" class="help">Component:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-component">
      <div class="name-info-outer dropdown">
        <span id="component-name" class="dropdown-button" tabindex="0" role="button"
             aria-haspopup="menu" aria-controls="component-info">DOM: Networking
          <span class="icon" aria-hidden="true">&#x25BE;</span>
        </span>
        <aside id="component-info" class="name-info-popup dropdown-content right hover-display" hidden role="menu"
               aria-label="Component description and actions">
          <header>
            <div class="title">Core :: DOM: Networking</div>
            <div class="description">Networking-related DOM APIs, such as  XmlHttpRequest, Fetch, Web Sockets, EventSource, and Beacon.</div>
          </header>
          <li role="separator"></li>
          <div class="actions">
            <div><a href="/buglist.cgi?product=Core&amp;component=DOM%3A%20Networking&amp;bug_status=__open__"
                    target="_blank" role="menuitem" tabindex="-1">See Open Bugs in This Component</a></div>
            <div><a href="/buglist.cgi?product=Core&amp;component=DOM%3A%20Networking&amp;chfield=resolution&chfieldfrom=-6m&chfieldvalue=FIXED&bug_status=__closed__"
                    target="_blank" role="menuitem" tabindex="-1">Recently Fixed Bugs in This Component</a></div>
            <div><a href="/enter_bug.cgi?product=Core&amp;component=DOM%3A%20Networking"
                    target="_blank" role="menuitem" tabindex="-1">File New Bug in This Component</a></div>
            <div><button disabled type="button" class="secondary component-watching" role="menuitem" tabindex="-1"
                         data-product="Core" data-component="DOM: Networking"
                         data-label-watch="Watch This Component" data-label-unwatch="Unwatch This Component"
                         data-source="BugModal">Watch This Component</button></div>
          </div>
        </aside>
      </div>
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-version" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#version" id="version-help-link" class="help">Version:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-version">
            unspecified

        </span>
    </div>

  
</div>

    <div class="field bug_modal"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#rep_platform" id="-help-link" class="help">Platform:
        </a>
    </div>



  
    <div class=" container"><div class="field bug_modal inline"
    id="field-rep_platform"
>



  
    <div class="value">
        <span id="field-value-rep_platform">
            x86_64

        </span>
    </div>

  
</div><div class="field bug_modal indent inline"
    id="field-op_sys"
>



  
    <div class="value">
        <span id="field-value-op_sys">
            Windows 10

        </span>
    </div>

  
</div><div class="field bug_modal"
>



  
    <div class=" container">
    </div>

  
</div>
    </div>

  
</div>
</div><div class="fields-rhs">

    <div class="field bug_modal contains-buttons"
    id="field-bug_type"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#bug_type" id="bug_type-help-link" class="help">Type:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-bug_type">
      <span class="bug-type-label iconic-text" data-type="defect">
        <span class="icon" aria-hidden="true"></span>defect</span>
        </span>
    </div>

  
</div>

    <div class="field bug_modal"
    id="field-importance"
>



  
    <div class=" container">
        <span id="field-value-importance"><div class="field bug_modal inline"
    id="field-priority"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#priority" id="priority-help-link" class="help">Priority:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-priority">P3
        </span>
    </div>

  
</div><div class="field bug_modal inline"
    id="field-bug_severity"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#bug_severity" id="bug_severity-help-link" class="help">Severity:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-bug_severity">
            S4

        </span>
    </div>

  
</div>
        </span>
    </div>

  
</div>


    <div class="field bug_modal edit-show"
    id="field-cf_fx_points" style="display:none"
>
    <div class="name">
      Points:
    </div>



  
    <div class="value">
        <span id="field-value-cf_fx_points">
            ---

        </span>
    </div>

  
</div>
</div>
  </div>
</section>


<section class="module" id="module-tracking"
>
    <header id="module-tracking-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Tracking section"
           data-label-collapsed="Expand Tracking section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-tracking-content"
             aria-expanded="true"
             aria-labeledby="module-tracking-title"
             aria-describedby="module-tracking-subtitle"></div>
        <h2 class="module-title" id="module-tracking-title">Tracking</h2>
          <h3 class="module-subtitle" id="module-tracking-subtitle">
            (<span id="readable-bug-status" data-readable-bug-status="{&quot;cf_accessibility_severity&quot;:&quot;---&quot;,&quot;cf_tracking_firefox_esr140&quot;:&quot;---&quot;,&quot;cf_status_firefox_esr153&quot;:&quot;---&quot;,&quot;status&quot;:&quot;RESOLVED&quot;,&quot;cf_webcompat_score&quot;:&quot;---&quot;,&quot;dupe_of&quot;:null,&quot;cf_performance_impact&quot;:&quot;---&quot;,&quot;target_milestone&quot;:&quot;84 Branch&quot;,&quot;cf_status_firefox_esr115&quot;:&quot;---&quot;,&quot;flags&quot;:[],&quot;cf_size_estimate&quot;:&quot;---&quot;,&quot;cf_tracking_thunderbird_esr153&quot;:&quot;---&quot;,&quot;cf_tracking_firefox_esr115&quot;:&quot;---&quot;,&quot;priority&quot;:&quot;P3&quot;,&quot;cf_tracking_firefox157&quot;:&quot;---&quot;,&quot;cf_status_firefox158&quot;:&quot;---&quot;,&quot;cf_status_firefox157&quot;:&quot;---&quot;,&quot;cf_webcompat_priority&quot;:&quot;---&quot;,&quot;cf_tracking_firefox_esr153&quot;:&quot;---&quot;,&quot;cf_status_firefox84&quot;:&quot;fixed&quot;,&quot;cf_tracking_firefox156&quot;:&quot;---&quot;,&quot;cf_tracking_firefox_relnote&quot;:&quot;---&quot;,&quot;cf_tracking_firefox158&quot;:&quot;---&quot;,&quot;cf_status_thunderbird_esr153&quot;:&quot;---&quot;,&quot;keywords&quot;:[],&quot;cf_a11y_review_project_flag&quot;:&quot;---&quot;,&quot;cf_tracking_thunderbird_esr140&quot;:&quot;---&quot;,&quot;cf_status_firefox156&quot;:&quot;---&quot;,&quot;cf_status_thunderbird_esr140&quot;:&quot;---&quot;,&quot;cf_status_firefox_esr140&quot;:&quot;---&quot;,&quot;cf_tracking_thunderbird_esr115&quot;:&quot;---&quot;,&quot;cf_status_thunderbird_esr115&quot;:&quot;---&quot;,&quot;id&quot;:1670675,&quot;resolution&quot;:&quot;FIXED&quot;}"></span>)
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-tracking-content"
  ><div class="fields-lhs">

    <div class="field bug_modal edit-hide"
    id="field-status-view"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugStatuses" id="status-view-help-link" class="help">Status:
        </a>
    </div>



  
    <div class=" container">
        <span id="field-value-status-view">RESOLVED
        FIXED
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-status-edit" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugStatuses" id="status-edit-help-link" class="help">Status:
        </a>
    </div>



  
    <div class=" container">
        <span id="field-value-status-edit"><div class="field bug_modal inline"
    id="field-bug_status"
>



  
    <div class="value">
        <span id="field-value-bug_status">
            RESOLVED

        </span>
    </div>

  
</div><div class="field bug_modal indent inline"
    id="field-resolution"
>



  
    <div class="value">
        <span id="field-value-resolution">
            FIXED

        </span>
    </div>

  
</div>
  <div id="status-action-buttons">
      <div id="assigned-container" style="display:none">
        <button type="button" class="secondary" id="mark-as-assigned-btn">
          Mark as Assigned
        </button>
      </div>
  </div>
        </span>
    </div>

  
</div>

    <div class="field bug_modal"
    id="field-target_milestone"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#target_milestone" id="target_milestone-help-link" class="help">Milestone:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-target_milestone">
            84 Branch

        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-cf_fx_iteration" style="display:none"
>
    <div class="name">
      Iteration:
    </div>



  
    <div class="value">
        <span id="field-value-cf_fx_iteration">
            ---

        </span>
    </div>

  
</div>


      <div class="field bug_modal edit-show" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide#Project_Flags" id="-help-link" class="help">Project Flags:
        </a>
    </div>



  
    <div class=" container"><div class="flags edit-show" style="display:none">
  <table class="layout-table tracking-flags">
      <tr>
        <td class="tracking-flag-name">a11y-review</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_a11y_review_project_flag-dirty">
  <select id="cf_a11y_review_project_flag" name="cf_a11y_review_project_flag">
        <option value="---"
          id="v4876_cf_a11y_review_project_flag" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">Accessibility Severity</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_accessibility_severity-dirty">
  <select id="cf_accessibility_severity" name="cf_accessibility_severity">
        <option value="---"
          id="v6045_cf_accessibility_severity" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">Performance Impact</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_performance_impact-dirty">
  <select id="cf_performance_impact" name="cf_performance_impact">
        <option value="---"
          id="v5427_cf_performance_impact" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">Size Estimate</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_size_estimate-dirty">
  <select id="cf_size_estimate" name="cf_size_estimate">
        <option value="---"
          id="v7004_cf_size_estimate" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">Webcompat Priority</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_webcompat_priority-dirty">
  <select id="cf_webcompat_priority" name="cf_webcompat_priority">
        <option value="---"
          id="v4274_cf_webcompat_priority" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">Webcompat Score</td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_webcompat_score-dirty">
  <select id="cf_webcompat_score" name="cf_webcompat_score">
        <option value="---"
          id="v6757_cf_webcompat_score" selected
        >---
        </option>
  </select></td>
      </tr>
  </table>
</div>
    </div>

  
</div>
</div><div class="fields-rhs">

      <div class="field tracking-flags-wrapper"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide#Tracking_Flags" id="-help-link" class="help">Tracking Flags:
        </a>
    </div>



  
    <div class=" container"><div class="flags edit-hide">
    <table class="layout-table tracking-flags">
        <tr>
          <th></th>
          <th>Tracking</th>
          <th>Status</th>
        </tr>
        <tr>
          <td class="tracking-flag-name">firefox84</td>
            <td class="tracking-flag-tracking">---
            </td>
          <td class="tracking-flag-status">
              <a href="/buglist.cgi?f1=cf_status_firefox84&amp;o1=equals&amp;v1=fixed">fixed</a>
          </td>
        </tr>
    </table>
  </div>


<div class="flags edit-show" style="display:none">
  <table class="layout-table tracking-flags">
      <tr>
        <th></th>
        <th>Tracking</th>
        <th>Status</th>
      </tr>
      <tr>
        <td class="tracking-flag-name">relnote-firefox</td>
          <td class="tracking-flag-tracking"></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_tracking_firefox_relnote-dirty">
  <select id="cf_tracking_firefox_relnote" name="cf_tracking_firefox_relnote">
        <option value="---"
          id="v539_cf_tracking_firefox_relnote" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">thunderbird_esr115</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_thunderbird_esr115-dirty">
  <select id="cf_tracking_thunderbird_esr115" name="cf_tracking_thunderbird_esr115">
        <option value="---"
          id="v6094_cf_tracking_thunderbird_esr115" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_thunderbird_esr115-dirty">
  <select id="cf_status_thunderbird_esr115" name="cf_status_thunderbird_esr115">
        <option value="---"
          id="v6100_cf_status_thunderbird_esr115" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">thunderbird_esr140</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_thunderbird_esr140-dirty">
  <select id="cf_tracking_thunderbird_esr140" name="cf_tracking_thunderbird_esr140">
        <option value="---"
          id="v7067_cf_tracking_thunderbird_esr140" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_thunderbird_esr140-dirty">
  <select id="cf_status_thunderbird_esr140" name="cf_status_thunderbird_esr140">
        <option value="---"
          id="v7098_cf_status_thunderbird_esr140" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">thunderbird_esr153</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_thunderbird_esr153-dirty">
  <select id="cf_tracking_thunderbird_esr153" name="cf_tracking_thunderbird_esr153">
        <option value="---"
          id="v7594_cf_tracking_thunderbird_esr153" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_thunderbird_esr153-dirty">
  <select id="cf_status_thunderbird_esr153" name="cf_status_thunderbird_esr153">
        <option value="---"
          id="v7613_cf_status_thunderbird_esr153" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox-esr115</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox_esr115-dirty">
  <select id="cf_tracking_firefox_esr115" name="cf_tracking_firefox_esr115">
        <option value="---"
          id="v6079_cf_tracking_firefox_esr115" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox_esr115-dirty">
  <select id="cf_status_firefox_esr115" name="cf_status_firefox_esr115">
        <option value="---"
          id="v6084_cf_status_firefox_esr115" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox-esr140</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox_esr140-dirty">
  <select id="cf_tracking_firefox_esr140" name="cf_tracking_firefox_esr140">
        <option value="---"
          id="v7040_cf_tracking_firefox_esr140" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox_esr140-dirty">
  <select id="cf_status_firefox_esr140" name="cf_status_firefox_esr140">
        <option value="---"
          id="v7057_cf_status_firefox_esr140" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox-esr153</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox_esr153-dirty">
  <select id="cf_tracking_firefox_esr153" name="cf_tracking_firefox_esr153">
        <option value="---"
          id="v7578_cf_tracking_firefox_esr153" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox_esr153-dirty">
  <select id="cf_status_firefox_esr153" name="cf_status_firefox_esr153">
        <option value="---"
          id="v7583_cf_status_firefox_esr153" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox84</td>
          <td class="tracking-flag-tracking"></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox84-dirty">
  <select id="cf_status_firefox84" name="cf_status_firefox84">
        <option value="fixed"
          id="v4978_cf_status_firefox84" selected
        >fixed
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox156</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox156-dirty">
  <select id="cf_tracking_firefox156" name="cf_tracking_firefox156">
        <option value="---"
          id="v7677_cf_tracking_firefox156" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox156-dirty">
  <select id="cf_status_firefox156" name="cf_status_firefox156">
        <option value="---"
          id="v7682_cf_status_firefox156" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox157</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox157-dirty">
  <select id="cf_tracking_firefox157" name="cf_tracking_firefox157">
        <option value="---"
          id="v7709_cf_tracking_firefox157" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox157-dirty">
  <select id="cf_status_firefox157" name="cf_status_firefox157">
        <option value="---"
          id="v7714_cf_status_firefox157" selected
        >---
        </option>
  </select></td>
      </tr>
      <tr>
        <td class="tracking-flag-name">firefox158</td>
          <td class="tracking-flag-tracking"><input type="hidden" id="cf_tracking_firefox158-dirty">
  <select id="cf_tracking_firefox158" name="cf_tracking_firefox158">
        <option value="---"
          id="v7738_cf_tracking_firefox158" selected
        >---
        </option>
  </select></td>
        <td class="tracking-flag-status"><input type="hidden" id="cf_status_firefox158-dirty">
  <select id="cf_status_firefox158" name="cf_status_firefox158">
        <option value="---"
          id="v7743_cf_status_firefox158" selected
        >---
        </option>
  </select></td>
      </tr>
  </table>
</div>
    </div>

  
</div>

</div>
  </div>
</section>



<section class="module" id="module-people"
>
    <header id="module-people-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse People section"
           data-label-collapsed="Expand People section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-people-content"
             aria-expanded="false"
             aria-labeledby="module-people-title"
             aria-describedby="module-people-subtitle"></div>
        <h2 class="module-title" id="module-people-title">People</h2>
          <h3 class="module-subtitle" id="module-people-subtitle">
            (Reporter: jujjyl, Assigned: valentin)
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-people-content" style="display:none"
  ><div class="fields-lhs">

    <div class="field bug_modal edit-hide"
    id="field-assigned_to"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#assigned_to" id="assigned_to-help-link" class="help">Assignee:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-assigned_to"><div class="vcard vcard_415378" ><img src="https://secure.gravatar.com/avatar/dedff9d4500fcbc5cdd1cd270f044b33?d=mm&size=40" class="gravatar" width="20" height="20"> <a class="email " href="/user_profile?user_id=415378" > <span class="fna">valentin</span></a>
</div>
        </span>
    </div>

  
</div><div class="field bug_modal edit-show"
    id="field-assigned_to" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#assigned_to" id="assigned_to-help-link" class="help">Assignee:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-assigned_to">
      <div class="set-default-container" style="display:none">
        <input type="checkbox" id="set-default-assignee" name="set_default_assignee" class="set-default"
          value="1" data-for="assigned_to">
        <label for="set-default-assignee">Reset Assignee to default</label>
      </div>
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-bug_mentors" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#bug_mentor" id="bug_mentors-help-link" class="help">Mentors:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-bug_mentors">---
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-qa_contact" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#qa_contact" id="qa_contact-help-link" class="help">QA Contact:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-qa_contact">
        <div class="set-default-container" style="display:none">
          <input type="checkbox" id="set-default-qa-contact" name="set_default_qa_contact" class="set-default"
            value="1" data-for="qa_contact">
          <label for="set-default-qa-contact">Reset QA Contact to default</label>
        </div>
        </span>
    </div>

  
</div>
</div><div class="fields-rhs">

    <div class="field bug_modal"
    id="field-reporter"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#reporter" id="reporter-help-link" class="help">Reporter:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-reporter">
            <div class="vcard vcard_467991" ><img src="https://secure.gravatar.com/avatar/6e5c7ba24b50106c443ffdc1886d3641?d=mm&size=40" class="gravatar" width="20" height="20"> <a class="email " href="/user_profile?user_id=467991" > <span class="fna">jujjyl</span></a>
</div>

        </span>
    </div>

  
</div>


    <div class="field bug_modal"
    id="field-triage_owner"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#triage_owner" id="triage_owner-help-link" class="help">Triage Owner:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-triage_owner">
            <div class="vcard vcard_11539" ><img src="https://secure.gravatar.com/avatar/ae002109ba1cfbb7f5ad990cc5d9fbaf?d=mm&size=40" class="gravatar" width="20" height="20"> <a class="email " href="/user_profile?user_id=11539" > <span class="fna">jesup</span></a>
</div>

        </span>
    </div>

  
</div>

    

    <div class="field bug_modal"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#cc" id="-help-link" class="help">CC:
        </a>
    </div>



  
    <div class=" container">


        <span aria-owns="cc-summary cc-latch">
          <span role="button" tabindex="0" id="cc-summary" data-count="1">1 person
          </span>
        </span>


        <div id="cc-list" style="display:none"></div>
    </div>

  
</div>
</div>
  </div>
</section>


<section class="module edit-show" style="display:none" id="module-references"
>
    <header id="module-references-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse References section"
           data-label-collapsed="Expand References section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-references-content"
             aria-expanded="false"
             aria-labeledby="module-references-title"
             aria-describedby="module-references-subtitle"></div>
        <h2 class="module-title" id="module-references-title">References</h2>
      </div>
    </header>
  <div class="module-content" id="module-references-content" style="display:none"
  >
<div class="fields-lhs">
    
    <div id="dependency-list-container" class="edit-show" ><div class="field bug_modal bug-list edit-show"
    id="field-dependson" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#dependson" id="dependson-help-link" class="help">Depends on:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-dependson">
        ---
        </span>
    </div>

  
</div><div class="field bug_modal bug-list edit-show"
    id="field-blocked" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#blocks" id="blocked-help-link" class="help">Blocks:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-blocked">
        ---
        </span>
    </div>

  
</div>
    </div>

    <div class="field bug_modal bug-list edit-show"
    id="field-regresses" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#regresses" id="regresses-help-link" class="help">Regressions:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-regresses">
        ---
        </span>
    </div>

  
</div><div class="field bug_modal bug-list edit-show"
    id="field-regressed_by" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#regressed_by" id="regressed_by-help-link" class="help">Regressed by:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-regressed_by">
        ---
        </span>
    </div>

  
</div>

    
</div><div class="fields-rhs">

    <div class="field bug_modal edit-show"
    id="field-bug_file_loc" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#bug_file_loc" id="bug_file_loc-help-link" class="help">URL:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-bug_file_loc"><div class="link">
      <span class="bug-url"
        title=""></span>
  </div>
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-see_also" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#see_also" id="see_also-help-link" class="help">See Also:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-see_also">
        ---
        </span>
    </div>

  
</div>
</div>
  </div>
</section>


<section class="module" id="module-details"
>
    <header id="module-details-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Details section"
           data-label-collapsed="Expand Details section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-details-content"
             aria-expanded="false"
             aria-labeledby="module-details-title"
             aria-describedby="module-details-subtitle"></div>
        <h2 class="module-title" id="module-details-title">Details</h2>
          <h3 class="module-subtitle" id="module-details-subtitle">
            (Whiteboard: [necko-triaged])
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-details-content" style="display:none"
  ><div class="fields-lhs">

    <div class="field bug_modal edit-show"
    id="field-alias" style="display:none"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#alias" id="alias-help-link" class="help">Alias:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-alias">
        ---
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-keywords" style="display:none"
>
    <div class="name">
      
        <a href="/describekeywords.cgi" id="keywords-help-link" class="help">Keywords:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-keywords">---
        </span>
    </div>

  
</div>

    <div class="field bug_modal"
    id="field-status_whiteboard"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/Whiteboard" id="status_whiteboard-help-link" class="help">Whiteboard:
        </a>
    </div>



  
    <div class="value">
        <span id="field-value-status_whiteboard">[necko-triaged]
        </span>
    </div>

  
</div><div class="field bug_modal edit-show"
    id="field-cf_qa_whiteboard" style="display:none"
>
    <div class="name">
      QA Whiteboard:
    </div>



  
    <div class="value">
        <span id="field-value-cf_qa_whiteboard">
        ---
        </span>
    </div>

  
</div>

    <div class="field bug_modal edit-show"
    id="field-cf_has_str" style="display:none"
>
    <div class="name">
      Has STR:
    </div>



  
    <div class="value">
        <span id="field-value-cf_has_str">
            ---

        </span>
    </div>

  
</div><div class="field bug_modal edit-show"
    id="field-cf_cab_review" style="display:none"
>
    <div class="name">
      Change Request:
    </div>



  
    <div class="value">
        <span id="field-value-cf_cab_review">
            ---

        </span>
    </div>

  
</div>

    <div class="field bug_modal"
    id="field-votes"
>
    <div class="name">
      
        <a href="https://wiki.mozilla.org/BMO/UserGuide/BugFields#votes" id="votes-help-link" class="help">Votes:
        </a>
    </div>



  
    <div class=" container">
        <span id="field-value-votes">0
        </span>
    </div>

  
</div>
</div><div class="fields-rhs">

    <div class="field bug_modal edit-show"
    id="field-bug_flags" style="display:none"
>
    <div class="name">
      Bug Flags:
    </div>



  
    <div class=" container">
        <span id="field-value-bug_flags"><div id="bug-flags" class="flags">
  <table class="layout-table">
    <tbody class="edit-show" style="display:none"><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Is this bug/feature enabled in a release by a pref flag?" for="flag_type-930">behind-pref</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-930-dirty">
      <select id="flag_type-930" name="flag_type-930"
        title="Is this bug/feature enabled in a release by a pref flag?"
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>


  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Flag tracking inclusion in the desktop Firefox product backlog." for="flag_type-846">firefox-backlog</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-846-dirty">
      <select id="flag_type-846" name="flag_type-846"
        title="Flag tracking inclusion in the desktop Firefox product backlog."
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>


  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Flag is used to track security bug bounty nominations. Mail security(at)mozilla.org to nominate a bug." for="flag_type-803">sec-bounty</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-803-dirty">
      <select id="flag_type-803" name="flag_type-803"
        title="Flag is used to track security bug bounty nominations. Mail security(at)mozilla.org to nominate a bug."
        class="bug-flag">
          <option value="X"></option>
            <option value="?" >?</option>
      </select>
    </td>


  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Flag is used to track whether the bug report is eligible for inclusion in the Bug Bounty Hall of Fame." for="flag_type-913">sec-bounty-hof</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-913-dirty">
      <select id="flag_type-913" name="flag_type-913"
        title="Flag is used to track whether the bug report is eligible for inclusion in the Bug Bounty Hall of Fame."
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>


  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Whether the bug has a testcase in the qa test suite or not. Set it to &quot;in-qa-testsuite?&quot; if the bug needs a testcase (only set this if the bug actually *needs* a testcase - not all bugs do, even layout bugs!), set it to &quot;in-qa-testsuite+&quot; if the bug has an appropriate testcase, and set it to &quot;in-qa-testsuite-&quot; if the bug doesn't need an explicit testcase (e.g. for code cleanup bugs). Only QA actively working on test cases in the component should use this keyword." for="flag_type-787">in-qa-testsuite</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-787-dirty">
      <select id="flag_type-787" name="flag_type-787"
        title="Whether the bug has a testcase in the qa test suite or not. Set it to &quot;in-qa-testsuite?&quot; if the bug needs a testcase (only set this if the bug actually *needs* a testcase - not all bugs do, even layout bugs!), set it to &quot;in-qa-testsuite+&quot; if the bug has an appropriate testcase, and set it to &quot;in-qa-testsuite-&quot; if the bug doesn't need an explicit testcase (e.g. for code cleanup bugs). Only QA actively working on test cases in the component should use this keyword."
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>

      <td class="flag-requestee">
        <div id="requestee_type-787-container" style="display:none"><input
    name="requestee_type-787"
    value="" class="requestee bz_autocomplete_user"  id="requestee_type-787" 
  >
        </div>
      <td>

  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="Whether the bug has a testcase in the test suite or not. Set it to &quot;in-testsuite?&quot; if the bug needs a testcase (only set this if the bug actually *needs* a testcase - not all bugs do, even layout bugs!), set it to &quot;in-testsuite+&quot; if the bug has an appropriate testcase, and set it to &quot;in-testsuite-&quot; if the bug doesn't need an explicit testcase (e.g. for code cleanup bugs). Only QA actively working on test cases in the component should use this keyword." for="flag_type-37">in-testsuite</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-37-dirty">
      <select id="flag_type-37" name="flag_type-37"
        title="Whether the bug has a testcase in the test suite or not. Set it to &quot;in-testsuite?&quot; if the bug needs a testcase (only set this if the bug actually *needs* a testcase - not all bugs do, even layout bugs!), set it to &quot;in-testsuite+&quot; if the bug has an appropriate testcase, and set it to &quot;in-testsuite-&quot; if the bug doesn't need an explicit testcase (e.g. for code cleanup bugs). Only QA actively working on test cases in the component should use this keyword."
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>


  </tr><tr>
    <td class="flag-setter">
    </td>

    <td class="flag-name">
      <label title="qe-verify: + ➜ request to verify the bug manually
qe-verify: – ➜ the bug will not/can not be verified manually" for="flag_type-864">qe-verify</label>
    </td>

    <td class="flag-value">
      <input type="hidden" id="flag_type-864-dirty">
      <select id="flag_type-864" name="flag_type-864"
        title="qe-verify: + ➜ request to verify the bug manually
qe-verify: – ➜ the bug will not/can not be verified manually"
          disabled
        class="bug-flag">
          <option value="X"></option>
      </select>
    </td>


  </tr>
    </tbody>
  </table>
</div>
        </span>
    </div>

  
</div>
</div>

  
  </div>
</section>


<section class="module edit-show" style="display:none" id="module-crash-data"
>
    <header id="module-crash-data-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Crash Data section"
           data-label-collapsed="Expand Crash Data section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-crash-data-content"
             aria-expanded="false"
             aria-labeledby="module-crash-data-title"
             aria-describedby="module-crash-data-subtitle"></div>
        <h2 class="module-title" id="module-crash-data-title">Crash Data</h2>
      </div>
    </header>
  <div class="module-content" id="module-crash-data-content" style="display:none"
  ><div class="field bug_modal edit-show"
    id="field-cf_crash_signature" style="display:none"
>
    <div class="name">
      Signature:
    </div>



  
    <div class="value">
        <span id="field-value-cf_crash_signature">
    <em>None</em>
        </span>
    </div>

  
</div>
  </div>
</section>


<section class="module edit-show" style="display:none" id="module-security"
>
    <header id="module-security-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Security section"
           data-label-collapsed="Expand Security section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-security-content"
             aria-expanded="false"
             aria-labeledby="module-security-title"
             aria-describedby="module-security-subtitle"></div>
        <h2 class="module-title" id="module-security-title">Security</h2>
          <h3 class="module-subtitle" id="module-security-subtitle">
            (public)
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-security-content" style="display:none"
  ><div class="groups edit-hide">
    This bug is publicly visible.
</div>

<div class="groups edit-show" style="display:none">


</div>
  </div>
</section>


<section class="module edit-show" style="display:none" id="module-user-story" data-non-stick="1"
>
    <header id="module-user-story-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse User Story section"
           data-label-collapsed="Expand User Story section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-user-story-content"
             aria-expanded="false"
             aria-labeledby="module-user-story-title"
             aria-describedby="module-user-story-subtitle"></div>
        <h2 class="module-title" id="module-user-story-title">User Story</h2>
      </div>
    </header>
  <div class="module-content" id="module-user-story-content" style="display:none"
  >
    <pre id="user-story"></pre>
  </div>
</section>







<section class="module" id="module-attachments"
>
    <header id="module-attachments-header" class="module-header">
      <div class="module-latch"
           data-label-expanded="Collapse Attachments section"
           data-label-collapsed="Expand Attachments section">
        <div class="module-spinner" role="button" tabindex="0"
             aria-controls="module-attachments-content"
             aria-expanded="true"
             aria-labeledby="module-attachments-title"
             aria-describedby="module-attachments-subtitle"></div>
        <h2 class="module-title" id="module-attachments-title">Attachments</h2>
          <h3 class="module-subtitle" id="module-attachments-subtitle">
            (2 files)
          </h3>
      </div>
    </header>
  <div class="module-content" id="module-attachments-content"
  ><table role="table" class="responsive" id="attachments">
    <tr data-attachment-id="9181028" class="
    " >
      <td class="attach-desc-td">
        <div class="attach-desc">
          <a href="/attachment.cgi?id=9181028" > build_webgl_release_brotli.zip
            </a>
        </div>
        <div>
            <a href="#c0" class="attach-time activity-ref"><span class="rel-time" title="2020-10-12 06:56 PDT" data-time="1602510963">5 years ago</span></a>
          <span class="attach-author"><div class="vcard vcard_467991" ><a class="email " href="/user_profile?user_id=467991" > <span class="fna">Jukka Jylänki</span></a>
</div></span>
        </div>
        <div class="attach-info">2.32 MB,
          application/x-zip-compressed        </div>
      </td>
      <td></td>
      <td class="attach-actions">
        <a href="/attachment.cgi?id=9181028&amp;action=edit" data-details="1">Details</a>
    </tr>
    <tr data-attachment-id="9182306" class=" attach-patch
    " >
      <td class="attach-desc-td">
        <div class="attach-desc">
          <a href="/attachment.cgi?id=9182306" > Bug 1670675 - Add test for loading brotli encoded files over unsecured HTTP r=#necko
            </a>
        </div>
        <div>
            <a href="#c2" class="attach-time activity-ref"><span class="rel-time" title="2020-10-19 02:39 PDT" data-time="1603100375">5 years ago</span></a>
          <span class="attach-author"><div class="vcard vcard_415378" ><a class="email " href="/user_profile?user_id=415378" > <span class="fna">Valentin Gosu [:valentin]</span></a>
</div></span>
        </div>
        <div class="attach-info">47 bytes,
          text/x-phabricator-request        </div>
      </td>
      <td></td>
      <td class="attach-actions">
        <a href="/attachment.cgi?id=9182306&amp;action=edit" data-details="1">Details</a>&#x0020; |
  <a href="/attachment.cgi?id=9182306">Review</a>
    </tr>
</table>

<footer id="attachments-footer">
  <div id="attachments-actions">
  </div>
  
</footer>
  </div>
</section>



<script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB">
  init_module_visibility();
</script>




<meta name="firefox-versions" content="{&quot;FIREFOX_AURORA&quot;:&quot;&quot;,&quot;FIREFOX_DEVEDITION&quot;:&quot;156.0b5&quot;,&quot;FIREFOX_ESR&quot;:&quot;140.15.0esr&quot;,&quot;FIREFOX_ESR115&quot;:&quot;115.40.0esr&quot;,&quot;FIREFOX_ESR_NEXT&quot;:&quot;153.2.0esr&quot;,&quot;FIREFOX_NIGHTLY&quot;:&quot;158.0a1&quot;,&quot;LAST_MERGE_DATE&quot;:&quot;2026-09-10&quot;,&quot;LAST_RELEASE_DATE&quot;:&quot;2026-09-11&quot;,&quot;LAST_STRINGFREEZE_DATE&quot;:&quot;2026-09-09&quot;,&quot;LATEST_FIREFOX_DEVEL_VERSION&quot;:&quot;156.0b5&quot;,&quot;LATEST_FIREFOX_OLDER_VERSION&quot;:&quot;3.6.28&quot;,&quot;LATEST_FIREFOX_RELEASED_DEVEL_VERSION&quot;:&quot;156.0b5&quot;,&quot;LATEST_FIREFOX_VERSION&quot;:&quot;155.0.1&quot;,&quot;NEXT_MERGE_DATE&quot;:&quot;2026-09-24&quot;,&quot;NEXT_RELEASE_DATE&quot;:&quot;2026-09-25&quot;,&quot;NEXT_STRINGFREEZE_DATE&quot;:&quot;2026-09-23&quot;}">


<div id="comment-actions">
    <button type="button" id="bottom-btn" class="secondary" aria-label="Go to Page Bottom">Bottom &darr;</button>
  <div class="dropdown">
    <button type="button" id="comment-tags-btn" aria-haspopup="true" aria-label="Tags"
      aria-expanded="false" aria-controls="comment-tags-menu" class="dropdown-button minor">Tags &#9662;</button>
    <ul id="comment-tags-menu" role="menu" tabindex="0" class="dropdown-content left" style="display:none">
      <li role="presentation">
        <a role="menuitem" tabindex="-1" data-comment-tag="">Reset</a>
      </li>
    </ul>
  </div>
  <div class="dropdown">
    <button type="button" id="view-menu-btn" aria-haspopup="true" aria-label="Timeline"
      aria-expanded="false" aria-controls="view-menu" class="dropdown-button minor">Timeline &#9662;</button>
    <ul id="view-menu" role="menu" tabindex="0" class="dropdown-content left" style="display:none">
      <li role="presentation">
        <a id="view-reset" role="menuitem" tabindex="-1">Reset</a>
      </li>
      <li role="separator"></li>
      <li role="presentation">
        <a id="view-collapse-all" role="menuitem" tabindex="-1">Collapse All</a>
      </li>
      <li role="presentation">
        <a id="view-expand-all" role="menuitem" tabindex="-1">Expand All</a>
      </li>
      <li role="presentation">
        <a id="view-comments-only" role="menuitem" tabindex="-1">Comments Only</a>
      </li>
    </ul>
   </div>
</div>
<div class="change-set" id="c0"><div class="comment" data-id="15080303" data-no="0"
       data-tags="">
    
    <table class="layout-table change-head reporter" id="ch-0" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_467991" ><img src="https://secure.gravatar.com/avatar/6e5c7ba24b50106c443ffdc1886d3641?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_467991" ><a class="email " href="/user_profile?user_id=467991" > <span class="fna">Jukka Jylänki</span></a>
</div>
              <span class="user-role">Reporter</span>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-0"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-0" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c0">Description</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-12 06:56 PDT" data-time="1602510963">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-0">
        <td colspan="2" class="comment-tags">
        </td>
      </tr>
    </table>

    
  </div><div id="att-9181028"
         class="attachment"
         data-id="9181028" itemscope itemtype="http://schema.org/MediaObject">
      <meta itemprop="name" content="build_webgl_release_brotli.zip">
      <meta itemprop="contentSize" content="2428886">
      <meta itemprop="encodingFormat" content="application/x-zip-compressed">
      <div class="label">
        Attached file
          <a class="link" href="attachment.cgi?id=9181028" itemprop="contentUrl" >
        <span id="att-9181028-description" itemprop="description">build_webgl_release_brotli.zip</span></a>
        — <a href="attachment.cgi?id=9181028&amp;action=edit" itemprop="url" data-details="1">Details</a>
      </div>
    </div>

  <div
      class="comment-text markdown-body "
      id="ct-0" data-comment-id="15080303"><p>STR:</p>
<ol>
<li>Download attached file</li>
<li>Run start_adhoc_server.bat , which spawns an ad hoc web server on <a href="http://localhost:6931/" rel="nofollow noreferrer" target="_blank">http://localhost:6931/</a></li>
<li>Visit the site</li>
</ol>
<p>Observe that the page does not load, but fails on error</p>
<pre><code>Uncaught SyntaxError: illegal character
build_webgl_release_brotli.framework.js.br:1:1
Uncaught ReferenceError: unityFramework is not defined
    onload http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    d http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    d http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    u http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    createUnityInstance http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    createUnityInstance http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/Build/build_webgl_release_brotli.loader.js:1
    onload http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/:73
    EventHandlerNonNull* http://localhost:9001/CallJSFromCSharp/build_webgl_release_brotli/:72
build_webgl_release_brotli.loader.js:1:3167
</code></pre>
<p>The ad hoc web server delivers all files that have suffix &#39;.br&#39; with &quot;Content-Encoding: br&quot;.</p>
<p>Some observations:</p>
<ol>
<li>
<p>Firefox does not send HTTP Request Header <code>Accept-Encoding: br</code> along with the request, which suggests that Firefox does not support Brotli here. Maybe it is due to the ad hoc server not being HTTPS? Note that Chrome (and Chrome-based Edge) and Safari all support this. If HTTPS is the issue, can <a href="http://localhost:%EF%BF%BDany_port%3E/" rel="nofollow noreferrer" target="_blank">http://localhost:&lt;any_port&gt;/</a> and <a href="http://127.0.0.1:%EF%BF%BDany_port%3E/" rel="nofollow noreferrer" target="_blank">http://127.0.0.1:&lt;any_port&gt;/</a> domains be treated special and allowed to support Brotli?</p>
</li>
<li>
<p>Even when Firefox does not support Brotli, it still attempts to load the received files as bare uncompressed content(!) That is, Firefox well knows when receiving the file that it had <code>Content-Encoding: br</code>, so it is compressed with some unknown or unsupported compression. Why does it still attempt to parse the received file?</p>
</li>
</ol>
<p>That is, instead of an error</p>
<pre><code>Uncaught SyntaxError: illegal character
build_webgl_release_brotli.framework.js.br:1:1
</code></pre>
<p>Firefox should print something along the lines of</p>
<pre><code>Uncaught UnsupportedEncodingError: Content-Encoding: &#39;br&#39; is only supported over HTTPS protocol.
</code></pre>
<p>instead of pretending the file did not have any compression at all?</p>
<ol start="3">
<li>Please add a boolean pref <code>support.brotli.over.insecure.http</code> so that developers can use Firefox to develop Brotli-enabled pages. Needing to do HTTPS just to be able to locally develop is an insane ask for developers. Paired with (1.) above that would make Brotli development less painful.</li>
</ol>
<p>Or perhaps the &quot;Brotli is HTTPS only&quot; is a misinterpretation here, and the root cause of the bug is something else? (has Brotli support regressed?)</p>
</div></div><div class="change-set" id="c1"><div class="comment" data-id="15080775" data-no="1"
       data-tags="">
    
    <table class="layout-table change-head assignee" id="ch-1" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_415378" ><img src="https://secure.gravatar.com/avatar/dedff9d4500fcbc5cdd1cd270f044b33?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_415378" ><a class="email " href="/user_profile?user_id=415378" > <span class="fna">Valentin Gosu [:valentin]</span></a>
</div>
              <span class="user-role">Assignee</span>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-1"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-1" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c1">Comment 1</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-12 11:01 PDT" data-time="1602525716">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-1">
        <td colspan="2" class="comment-tags">
        </td>
      </tr>
    </table>

    
  </div><div
      class="comment-text markdown-body "
      id="ct-1" data-comment-id="15080775"><p>You are correct that brotli is HTTPS only.<br>
<a href="https://hacks.mozilla.org/2015/11/better-than-gzip-compression-with-brotli/#comment-19069" rel="nofollow noreferrer" target="_blank">https://hacks.mozilla.org/2015/11/better-than-gzip-compression-with-brotli/#comment-19069</a></p>
<p>I&#39;ll try to take a look at what fails there.<br>
You&#39;re right that we should be better at handling this issue.<br>
I&#39;ll try to take a look at why things are breaking tomorrow.</p>
</div></div><div class="change-set" id="c2"><div class="comment" data-id="15089728" data-no="2"
       data-tags="">
    
    <table class="layout-table change-head assignee" id="ch-2" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_415378" ><img src="https://secure.gravatar.com/avatar/dedff9d4500fcbc5cdd1cd270f044b33?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_415378" ><a class="email " href="/user_profile?user_id=415378" > <span class="fna">Valentin Gosu [:valentin]</span></a>
</div>
              <span class="user-role">Assignee</span>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-2"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-2" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c2">Comment 2</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-19 02:39 PDT" data-time="1603100375">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-2">
        <td colspan="2" class="comment-tags">
        </td>
      </tr>
    </table>

    
  </div><div id="att-9182306"
         class="attachment"
         data-id="9182306" itemscope itemtype="http://schema.org/MediaObject">
      <meta itemprop="name" content="phabricator-D93924-url.txt">
      <meta itemprop="contentSize" content="47">
      <meta itemprop="encodingFormat" content="text/x-phabricator-request">
      <div class="label">
        Attached file
          <a class="link" href="attachment.cgi?id=9182306" itemprop="contentUrl" >
        <span id="att-9182306-description" itemprop="description">Bug 1670675 - Add test for loading brotli encoded files over unsecured HTTP r=#necko</span></a>
        — <a href="attachment.cgi?id=9182306&amp;action=edit" itemprop="url" data-details="1">Details</a>
      </div>
    </div>

  <div
      class="comment-text markdown-body empty"
      id="ct-2" data-comment-id="15089728"></div></div><div class="change-set" id="a589412_600971"><div class="change" id="aa589412_600971">
    <table class="layout-table change-head " role="presentation">
      <tr>
        <td rowspan="2" class="change-gravatar"><div class="vcard vcard_600971" id="a589412_600971"><img src="https://secure.gravatar.com/avatar/a088418052679d9583556d277e6774ee?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
        </td>
        <td class="change-author"><div class="vcard vcard_600971" id="a589412_600971"><a class="email " href="/user_profile?user_id=600971" > <span class="fna">Phabricator Automation</span></a>
</div>
        </td>
        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="as-a589412_600971"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>
      <tr id="ar-a589412_600971">
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#a589412_600971">Updated</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-19 02:39 PDT" data-time="1603100375">5 years ago</span>
          </div>
        </td>
      </tr>
    </table>
  </div><div class="activity"><div class="change">Assignee: nobody &rarr; valentin.gosu</div><div class="change">Status: NEW &rarr; ASSIGNED</div></div></div><div class="change-set" id="c3"><div class="comment" data-id="15089731" data-no="3"
       data-tags="">
    
    <table class="layout-table change-head assignee" id="ch-3" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_415378" id="a589412_600971"><img src="https://secure.gravatar.com/avatar/dedff9d4500fcbc5cdd1cd270f044b33?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_415378" id="a589412_600971"><a class="email " href="/user_profile?user_id=415378" > <span class="fna">Valentin Gosu [:valentin]</span></a>
</div>
              <span class="user-role">Assignee</span>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-3"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-3" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c3">Comment 3</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-19 02:41 PDT" data-time="1603100469">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-3">
        <td colspan="2" class="comment-tags">
        </td>
      </tr>
    </table>

    
  </div><div
      class="comment-text markdown-body "
      id="ct-3" data-comment-id="15089731"><p>(In reply to Jukka Jylänki from <a class="bz_bug_link
          bz_status_RESOLVED bz_closed" href="/show_bug.cgi?id=1670675#c0" title="RESOLVED FIXED - Brotli compression does not work (at least on http://localhost/ ?)">comment #0</a>)</p>
<blockquote>
<ol start="3">
<li>Please add a boolean pref <code>support.brotli.over.insecure.http</code> so that developers can use Firefox to develop Brotli-enabled pages. Needing to do HTTPS just to be able to locally develop is an insane ask for developers. Paired with (1.) above that would make Brotli development less painful.</li>
</ol>
</blockquote>
<p>You can use the <code>network.http.accept-encoding</code> pref and set it to <code>gzip, deflate, br</code><br>
I&#39;m submitting a patch to make sure the pref works well, and to document this better for future uses.<br>
Thanks!</p>
</div><div class="activity"><div class="change">Severity: -- &rarr; S4</div><div class="change">Priority: -- &rarr; P3</div><div class="change">Whiteboard: [necko-triaged]</div></div></div><div class="change-set" id="c4"><div class="comment" data-id="15094904" data-no="4"
       data-tags="">
    
    <table class="layout-table change-head " id="ch-4" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_510726" id="a589412_600971"><img src="https://secure.gravatar.com/avatar/a9d6ca739b340c670a0fecbd2c36f516?d=mm&size=64" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_510726" id="a589412_600971"><a class="email " href="/user_profile?user_id=510726" > <span class="fna">Pulsebot</span></a>
</div>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-4"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-4" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c4">Comment 4</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-22 04:48 PDT" data-time="1603367333">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-4">
        <td colspan="2" class="comment-tags">
        </td>
      </tr>
    </table>

    
  </div><div
      class="comment-text  "
      id="ct-4" data-comment-id="15094904">Pushed by <a href="mailto:valentin.gosu&#64;gmail.com">valentin.gosu&#64;gmail.com</a>:
<a target="_blank" rel="nofollow noreferrer" href="https://hg.mozilla.org/integration/autoland/rev/fe1cffc8ac28">https://hg.mozilla.org/integration/autoland/rev/fe1cffc8ac28</a>
Add test for loading brotli encoded files over unsecured HTTP r=necko-reviewers,kershaw</div></div><div class="change-set" id="c5"><div class="comment" data-id="15095289" data-no="5"
       data-tags="bugherder">
    
    <table class="layout-table change-head " id="ch-5" role="presentation">
      <tr>
          <td rowspan="2" class="change-gravatar"><div class="vcard vcard_600553" id="a589412_600971"><img src="extensions/Gravatar/web/default.jpg" class="gravatar" width="32" height="32">
</div>
          </td>

          <td class="change-author"><div class="vcard vcard_600553" id="a589412_600971"><a class="email disabled" href="/user_profile?user_id=600553" > <span class="fna">Andreea Pavel [:apavel]</span></a>
</div>
          </td>

        <td rowspan="2" class="comment-actions"><div role="group">
          <button type="button" class="change-spinner ghost iconic" id="cs-5"
                  aria-label="Collapse" aria-expanded="true"
                  data-strings='{ "collapse_label": "Collapse", "expand_label": "Expanded" }'>
            <span class="icon" aria-hidden="true"></span>
          </button>
        </div></td>
      </tr>

      <tr id="cr-5" >
        <td>
          <h3 class="change-name">
            <a href="/show_bug.cgi?id=1670675#c5">Comment 5</a>
          </h3>
          &bull;
          <div class="change-time"><span class="rel-time" title="2020-10-22 08:02 PDT" data-time="1603378978">5 years ago</span>
          </div>
        </td>
      </tr>

      <tr id="ctag-5">
        <td colspan="2" class="comment-tags"><span class="comment-tag" data-tag="bugherder">bugherder
  </span>
        </td>
      </tr>
    </table>

    
  </div><div
      class="comment-text markdown-body "
      id="ct-5" data-comment-id="15095289"><p><a href="https://hg.mozilla.org/mozilla-central/rev/fe1cffc8ac28" rel="nofollow noreferrer" target="_blank">https://hg.mozilla.org/mozilla-central/rev/fe1cffc8ac28</a></p>
</div><div class="activity"><div class="change">Status: ASSIGNED &rarr; RESOLVED</div><div class="change">Closed: <span class="rel-time" title="2020-10-22 08:02 PDT" data-time="1603378978">5 years ago</span></div><div class="change">
          <a href="/buglist.cgi?f1=cf_status_firefox84&amp;o1=isnotempty">status-firefox84</a>:
          --- &rarr; <a href="/buglist.cgi?f1=cf_status_firefox84&amp;o1=equals&amp;v1=fixed">fixed</a></div><div class="change">Resolution: --- &rarr; FIXED</div><div class="change">Target Milestone: --- &rarr; 84 Branch</div></div></div><div id="new-comment-notice">
          You need to <a href="/show_bug.cgi?id=1670675&amp;GoAheadAndLogIn=1">log in</a>
          before you can comment on or make changes to this bug.
        </div>



<div id="bottom-actions">
  <div id="bottom-right-actions">
    <button type="button" id="top-btn" class="secondary" aria-label="Go to Page Top">Top &uarr;</button>
  </div>
</div>



<dialog id="att-overlay" class="readonly"
        aria-labelledby="att-overlay-title" data-attachment-count="2">
  <form method="dialog">
    <div class="header">
      <h2 id="att-overlay-title" class="title">Attachment</h2>
      <div class="spacer"></div>
      <button type="button" class="secondary iconic" hidden disabled data-action="prev"
              title="Previous Attachment" aria-keyshortcuts="ArrowLeft">
        <span class="icon" aria-hidden="true"></span>
      </button>
      <button type="button" class="secondary iconic" hidden disabled data-action="next"
              title="Next Attachment" aria-keyshortcuts="ArrowRight">
        <span class="icon" aria-hidden="true"></span>
      </button>
      <button type="button" class="secondary" data-action="toggle-details">Hide Details</button>
      <button type="button" class="secondary iconic" data-action="close" aria-label="Close">
        <span class="icon" aria-hidden="true"></span>
      </button>
    </div>
    <div class="body">
      <div class="sub-column">
        <div class="detail-pane">
          <section class="cols">
            <h3>General</h3>
            <div class="creator">
              Creator: <div class="vcard vcard_467991" ><a class="email " href="/user_profile?user_id=467991" > <span class="fna">Jukka Jylänki</span></a>
</div>
            </div>
            <div>Created: <span class="created-date rel-time"></span></div>
            <div>Updated: <span class="updated-date rel-time"></span></div>
            <div>Size: <span class="file-size"></span></div>
          </section>
          <section class="cols">
            <h3>
              <label for="att-overlay-description">Description</label>
            </h3>
            <div>
              <input type="text" name="description" disabled
                     id="att-overlay-description" class="flex">
            </div>
          </section>
          <section class="cols">
            <h3>
              <label for="att-overlay-file-name">File Name</label>
            </h3>
            <div>
              <input type="text" name="filename" disabled
                     id="att-overlay-file-name" class="flex">
            </div>
          </section>
          <section class="cols">
            <h3>
              <label for="att-overlay-content-type">Content Type</label>
            </h3>
              <div>
                <input type="text" name="contenttypeentry" disabled id="att-overlay-content-type"
                       class="flex">
              </div>
          </section>
          
        </div>
      </div>
      <div class="main-column">
        <div class="preview-pane">
          <div class="preview ">
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <button type="button" class="secondary" data-action="raw">Raw</button>
        <button type="button" class="secondary" disabled data-action="diff">Diff</button>
        <button type="button" class="secondary" disabled data-action="review"
                data-base="https://bugzilla.mozilla.org/page.cgi?id=splinter.html&amp;ignore=">Splinter Review</button>
      <div class="spacer"></div>
    </div>
  </form>
</dialog>
<link rel="stylesheet" href="/static/v20260908.1/extensions/FlagTypeComment/web/styles/ftc.css">
<script nonce="TV4g6Xg7KJK2XggfFRyjpcRTESq4gfLn1YxEPtcYoMKz8ZxB" src="/static/v20260908.1/extensions/FlagTypeComment/web/js/ftc.js"></script></div> 
</main> 
</div> 


</body>
</html>