<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
<meta property="og:type" content="website">
<meta property="og:title" content="Bugzilla QuickSearch">

    

    <meta name="viewport"
          content="width=1024">
    <meta name="color-scheme" content="dark light">
    <meta name="generator" content="Bugzilla 20260908.1">
    <meta name="bugzilla-global" content="dummy"
        id="bugzilla-global" data-bugzilla="{&quot;api_token&quot;:&quot;&quot;,&quot;config&quot;:{&quot;basepath&quot;:&quot;\/&quot;,&quot;cookie_consent_enabled&quot;:true,&quot;cookie_consent_required&quot;:false,&quot;essential_cookies&quot;:[&quot;bugzilla&quot;,&quot;Bugzilla_login&quot;,&quot;Bugzilla_logincookie&quot;,&quot;Bugzilla_login_request_cookie&quot;,&quot;github_state&quot;,&quot;github_token&quot;,&quot;mfa_verification_token&quot;,&quot;moz-consent-pref&quot;,&quot;sudo&quot;],&quot;urlbase&quot;:&quot;https:\/\/bugzilla.mozilla.org\/&quot;},&quot;constant&quot;:{&quot;CGI_URI_LIMIT&quot;:8000,&quot;COMMENT_COLS&quot;:80},&quot;param&quot;:{&quot;allow_attachment_display&quot;:true,&quot;maxattachmentsize&quot;:&quot;10240&quot;,&quot;maxusermatches&quot;:&quot;50&quot;,&quot;splinter_base&quot;:&quot;\/page.cgi?id=splinter.html&amp;ignore=\/&quot;,&quot;use_markdown&quot;:true},&quot;string&quot;:{&quot;bug&quot;:&quot;bug&quot;,&quot;bug_type_required&quot;:&quot;You must select a Type for this bug&quot;,&quot;component_required&quot;:&quot;You must select a Component for this bug&quot;,&quot;description_required&quot;:&quot;You must enter a Description for this bug&quot;,&quot;short_desc_required&quot;:&quot;You must enter a Summary for this bug&quot;,&quot;version_required&quot;:&quot;You must select a Version for this bug&quot;},&quot;user&quot;:{&quot;cookie_consent&quot;:&quot;&quot;,&quot;is_new&quot;:true,&quot;login&quot;:&quot;&quot;}}">
    <meta name="google-site-verification" content="JYXIuR9cAlV7fLmglSrc_4UaJS6Wzh5Mdxiorqu5AQc" />
    <title>Bugzilla QuickSearch</title>

<link rel="Top" href="/">

<link href="/static/v20260908.1/skins/standard/global.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/page.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-structure-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/js/jquery/ui/jquery-ui-theme-min.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/lib/prism.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/skins/standard/consent.css" rel="stylesheet" type="text/css"><link href="/static/v20260908.1/extensions/Review/web/styles/badge.css" rel="stylesheet" type="text/css">



    
<script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/jquery/jquery-min.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/jquery/ui/jquery-ui-min.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/jquery/plugins/devbridgeAutocomplete/devbridgeAutocomplete-min.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/global.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/util.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/widgets.js"></script>

      <script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r">BUGZILLA.value_descs = JSON.parse('{\"bug_status\":{},\"resolution\":{\"\":\"---\"}}');

      </script>
<script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/lib/prism.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/consent.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/cookie-helper.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/js/lib/md5.min.js"></script><script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r" src="/static/v20260908.1/extensions/Review/web/js/badge.js"></script>

    

    
    <link href="/static/v20260908.1/skins/lib/fontawesome.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-brands.min.css" rel="stylesheet" type="text/css">
    <link href="/static/v20260908.1/skins/lib/fontawesome-solid.min.css" rel="stylesheet" type="text/css">

    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla@Mozilla" href="/search_plugin.cgi"><link rel="shortcut icon" href="/extensions/BMO/web/images/favicon.ico">
<link rel="icon" type="image/svg+xml" href="/extensions/BMO/web/images/favicon.svg"><meta name="robots" content="noarchive">
  </head>



  <script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r">
  $(function() { document.forms['f'].quicksearch.focus() });
  </script>
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
    <input type="hidden" name="github_token" value="KBcuuRQd4t9f14XB7QhgHAqKdF1xdAr7qexg9AWUFLycYUo7VeieyDpa7TkqA9xDyiCpd3n9uiznOSnyL8SwzF4Vs2hi2eymS2Hhmq8uRzqnU8iIXyHBq8fCHknnV66LeZ2j9nWB07SG6fhknlGFIyr5WO1dyyrAidOP7a2tD6y4uakh8PZhmlBukc6lhaS3nxHuGXuFylCqG51NpXA3yMOb118HHyHs8RAmMjh36fY5BnWsmFFcdjkbCcKRGg6C">
    <input type="hidden" name="target_uri" value="https://bugzilla.mozilla.org/page.cgi">
    <button type="submit">
      <i class="fab fa-github"></i> Log In with GitHub
    </button>
  </form>

    <div class="method-separator">or</div>

  <form action="/page.cgi?id=quicksearch.html" method="POST"
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
           value="1789094988-1W1cu96QThp9YkDm0QqAogi99lpES-3SPQ-i8n7S6WA">
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
    <input type="hidden" id="token_top" name="token" value="1789094988-PC5zh5Vb4FxU4iqTKRnGf5I-7ss63KmSRagKnjJDO0Y">
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


<p>Type in one or more words (or pieces of words) to search for:</p>

<form name="f" action="/buglist.cgi" method="get"
      class='quicksearch_check_empty' data-no-csrf>
  <input type="text" size="40" name="quicksearch">
  <input type="submit" value="Search" id="find">
</form>

<ul>
  <li><a href="#basics">The Basics</a></li>
  <li><a href="#basic_examples">Examples of Simple Queries</a></li>
  <li><a href="#fields">Fields You Can Search On</a></li>
  <li><a href="#advanced_features">Advanced Features</a></li>
  <li><a href="#shortcuts">Advanced Shortcuts</a></li>
  <li><a href="#advanced_examples">Examples of Complex Queries</a></li>
</ul>


<h2 id="intro">"Is this going to be a stand-up fight, sir, or another bug hunt?"</h2>
<ul>
  <li>Private First Class William L. Hudson, "<i>Aliens</i>".</li>
</ul>

<p>This is an overview of how to effectively use search in Bugzilla.
  For more general information about Bugzilla usage, including the jargon and
  shorthand that the Mozilla community uses in bug discussions, please look at
  <a href="https://wiki.mozilla.org/Introduction_to_Bugzilla">Introduction toBugzilla</a> page on <a href="https://wiki.mozilla.org/">Wiki.m.o</a>.</p>

<h2 id="basics">The Basics</h2>

<ul class="qs_help">
  <li>If you just put a word or series of words in the search box,
    Bugzilla will search the
    Product,
    Component,
    Keywords,
    Alias,
    Summary,
    Whiteboard,
    and Comment fields for your word or words.</li>

  <li>Typing just a <strong>number</strong> in the search box will take
    you directly to the bug with that ID.
      Also, just typing the <strong>alias</strong> of a bug
      will take you to that bug.
  </li>

  <li>Adding more terms <strong>narrows down</strong> the search, it does not
     expand it. (In other words, Bugzilla searches for
     bugs that match <em>all</em> your criteria, not
     bugs that match <em>any</em> of your criteria.)</li>

  <li>Searching is <strong>case-insensitive</strong>. So <kbd>table</kbd>,
    <kbd>Table</kbd>, and <kbd>TABLE</kbd> are all the same.</li>

  <li>Bugzilla does not just search for the exact word you put in,
    but also for any word that <strong>contains</strong> that word.
    So, for example, searching for "cat" would also find bugs
    that contain it as part of other words&mdash;for example, a bug
    mentioning "<strong>cat</strong>ch" or "certifi<strong>cat</strong>e". It
    will not find partial words in the Comment
    or Keywords fields,
    though&mdash;only full words are matched, there.</li>

  <li>By default, only <strong>open</strong> bugs are
    searched. If you want to know how to also search closed bugs,
    see the <a href="#shortcuts">Advanced Shortcuts</a> section.</li>

  <li>If you want to search <strong>specific fields</strong>, you do it like
    <kbd>field:value</kbd>, where <kbd>field</kbd> is one of the
    <a href="#fields">field names</a> lower down in this
    document and <kbd>value</kbd> is the value you want to search for
    in that field. If you put commas in the <kbd>value</kbd>, then it is
    interpreted as a list of values, and bugs that match
    <em>any</em> of those values will be searched for.</li>
</ul>

<h2 id="basic_examples">Examples of Simple Queries</h2>

<p>Here are some examples of how to write some simple queries.
  <a href="#advanced_examples">Examples for more complex queries</a> can be
  found lower in this page.</p>

<ul class="qs_help">
  <li>All open bugs where userA@company.com is in the CC list
    (no need to mention open bugs, this is the default):<br>
    <kbd>cc:userA@company.com</kbd></li>
  <li>All unconfirmed bugs in product productA (putting the
    bug status at the first position make it being automatically
    considered as a bug status):<br>
    <kbd>UNCONFIRMED product:productA</kbd>
  <li>All open and closed bugs reported by userB@company.com
    (we must specify ALL as the first word, else only open bugs
    are taken into account):<br>
    <kbd>ALL reporter:userB@company.com</kbd>
  <li>All open bugs with severity blocker or critical with the
    target milestone set to 2.5:<br>
    <kbd>severity:blocker,critical milestone:2.5</kbd>
  <li>All open bugs in the component Research & Development
    with priority P1 or P2 (we must use quotes for the component as its name
    contains whitespaces):<br>
    <kbd>component:"Research & Development" priority:P1,P2</kbd></li>
</ul>

<h2 id="fields">Fields You Can Search On</h2>

<p>You can specify any of these fields like <kbd>field:value</kbd>
  in the search box, to search on them. You can also abbreviate
  the field name, as long as your abbreviation matches only one field name.
  So, for example, searching on <kbd>stat:VERIFIED</kbd> will find all
  bugs in the <kbd>VERIFIED</kbd> status. Some fields have
  multiple names, and you can use any of those names to search for them.</p>

  <p>For custom fields, they can be used and abbreviated
    based on the part of their name <em>after</em> the <kbd>cf_</kbd>
    if you'd like, in addition to their standard name starting with
    <kbd>cf_</kbd>. So for example,
    <kbd>cf_colo_site</kbd> can be
    referred to as
    <kbd>colo_site</kbd>,
    also. However, if this causes a conflict between the standard
    Bugzilla field names and the custom field names, the
    standard field names always take precedence.</p>

  <p>
    <label>
      <input type="checkbox" id="qs_show_inactive_fields" />
      Show Inactive Fields (You can still search on these fields)
    </label>
  </p>

  <script nonce="cPLqIvfNpJVZzoGWn0z5gIH8IM75WdVI1W750s9EbspHZx4r">
    window.addEventListener('DOMContentLoaded', () => {
      const $checkbox = document.getElementById('qs_show_inactive_fields');
      const inactiveFields = document.querySelectorAll('.qs_fields tr.inactive');

      $checkbox.checked = false;
      $checkbox.addEventListener('change', () => {
        const showInactive = $checkbox.checked;

        inactiveFields.forEach((row) => {
          row.hidden = !showInactive;
        });
      });
    });
  </script>


<div class="qs_field_table_wrapper"><table cellspacing="0" cellpadding="0" border="0" class="standard qs_fields">
    <thead>
      <tr>
        <th class="field_name">Field</th>
        <th class="field_nickname">Field Names For Search</th>
      </tr>
    </thead>
    <tbody>
        <tr >
          <td class="field_name">%Complete 
          </td>
          <td class="field_nickname">
              <code>percentage_complete</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">a11y-review 
          </td>
          <td class="field_nickname">
              <code>cf_a11y_review_project_flag</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Accessibility Severity 
          </td>
          <td class="field_nickname">
              <code>cf_accessibility_severity</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Alias 
          </td>
          <td class="field_nickname">
              <code>alias</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Any field 
          </td>
          <td class="field_nickname">
              <code>anything</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Assignee 
          </td>
          <td class="field_nickname">
              <code>assigned_to</code><br>
              <code>assignee</code><br>
              <code>owner</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Assignee Last Login Date 
          </td>
          <td class="field_nickname">
              <code>assignee_last_login</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Attachment description 
          </td>
          <td class="field_nickname">
              <code>attachmentdesc</code><br>
              <code>attachdesc</code><br>
              <code>attachment</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Attachment mime type 
          </td>
          <td class="field_nickname">
              <code>attachmentmimetype</code><br>
              <code>attachmimetype</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">b2g-ota-blocker 
          </td>
          <td class="field_nickname">
              <code>cf_b2g_ota_blocker</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">backlog 
          </td>
          <td class="field_nickname">
              <code>cf_backlog</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-b2g 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_b2g</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-basecamp 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_basecamp</code><br>
              <code>blocking-basecamp</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-fennec1.0 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_fennec10</code><br>
              <code>blocking-fennec1.0</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-fx 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_fx</code><br>
              <code>blocking-fx</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-kilimanjaro 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_kilimanjaro</code><br>
              <code>blocking-kilimanjaro</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-seamonkey2.1 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_seamonkey21</code><br>
              <code>blocking-seamonkey2.1</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-thunderbird3.0 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_thunderbird30</code><br>
              <code>blocking-thunderbird3.0</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-thunderbird3.1 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_thunderbird31</code><br>
              <code>blocking-thunderbird3.1</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-thunderbird3.2 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_thunderbird32</code><br>
              <code>blocking-thunderbird3.2</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking-thunderbird5.0 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_thunderbird33</code><br>
              <code>blocking-thunderbird3.3</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking1.9.1 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_191</code><br>
              <code>blocking1.9.1</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking1.9.2 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_192</code><br>
              <code>blocking1.9.2</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">blocking2.0 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_20</code><br>
              <code>blocking2.0</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Blocks 
          </td>
          <td class="field_nickname">
              <code>blocked</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">bmo-component-move 
          </td>
          <td class="field_nickname">
              <code>cf_bmo_component_move</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Bug ID 
          </td>
          <td class="field_nickname">
              <code>bug_id</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Bug Interest 
          </td>
          <td class="field_nickname">
              <code>bug_interest_ts</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">CC 
          </td>
          <td class="field_nickname">
              <code>cc</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Change Request 
          </td>
          <td class="field_nickname">
              <code>cf_cab_review</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Classification 
          </td>
          <td class="field_nickname">
              <code>classification</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Closed 
          </td>
          <td class="field_nickname">
              <code>cf_last_resolved</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">colo-trip 
          </td>
          <td class="field_nickname">
              <code>cf_colo_site</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Comment 
          </td>
          <td class="field_nickname">
              <code>description</code><br>
              <code>longdesc</code><br>
              <code>comment</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Comment Tag 
          </td>
          <td class="field_nickname">
              <code>comment_tag</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Commenter 
          </td>
          <td class="field_nickname">
              <code>commenter</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Component 
          </td>
          <td class="field_nickname">
              <code>component</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Content 
          </td>
          <td class="field_nickname">
              <code>content</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Crash Signature 
          </td>
          <td class="field_nickname">
              <code>cf_crash_signature</code><br>
              <code>sig</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">data-science-status 
          </td>
          <td class="field_nickname">
              <code>cf_data_science_status</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Days since bug changed 
          </td>
          <td class="field_nickname">
              <code>days_elapsed</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Deadline 
          </td>
          <td class="field_nickname">
              <code>deadline</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Depends on 
          </td>
          <td class="field_nickname">
              <code>dependson</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Due Date 
          </td>
          <td class="field_nickname">
              <code>cf_due_date</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Duplicate of 
          </td>
          <td class="field_nickname">
              <code>dup_id</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Duplicates 
          </td>
          <td class="field_nickname">
              <code>duplicates</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Ever confirmed 
          </td>
          <td class="field_nickname">
              <code>everconfirmed</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">feature-b2g 
          </td>
          <td class="field_nickname">
              <code>cf_feature_b2g</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Filed via 
          </td>
          <td class="field_nickname">
              <code>filed_via</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Flag Requestee 
          </td>
          <td class="field_nickname">
              <code>requestee</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Flag Setter 
          </td>
          <td class="field_nickname">
              <code>setter</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Flags 
          </td>
          <td class="field_nickname">
              <code>flag</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">geckoview 
          </td>
          <td class="field_nickname">
              <code>cf_geckoview</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Group 
          </td>
          <td class="field_nickname">
              <code>group</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Hardware 
          </td>
          <td class="field_nickname">
              <code>platform</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Has STR 
          </td>
          <td class="field_nickname">
              <code>cf_has_str</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Hours Left 
          </td>
          <td class="field_nickname">
              <code>remaining_time</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Hours Worked 
          </td>
          <td class="field_nickname">
              <code>work_time</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Install Update Workflow 
          </td>
          <td class="field_nickname">
              <code>cf_install_update_workflow</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Is Triaged 
          </td>
          <td class="field_nickname">
              <code>is_triaged</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Iteration 
          </td>
          <td class="field_nickname">
              <code>cf_fx_iteration</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Keywords 
          </td>
          <td class="field_nickname">
              <code>keywords</code><br>
              <code>kw</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Last Visit 
          </td>
          <td class="field_nickname">
              <code>last_visit_ts</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Locale 
          </td>
          <td class="field_nickname">
              <code>cf_locale</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Machine State 
          </td>
          <td class="field_nickname">
              <code>cf_machine_state</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Mentor 
          </td>
          <td class="field_nickname">
              <code>bug_mentor</code><br>
              <code>mentor</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Mozilla Project 
          </td>
          <td class="field_nickname">
              <code>cf_mozilla_project</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Number of CC 
          </td>
          <td class="field_nickname">
              <code>cc_count</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Number of Duplicates 
          </td>
          <td class="field_nickname">
              <code>dupe_count</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Number of See Also 
          </td>
          <td class="field_nickname">
              <code>see_also_count</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Office/Space 
          </td>
          <td class="field_nickname">
              <code>cf_office</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Opened 
          </td>
          <td class="field_nickname">
              <code>creation_ts</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Orig. Est. 
          </td>
          <td class="field_nickname">
              <code>estimated_time</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">OS 
          </td>
          <td class="field_nickname">
              <code>op_sys</code><br>
              <code>os</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Performance Impact 
          </td>
          <td class="field_nickname">
              <code>cf_performance_impact</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">platform-rel 
          </td>
          <td class="field_nickname">
              <code>cf_platform_rel</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Points 
          </td>
          <td class="field_nickname">
              <code>cf_fx_points</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Priority 
          </td>
          <td class="field_nickname">
              <code>priority</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Product 
          </td>
          <td class="field_nickname">
              <code>product</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Product Support Area (PSA) 
          </td>
          <td class="field_nickname">
              <code>cf_data_science_product_support_area</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">QA Contact 
          </td>
          <td class="field_nickname">
              <code>qa_contact</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">QA Whiteboard 
          </td>
          <td class="field_nickname">
              <code>cf_qa_whiteboard</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Rank 
          </td>
          <td class="field_nickname">
              <code>cf_rank</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Regressed by 
          </td>
          <td class="field_nickname">
              <code>regressed_by</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Regressions 
          </td>
          <td class="field_nickname">
              <code>regressions</code><br>
              <code>regresses</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Reporter 
          </td>
          <td class="field_nickname">
              <code>reporter</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Resolution 
          </td>
          <td class="field_nickname">
              <code>resolution</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Restrict Comments 
          </td>
          <td class="field_nickname">
              <code>restrict_comments</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Root Cause 
          </td>
          <td class="field_nickname">
              <code>cf_root_cause</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">See Also 
          </td>
          <td class="field_nickname">
              <code>see_also</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Severity 
          </td>
          <td class="field_nickname">
              <code>severity</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Size Estimate 
          </td>
          <td class="field_nickname">
              <code>cf_size_estimate</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Status 
          </td>
          <td class="field_nickname">
              <code>status</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Summary 
          </td>
          <td class="field_nickname">
              <code>short_desc</code><br>
              <code>summary</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Tags 
          </td>
          <td class="field_nickname">
              <code>tag</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Target Milestone 
          </td>
          <td class="field_nickname">
              <code>target_milestone</code><br>
              <code>milestone</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Team Name 
          </td>
          <td class="field_nickname">
              <code>team_name</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Time Since Assignee Touched 
          </td>
          <td class="field_nickname">
              <code>owner_idle_time</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-fennec 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_fennec</code><br>
              <code>blocking-fennec</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Triage Owner 
          </td>
          <td class="field_nickname">
              <code>triage_owner</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Type 
          </td>
          <td class="field_nickname">
              <code>type</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Updated 
          </td>
          <td class="field_nickname">
              <code>delta_ts</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">URL 
          </td>
          <td class="field_nickname">
              <code>url</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">User Story 
          </td>
          <td class="field_nickname">
              <code>cf_user_story</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">ux-b2g 
          </td>
          <td class="field_nickname">
              <code>cf_ux_b2g</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Version 
          </td>
          <td class="field_nickname">
              <code>version</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Votes 
          </td>
          <td class="field_nickname">
              <code>votes</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Webcompat Priority 
          </td>
          <td class="field_nickname">
              <code>cf_webcompat_priority</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Webcompat Score 
          </td>
          <td class="field_nickname">
              <code>cf_webcompat_score</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">webextensions 
          </td>
          <td class="field_nickname">
              <code>cf_blocking_webextensions</code><br>
              <code>blocking-webextensions</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">Whiteboard 
          </td>
          <td class="field_nickname">
              <code>whiteboard</code><br>
              <code>sw</code>
          </td>
        </tr>
    </tbody>
  </table><table cellspacing="0" cellpadding="0" border="0" class="standard qs_fields">
    <thead>
      <tr>
        <th class="field_name">Field</th>
        <th class="field_nickname">Field Names For Search</th>
      </tr>
    </thead>
    <tbody>
        <tr class="inactive" hidden>
          <td class="field_name">relnote-b2g (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_relnote_b2g</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">relnote-firefox 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_relnote</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">relnote-thunderbird 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_relnote</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-master (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_master</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v1.1hd (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_1_1_hd</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v1.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_1_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v1.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_1_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v1.3T (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_1_3t</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v1.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_1_4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.0M (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_0m</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.1S (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_1_s</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.2r (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_2r</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g-v2.6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g_2_6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g18</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g18-v1.0.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g18_1_0_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g18-v1.0.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g18_1_0_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-b2g30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_b2g30</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-bmo-push 
          </td>
          <td class="field_nickname">
              <code>cf_status_bmo_push</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-conduit-push 
          </td>
          <td class="field_nickname">
              <code>cf_status_conduit_push</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-beta 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_beta</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-esr 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_esr10</code><br>
              <code>status-esr1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr102</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-esr115 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr128</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-esr140 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr140</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-esr153 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr153</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr17</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr24</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox-esr91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_esr91</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-nightly 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_nightly</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox-release 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox_release</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox10</code><br>
              <code>status-firefox1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox100 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox100</code><br>
              <code>status-firefox1.0.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox101 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox101</code><br>
              <code>status-firefox1.0.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox102</code><br>
              <code>status-firefox1.0.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox103 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox103</code><br>
              <code>status-firefox1.0.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox104 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox104</code><br>
              <code>status-firefox1.0.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox105 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox105</code><br>
              <code>status-firefox1.0.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox106 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox106</code><br>
              <code>status-firefox1.0.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox107 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox107</code><br>
              <code>status-firefox1.0.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox108 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox108</code><br>
              <code>status-firefox1.0.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox109 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox109</code><br>
              <code>status-firefox1.0.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox11</code><br>
              <code>status-firefox1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox110 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox110</code><br>
              <code>status-firefox1.1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox111 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox111</code><br>
              <code>status-firefox1.1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox112 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox112</code><br>
              <code>status-firefox1.1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox113 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox113</code><br>
              <code>status-firefox1.1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox114 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox114</code><br>
              <code>status-firefox1.1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox115 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox115</code><br>
              <code>status-firefox1.1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox116 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox116</code><br>
              <code>status-firefox1.1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox117 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox117</code><br>
              <code>status-firefox1.1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox118 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox118</code><br>
              <code>status-firefox1.1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox119 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox119</code><br>
              <code>status-firefox1.1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox12</code><br>
              <code>status-firefox1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox120 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox120</code><br>
              <code>status-firefox1.2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox121 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox121</code><br>
              <code>status-firefox1.2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox122 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox122</code><br>
              <code>status-firefox1.2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox123 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox123</code><br>
              <code>status-firefox1.2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox124 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox124</code><br>
              <code>status-firefox1.2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox125 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox125</code><br>
              <code>status-firefox1.2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox126 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox126</code><br>
              <code>status-firefox1.2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox127 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox127</code><br>
              <code>status-firefox1.2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox128</code><br>
              <code>status-firefox1.2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox129 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox129</code><br>
              <code>status-firefox1.2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox13</code><br>
              <code>status-firefox1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox130 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox130</code><br>
              <code>status-firefox1.3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox131 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox131</code><br>
              <code>status-firefox1.3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox132 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox132</code><br>
              <code>status-firefox1.3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox133 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox133</code><br>
              <code>status-firefox1.3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox134 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox134</code><br>
              <code>status-firefox1.3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox135 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox135</code><br>
              <code>status-firefox1.3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox136 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox136</code><br>
              <code>status-firefox1.3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox137 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox137</code><br>
              <code>status-firefox1.3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox138 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox138</code><br>
              <code>status-firefox1.3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox139 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox139</code><br>
              <code>status-firefox1.3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox14</code><br>
              <code>status-firefox1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox140 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox140</code><br>
              <code>status-firefox1.4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox141 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox141</code><br>
              <code>status-firefox1.4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox142 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox142</code><br>
              <code>status-firefox1.4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox143 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox143</code><br>
              <code>status-firefox1.4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox144 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox144</code><br>
              <code>status-firefox1.4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox145 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox145</code><br>
              <code>status-firefox1.4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox146 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox146</code><br>
              <code>status-firefox1.4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox147 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox147</code><br>
              <code>status-firefox1.4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox148 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox148</code><br>
              <code>status-firefox1.4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox149 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox149</code><br>
              <code>status-firefox1.4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox15</code><br>
              <code>status-firefox1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox150 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox150</code><br>
              <code>status-firefox1.5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox151 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox151</code><br>
              <code>status-firefox1.5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox152 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox152</code><br>
              <code>status-firefox1.5.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox153 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox153</code><br>
              <code>status-firefox1.5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox154 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox154</code><br>
              <code>status-firefox1.5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox155 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox155</code><br>
              <code>status-firefox1.5.5</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox156 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox156</code><br>
              <code>status-firefox1.5.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox157 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox157</code><br>
              <code>status-firefox1.5.7</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-firefox158 
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox158</code><br>
              <code>status-firefox1.5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox16</code><br>
              <code>status-firefox1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox17</code><br>
              <code>status-firefox1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox18</code><br>
              <code>status-firefox1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox19</code><br>
              <code>status-firefox1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox20</code><br>
              <code>status-firefox2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox21</code><br>
              <code>status-firefox2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox22</code><br>
              <code>status-firefox2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox23</code><br>
              <code>status-firefox2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox24</code><br>
              <code>status-firefox2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox25</code><br>
              <code>status-firefox2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox26</code><br>
              <code>status-firefox2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox27</code><br>
              <code>status-firefox2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox28</code><br>
              <code>status-firefox2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox29</code><br>
              <code>status-firefox2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox30</code><br>
              <code>status-firefox3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox31</code><br>
              <code>status-firefox3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox32</code><br>
              <code>status-firefox3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox33</code><br>
              <code>status-firefox3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox34</code><br>
              <code>status-firefox3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox35</code><br>
              <code>status-firefox3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox36</code><br>
              <code>status-firefox3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox37</code><br>
              <code>status-firefox3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox38</code><br>
              <code>status-firefox3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox38.0.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox38_0_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox39</code><br>
              <code>status-firefox3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox40</code><br>
              <code>status-firefox4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox41</code><br>
              <code>status-firefox4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox42</code><br>
              <code>status-firefox4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox43</code><br>
              <code>status-firefox4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox44</code><br>
              <code>status-firefox4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox45</code><br>
              <code>status-firefox4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox46</code><br>
              <code>status-firefox4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox47</code><br>
              <code>status-firefox4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox48</code><br>
              <code>status-firefox4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox49 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox49</code><br>
              <code>status-firefox4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox5</code><br>
              <code>status-firefox5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox50</code><br>
              <code>status-firefox5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox51</code><br>
              <code>status-firefox5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox52</code><br>
              <code>status-firefox5.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox53 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox53</code><br>
              <code>status-firefox5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox54</code><br>
              <code>status-firefox5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox55</code><br>
              <code>status-firefox5.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox56</code><br>
              <code>status-firefox5.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox57 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox57</code><br>
              <code>status-firefox5.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox58</code><br>
              <code>status-firefox5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox59</code><br>
              <code>status-firefox5.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox6</code><br>
              <code>status-firefox6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox60</code><br>
              <code>status-firefox6.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox61 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox61</code><br>
              <code>status-firefox6.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox62</code><br>
              <code>status-firefox6.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox63</code><br>
              <code>status-firefox6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox64</code><br>
              <code>status-firefox6.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox65</code><br>
              <code>status-firefox6.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox66</code><br>
              <code>status-firefox6.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox67 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox67</code><br>
              <code>status-firefox6.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox67.0.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox67_0_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox68</code><br>
              <code>status-firefox6.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox69 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox69</code><br>
              <code>status-firefox6.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox7</code><br>
              <code>status-firefox7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox70 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox70</code><br>
              <code>status-firefox7.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox71 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox71</code><br>
              <code>status-firefox7.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox72 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox72</code><br>
              <code>status-firefox7.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox73 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox73</code><br>
              <code>status-firefox7.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox74 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox74</code><br>
              <code>status-firefox7.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox75 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox75</code><br>
              <code>status-firefox7.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox76 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox76</code><br>
              <code>status-firefox7.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox77 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox77</code><br>
              <code>status-firefox7.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox78</code><br>
              <code>status-firefox7.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox79 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox79</code><br>
              <code>status-firefox7.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox8</code><br>
              <code>status-firefox8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox80 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox80</code><br>
              <code>status-firefox8.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox81 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox81</code><br>
              <code>status-firefox8.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox82 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox82</code><br>
              <code>status-firefox8.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox83 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox83</code><br>
              <code>status-firefox8.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox84 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox84</code><br>
              <code>status-firefox8.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox85 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox85</code><br>
              <code>status-firefox8.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox86 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox86</code><br>
              <code>status-firefox8.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox87 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox87</code><br>
              <code>status-firefox8.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox88 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox88</code><br>
              <code>status-firefox8.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox89 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox89</code><br>
              <code>status-firefox8.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox9</code><br>
              <code>status-firefox9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox90 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox90</code><br>
              <code>status-firefox9.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox91</code><br>
              <code>status-firefox9.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox92 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox92</code><br>
              <code>status-firefox9.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox93 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox93</code><br>
              <code>status-firefox9.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox94 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox94</code><br>
              <code>status-firefox9.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox95 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox95</code><br>
              <code>status-firefox9.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox96 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox96</code><br>
              <code>status-firefox9.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox97 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox97</code><br>
              <code>status-firefox9.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox98 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox98</code><br>
              <code>status-firefox9.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-firefox99 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_firefox99</code><br>
              <code>status-firefox9.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-flowstate-0.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_flowstate01</code><br>
              <code>status-flowstate0.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-flowstate-0.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_flowstate02</code><br>
              <code>status-flowstate0.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-flowstate-0.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_flowstate03</code><br>
              <code>status-flowstate0.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v1.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v1_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v1.0.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v1_0_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v1.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v1_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v10.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v10_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v10.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v10_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v10.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v10_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v10.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v10_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v10.6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v10_6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v11.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v11_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v11.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v11_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v12.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v12_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v12.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v12_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v12.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v12_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v13.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v13_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v13.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v13_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v13.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v13_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v13.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v13_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v14.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v14_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v14.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v14_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v14.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v14_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v14.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v14_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v15.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v15_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v15.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v15_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v16.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v16_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v2.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v2_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v3.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v3_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v4.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v4_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v5.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v5_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v5.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v5_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v5.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v5_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v5.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v5_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v6.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v6_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v6.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v6_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v7.6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v7_6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v8.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v8_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v8.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v8_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v8.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v8_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v8.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v8_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v8.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v8_4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v9.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v9_0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v9.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v9_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v9.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v9_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v9.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v9_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-fxios-v9.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_fxios_v9_4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-geckoview62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_geckoview62</code><br>
              <code>status-geckoview6.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-geckoview63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_geckoview63</code><br>
              <code>status-geckoview6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-geckoview64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_geckoview64</code><br>
              <code>status-geckoview6.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-geckoview65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_geckoview65</code><br>
              <code>status-geckoview6.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-geckoview66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_geckoview66</code><br>
              <code>status-geckoview6.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-nss 
          </td>
          <td class="field_nickname">
              <code>cf_status_nss</code><br>
              <code>status-nss</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey21</code><br>
              <code>status-seamonkey2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey210</code><br>
              <code>status-seamonkey2.1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey211</code><br>
              <code>status-seamonkey2.1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey212</code><br>
              <code>status-seamonkey2.1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey213</code><br>
              <code>status-seamonkey2.1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey214</code><br>
              <code>status-seamonkey2.1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey215</code><br>
              <code>status-seamonkey2.1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey216</code><br>
              <code>status-seamonkey2.1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey217</code><br>
              <code>status-seamonkey2.1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey218</code><br>
              <code>status-seamonkey2.1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey219</code><br>
              <code>status-seamonkey2.1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey22</code><br>
              <code>status-seamonkey2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey220</code><br>
              <code>status-seamonkey2.2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey221</code><br>
              <code>status-seamonkey2.2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey222</code><br>
              <code>status-seamonkey2.2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey223</code><br>
              <code>status-seamonkey2.2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey224</code><br>
              <code>status-seamonkey2.2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey225</code><br>
              <code>status-seamonkey2.2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey226</code><br>
              <code>status-seamonkey2.2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey227</code><br>
              <code>status-seamonkey2.2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey228</code><br>
              <code>status-seamonkey2.2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey229</code><br>
              <code>status-seamonkey2.2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey23</code><br>
              <code>status-seamonkey2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey230</code><br>
              <code>status-seamonkey2.3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey231</code><br>
              <code>status-seamonkey2.3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey232</code><br>
              <code>status-seamonkey2.3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey233</code><br>
              <code>status-seamonkey2.3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey234</code><br>
              <code>status-seamonkey2.3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey235</code><br>
              <code>status-seamonkey2.3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey236</code><br>
              <code>status-seamonkey2.3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey237</code><br>
              <code>status-seamonkey2.3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey238</code><br>
              <code>status-seamonkey2.3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey239</code><br>
              <code>status-seamonkey2.3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey24</code><br>
              <code>status-seamonkey2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey240</code><br>
              <code>status-seamonkey2.4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey241</code><br>
              <code>status-seamonkey2.4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey242</code><br>
              <code>status-seamonkey2.4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey243</code><br>
              <code>status-seamonkey2.4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey244</code><br>
              <code>status-seamonkey2.4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey245</code><br>
              <code>status-seamonkey2.4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey246</code><br>
              <code>status-seamonkey2.4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey247</code><br>
              <code>status-seamonkey2.4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey248</code><br>
              <code>status-seamonkey2.4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.49esr (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey249</code><br>
              <code>status-seamonkey2.4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey25</code><br>
              <code>status-seamonkey2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey250</code><br>
              <code>status-seamonkey2.5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey251</code><br>
              <code>status-seamonkey2.5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey252</code><br>
              <code>status-seamonkey2.5.2</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-seamonkey2.53 
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey253</code><br>
              <code>status-seamonkey2.5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey254</code><br>
              <code>status-seamonkey2.5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey255</code><br>
              <code>status-seamonkey2.5.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey256</code><br>
              <code>status-seamonkey2.5.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-seamonkey2.57esr 
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey257esr</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey258</code><br>
              <code>status-seamonkey2.5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey259</code><br>
              <code>status-seamonkey2.5.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey26</code><br>
              <code>status-seamonkey2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey260</code><br>
              <code>status-seamonkey2.6.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey263</code><br>
              <code>status-seamonkey2.6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey27</code><br>
              <code>status-seamonkey2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey28</code><br>
              <code>status-seamonkey2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-seamonkey2.9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_seamonkey29</code><br>
              <code>status-seamonkey2.9</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird-beta 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_beta</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird-esr10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr10</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird-esr17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr17</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird-nightly 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_nightly</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird-release 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_release</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird10</code><br>
              <code>status-thunderbird1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird100 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_100</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird101 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_101</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_102</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird103 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_103</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird104 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_104</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird105 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_105</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird106 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_106</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird107 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_107</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird108 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_108</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird109 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_109</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird11</code><br>
              <code>status-thunderbird1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird110 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_110</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird111 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_111</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird112 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_112</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird113 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_113</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird114 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_114</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird115 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird116 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_116</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird117 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_117</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird118 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_118</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird119 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_119</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird12</code><br>
              <code>status-thunderbird1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird120 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_120</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird121 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_121</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird122 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_122</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird123 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_123</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird124 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_124</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird125 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_125</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird126 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_126</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird127 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_127</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_128</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird129 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_129</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird13</code><br>
              <code>status-thunderbird1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird130 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_130</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird131 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_131</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird132 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_132</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird133 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_133</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird134 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_134</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird135 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_135</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird136 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_136</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird137 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_137</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird138 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_138</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird139 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_139</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird14</code><br>
              <code>status-thunderbird1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird140 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_140</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird141 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_141</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird142 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_142</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird143 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_143</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird144 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_144</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird145 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_145</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird146 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_146</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird147 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_147</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird148 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_148</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird149 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_149</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird15</code><br>
              <code>status-thunderbird1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird150 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_150</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird151 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_151</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird152 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_152</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird153 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_153</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird154 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_154</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird155 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_155</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird156 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_156</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird157 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_157</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird158 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_158</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird16</code><br>
              <code>status-thunderbird1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird17</code><br>
              <code>status-thunderbird1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird18</code><br>
              <code>status-thunderbird1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird19</code><br>
              <code>status-thunderbird1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird20</code><br>
              <code>status-thunderbird2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird21</code><br>
              <code>status-thunderbird2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird22</code><br>
              <code>status-thunderbird2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird23</code><br>
              <code>status-thunderbird2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird24</code><br>
              <code>status-thunderbird2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird25</code><br>
              <code>status-thunderbird2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird26</code><br>
              <code>status-thunderbird2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird27</code><br>
              <code>status-thunderbird2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird28</code><br>
              <code>status-thunderbird2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird29</code><br>
              <code>status-thunderbird2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird3.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird30</code><br>
              <code>status-thunderbird3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird3.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird31</code><br>
              <code>status-thunderbird3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird3.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird32</code><br>
              <code>status-thunderbird3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_30</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_32</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_33</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_34</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_35</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_36</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_37</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_39</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_40</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_41</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_42</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_43</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_44</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_46</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_47</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_48</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird49 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_49</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird5.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird33</code><br>
              <code>status-thunderbird3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_50</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_51</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird53 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_53</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_54</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_55</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_56</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird57 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_57</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_58</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_59</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird6</code><br>
              <code>status-thunderbird6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird61 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_61</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_62</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_63</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_64</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_65</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_66</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird67 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_67</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird69 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_69</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird7</code><br>
              <code>status-thunderbird7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird70 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_70</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird71 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_71</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird72 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_72</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird73 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_73</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird74 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_74</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird75 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_75</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird76 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_76</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird77 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_77</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird79 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_79</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird8</code><br>
              <code>status-thunderbird8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird80 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_80</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird81 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_81</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird82 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_82</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird83 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_83</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird84 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_84</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird85 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_85</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird86 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_86</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird87 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_87</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird88 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_88</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird89 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_89</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird9</code><br>
              <code>status-thunderbird9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird90 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_90</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_91</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird92 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_92</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird93 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_93</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird94 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_94</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird95 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_95</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird96 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_96</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird97 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_97</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird98 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_98</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird99 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_99</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr102</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird_esr115 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr128</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird_esr140 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr140</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">status-thunderbird_esr153 
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr153</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr24</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status-thunderbird_esr91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_thunderbird_esr91</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status1.9.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_191</code><br>
              <code>status1.9.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status1.9.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_192</code><br>
              <code>status1.9.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">status2.0 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_status_20</code><br>
              <code>status2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-b2g (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_b2g</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-b2g-v1.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_b2g_v1_2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-b2g-v1.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_b2g_v1_3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-b2g18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_b2g18</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-bmo-push 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_bmo_push</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-conduit-push 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_conduit_push</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-e10s (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_e10s</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-beta 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_beta</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-esr 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_esr10</code><br>
              <code>tracking-esr1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr102</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-esr115 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr128</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-esr140 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr140</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-esr153 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr153</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr17</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr24</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox-esr91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_esr91</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-nightly 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_nightly</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox-release 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_release</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox10</code><br>
              <code>tracking-firefox1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox100 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox100</code><br>
              <code>tracking-firefox1.0.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox101 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox101</code><br>
              <code>tracking-firefox1.0.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox102</code><br>
              <code>tracking-firefox1.0.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox103 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox103</code><br>
              <code>tracking-firefox1.0.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox104 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox104</code><br>
              <code>tracking-firefox1.0.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox105 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox105</code><br>
              <code>tracking-firefox1.0.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox106 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox106</code><br>
              <code>tracking-firefox1.0.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox107 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox107</code><br>
              <code>tracking-firefox1.0.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox108 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox108</code><br>
              <code>tracking-firefox1.0.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox109 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox109</code><br>
              <code>tracking-firefox1.0.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox11</code><br>
              <code>tracking-firefox1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox110 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox110</code><br>
              <code>tracking-firefox1.1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox111 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox111</code><br>
              <code>tracking-firefox1.1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox112 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox112</code><br>
              <code>tracking-firefox1.1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox113 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox113</code><br>
              <code>tracking-firefox1.1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox114 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox114</code><br>
              <code>tracking-firefox1.1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox115 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox115</code><br>
              <code>tracking-firefox1.1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox116 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox116</code><br>
              <code>tracking-firefox1.1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox117 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox117</code><br>
              <code>tracking-firefox1.1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox118 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox118</code><br>
              <code>tracking-firefox1.1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox119 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox119</code><br>
              <code>tracking-firefox1.1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox12</code><br>
              <code>tracking-firefox1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox120 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox120</code><br>
              <code>tracking-firefox1.2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox121 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox121</code><br>
              <code>tracking-firefox1.2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox122 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox122</code><br>
              <code>tracking-firefox1.2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox123 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox123</code><br>
              <code>tracking-firefox1.2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox124 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox124</code><br>
              <code>tracking-firefox1.2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox125 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox125</code><br>
              <code>tracking-firefox1.2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox126 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox126</code><br>
              <code>tracking-firefox1.2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox127 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox127</code><br>
              <code>tracking-firefox1.2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox128</code><br>
              <code>tracking-firefox1.2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox129 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox129</code><br>
              <code>tracking-firefox1.2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox13</code><br>
              <code>tracking-firefox1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox130 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox130</code><br>
              <code>tracking-firefox1.3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox131 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox131</code><br>
              <code>tracking-firefox1.3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox132 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox132</code><br>
              <code>tracking-firefox1.3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox133 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox133</code><br>
              <code>tracking-firefox1.3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox134 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox134</code><br>
              <code>tracking-firefox1.3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox135 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox135</code><br>
              <code>tracking-firefox1.3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox136 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox136</code><br>
              <code>tracking-firefox1.3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox137 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox137</code><br>
              <code>tracking-firefox1.3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox138 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox138</code><br>
              <code>tracking-firefox1.3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox139 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox139</code><br>
              <code>tracking-firefox1.3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox14</code><br>
              <code>tracking-firefox1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox140 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox140</code><br>
              <code>tracking-firefox1.4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox141 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox141</code><br>
              <code>tracking-firefox1.4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox142 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox142</code><br>
              <code>tracking-firefox1.4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox143 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox143</code><br>
              <code>tracking-firefox1.4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox144 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox144</code><br>
              <code>tracking-firefox1.4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox145 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox145</code><br>
              <code>tracking-firefox1.4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox146 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox146</code><br>
              <code>tracking-firefox1.4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox147 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox147</code><br>
              <code>tracking-firefox1.4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox148 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox148</code><br>
              <code>tracking-firefox1.4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox149 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox149</code><br>
              <code>tracking-firefox1.4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox15</code><br>
              <code>tracking-firefox1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox150 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox150</code><br>
              <code>tracking-firefox1.5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox151 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox151</code><br>
              <code>tracking-firefox1.5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox152 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox152</code><br>
              <code>tracking-firefox1.5.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox153 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox153</code><br>
              <code>tracking-firefox1.5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox154 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox154</code><br>
              <code>tracking-firefox1.5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox155 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox155</code><br>
              <code>tracking-firefox1.5.5</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox156 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox156</code><br>
              <code>tracking-firefox1.5.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox157 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox157</code><br>
              <code>tracking-firefox1.5.7</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-firefox158 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox158</code><br>
              <code>tracking-firefox1.5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox16</code><br>
              <code>tracking-firefox1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox17</code><br>
              <code>tracking-firefox1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox18</code><br>
              <code>tracking-firefox1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox19</code><br>
              <code>tracking-firefox1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox20</code><br>
              <code>tracking-firefox2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox21</code><br>
              <code>tracking-firefox2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox22</code><br>
              <code>tracking-firefox2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox23</code><br>
              <code>tracking-firefox2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox24</code><br>
              <code>tracking-firefox2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox25</code><br>
              <code>tracking-firefox2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox26</code><br>
              <code>tracking-firefox2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox27</code><br>
              <code>tracking-firefox2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox28</code><br>
              <code>tracking-firefox2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox29</code><br>
              <code>tracking-firefox2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox30</code><br>
              <code>tracking-firefox3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox31</code><br>
              <code>tracking-firefox3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox32</code><br>
              <code>tracking-firefox3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox33</code><br>
              <code>tracking-firefox3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox34</code><br>
              <code>tracking-firefox3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox35</code><br>
              <code>tracking-firefox3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox36</code><br>
              <code>tracking-firefox3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox37</code><br>
              <code>tracking-firefox3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox38</code><br>
              <code>tracking-firefox3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox38.0.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox38_0_5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox39</code><br>
              <code>tracking-firefox3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox40</code><br>
              <code>tracking-firefox4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox41</code><br>
              <code>tracking-firefox4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox42</code><br>
              <code>tracking-firefox4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox43</code><br>
              <code>tracking-firefox4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox44</code><br>
              <code>tracking-firefox4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox45</code><br>
              <code>tracking-firefox4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox46</code><br>
              <code>tracking-firefox4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox47</code><br>
              <code>tracking-firefox4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox48</code><br>
              <code>tracking-firefox4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox49 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox49</code><br>
              <code>tracking-firefox4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox5</code><br>
              <code>tracking-firefox5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox50</code><br>
              <code>tracking-firefox5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox51</code><br>
              <code>tracking-firefox5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox52</code><br>
              <code>tracking-firefox5.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox53 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox53</code><br>
              <code>tracking-firefox5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox54</code><br>
              <code>tracking-firefox5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox55</code><br>
              <code>tracking-firefox5.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox56</code><br>
              <code>tracking-firefox5.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox57 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox57</code><br>
              <code>tracking-firefox5.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox58</code><br>
              <code>tracking-firefox5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox59</code><br>
              <code>tracking-firefox5.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox6</code><br>
              <code>tracking-firefox6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox60</code><br>
              <code>tracking-firefox6.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox61 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox61</code><br>
              <code>tracking-firefox6.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox62</code><br>
              <code>tracking-firefox6.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox63</code><br>
              <code>tracking-firefox6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox64</code><br>
              <code>tracking-firefox6.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox65</code><br>
              <code>tracking-firefox6.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox66</code><br>
              <code>tracking-firefox6.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox67 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox67</code><br>
              <code>tracking-firefox6.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox67.0.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox67_0_1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox68</code><br>
              <code>tracking-firefox6.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox69 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox69</code><br>
              <code>tracking-firefox6.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox7</code><br>
              <code>tracking-firefox7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox70 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox70</code><br>
              <code>tracking-firefox7.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox71 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox71</code><br>
              <code>tracking-firefox7.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox72 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox72</code><br>
              <code>tracking-firefox7.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox73 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox73</code><br>
              <code>tracking-firefox7.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox74 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox74</code><br>
              <code>tracking-firefox7.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox75 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox75</code><br>
              <code>tracking-firefox7.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox76 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox76</code><br>
              <code>tracking-firefox7.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox77 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox77</code><br>
              <code>tracking-firefox7.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox78</code><br>
              <code>tracking-firefox7.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox79 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox79</code><br>
              <code>tracking-firefox7.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox8</code><br>
              <code>tracking-firefox8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox80 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox80</code><br>
              <code>tracking-firefox8.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox81 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox81</code><br>
              <code>tracking-firefox8.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox82 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox82</code><br>
              <code>tracking-firefox8.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox83 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox83</code><br>
              <code>tracking-firefox8.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox84 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox84</code><br>
              <code>tracking-firefox8.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox85 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox85</code><br>
              <code>tracking-firefox8.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox86 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox86</code><br>
              <code>tracking-firefox8.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox87 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox87</code><br>
              <code>tracking-firefox8.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox88 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox88</code><br>
              <code>tracking-firefox8.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox89 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox89</code><br>
              <code>tracking-firefox8.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox9</code><br>
              <code>tracking-firefox9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox90 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox90</code><br>
              <code>tracking-firefox9.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox91</code><br>
              <code>tracking-firefox9.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox92 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox92</code><br>
              <code>tracking-firefox9.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox93 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox93</code><br>
              <code>tracking-firefox9.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox94 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox94</code><br>
              <code>tracking-firefox9.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox95 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox95</code><br>
              <code>tracking-firefox9.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox96 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox96</code><br>
              <code>tracking-firefox9.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox97 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox97</code><br>
              <code>tracking-firefox9.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox98 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox98</code><br>
              <code>tracking-firefox9.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-firefox99 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox99</code><br>
              <code>tracking-firefox9.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-flowstate-0.1 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_flowstate01</code><br>
              <code>tracking-flowstate0.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-flowstate-0.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_flowstate02</code><br>
              <code>tracking-flowstate0.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-flowstate-0.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_flowstate03</code><br>
              <code>tracking-flowstate0.3</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-fxios 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_fxios</code><br>
              <code>tracking-fxios</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-geckoview62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_geckoview62</code><br>
              <code>tracking-geckoview6.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-geckoview63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_geckoview63</code><br>
              <code>tracking-geckoview6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-geckoview64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_geckoview64</code><br>
              <code>tracking-geckoview6.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-geckoview65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_geckoview65</code><br>
              <code>tracking-geckoview6.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-geckoview66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_geckoview66</code><br>
              <code>tracking-geckoview6.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-nss 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_nss</code><br>
              <code>tracking-nss</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-p11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_p11</code><br>
              <code>tracking-p1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey210</code><br>
              <code>tracking-seamonkey2.1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey211</code><br>
              <code>tracking-seamonkey2.1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey212</code><br>
              <code>tracking-seamonkey2.1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey213</code><br>
              <code>tracking-seamonkey2.1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey214</code><br>
              <code>tracking-seamonkey2.1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey215</code><br>
              <code>tracking-seamonkey2.1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey216</code><br>
              <code>tracking-seamonkey2.1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey217</code><br>
              <code>tracking-seamonkey2.1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey218</code><br>
              <code>tracking-seamonkey2.1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey219</code><br>
              <code>tracking-seamonkey2.1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.2 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey22</code><br>
              <code>tracking-seamonkey2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey220</code><br>
              <code>tracking-seamonkey2.2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey221</code><br>
              <code>tracking-seamonkey2.2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey222</code><br>
              <code>tracking-seamonkey2.2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey223</code><br>
              <code>tracking-seamonkey2.2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey224</code><br>
              <code>tracking-seamonkey2.2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey225</code><br>
              <code>tracking-seamonkey2.2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey226</code><br>
              <code>tracking-seamonkey2.2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey227</code><br>
              <code>tracking-seamonkey2.2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey228</code><br>
              <code>tracking-seamonkey2.2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey229</code><br>
              <code>tracking-seamonkey2.2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.3 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey23</code><br>
              <code>tracking-seamonkey2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey230</code><br>
              <code>tracking-seamonkey2.3.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey231</code><br>
              <code>tracking-seamonkey2.3.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey232</code><br>
              <code>tracking-seamonkey2.3.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey233</code><br>
              <code>tracking-seamonkey2.3.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey234</code><br>
              <code>tracking-seamonkey2.3.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey235</code><br>
              <code>tracking-seamonkey2.3.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey236</code><br>
              <code>tracking-seamonkey2.3.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey237</code><br>
              <code>tracking-seamonkey2.3.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey238</code><br>
              <code>tracking-seamonkey2.3.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey239</code><br>
              <code>tracking-seamonkey2.3.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.4 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey24</code><br>
              <code>tracking-seamonkey2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey240</code><br>
              <code>tracking-seamonkey2.4.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey241</code><br>
              <code>tracking-seamonkey2.4.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey242</code><br>
              <code>tracking-seamonkey2.4.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey243</code><br>
              <code>tracking-seamonkey2.4.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey244</code><br>
              <code>tracking-seamonkey2.4.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey245</code><br>
              <code>tracking-seamonkey2.4.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey246</code><br>
              <code>tracking-seamonkey2.4.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey247</code><br>
              <code>tracking-seamonkey2.4.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey248</code><br>
              <code>tracking-seamonkey2.4.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.49esr (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey249</code><br>
              <code>tracking-seamonkey2.4.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.5 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey25</code><br>
              <code>tracking-seamonkey2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey250</code><br>
              <code>tracking-seamonkey2.5.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey251</code><br>
              <code>tracking-seamonkey2.5.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey252</code><br>
              <code>tracking-seamonkey2.5.2</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-seamonkey2.53 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey253</code><br>
              <code>tracking-seamonkey2.5.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey254</code><br>
              <code>tracking-seamonkey2.5.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey255</code><br>
              <code>tracking-seamonkey2.5.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey256</code><br>
              <code>tracking-seamonkey2.5.6</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-seamonkey2.57esr 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey257esr</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey258</code><br>
              <code>tracking-seamonkey2.5.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey259</code><br>
              <code>tracking-seamonkey2.5.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey26</code><br>
              <code>tracking-seamonkey2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey260</code><br>
              <code>tracking-seamonkey2.6.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey263</code><br>
              <code>tracking-seamonkey2.6.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey27</code><br>
              <code>tracking-seamonkey2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey28</code><br>
              <code>tracking-seamonkey2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-seamonkey2.9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_seamonkey29</code><br>
              <code>tracking-seamonkey2.9</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird-beta 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_beta</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird-esr10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr10</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird-esr17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr17</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird-nightly 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_nightly</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird-release 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_release</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird10 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird10</code><br>
              <code>tracking-thunderbird1.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird100 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_100</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird101 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_101</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_102</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird103 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_103</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird104 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_104</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird105 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_105</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird106 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_106</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird107 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_107</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird108 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_108</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird109 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_109</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird11 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird11</code><br>
              <code>tracking-thunderbird1.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird110 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_110</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird111 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_111</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird112 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_112</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird113 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_113</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird114 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_114</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird115 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird116 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_116</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird117 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_117</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird118 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_118</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird119 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_119</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird12 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird12</code><br>
              <code>tracking-thunderbird1.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird120 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_120</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird121 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_121</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird122 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_122</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird123 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_123</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird124 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_124</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird125 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_125</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird126 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_126</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird127 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_127</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_128</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird129 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_129</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird13 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird13</code><br>
              <code>tracking-thunderbird1.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird130 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_130</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird131 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_131</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird132 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_132</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird133 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_133</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird134 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_134</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird135 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_135</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird136 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_136</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird137 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_137</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird138 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_138</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird139 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_139</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird14 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird14</code><br>
              <code>tracking-thunderbird1.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird140 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_140</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird141 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_141</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird142 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_142</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird143 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_143</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird144 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_144</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird145 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_145</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird146 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_146</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird147 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_147</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird148 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_148</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird149 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_149</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird15 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird15</code><br>
              <code>tracking-thunderbird1.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird150 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_150</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird151 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_151</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird152 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_152</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird153 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_153</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird154 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_154</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird155 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_155</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird156 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_156</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird157 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_157</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird158 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_158</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird16 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird16</code><br>
              <code>tracking-thunderbird1.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird17 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird17</code><br>
              <code>tracking-thunderbird1.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird18 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird18</code><br>
              <code>tracking-thunderbird1.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird19 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird19</code><br>
              <code>tracking-thunderbird1.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird20 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird20</code><br>
              <code>tracking-thunderbird2.0</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird21 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird21</code><br>
              <code>tracking-thunderbird2.1</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird22 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird22</code><br>
              <code>tracking-thunderbird2.2</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird23 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird23</code><br>
              <code>tracking-thunderbird2.3</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird24</code><br>
              <code>tracking-thunderbird2.4</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird25 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird25</code><br>
              <code>tracking-thunderbird2.5</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird26 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird26</code><br>
              <code>tracking-thunderbird2.6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird27 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird27</code><br>
              <code>tracking-thunderbird2.7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird28 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird28</code><br>
              <code>tracking-thunderbird2.8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird29 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird29</code><br>
              <code>tracking-thunderbird2.9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird30 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_30</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird32 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_32</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird33 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_33</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird34 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_34</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird35 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_35</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird36 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_36</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird37 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_37</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird39 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_39</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird40 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_40</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird41 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_41</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird42 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_42</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird43 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_43</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird44 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_44</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird46 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_46</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird47 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_47</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird48 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_48</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird49 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_49</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird50 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_50</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird51 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_51</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird53 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_53</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird54 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_54</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird55 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_55</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird56 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_56</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird57 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_57</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird58 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_58</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird59 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_59</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird6 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird6</code><br>
              <code>tracking-thunderbird6</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird61 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_61</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird62 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_62</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird63 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_63</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird64 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_64</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird65 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_65</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird66 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_66</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird67 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_67</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird69 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_69</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird7 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird7</code><br>
              <code>tracking-thunderbird7</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird70 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_70</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird71 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_71</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird72 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_72</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird73 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_73</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird74 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_74</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird75 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_75</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird76 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_76</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird77 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_77</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird79 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_79</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird8 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird8</code><br>
              <code>tracking-thunderbird8</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird80 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_80</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird81 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_81</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird82 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_82</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird83 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_83</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird84 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_84</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird85 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_85</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird86 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_86</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird87 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_87</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird88 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_88</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird89 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_89</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird9 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird9</code><br>
              <code>tracking-thunderbird9</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird90 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_90</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_91</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird92 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_92</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird93 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_93</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird94 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_94</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird95 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_95</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird96 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_96</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird97 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_97</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird98 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_98</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird99 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_99</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr102 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr102</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird_esr115 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr115</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr128 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr128</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird_esr140 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr140</code>
          </td>
        </tr>
        <tr >
          <td class="field_name">tracking-thunderbird_esr153 
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr153</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr24 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr24</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr31 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr31</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr38 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr38</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr45 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr45</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr52 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr52</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr60 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr60</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr68 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr68</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr78 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr78</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-thunderbird_esr91 (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_thunderbird_esr91</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">tracking-win (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_win</code><br>
              <code>tracking-win</code>
          </td>
        </tr>
        <tr class="inactive" hidden>
          <td class="field_name">user-doc-firefox (inactive)
          </td>
          <td class="field_nickname">
              <code>cf_tracking_firefox_sumo</code>
          </td>
        </tr>
    </tbody>
  </table>
</div>

<h2 id="advanced_features">Advanced Features</h2>

<ul class="qs_help">
  <li>If you want to search for a <strong>phrase</strong> or something that
    contains spaces, commas, colons or quotes, you must put it in quotes, like:
    <kbd>"yes, this is a phrase"</kbd>. You must also use quotes to search for
    characters that would otherwise be interpreted specially by quicksearch.
    For example, <kbd>"this|that"</kbd> would search for the literal string
    <em>this|that</em> and would not be parsed as <kbd>"this OR that"</kbd>.
    Also, <kbd>"-field:value"</kbd> would search for the literal phrase
    <em>-field:value</em> and would not be parsed as
    <kbd>"NOT field:value"</kbd>.</li>

  <li>You can use <strong>AND</strong>, <strong>NOT</strong>,
    and <strong>OR</strong> in searches.

    You can also use <kbd>-</kbd> to mean "NOT", and <kbd>|</kbd> to mean "OR".
    There is no special character for "AND", because by default any search
    terms that are separated by a space are joined by an "AND".
    Examples:
    <ul>
      <li>
        <strong>NOT</strong>:<br>
        Use <kbd><strong>-</strong><em>summary:foo</em></kbd> to exclude
        bugs with <kbd>foo</kbd> in the summary.<br>
        <kbd><em>NOT summary:foo</em></kbd> would have the same effect.
      </li>
      <li>
        <strong>AND</strong>:<br>
        <kbd><em>foo bar</em></kbd> searches for bugs that contains
        both <kbd>foo</kbd> and <kbd>bar</kbd>.<br>
        <kbd><em>foo AND bar</em></kbd> would have the same effect.
      </li>
      <li>
        <strong>OR</strong>:<br>
        <kbd><em>foo<strong>|</strong>bar</em></kbd> would search
        for bugs that contain <kbd>foo</kbd> OR <kbd>bar</kbd>.<br>
        <kbd><em>foo OR bar</em></kbd> would have the same effect.<br>
      </li>
    </ul>

    <p>You cannot use | nor OR to enumerate possible values for a given field.
      You must use commas instead. So <kbd>field:value1,value2</kbd> does what
      you expect, but <kbd>field:value1|value2</kbd> would be treated as
      <kbd>field:value1 OR value2</kbd>, which means value2 is not bound to
      the given field.</p>

    <p>OR has higher precedence than AND; AND is the top level operation.
      For example:</p>
    <p>Searching for <em><kbd>url|location bar|field -focus</kbd></em> means
      (<kbd>url</kbd> OR <kbd>location</kbd>) AND (<kbd>bar</kbd> OR
      <kbd>field</kbd>) AND (NOT <kbd>focus</kbd>)</p>
  </li>

  <li>
    The default operator, colon (:), performs a <strong>substring</strong>
    match of the value. The following operators are supported:
    <ul>
      <li>
        <strong>:</strong> (substring):<br>
        <kbd><em>summary:foo</em></kbd> will search for bugs
        where the <kbd>summary</kbd> contains <kbd>foo</kbd>.
      </li>
      <li>
        <strong>=</strong> (equals):<br>
        <kbd><em>summary=foo</em></kbd> will search for bugs
        where the <kbd>summary</kbd> is exactly <kbd>foo</kbd>.
      </li>
      <li>
        <strong>!=</strong> (notequals):<br>
        <kbd><em>summary!=foo</em></kbd> will search for bugs
        where the <kbd>summary</kbd> is not <kbd>foo</kbd>.
      </li>
      <li>
        <strong>&gt;</strong> (greaterthan):<br>
        <kbd><em>creation_ts&gt;-2w</em></kbd> will search for bugs
        where that were created between two weeks ago and now, excluding bugs exactly two weeks old.
      </li>
      <li>
        <strong>&gt;=</strong> (greaterthaneq):<br>
        <kbd><em>creation_ts&gt;=-2w</em></kbd> will search for bugs
        where that were created between two weeks ago and now, including bugs exactly two weeks old.
      </li>
      <li>
        <strong>&lt;</strong> (lessthan):<br>
        <kbd><em>creation_ts&lt;-2w</em></kbd> will search for bugs
        where that were created more than two weeks ago, excluding bugs exactly two weeks old.
      </li>
      <li>
        <strong>&lt;=</strong> (lessthaneq):<br>
        <kbd><em>creation_ts&lt;=-2w</em></kbd> will search for bugs
        where that were created more than two weeks ago, including bugs exactly two weeks old.
      </li>
    </ul>
  </li>
</ul>

<h2 id="shortcuts">Advanced Shortcuts</h2>

<p>In addition to using <a href="#fields">field names</a> to search
  specific fields, there are certain characters or words that you can
  use as a "shortcut" for searching certain fields:</p>

<table cellspacing="0" cellpadding="0" border="0" class="standard qs_fields">
  <thead>
    <tr>
      <th class="field_name">Field</th>
      <th class="field_nickname">Shortcut(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="field_name">Status</td>
      <td class="field_nickname">
        Make the <strong>first word</strong> of your search the name of any
        status, or even an abbreviation of any status, and bugs
        in that status will be searched. <strong><kbd>ALL</kbd></strong>
        is a special shortcut that means "all statuses".
        <strong><kbd>OPEN</kbd></strong> is a special shortcut that means
        "all open statuses". Adding a '+' to the end of a status name will
        set the result limit to 0.
      </td>
    </tr>
    <tr>
      <td class="field_name">Resolution</td>
      <td class="field_nickname">
        Make the <strong>first word</strong> of your search the name of any
        resolution, or even an abbreviation of any resolution, and
        bugs with that resolution will be searched. For example,
        making <kbd>FIX</kbd> the first word of your search will find all
        bugs with a resolution of <kbd>FIXED</kbd>.
        Adding a '+' to the end of a resolution name will set the result limit
        to 0.
    </tr>
    <tr>
      <td class="field_name">Priority</td>
      <td class="field_nickname">"<strong>P1</strong>" (as a word anywhere in
        the search) means "find bugs with the highest priority.
        "P2" means the second-highest priority, and so on.
        <p>Searching for "<strong>P1-3</strong>" will find bugs in
        any of the three highest priorities, and so on.</p>
      </td>
    </tr>
    <tr>
      <td class="field_name">Assignee</td>
      <td class="field_nickname"><strong>@</strong><em>value</em></td>
    </tr>
    <tr>
      <td class="field_name">Product or
        Component</td>
      <td class="field_nickname"><strong>:</strong><em>value</em></td>
    </tr>
      <tr>
        <td class="field_name">Keywords</td>
        <td class="field_nickname"><strong>!</strong><em>value</em></td>
      </tr>
    <tr>
      <td class="field_name">Flags</td>
      <td class="field_nickname">
        <em>flag</em><strong>?</strong><em>requestee</em>
      </td>
    </tr>
    <tr>
      <td class="field_name">Comment
        or Summary</td>
      <td class="field_nickname">
        <strong>#</strong><em>value</em>
      </td>
    </tr>
    <tr>
      <td class="field_name">Comment Searching</td>
      <td class="field_nickname">
        Allows overriding of the comment searching preference.<br>
        "<strong>++comments</strong>" enables full-text search (all comments, slow)<br>
        "<strong>--comments</strong>" disables full-text search<br>
        "<strong>++description</strong>" enables description search (initial comment only)<br>
        "<strong>--description</strong>" disables description search<br>
      </td>
    </tr>
      <tr>
        <td class="field_name">Summary
          or Whiteboard</td>
        <td class="field_nickname"><strong>[</strong><em>value</em></td>
      </tr>
  </tbody>
</table>

<h2 id="advanced_examples">Examples of Complex Queries</h2>

<p>It is pretty easy to write rather complex queries without too much effort.
  For very complex queries, you have to use the
  <a href="/query.cgi?format=advanced">Advanced Search</a> form.</p>

<ul class="qs_help">
  <li>All bugs reported by userA@company.com or assigned to them
    (the initial @ is a shortcut for the assignee, see the
    <a href="#shortcuts">Advanced Shortcuts</a> section above):<br>
    <kbd>ALL @userA@company.com OR reporter:userA@company.com</kbd></li>
  <li>All open bugs in product productA with either severity
    blocker, critical or major, or with priority P1, or with the blocker+
    flag set, and which are neither assigned to userB@company.com nor to
    userC@company.com (we make the assumption that there are only two users
    matching userB and userC, else we would write the whole login name):<br>
    <kbd>:productA sev:blocker,critical,major OR pri:P1 OR flag:blocker+ -assign:userB,userC</kbd></li>
  <li>All FIXED bugs with the blocker+ flag set, but without
    the approval+ nor approval? flags set:<br>
    <kbd>FIXED flag:blocker+ -flag:approval+ -flag:approval?</kbd></li>
  <li>Bugs with <em>That's a "unusual" issue</em> in the
    bug summary (double quotes are escaped using <em>\"</em>):<br>
    <kbd>summary:"That's a \"unusual\" issue"</kbd></li>
</ul>
</div> 
</main> 
</div> 


</body>
</html>