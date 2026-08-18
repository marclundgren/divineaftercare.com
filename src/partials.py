# -*- coding: utf-8 -*-
"""Shared markup fragments for the Divine AfterCare static site."""

PHONE_DISPLAY = "(949) 787-6445"
PHONE_TEL = "+19497876445"
EMAIL = "info@divineaftercare.com"

# Icon sprite + the gradient the hour dials stroke with.
SPRITE = """
<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">
  <defs>
    <linearGradient id="dialgrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#C08A6C"/><stop offset="100%" stop-color="#A15576"/>
    </linearGradient>
    <symbol id="i-leaf" viewBox="0 0 24 24">
      <path d="M12 3c3.6 2.3 5.6 5.5 5.6 9s-2 6.7-5.6 9c-3.6-2.3-5.6-5.5-5.6-9S8.4 5.3 12 3Z" fill="none" stroke="currentColor" stroke-width="1.3"/>
      <path d="M12 3.4v17.2M12 9.5l3.6-2.6M12 9.5 8.4 6.9M12 14.6l3.6-2.6M12 14.6 8.4 12" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>
    </symbol>
    <symbol id="i-check" viewBox="0 0 24 24">
      <circle cx="12" cy="12" r="10.2" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".38"/>
      <path d="m7.8 12.3 2.9 2.9 5.6-6.2" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-arrow" viewBox="0 0 24 24">
      <path d="M4 12h15m0 0-5.4-5.4M19 12l-5.4 5.4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-phone" viewBox="0 0 24 24">
      <path d="M6.3 3.5h3l1.5 3.8-2 1.3a12.5 12.5 0 0 0 6.6 6.6l1.3-2 3.8 1.5v3a2 2 0 0 1-2.2 2A16.8 16.8 0 0 1 4.3 5.7a2 2 0 0 1 2-2.2Z" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-mail" viewBox="0 0 24 24">
      <rect x="2.8" y="5" width="18.4" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.3"/>
      <path d="m3.4 6.4 8.6 6.2 8.6-6.2" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
    </symbol>
    <symbol id="i-pin" viewBox="0 0 24 24">
      <path d="M12 21.5S4.9 15.6 4.9 10a7.1 7.1 0 1 1 14.2 0c0 5.6-7.1 11.5-7.1 11.5Z" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
      <circle cx="12" cy="10" r="2.6" fill="none" stroke="currentColor" stroke-width="1.3"/>
    </symbol>
    <symbol id="i-clock" viewBox="0 0 24 24">
      <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.3"/>
      <path d="M12 6.8V12l3.6 2.2" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-shield" viewBox="0 0 24 24">
      <path d="M12 2.8 4.8 5.7v6c0 4.6 3 8.2 7.2 9.5 4.2-1.3 7.2-4.9 7.2-9.5v-6L12 2.8Z" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
      <path d="m8.9 11.9 2.2 2.2 4-4.4" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-badge" viewBox="0 0 24 24">
      <circle cx="12" cy="9.4" r="5.6" fill="none" stroke="currentColor" stroke-width="1.3"/>
      <path d="m9.6 8.3 2 2 3.1-3.3" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="m8.4 14.4-1.3 6.4 4.9-2.6 4.9 2.6-1.3-6.4" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
    </symbol>
    <symbol id="i-star" viewBox="0 0 24 24">
      <path d="m12 3.4 2.6 5.6 6 .8-4.4 4.2 1.1 6L12 17.2 6.7 20l1.1-6L3.4 9.8l6-.8L12 3.4Z" fill="currentColor"/>
    </symbol>
    <symbol id="i-ig" viewBox="0 0 24 24">
      <rect x="3.4" y="3.4" width="17.2" height="17.2" rx="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
      <circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.4"/>
      <circle cx="16.9" cy="7.1" r="1.1" fill="currentColor"/>
    </symbol>
    <symbol id="i-fb" viewBox="0 0 24 24">
      <path d="M14.6 8.4h2.3V5.2h-2.6c-2.5 0-4 1.6-4 4.1v2H8v3.2h2.3v6.3h3.3v-6.3h2.4l.5-3.2h-2.9V9.6c0-.8.4-1.2 1-1.2Z" fill="currentColor"/>
    </symbol>
  </defs>
</svg>
"""

def head(title, description, canonical, extra=""):
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.divineaftercare.com{canonical}">
<meta name="theme-color" content="#FCFAF9">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Divine AfterCare">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.divineaftercare.com{canonical}">
<meta property="og:image" content="https://www.divineaftercare.com/assets/img/hero.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon.ico" sizes="any">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{SPRITE}"""


def header(active=""):
    def cur(name):
        return ' aria-current="page"' if active == name else ""
    return f"""
<header class="header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Divine AfterCare — home">
      <img src="/assets/img/mark.webp" alt="" width="340" height="223" fetchpriority="high">
      <span class="brand-text">
        <span class="brand-name">Divine</span>
        <span class="brand-sub">AfterCare</span>
      </span>
    </a>

    <nav class="nav" aria-label="Primary">
      <a href="/"{cur('home')}>Home</a>
      <a href="/services.html"{cur('services')}>Services</a>
      <a href="/recovery-packages.html"{cur('packages')}>Recovery Packages</a>
      <a href="/contact.html"{cur('contact')}>Contact</a>
    </nav>

    <div class="header-cta">
      <a class="tel-link" href="tel:{PHONE_TEL}">
        <svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg>{PHONE_DISPLAY}
      </a>
      <a class="btn btn-rose" href="/contact.html"><span>Reserve Care</span></a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>

<div class="drawer" id="drawer" aria-hidden="true">
  <nav class="drawer-nav" aria-label="Mobile">
    <a href="/">Home <span>01</span></a>
    <a href="/services.html">Services <span>02</span></a>
    <a href="/recovery-packages.html">Packages <span>03</span></a>
    <a href="/contact.html">Contact <span>04</span></a>
  </nav>
  <div class="drawer-foot">
    <a class="btn btn-rose" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>Call {PHONE_DISPLAY}</span></a>
    <a class="btn btn-ghost" href="mailto:{EMAIL}"><span>Email us</span></a>
  </div>
</div>
"""


FOOTER = f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" aria-label="Divine AfterCare — home">
          <img src="/assets/img/mark.webp" alt="" width="340" height="223" loading="lazy">
          <span class="brand-text">
            <span class="brand-name">Divine</span>
            <span class="brand-sub">AfterCare</span>
          </span>
        </a>
        <p class="footer-about">Divine AfterCare, LLC — Orange County, California. We connect you with licensed, independently practicing nurses for compassionate, concierge-level post-surgical care.</p>
        <div class="socials">
          <a href="https://www.instagram.com/divineaftercare/" target="_blank" rel="noopener" aria-label="Divine AfterCare on Instagram">
            <svg width="17" height="17" aria-hidden="true"><use href="#i-ig"/></svg>
          </a>
          <a href="https://www.facebook.com/profile.php?id=61592005871774" target="_blank" rel="noopener" aria-label="Divine AfterCare on Facebook">
            <svg width="17" height="17" aria-hidden="true"><use href="#i-fb"/></svg>
          </a>
        </div>
      </div>

      <div>
        <h3>Get in touch</h3>
        <div class="footer-links">
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="/contact.html">Submit a private inquiry</a>
          <span style="color:rgba(255,255,255,.44)">Orange County · Los Angeles · San Diego</span>
        </div>
      </div>

      <div>
        <h3>Explore</h3>
        <div class="footer-links">
          <a href="/">Home</a>
          <a href="/services.html">Services</a>
          <a href="/recovery-packages.html">Recovery packages</a>
          <a href="/privacy-policy.html">Privacy policy</a>
        </div>
      </div>
    </div>

    <p class="footer-disclaimer">Divine AfterCare is a private care coordination company. Nursing services are delivered by licensed, independently practicing nurses. Nothing on this site is medical advice — always follow the post-operative instructions given by your surgeon.</p>

    <div class="footer-bar">
      <span>&copy; <span data-year>2026</span> Divine AfterCare, LLC. All rights reserved.</span>
      <span>Orange County, California</span>
    </div>
  </div>
</footer>

<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""
