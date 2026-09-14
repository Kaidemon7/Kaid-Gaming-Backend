"use strict";

(function () {

    let currentOAuthPopup = null;
    let notificationWrapper;
    let returnValue;
    let parentOverlay;

    window.OAuth = {
        init: function() {

            const params = new URLSearchParams(window.location.search);
            returnValue = params.get("return") ?? "";

            const providerLists = document.querySelectorAll(".oauthProviderList");
            for (let i = 0; i < providerLists.length; i++) {
                const providerList = providerLists[i];
                OAuth.initProviderList(providerList);
            }

            notificationWrapper = document.getElementById("OAuthNotificationWrapper"); 
        },

        showParentWindowOverlay: function () {

            if (parentOverlay) return;

            parentOverlay = document.createElement("div");
            parentOverlay.classList.add("oAuthOverlay");
            parentOverlay.classList.add("fixed");

            const link = document.createElement("a");
            link.innerText = "Continue with log in";
            link.setAttribute("href", "#");
            parentOverlay.addEventListener("click",
                function () {
                    if (!currentOAuthPopup || currentOAuthPopup === null || currentOAuthPopup.closed) {
                        OAuth.hideParentWindowOverlay();
                    } else {
                        currentOAuthPopup.focus();
                    }
                }
            );
            link.addEventListener("click",
                function() {
                    if (!currentOAuthPopup || currentOAuthPopup === null || currentOAuthPopup.closed) {
                        OAuth.hideParentWindowOverlay();
                    } else {
                        currentOAuthPopup.focus();
                    }
                }
            );
            parentOverlay.appendChild(link);

            document.body.appendChild(parentOverlay);
        },

        hideParentWindowOverlay: function () {
            if (!parentOverlay) return;
            parentOverlay.remove();
            parentOverlay = null;
        },

        initProviderList: function(providerList) {

            // Register/login/link etc.
            const mode = providerList.getAttribute("data-mode");

            const providerLinks = providerList.querySelectorAll("a.provider");
            for (let i = 0; i < providerLinks.length; i++) {
                const providerLink = providerLinks[i];
                providerLink.addEventListener("click",
                    function(e) {
                        e.preventDefault();

                        // Close current
                        if (currentOAuthPopup && !currentOAuthPopup.closed) {
                            currentOAuthPopup.close();
                            currentOAuthPopup = null;
                        }

                        // If linked, don't popup
                        const linked = this.getAttribute("data-linked");
                        if (linked && linked === "1") {
                            return;
                        }

                        const provider = this.getAttribute("data-provider");

                        // Get width/height
                        const popupWidth = Math.min(parseInt(this.getAttribute("data-popup-width")),
                            window.screen.availWidth);
                        const popupHeight = Math.min(parseInt(this.getAttribute("data-popup-height")),
                            window.screen.availHeight);

                        // Center the popup
                        const left = Math.max(0, (window.screen.availWidth - popupWidth) / 2);
                        const top = Math.max(0, (window.screen.availHeight - popupHeight) / 2);

                        const popupUrl = `/handlers/oauth/redirect.json?mode=${mode}&provider=${provider}&return=${encodeURIComponent(returnValue)}`;
                        currentOAuthPopup = window.open(
                            popupUrl,
                            `oAuthPop${provider}`,
                            `width=${popupWidth},height=${popupHeight},left=${left},top=${top},resizable=yes`
                        );
                        if (!currentOAuthPopup ||
                            currentOAuthPopup.closed ||
                            typeof currentOAuthPopup.closed === "undefined") {
                            alert("Popup was blocked by the browser.");
                        } 

                        OAuth.showParentWindowOverlay();

                        const interval = setInterval(() => {
                            if (!currentOAuthPopup || currentOAuthPopup.closed) {
                                clearInterval(interval);
                                OAuth.hideParentWindowOverlay();
                            }
                        }, 250);

                        window.addEventListener("message",
                            (event) => {

                                if (!secureRootDomain) {
                                    currentOAuthPopup.close();
                                    OAuth.showNotification("Secure root domain not available.", true);
                                    return;
                                }
                                
                                // Check if origin is valid
                                {
                                    const validOrigin = secureRootDomain
                                        .split(",")
                                        .map(s => s.trim().toLowerCase())
                                        .includes(event.origin.toLowerCase());
                                    if (!validOrigin) {
                                        console.warn("Invalid post message origin: " + event.origin);
                                        return;
                                    }
                                }

                                // Close the popup here - sometimes we have other origins posting here (EG stripe)
                                currentOAuthPopup.close();

                                const responseType = event.data.oAuthResponseType.toLowerCase();
                                const message = (event.data.message ?? "");
                                if (responseType === "Error".toLowerCase()) {

                                    OAuth.showNotification(message, true);
                                    OAuth.hideParentWindowOverlay();

                                } else if (responseType === "LoggedIn".toLowerCase()) {

                                    if (event.data.token) {
                                        const token = event.data.token;
                                        const userID = event.data.userID;
                                        window.location.href = window.location.origin + "/login?token=" + token + "&userID=" + userID + "&return=" + encodeURIComponent(event.data.redirectURL);
                                        return;
                                    }

                                    OAuth.showNotification("You're now logged in!  Redirecting...", false);
                                    OAuth.hideParentWindowOverlay();
                                    OAuth.disableFormOnRedirect();
                                    window.location.href = event.data.redirectURL;

                                } else if (responseType === "Registered".toLowerCase()) {

                                    OAuth.showNotification("Account created!  Redirecting...", false);
                                    OAuth.hideParentWindowOverlay();
                                    OAuth.disableFormOnRedirect();
                                    window.location.href = event.data.redirectURL;

                                } else if (responseType === "Linked".toLowerCase()) {

                                    OAuth.showNotification("Account linked!  Redirecting...", false);
                                    OAuth.hideParentWindowOverlay();
                                    window.location.reload();

                                }
                            });
                    });
            }
        },

        disableFormOnRedirect: function() {

            const formWraps = document.querySelectorAll(".oAuthFormWrap");
            for (let i = 0; i < formWraps.length; i++) {

                const formWrap = formWraps[i];

                const overlay = document.createElement("div");
                overlay.classList.add("oAuthOverlay");

                const spinner = document.createElement("span");
                spinner.classList.add("overlaySpinner");
                overlay.appendChild(spinner);

                formWrap.appendChild(overlay);

            }

        },

        showNotification: function(errorMessage, isError) {

            if (!notificationWrapper) {
                console.error(errorMessage);
                return;
            }
            
            notificationWrapper.innerHTML = "";
            const newNotification = document.createElement("div");
            newNotification.classList.add("notification");
            if (isError) newNotification.classList.add("error");
            else newNotification.classList.add("success");
            newNotification.innerHTML = errorMessage;
            notificationWrapper.appendChild(newNotification);
        }
    }

    OAuth.init();

})();