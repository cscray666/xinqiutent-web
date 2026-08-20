/*
 * Xinqiu Tent — B2B Conversion Tracking & Attribution
 * Purpose: (1) capture & persist UTM source so lost referrers are recoverable
 *          (2) fire GA4 key events for every high-intent B2B action
 * Loaded on every page after gtag.js
 */
(function () {
  'use strict';

  var STORE_KEY = 'xq_attribution';

  /* ---------- 1. Attribution capture & persistence ---------- */
  function captureAttribution() {
    var params = new URLSearchParams(window.location.search);
    var utmSource = params.get('utm_source');
    var utmMedium = params.get('utm_medium');
    var utmCampaign = params.get('utm_campaign');

    var stored = null;
    try { stored = JSON.parse(sessionStorage.getItem(STORE_KEY)); } catch (e) {}

    // New UTM in URL always wins
    if (utmSource) {
      stored = {
        source: utmSource,
        medium: utmMedium || '(none)',
        campaign: utmCampaign || '(none)',
        landing: window.location.pathname + window.location.search,
        ts: Date.now()
      };
    } else if (!stored) {
      // No UTM and nothing stored → infer from referrer
      var ref = document.referrer || '';
      var inferred = '(direct)';
      var medium = '(none)';
      if (ref) {
        try {
          var host = new URL(ref).hostname.replace(/^www\./, '');
          if (host.indexOf(window.location.hostname.replace(/^www\./, '')) === -1) {
            inferred = host;
            medium = 'referral';
            if (/google\.|bing\.|duckduckgo|yahoo\./.test(host)) medium = 'organic';
            if (/chatgpt|openai|perplexity|claude\.ai|copilot/.test(host)) medium = 'ai_search';
            if (/linkedin|facebook|instagram|tiktok|twitter|x\.com/.test(host)) medium = 'social';
          }
        } catch (e) {}
      }
      stored = {
        source: inferred, medium: medium, campaign: '(none)',
        landing: window.location.pathname, ts: Date.now()
      };
    }

    if (stored) {
      try { sessionStorage.setItem(STORE_KEY, JSON.stringify(stored)); } catch (e) {}
    }
    return stored || {};
  }

  var attr = captureAttribution();

  function track(eventName, extra) {
    var payload = {
      attributed_source: attr.source || '(unknown)',
      attributed_medium: attr.medium || '(none)',
      attributed_campaign: attr.campaign || '(none)',
      page_path: window.location.pathname + window.location.search
    };
    if (extra) { for (var k in extra) { if (extra.hasOwnProperty(k)) payload[k] = extra[k]; } }
    if (typeof gtag === 'function') gtag('event', eventName, payload);
  }
  window.xqTrack = track;

  // Fire once per session so every visit carries a resolved source
  track('attribution_resolved', { landing_page: attr.landing || '' });

  /* ---------- 2. Auto-bind B2B key events ---------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest('a, button');
    if (!el) return;

    var href = (el.getAttribute('href') || '').toLowerCase();
    var text = (el.textContent || '').trim().substring(0, 80);

    // WhatsApp — highest intent
    if (href.indexOf('wa.me') > -1 || href.indexOf('whatsapp') > -1) {
      track('contact_whatsapp', { link_text: text });
      return;
    }
    // Email
    if (href.indexOf('mailto:') === 0) {
      track('contact_email', { link_text: text });
      return;
    }
    // Phone
    if (href.indexOf('tel:') === 0) {
      track('contact_phone', { link_text: text });
      return;
    }
    // Catalog / sample requests
    if (/catalog|swatch|sample/i.test(href) || /catalog|swatch|sample/i.test(text)) {
      track('lead_catalog_request', { link_text: text });
      return;
    }
    // Article reads
    if (href.indexOf('news.html?id=') > -1) {
      track('article_open', { article_url: href, link_text: text });
      return;
    }
    // Product category pages
    if (/(camping|pop-up|changing|roof-top|beach|inflatable|outdoor-furniture)-?tents?|outdoor-furniture/.test(href)) {
      track('product_category_view', { category_url: href });
      return;
    }
    // Outbound social
    if (/linkedin|facebook|instagram|tiktok/.test(href)) {
      track('social_outbound', { network_url: href });
    }
  }, true);

  /* ---------- 3. Form submissions ---------- */
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form || form.tagName !== 'FORM') return;
    track('lead_form_submit', { form_id: form.id || form.name || 'unnamed' });
  }, true);

  /* ---------- 4. Scroll depth (engagement quality) ---------- */
  var marks = { 25: false, 50: false, 75: false, 90: false };
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      if (h > 0) {
        var pct = (window.scrollY / h) * 100;
        for (var m in marks) {
          if (!marks[m] && pct >= Number(m)) {
            marks[m] = true;
            track('scroll_depth', { depth_percent: Number(m) });
          }
        }
      }
      ticking = false;
    });
  }, { passive: true });

  /* ---------- 5. Deep-read signal (60s+ on article) ---------- */
  if (window.location.pathname.indexOf('news.html') > -1) {
    setTimeout(function () { track('article_deep_read', { seconds: 60 }); }, 60000);
    setTimeout(function () { track('article_deep_read', { seconds: 180 }); }, 180000);
  }
})();
