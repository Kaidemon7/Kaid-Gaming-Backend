<!DOCTYPE html>
<html lang='en' dir='ltr'>
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>VK | Login</title>
    <link type="text/css"  rel="stylesheet" href="https://vk.com/css/al/common.a1752a2c.css" /><link type="text/css"  rel="stylesheet" href="https://vk.com/css/al/base.6a12502f.css" /><link type="text/css"  rel="stylesheet" href="https://vk.com/css/al/vkui.490dad1c.css" /><link type="text/css"  rel="stylesheet" href="https://vk.com/css/al/fonts_utf.d8d897c2.css" /><link type="text/css"  rel="stylesheet" href="https://vk.com/css/al/fonts_cnt_async.238bb183.css" />
    <link type="text/css"  rel="stylesheet" href="https://vk.com/css/api/oauth_popup.fd217d97.css" />
    <script type="text/javascript" language="javascript" src="https://vk.com/js/api/common_light.js?2"></script>
    <script type="text/javascript" language="javascript">// <![CDATA[
      function allow(button) {
        if (isButtonLocked(button)) return false;
        lockButton(button);

        var addr = '';
        if (isChecked('allow_notifications')) {
          addr = '&notify=1';
        }
        if (isChecked('denied_email')) {
          addr += '&email_denied=1';
        }
        if (isChecked('denied_phone')) {
          addr += '&phone_denied=1';
        }
        location.href = "https://login.vk.com/?act=grant_access&client_id=-1&settings=0&scope=&response_type=code&group_ids=&token_type=0&v=&display=widget&ip_h=1895db4b28f9562b31&hash=1789102016_dabc63010df1aac920&https=1&state=&redirect_uri=https%3A%2F%2Fvk.com%2Fshare.php%3Furl%3D%257B0%257D%26title%3D%257B1%257D%26description%3D%257B2%257D%26image%3D%257B3%257D"+addr;
        return false;
      }

      function cancel() {
        location.href = "https://login.vk.com/?act=grant_access&client_id=-1&settings=0&scope=&response_type=code&group_ids=&token_type=0&v=&display=widget&ip_h=1895db4b28f9562b31&hash=1789102016_dabc63010df1aac920&https=1&state=&redirect_uri=https%3A%2F%2Fvk.com%2Fshare.php%3Furl%3D%257B0%257D%26title%3D%257B1%257D%26description%3D%257B2%257D%26image%3D%257B3%257D&cancel=1";
        return false;
      }

      function login(button) {
        if (isButtonLocked(button)) return false;
        lockButton(button);
        document.querySelector('#login_submit').submit();
      }

      function doResize(onResize) {
        onResize && setTimeout(function() {
          doResize()
        }, 100);

        if (!hasClass(document.body, 'oauth_centered') && !onResize) {
          if (window.outerHeight !== void 0) {
            var panelH = (window.outerHeight - window.innerHeight) | 0,
              panelW = (window.outerWidth - window.innerWidth) | 0;
          } else {
            var panelH = 50,
              panelW = 0;
          }
          var contentH = Math.max(document.querySelector('#oauth_wrap_content').offsetHeight, 430),
            contentW = 655;
          window.resizeTo(contentW + panelW, contentH + panelH);
          window.moveTo(
            (screen.width - contentW) / 2 + (screen.availLeft | 0),
            ((screen.height - contentH) / 2) + (screen.availTop | 0)
          );
        }
      }

      function toggleEmailPrivacy() {
        checkbox('denied_email');
        if (!isChecked('denied_email')) {
          hide('denied_email');
          show('allowed_email');
        } else {
          hide('allowed_email');
          show('denied_email');
        }
      }

      function togglePhonePrivacy() {
        checkbox('denied_phone');
        if (!isChecked('denied_phone')) {
          hide('denied_phone');
          show('allowed_phone');
        } else {
          hide('allowed_phone');
          show('denied_phone');
        }
      }

      if (parent && parent != window) {
        location.href = "https://oauth.vk.com/blank.html";
      }

      
    // ]]></script>
  </head>

  <body onload="doResize();" class="VK1 oauth_full">
    <script>
      if (window.devicePixelRatio >= 2) document.body.className += ' is_2x';
    </script>
    <div class="oauth_wrap">
      <div class="oauth_wrap_inner">
        <div class="oauth_wrap_content" id="oauth_wrap_content">
          <div class="oauth_head">
  <a class="oauth_logo fl_l" href="https://vk.com" target="_blank"></a>
  <div id="oauth_head_info" class="oauth_head_info fl_r">
  <a class="oauth_reg_link" href="https://vk.com/join?reg=1" target="_blank">Sign up</a>
</div>
</div>

<div class="oauth_content box_body clear_fix">
  <div class="box_msg_gray box_msg_padded">Sign in to <b>VK</b> to continue</div>

  <form method="POST" id="login_submit" action="https://login.vk.com/?act=login&soft=1">
    <div class="oauth_form">

      

      <div>
        <div class="oauth_form_login_content">
          <input type="hidden" name="ip_h" value="1895db4b28f9562b31" />
          <input type="hidden" name="lg_domain_h" value="8e383f5585ba6f926b" />
          <input type="hidden" name="_origin" value="https://oauth.vk.com" />
          <input type="hidden" name="to" value="aHR0cHM6Ly9vYXV0aC52ay5jb20vYXV0aG9yaXplP2NsaWVudF9pZD0tMSZyZWRpcmVjdF91cmk9aHR0cHMlM0ElMkYlMkZ2ay5jb20lMkZzaGFyZS5waHAlM0Z1cmwlM0QlMjU3QjAlMjU3RCUyNnRpdGxlJTNEJTI1N0IxJTI1N0QlMjZkZXNjcmlwdGlvbiUzRCUyNTdCMiUyNTdEJTI2aW1hZ2UlM0QlMjU3QjMlMjU3RCZyZXNwb25zZV90eXBlPSZzY29wZT0wJnY9JnN0YXRlPSZkaXNwbGF5PXdpZGdldA--" />
          <input type="hidden" id="expire" name="expire" value="0" />

          <div class="oauth_form_header">Phone or email</div>
          <input type="text" class="oauth_form_input dark" name="email" value="">
          <div class="oauth_form_header">Password</div>
          <input type="password" class="oauth_form_input dark" name="pass" />
        </div>

        <input type="hidden" name="captcha_sid" value="40819f34-644a-42cd-b5dc-eca0b030e00e">

<div class="oauth_form_not_robot_captcha_container"></div>
<input class="oauth_form_not_robot_captcha_token_input" type="hidden" name="success_token" />

<script type="text/javascript" language="javascript" src="https://static.vk.com/captchaSDK/loader/1/umd/index.js"></script>

<script>
  (function() {
    const initNotRobotCaptcha = async () => {
      const { CaptchaWidget } = await window.vkidCaptcha;
      const captchaWidget = new CaptchaWidget();
      const captchaContainer = document.querySelector('.oauth_form_not_robot_captcha_container');

      try {
        const successToken = await captchaWidget.show({
          container: captchaContainer,
          iframeSrc: 'https://id.vk.com/not_robot_captcha?domain=vk.com&session_token=eyJhbGciOiJBMjU2R0NNS1ciLCJlbmMiOiJBMjU2R0NNIiwiaXYiOiI4RmJya1huZ3RRZEc0WGp4Iiwia2lkIjoiNmFmMDVhYjEtMzFjNi00YmNjLTgzYWMtM2QyMGU3YjFjNjA2IiwidGFnIjoiNUpGNWcxS3MtYVJ2ZWZoSlM3bDFWZyIsInppcCI6IkRFRiJ9.sEoqYLUXKUrpb-AZpv59gzIndV0ems47zInLdnnS6jc.GqhpkCUt0YWjGaw3.2o_PIhToseVWUEKag-nr848akuod_hCH3qz-7uGpzTIXpBeojUAINPozC-j18yIRw47zoQw3o1iXuZdBuD-rDBRZKy8c4e_550CSTHDsdsirvsCqzULcSJYLi7EMFzp_5sKrMCGtv_4b9JP6iLAZhcSAqKigC-bqpsKrfwIjX7JMW7nt2JHi8jO-CI3HPmLDnSe-gjRppkKjWJ-83xStVfX8cFzX2xjp6a5OEeDSy_ufQah92Vl98AWx01EHW8hu-AqmxqO3J7s5-naGvT_hIv5wcGhSV_VSJM5rGWH6h8KpDg08EDHCPr73NGYz298amGCoGlJo4DZ_0QSqysMUpFUV-xd9DoQhY360u7vVKWqorpY9lE6l-OI7Vtv7CiQG5ALQCDUqccOeiI_tdtmM4NpzcVdLewb7lir4YcwQs0GjIUV2cwQHLD6ev9Ongxl2g8jg86sp-McwdLhhQQqvCkpWs9MF8JAQI3qIP6AYMrLCeqWUv56WmwONdr4KETm5vU0Y3qoDdTwG4XJ5UE5DdZJ9mrAs-r4hN3RxtuwhE4WXG8lasWABTsTMufYKSBfictuKq_fpu9ALpiRVs5mdqhycpBQpqH3trFhZxWtnxO1wAaTTevXacNKrNrT4JVE_v005MYl15loqfmHDBy6700spneltMJfrIq7SihMbITbdIQn2_OWsJ24zlLimYdy219e9AJTmILmetBunekD13P-YnBqQdGHPEsrEiV3FERnCX_35Dazmu5u1zxi966sr4ejU1usc5M3ziYdwGHGXjLI9-mgyFRRNF0iinBwKEP0lt4n8IhSl8bboBw0XE9x-UCEg0o1olpu5DBd5j6jeFyAYFt0jLeh5ih1tIIluEUqBBQpL-3pdZGObbxL4HOCHcBrtEsRIX4ssrMPQ6IMG72bihFncURpRViFV6i65N6A_nCmRv4dS-mgPb4ILUzUIhPmG6qYpWhMPB7BrlB6beFPArO3DgcmyqPGLXZ8EXjBc5yYkHIveABLJosui4s7RcORw0YwGS9NmT4TN9HNJ86rC4KXW2D3HNkzRktolUD9EwOFycUjFowqVt3yLfRzIOfJmEbdfEJk2IceSZzqK6I9XinXt_OJaSAySdk5lwxYlf8n6wye0QqGZVoE_By12fmy1z7iGEwfBPalaCpsJ9OoxZVlZGs84WCVbtkLmgrnssCARwmU1v6IWHdbmkRdLrdtkgUlWCnIyUIQnBHnUPqbec2furmaFsqHC6RhnTPKhIKpv-uJ20sAPfFVmm5wjwKy8.yi-LI_N3sM2CgSs3y_NxRg&variant=popup&blank=1',
          captchaType: 'type_1',
          view: 'block',
        });
        const tokenInputElement = document.querySelector('.oauth_form_not_robot_captcha_token_input');
        tokenInputElement.value = successToken;
      } catch (error) {
        if (error !== 'close') {
          console.error(error);
        }
      }
    };

    initNotRobotCaptcha();
  })();
</script>

        <div class="oauth_form_login_content">
          <button class="flat_button oauth_button button_wide" id="install_allow" type="submit" onclick="return login(this);">Sign in</button>
          <a class="oauth_forgot" href="https://vk.com/restore" target="_blank">Forgot your password?</a>
          <input type="submit" name="submit_input" class="unshown">
        </div>
      </div>
    </div>
  </form>
</div>
        </div>
      </div>
    </div>
  </body>
</html>