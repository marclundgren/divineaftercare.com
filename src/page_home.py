# -*- coding: utf-8 -*-
from partials import PHONE_DISPLAY, PHONE_TEL, EMAIL

SERVICES = [
    ("In-home aftercare", "Healing in the comfort of your own home",
     "One-on-one nursing tailored to your procedure — medication administration, wound and drain care, mobility assistance, and continuous monitoring, all in your own space.",
     "/assets/img/service-inhome.webp",
     "A licensed nurse checks a recovering patient's blood pressure in her bedroom at home.",
     "/services.html#in-home"),
    ("Hotel &amp; away aftercare", "Professional recovery wherever you stay",
     "Traveling for surgery shouldn't mean compromising your recovery. We bring the same nursing care to your hotel, recovery suite, or short-term residence.",
     "/assets/img/service-hotel.webp",
     "An ocean-view hotel suite in Orange County prepared for post-surgical recovery.",
     "/services.html#hotel"),
    ("Personalized care plans", "Care designed around your recovery",
     "Every procedure is different and so is every patient. We build your plan around your surgery, your timeline, your household, and your surgeon's instructions.",
     "/assets/img/service-plans.webp",
     "A private duty nurse takes a patient's pulse during an in-home recovery visit.",
     "/services.html#plans"),
]

DIFFERENCE = [
    ("i-pin", "Care at your location",
     "After surgery, movement should be reserved entirely for healing. Your nurse comes to you — at home or at your hotel, anywhere in Southern California."),
    ("i-badge", "Surgical team coordination",
     "We stay in close contact with your surgeon and their team throughout recovery, so every post-operative instruction is observed and nothing falls between the cracks."),
    ("i-leaf", "Truly personalized nursing",
     "You are not a case number or a care protocol. Every shift is built around you — your needs, your procedure, your recovery — with undivided attention start to finish."),
    ("i-shield", "Absolute privacy",
     "What you are going through is deeply personal. Your care, your story, and the details of your recovery stay entirely confidential. Always."),
    ("i-clock", "Flexible, responsive scheduling",
     "Recovery doesn't conform to a calendar. Care comes in 4, 6, 8, 12, and 24-hour increments, adapted to your procedure and your evolving needs."),
    ("i-check", "Fully equipped, fully prepared",
     "Nothing for you to arrange. Your nurse arrives with wound care supplies, vital monitoring equipment, and everything else the shift requires."),
]

SCOPE = [
    "Medication administration and pain management",
    "Post-operative monitoring — swelling, bruising, and discomfort assessment",
    "Wound care, dressing changes, and surgical drain management",
    "Vital signs monitoring",
    "Compression garment assistance and lymphatic support",
    "Monitoring for infection, excessive bleeding, and post-surgical complications",
    "Direct communication with your plastic surgeon and surgical team",
    "Mobility support and positioning guidance",
    "Assistance with personal hygiene, bathing, dressing, and grooming",
    "Housekeeping, laundry, pet assistance, and activities of daily living",
    "Emotional reassurance and attentive check-ins throughout your recovery",
    "Concierge transport from your surgical facility to your place of recovery",
]

QUOTES = [
    ("The nursing care I received was exceptional. My nurse was attentive, compassionate, and made my recovery feel much less overwhelming.", "Danielle M. — Mission Viejo"),
    ("I felt supported every step of the way. The nurse answered all my questions and helped me feel comfortable during recovery.", "Connie S. — Lake Forest"),
    ("Professional, knowledgeable, and reliable. The aftercare gave me confidence that I was healing properly.", "James H. — Irvine"),
    ("Outstanding care and attention to detail. My nurse was patient, reassuring, and always available when I needed assistance.", "Andrea L. — Trabuco Canyon"),
    ("The level of care exceeded my expectations. Recovery was much smoother thanks to the guidance and support I received.", "Jennifer F. — Newport Beach"),
    ("Friendly and attentive from start to finish. The nursing team made me feel safe, comfortable, and well cared for throughout my recovery.", "Kristen S. — Los Angeles"),
]

FAQS = [
    ("What is included in your care packages?",
     "All packages carry a four-hour minimum and include medication monitoring, wound care, dressing changes, vital sign monitoring, compression garment assistance, bathing and grooming assistance, meal preparation, and direct communication with your surgical team. Every plan can be further tailored to your specific procedure and recovery requirements."),
    ("Are your nurses licensed?",
     "Yes. Every member of the Divine AfterCare nursing team is fully licensed and has completed a thorough background screening before joining our practice."),
    ("How far in advance should I arrange care?",
     "Reach out as soon as your surgery date is confirmed. Availability fills quickly, and booking early ensures we are with you from the very first day of your recovery."),
    ("Do you coordinate with my surgeon?",
     "Yes. We work in close collaboration with your surgical team so all post-operative instructions are followed and any concerns arising during recovery are communicated promptly."),
    ("What types of care do you specialize in?",
     "Personalized post-surgical recovery and compassionate elderly companion care. For seniors we provide assistance with daily activities, companionship, mobility support, medication reminders, and overall wellness — whether you are recovering from surgery yourself or arranging trusted care for a loved one."),
    ("What procedures do you support?",
     "A wide range, including body contouring, breast augmentation and revision, rhinoplasty, facelifts, liposuction, tummy tucks, and orthopedic surgeries. Whether your procedure was elective, reconstructive, or medically necessary, we are here to support your recovery."),
    ("Is my personal and health information kept private?",
     "Absolutely. Anything you share — medical history, surgical details, personal contact information — is kept strictly confidential, used solely to coordinate your care, and never sold or shared with third parties without your explicit consent. All client information is handled in accordance with applicable California privacy laws."),
    ("What is your cancellation policy?",
     "Cancellations must be made a minimum of 48 hours in advance."),
]

PRESS = ["Vogue", "Harper's Bazaar", "Allure", "Well + Good", "RealSelf"]


def build():
    svc = "\n".join(f"""
        <a class="svc-card reveal" data-delay="{i*90}" href="{link}">
          <div class="svc-media"><img src="{img}" alt="{alt}" loading="lazy" width="900" height="600"></div>
          <div class="svc-body">
            <p class="eyebrow">{eyebrow}</p>
            <h3 class="h-3">{title}</h3>
            <p>{body}</p>
            <span class="link-arrow">Learn more <svg width="14" height="14" aria-hidden="true"><use href="#i-arrow"/></svg></span>
          </div>
        </a>""" for i, (eyebrow, title, body, img, alt, link) in enumerate(SERVICES))

    diff = "\n".join(f"""
        <article class="diff">
          <svg class="diff-icon" width="26" height="26" aria-hidden="true"><use href="#{icon}"/></svg>
          <h3>{t}</h3>
          <p>{b}</p>
        </article>""" for icon, t, b in DIFFERENCE)

    half = (len(SCOPE) + 1) // 2
    def scope_col(items):
        return "\n".join(f"""            <li><svg width="17" height="17" aria-hidden="true" style="color:var(--gold-lt)"><use href="#i-leaf"/></svg>{s}</li>""" for s in items)

    quotes = "\n".join(f"""
        <figure class="quote reveal" data-delay="{(i%3)*90}">
          <div class="stars" aria-label="Five out of five stars">{'<svg width="13" height="13" style="color:var(--gold)" aria-hidden="true"><use href="#i-star"/></svg>' * 5}</div>
          <blockquote><p>{q}</p></blockquote>
          <figcaption><cite>{who}</cite></figcaption>
        </figure>""" for i, (q, who) in enumerate(QUOTES))

    faqs = "\n".join(f"""
        <details{' open' if i == 0 else ''}>
          <summary>{q}</summary>
          <div class="faq-body"><p>{a}</p></div>
        </details>""" for i, (q, a) in enumerate(FAQS))

    press = "".join(f"<span>{p}</span>" for p in PRESS)

    return f"""
<main id="main">

  <!-- ── hero ────────────────────────────────────────────── -->
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy reveal is-in">
        <p class="eyebrow">Southern California aftercare</p>
        <h1 class="h-display">Where clinical excellence meets <em>genuine compassion</em>.</h1>
        <p class="lede hero-lede">Concierge post-surgical aftercare delivered by licensed nurses — to your home, your hotel, or wherever your recovery takes you across Orange County, Los Angeles, and San Diego.</p>
        <div class="btn-row">
          <a class="btn btn-rose" href="/contact.html"><span>Reserve your recovery</span></a>
          <a class="btn btn-ghost" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>{PHONE_DISPLAY}</span></a>
        </div>
      </div>

      <div class="arch-frame reveal is-in" data-delay="160">
        <div class="arch">
          <img src="/assets/img/hero.webp" alt="A calm, light-filled coastal suite prepared for post-surgical recovery." width="1200" height="1500" fetchpriority="high">
        </div>
        <div class="hero-stat">
          <svg width="26" height="26" aria-hidden="true" style="color:var(--rose)"><use href="#i-badge"/></svg>
          <span>
            <b>Licensed &amp; vetted</b>
            <small>Every nurse, every shift</small>
          </span>
        </div>
      </div>
    </div>
  </section>

  <!-- ── trust strip ─────────────────────────────────────── -->
  <section class="trust">
    <div class="wrap" style="padding-inline:0">
      <div class="trust-inner">
        <div class="trust-item"><svg width="20" height="20" style="color:var(--rose)" aria-hidden="true"><use href="#i-badge"/></svg><span><b>Licensed nurses</b><span>Background-screened before their first shift</span></span></div>
        <div class="trust-item"><svg width="20" height="20" style="color:var(--rose)" aria-hidden="true"><use href="#i-clock"/></svg><span><b>4 to 24-hour shifts</b><span>Overnight and round-the-clock coverage</span></span></div>
        <div class="trust-item"><svg width="20" height="20" style="color:var(--rose)" aria-hidden="true"><use href="#i-pin"/></svg><span><b>OC · LA · San Diego</b><span>We come to your home or hotel</span></span></div>
        <div class="trust-item"><svg width="20" height="20" style="color:var(--rose)" aria-hidden="true"><use href="#i-shield"/></svg><span><b>Complete discretion</b><span>Your recovery stays entirely private</span></span></div>
      </div>
    </div>
  </section>

  <!-- ── about ───────────────────────────────────────────── -->
  <section class="section">
    <div class="wrap split">
      <div class="split-media reveal">
        <div class="arch-frame">
          <div class="arch" style="aspect-ratio:4/4.7">
            <img src="/assets/img/about-owner.webp" alt="The founder of Divine AfterCare in branded scrubs with a stethoscope." loading="lazy" width="1000" height="1180">
          </div>
        </div>
      </div>
      <div class="stack-lg reveal" data-delay="120">
        <div>
          <p class="eyebrow">About</p>
          <h2 class="h-1">Built for the moments that matter most.</h2>
        </div>
        <p class="lede">Divine AfterCare is a private care coordination company specializing in post-surgical aftercare for people who recognize that results are shaped as much by the recovery as by the procedure itself.</p>
        <p>We coordinate care wherever you are — at home, at your hotel, anywhere in Southern California — connecting you with independently licensed nurses who bring expert post-surgical care with the elegance, discretion, and personal attention you deserve. Every visit is tailored, every detail considered, every client treated as the priority.</p>
        <p class="rule-quote">This is recovery, elevated.</p>
        <div class="btn-row"><a class="btn" href="/contact.html"><span>Connect with our team</span></a></div>
      </div>
    </div>
  </section>

  <!-- ── press marquee ───────────────────────────────────── -->
  <section class="section-tight" style="padding-block:0">
    <p class="eyebrow eyebrow-c center" style="margin-bottom:1.5rem">Our clients&rsquo; world</p>
    <div class="marquee">
      <div class="marquee-track" aria-hidden="true">{press}{press}</div>
    </div>
  </section>

  <!-- ── services ────────────────────────────────────────── -->
  <section class="section band-linen">
    <div class="wrap">
      <div class="section-head center reveal" style="margin-bottom:clamp(2.5rem,4vw,3.5rem)">
        <p class="eyebrow">Services</p>
        <h2 class="h-1">Our concierge recovery services</h2>
      </div>
      <div class="cards-3">{svc}
      </div>
    </div>
  </section>

  <!-- ── packages teaser ─────────────────────────────────── -->
  <section class="section">
    <div class="wrap split reverse">
      <div class="split-media reveal">
        <div class="arch">
          <img src="/assets/img/woman-recovering.webp" alt="A patient resting comfortably during recovery." loading="lazy" width="1000" height="1250">
        </div>
      </div>
      <div class="stack-lg reveal" data-delay="120">
        <div>
          <p class="eyebrow">Recovery packages</p>
          <h2 class="h-1">Care measured in hours, not guesswork.</h2>
        </div>
        <p class="lede">From a focused four-hour visit right after your procedure to round-the-clock overnight coverage, every package is priced transparently and can be tailored to your recovery.</p>
        <ul class="scope-list" style="max-width:44ch">
          <li><svg width="17" height="17" style="color:var(--gold)" aria-hidden="true"><use href="#i-check"/></svg>Four-hour minimum, up to 24-hour continuous care</li>
          <li><svg width="17" height="17" style="color:var(--gold)" aria-hidden="true"><use href="#i-check"/></svg>Ongoing companion care for elderly clients</li>
          <li><svg width="17" height="17" style="color:var(--gold)" aria-hidden="true"><use href="#i-check"/></svg>Concierge transport from your surgical facility</li>
        </ul>
        <div class="btn-row"><a class="btn btn-rose" href="/recovery-packages.html"><span>View packages &amp; pricing</span></a></div>
      </div>
    </div>
  </section>

  <!-- ── the divine difference ───────────────────────────── -->
  <section class="section band-deep">
    <div class="wrap">
      <div class="section-head reveal" style="margin-bottom:clamp(2.5rem,4vw,3.5rem)">
        <p class="eyebrow">The Divine difference</p>
        <h2 class="h-1">A standard of care that exceeds the ordinary.</h2>
      </div>
      <div class="grid-6 reveal">{diff}
      </div>
    </div>
  </section>

  <!-- ── scope of care ───────────────────────────────────── -->
  <section class="section">
    <div class="wrap">
      <div class="section-head reveal" style="margin-bottom:clamp(2rem,3.5vw,3rem)">
        <p class="eyebrow">Scope of care</p>
        <h2 class="h-1">Comprehensive support, from the first hour forward.</h2>
        <p class="lede" style="margin-top:1.25rem">From the moment your procedure ends to the day you feel fully yourself again, we manage every clinical and personal detail — so your only responsibility is to rest and heal.</p>
      </div>
      <div class="scope-grid reveal" data-delay="100">
        <ul class="scope-list">
{scope_col(SCOPE[:half])}
        </ul>
        <ul class="scope-list">
{scope_col(SCOPE[half:])}
        </ul>
      </div>
    </div>
  </section>

  <!-- ── cta band ────────────────────────────────────────── -->
  <section class="section cta-band">
    <div class="band-bg" style="background-image:url('/assets/img/hotel-bamboo.webp')"></div>
    <div class="wrap center stack-lg">
      <div class="reveal">
        <p class="eyebrow eyebrow-c">Unwind · Restore · Recover</p>
        <h2 class="h-1" style="max-width:20ch;margin-inline:auto">Let us design a care plan built entirely around you.</h2>
      </div>
      <p class="lede reveal" style="max-width:52ch;margin-inline:auto">Reach out today and we will handle every detail — from your first night home to your final follow-up appointment.</p>
      <div class="btn-row center reveal">
        <a class="btn btn-rose" href="/contact.html"><span>Arrange your care</span></a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </section>

  <!-- ── testimonials ────────────────────────────────────── -->
  <section class="section band-linen">
    <div class="wrap">
      <div class="section-head center reveal" style="margin-bottom:clamp(2.5rem,4vw,3.5rem)">
        <p class="eyebrow">Testimonials</p>
        <h2 class="h-1">What our patients are saying</h2>
      </div>
      <div class="quotes">{quotes}
      </div>
    </div>
  </section>

  <!-- ── faq ─────────────────────────────────────────────── -->
  <section class="section">
    <div class="wrap split" style="align-items:start">
      <div class="stack reveal sticky-col">
        <p class="eyebrow">Questions &amp; answers</p>
        <h2 class="h-1">What you may wish to know.</h2>
        <p>Still have a question? We answer every inquiry personally.</p>
        <div class="btn-row" style="margin-top:.5rem"><a class="btn btn-ghost" href="/contact.html"><span>Ask us directly</span></a></div>
      </div>
      <div class="faq reveal" data-delay="100">{faqs}
      </div>
    </div>
  </section>

  <!-- ── contact ─────────────────────────────────────────── -->
  <section class="section band-deep" id="contact">
    <div class="wrap contact-grid">
      <div class="stack-lg reveal">
        <div>
          <p class="eyebrow">Get in touch</p>
          <h2 class="h-1">We are here when you need us.</h2>
        </div>
        <p class="lede">Your comfort and discretion come first, even in how you reach us. Connect by phone, email, or our confidential inquiry form and we will respond personally.</p>
        <div class="btn-row">
          <a class="btn btn-rose" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>Call now</span></a>
          <a class="btn btn-ghost" href="mailto:{EMAIL}"><span>Email us</span></a>
        </div>
      </div>

      <div class="stack-lg reveal" data-delay="120">
        <p style="color:#fff;font-family:var(--serif);font-size:1.35rem;line-height:1.4">Not sure if we serve your area?</p>
        <p>Divine AfterCare provides private, concierge post-surgical aftercare throughout Orange County, with extended coverage across Los Angeles and San Diego. Wherever your recovery takes you, we are there.</p>
        <ul class="chips">
          <li>Newport Beach</li><li>Irvine</li><li>Mission Viejo</li><li>Laguna Niguel</li>
          <li>Dana Point</li><li>San Clemente</li><li>Los Angeles</li><li>San Diego</li>
        </ul>
        <div class="btn-row"><a class="btn btn-ghost" href="/contact.html"><span>Submit a private inquiry</span></a></div>
      </div>
    </div>
  </section>

</main>
"""
