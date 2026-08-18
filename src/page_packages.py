# -*- coding: utf-8 -*-
from partials import PHONE_DISPLAY, PHONE_TEL

# (hours, label, name, price, blurb, featured)
PACKAGES = [
    (4, "4 hrs", "4-hour recovery visit", "400",
     "A focused window of one-on-one nursing right after your procedure. Ideal for outpatient surgery and shorter recoveries.", False),
    (6, "6 hrs", "6-hour recovery visit", "575",
     "Extended daytime support through the most delicate hours of early recovery, with continuous monitoring and comfort care.", False),
    (8, "8 hrs", "8-hour recovery visit", "750",
     "A full shift of dedicated nursing, allowing for thorough post-op observation, medication timing, and uninterrupted rest.", False),
    (12, "12 hrs", "12-hour recovery visit", "1,050",
     "Day-into-evening coverage for patients who benefit from sustained observation through the first critical day.", True),
    (24, "24 hrs", "24-hour recovery visit", "1,900",
     "Round-the-clock concierge nursing — overnight included — during the most intensive stretch of recovery.", False),
    (1, "1 hr", "Transport only", "150",
     "Escort and transport from your surgery center to home, hotel, or short-term residence. Rate may vary by distance.", False),
]

INCLUDED = [
    "Post-operative progress monitoring — swelling, bruising, and discomfort assessment",
    "Medication administration and pain management",
    "Wound care, dressing changes, and drain management",
    "Vital signs monitoring",
    "Compression garment assistance and lymphatic support",
    "Monitoring for infection, excessive bleeding, and post-surgical complications",
    "Direct communication with your plastic surgeon and surgical team",
    "Assistance with personal hygiene, bathing, grooming, and dressing",
    "Assistance with housekeeping and activities of daily living",
    "Mobility support and positioning guidance",
    "Emotional reassurance and attentive check-ins throughout your recovery",
    "Concierge transport from your surgical facility to your place of recovery",
]

COMPANION = [
    ("&Agrave; la carte, hourly", "$75<span>/hr</span>", "Standard ongoing rate"),
    ("Part-time &mdash; 12 hrs/week", "$70<span>/hr</span>", "For example, three visits of four hours"),
    ("Standard &mdash; 20 hrs/week", "$68<span>/hr</span>", "Our most popular ongoing plan"),
    ("Full-time &mdash; 40 hrs/week", "$65<span>/hr</span>", "Daily coverage with a single caregiver"),
    ("Monthly retainer", "&minus;3%", "For clients committing a full month upfront"),
]


def build():
    pkgs = []
    for i, (hours, label, name, price, blurb, featured) in enumerate(PACKAGES):
        num, unit = label.split(" ")
        pkgs.append(f"""
        <article class="pkg{' pkg-featured' if featured else ''} reveal" data-delay="{(i % 3) * 90}">
          {'<span class="pkg-tag">Most requested</span>' if featured else ''}
          <div class="pkg-head">
            <h3>{name}</h3>
            <div class="dial" data-hours="{hours}" role="img" aria-label="{label} of a 24-hour day">
              <svg viewBox="0 0 58 58"><circle class="dial-track" cx="29" cy="29" r="25"/><circle class="dial-fill" cx="29" cy="29" r="25"/></svg>
              <b>{num}<i>{unit.upper()}</i></b>
            </div>
          </div>
          <p>{blurb}</p>
          <p class="pkg-price"><b>${price}</b> <span>{'per hour' if name == 'Transport only' else 'flat'}</span></p>
        </article>""")

    included = "\n".join(f"""          <li><svg width="17" height="17" style="color:var(--gold-lt)" aria-hidden="true"><use href="#i-leaf"/></svg>{s}</li>""" for s in INCLUDED)
    half = (len(INCLUDED) + 1) // 2
    col_a = "\n".join(f"""          <li><svg width="17" height="17" style="color:var(--gold-lt)" aria-hidden="true"><use href="#i-leaf"/></svg>{s}</li>""" for s in INCLUDED[:half])
    col_b = "\n".join(f"""          <li><svg width="17" height="17" style="color:var(--gold-lt)" aria-hidden="true"><use href="#i-leaf"/></svg>{s}</li>""" for s in INCLUDED[half:])

    rates = "\n".join(f"""
        <div class="rate-row">
          <b>{n}</b>
          <span class="rate-price">{p}</span>
          <span class="rate-note">{note}</span>
        </div>""" for n, p, note in COMPANION)

    return f"""
<main id="main">

  <section class="page-hero">
    <div class="band-bg" style="background-image:url('/assets/img/hotel-bamboo.webp');--bg-pos:75% 45%"></div>
    <div class="wrap">
      <div class="section-head reveal is-in">
        <p class="eyebrow">Concierge post-surgical recovery</p>
        <h1 class="h-display">Recovery packages.</h1>
        <p class="lede" style="margin-top:1.5rem;max-width:54ch">Transparent, hour-based pricing for licensed nursing care across Orange County, San Diego, and Los Angeles. Every package can be tailored to your procedure.</p>
        <ul class="chips" style="margin-top:2rem">
          <li>Four-hour minimum</li><li>Licensed RNs</li><li>Overnight available</li><li>Advance booking recommended</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ── packages ────────────────────────────────────────── -->
  <section class="section">
    <div class="wrap">
      <div class="section-head reveal" style="margin-bottom:clamp(2.5rem,4vw,3.5rem)">
        <p class="eyebrow">Post-surgical care</p>
        <h2 class="h-1">Choose the coverage your recovery calls for.</h2>
        <p class="lede" style="margin-top:1.25rem">Each dial shows how much of a 24-hour day the package covers.</p>
      </div>
      <div class="pkg-grid">{''.join(pkgs)}
      </div>
      <p class="form-note reveal" style="margin-top:2rem;max-width:62ch">Concierge service. Packages may be combined or tailored to your specific recovery — reach out and we will build a custom plan. Cancellations require 48 hours&rsquo; notice.</p>
    </div>
  </section>

  <!-- ── included ────────────────────────────────────────── -->
  <section class="section band-deep">
    <div class="wrap">
      <div class="section-head reveal" style="margin-bottom:clamp(2rem,3.5vw,3rem)">
        <p class="eyebrow">No add-ons, no surprises</p>
        <h2 class="h-1">Included in every recovery package.</h2>
      </div>
      <div class="scope-grid reveal" data-delay="100">
        <ul class="scope-list">
{col_a}
        </ul>
        <ul class="scope-list">
{col_b}
        </ul>
      </div>
    </div>
  </section>

  <!-- ── companion care ──────────────────────────────────── -->
  <section class="section band-linen">
    <div class="wrap split" style="align-items:start">
      <div class="stack-lg reveal sticky-col">
        <div>
          <p class="eyebrow">Ongoing companion care</p>
          <h2 class="h-1">For elderly and long-term clients.</h2>
        </div>
        <p class="lede">Weekly and monthly plans for families arranging consistent, compassionate support — companionship, mobility assistance, medication reminders, and help with daily living.</p>
        <p>The more hours you reserve each week, the lower the hourly rate, and full-time plans keep the same caregiver for continuity.</p>
        <div class="btn-row"><a class="btn btn-rose" href="/contact.html"><span>Arrange companion care</span></a></div>
      </div>

      <div class="rates reveal" data-delay="100">
        <div class="rate-row rate-head">
          <b>Plan</b><span>Rate</span><span>Notes</span>
        </div>{rates}
      </div>
    </div>
  </section>

  <!-- ── cta ─────────────────────────────────────────────── -->
  <section class="section cta-band">
    <div class="band-bg" style="background-image:url('/assets/img/service-hotel.webp')"></div>
    <div class="wrap center stack-lg">
      <div class="reveal">
        <p class="eyebrow eyebrow-c">Los Angeles · Orange County · San Diego</p>
        <h2 class="h-1" style="max-width:22ch;margin-inline:auto">Not sure which package fits? We will help you decide.</h2>
      </div>
      <p class="lede reveal" style="max-width:52ch;margin-inline:auto">Tell us your procedure and surgery date and we will recommend the right level of coverage — no obligation.</p>
      <div class="btn-row center reveal">
        <a class="btn btn-rose" href="/contact.html"><span>Arrange your care</span></a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </section>

</main>
"""
