
// Ensure dataLayer and gtag exist before GA4 script loads.
// GA4 will automatically flush this queue once it initializes.
window.dataLayer = window.dataLayer || [];
window.gtag = window.gtag || function() { window.dataLayer.push(arguments); };

function sendEventToGA(eventName, params) {
    gtag('event', eventName, params || {});
}