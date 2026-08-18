# -*- coding: utf-8 -*-
from partials import PHONE_DISPLAY, PHONE_TEL, EMAIL

AREAS = ["Newport Beach", "Irvine", "Mission Viejo", "Laguna Niguel", "Dana Point",
         "San Clemente", "Laguna Beach", "Costa Mesa", "Huntington Beach",
         "Los Angeles", "San Diego", "Beverly Hills"]


def build():
    chips = "".join(f"<li>{a}</li>" for a in AREAS)
    return f"""
<main id="main">

  <section class="page-hero">
    <div class="band-bg" style="background-image:url('/assets/img/nurse-bp.webp');--bg-pos:62% 32%"></div>
    <div class="wrap">
      <div class="section-head reveal is-in">
        <p class="eyebrow">Get in touch</p>
        <h1 class="h-display">Exceptional care begins with a conversation.</h1>
        <p class="lede" style="margin-top:1.5rem;max-width:56ch">Connect with us by phone, email, or the confidential form below, and we will walk you through your post-surgical aftercare options. Every inquiry is handled personally and privately.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap contact-grid">

      <div class="stack-lg reveal">
        <div class="contact-methods">
          <a class="contact-method" href="tel:{PHONE_TEL}">
            <svg width="24" height="24" style="color:var(--rose)" aria-hidden="true"><use href="#i-phone"/></svg>
            <span><small>Call us</small><b>{PHONE_DISPLAY}</b></span>
          </a>
          <a class="contact-method" href="mailto:{EMAIL}">
            <svg width="24" height="24" style="color:var(--rose)" aria-hidden="true"><use href="#i-mail"/></svg>
            <span><small>Email us</small><b>{EMAIL}</b></span>
          </a>
          <a class="contact-method" href="sms:{PHONE_TEL}">
            <svg width="24" height="24" style="color:var(--rose)" aria-hidden="true"><use href="#i-pin"/></svg>
            <span><small>Service area</small><b>Orange County &amp; beyond</b></span>
          </a>
        </div>

        <div class="stack">
          <h2 class="h-2">Where we provide care</h2>
          <p>Concierge post-surgical aftercare throughout Orange County, with extended coverage across Los Angeles and San Diego. If your city is not listed, ask — we very likely cover it.</p>
          <ul class="chips">{chips}</ul>
        </div>

        <div class="stack">
          <h2 class="h-2">Before you reach out</h2>
          <p>It helps to have your procedure type and surgery date handy, along with where you plan to recover. If your date is not confirmed yet, reach out anyway — availability fills quickly and we can hold time provisionally.</p>
        </div>
      </div>

      <div class="reveal" data-delay="120">
        <div class="stack" style="margin-bottom:2rem">
          <p class="eyebrow">Private inquiry</p>
          <h2 class="h-1">Tell us about your recovery.</h2>
        </div>

        <form class="form" id="inquiry" novalidate>
          <div class="form-row">
            <div class="field">
              <label for="f-name">Full name</label>
              <input id="f-name" name="name" type="text" autocomplete="name" required placeholder="Jane Doe">
            </div>
            <div class="field">
              <label for="f-phone">Phone</label>
              <input id="f-phone" name="phone" type="tel" autocomplete="tel" required placeholder="(949) 555-0100">
            </div>
          </div>

          <div class="field">
            <label for="f-email">Email</label>
            <input id="f-email" name="email" type="email" autocomplete="email" required placeholder="jane@example.com">
          </div>

          <div class="form-row">
            <div class="field">
              <label for="f-procedure">Procedure or care needed</label>
              <input id="f-procedure" name="procedure" type="text" required placeholder="e.g. tummy tuck, companion care">
            </div>
            <div class="field">
              <label for="f-date">Surgery or start date</label>
              <input id="f-date" name="date" type="date">
            </div>
          </div>

          <div class="form-row">
            <div class="field">
              <label for="f-location">Where will you recover?</label>
              <select id="f-location" name="location">
                <option>At home</option>
                <option>Hotel or recovery suite</option>
                <option>Short-term rental</option>
                <option>Not yet decided</option>
              </select>
            </div>
            <div class="field">
              <label for="f-duration">Coverage needed</label>
              <select id="f-duration" name="duration">
                <option>4 hours</option>
                <option>6 hours</option>
                <option>8 hours</option>
                <option>12 hours</option>
                <option>24 hours</option>
                <option>Ongoing companion care</option>
                <option>Transport only</option>
                <option>Not sure &mdash; please advise</option>
              </select>
            </div>
          </div>

          <div class="field">
            <label for="f-message">Anything else we should know?</label>
            <textarea id="f-message" name="message" placeholder="Your surgeon, mobility considerations, who else is at home, preferred contact times&hellip;"></textarea>
          </div>

          <div class="btn-row" style="margin-top:.5rem">
            <button type="submit" class="btn btn-rose"><span>Send private inquiry</span></button>
          </div>

          <p class="form-status" role="status"></p>
          <p class="form-note">Everything you share is kept strictly confidential and used solely to coordinate your care. Read our <a href="/privacy-policy.html" style="color:var(--rose-text)">privacy policy</a>. Prefer to talk? Call <a href="tel:{PHONE_TEL}" style="color:var(--rose-text)">{PHONE_DISPLAY}</a>.</p>
        </form>
      </div>

    </div>
  </section>

  <section class="section-tight cta-band">
    <div class="band-bg" style="background-image:url('/assets/img/hotel-bamboo.webp')"></div>
    <div class="wrap center stack">
      <h2 class="h-2 reveal">We look forward to connecting with you.</h2>
      <div class="btn-row center reveal" style="margin-top:1.5rem">
        <a class="btn btn-rose" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </section>

</main>
"""
