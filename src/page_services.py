# -*- coding: utf-8 -*-
from partials import PHONE_DISPLAY, PHONE_TEL

BLOCKS = [
    dict(
        id="in-home", nav="In-home aftercare", eyebrow="In-home aftercare",
        title="Professional nursing care, delivered to your door",
        lede="Recovering at home lets you heal in a familiar environment while receiving one-on-one nursing care. Divine AfterCare brings experienced licensed nurses directly to you, so you can recover with comfort and confidence while following your surgeon's post-operative instructions.",
        img="/assets/img/service-inhome.webp",
        alt="A licensed nurse checks a recovering patient's blood pressure in her bedroom at home.",
        cells=[
            ("Comfort at home", "Recover in the comfort of home",
             "Your home provides the comfort and privacy healing requires. Recovering in a familiar environment lets you rest without the stress of travel, while your nurse creates a calm, supportive atmosphere focused entirely on your safety and well-being."),
            ("Clinical support", "Medication administration &amp; clinical care",
             "Your nurse administers medication as prescribed by your physician while monitoring your comfort and response throughout the shift, alongside ongoing post-operative assessments and vital signs monitoring."),
            ("Surgical care", "Wound, drain &amp; incision management",
             "Professional wound assessments, incision care, dressing changes, and surgical drain management, with the healing process monitored throughout. Should concerns arise, we contact your surgeon's office."),
            ("Personalized support", "Comfort, mobility &amp; daily living",
             "Healing extends beyond clinical care. We assist with mobility, repositioning, hydration, nutrition, compression garments, and personal comfort as you regain confidence."),
        ],
        cta=("Care designed around your recovery", "Experience compassionate, personalized nursing built around how you actually heal.", "Book your care"),
    ),
    dict(
        id="hotel", nav="Hotel &amp; away", eyebrow="Hotel &amp; away aftercare",
        title="Concierge nursing wherever you recover",
        lede="Whether you are travelling across California or across the country, we bring experienced licensed nurses directly to your recovery location — so you can focus entirely on healing, in the comfort and privacy of your chosen accommodations.",
        img="/assets/img/service-hotel.webp",
        alt="An ocean-view hotel suite in Orange County prepared for post-surgical recovery.",
        cells=[
            ("Comfort away from home", "Recover comfortably away from home",
             "Recovering after surgery somewhere unfamiliar can feel overwhelming. Your nurse creates a supportive environment while following your surgeon's recovery instructions, so you heal confidently with professional care at your side."),
            ("One-on-one support", "Personalized nursing care",
             "Individualized post-operative care that may include medication administration, wound and incision care, drain management, mobility assistance, hydration support, and continuous recovery monitoring."),
            ("Elevated experience", "A luxury recovery experience",
             "Discreet, hotel-appropriate care delivered with the presentation you would expect from any luxury service — arriving fully equipped, working quietly, and leaving your suite as it was found."),
            ("Travel support", "Travel with confidence",
             "Many of our patients travel specifically for surgery. We understand the particular challenges of recovering away from home and handle the details so you can focus on healing."),
        ],
        cta=("Professional care, wherever you stay", "Nursing delivered with compassion, discretion, and attention to every detail.", "Schedule your recovery"),
    ),
    dict(
        id="plans", nav="Personalized plans", eyebrow="Personalized care plans",
        title="Because every recovery is unique",
        lede="Your recovery deserves more than a standard approach. We develop individualized nursing care plans designed specifically around your procedure, your recovery timeline, and your surgeon's post-operative instructions.",
        img="/assets/img/service-plans.webp",
        alt="A private duty nurse takes a patient's pulse during an in-home recovery visit.",
        cells=[
            ("Built around you", "A personalized approach",
             "Before care begins we review your procedure, anticipated recovery, medical needs, and your surgeon's recommendations to build a nursing plan that supports every stage of healing."),
            ("Flexible support", "Care that adapts with you",
             "Recovery changes day to day. As your needs evolve, your nurse continuously evaluates your progress and adjusts your care accordingly."),
            ("One-on-one attention", "Focused entirely on you",
             "Your nurse is dedicated exclusively to your care during each visit — individualized attention, continuous assessment, and compassionate support, with nothing divided."),
            ("Coordinated care", "Recovery with peace of mind",
             "From medication administration and clinical assessment to comfort measures and communication with your surgeon's office, every aspect of your care is coordinated for you."),
        ],
        cta=("Personalized support at every step", "Nursing care that prioritizes your comfort, safety, and recovery from the first hour forward.", "Contact us today"),
    ),
]


def build():
    subnav = "\n".join(f'        <li><a href="#{b["id"]}">{b["nav"]}</a></li>' for b in BLOCKS)

    sections = []
    for i, b in enumerate(BLOCKS):
        cells = "\n".join(f"""
          <div class="quad-cell">
            <p class="eyebrow">{e}</p>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>""" for e, t, d in b["cells"])

        reverse = " reverse" if i % 2 else ""
        band = ' band-linen' if i % 2 else ''
        ct, cd, cb = b["cta"]

        sections.append(f"""
  <section class="section{band}" id="{b['id']}">
    <div class="wrap stack-lg">
      <div class="split{reverse}" style="margin-bottom:clamp(2.5rem,4vw,3.5rem)">
        <div class="split-media reveal">
          <div class="arch" style="aspect-ratio:4/4.4">
            <img src="{b['img']}" alt="{b['alt']}" loading="lazy" width="1000" height="1100">
          </div>
        </div>
        <div class="stack reveal" data-delay="120">
          <p class="eyebrow">{b['eyebrow']}</p>
          <h2 class="h-1">{b['title']}</h2>
          <p class="lede" style="margin-top:1.25rem">{b['lede']}</p>
        </div>
      </div>

      <div class="quad reveal">{cells}
      </div>

      <div class="center stack reveal" style="padding-top:clamp(1.5rem,3vw,2.5rem)">
        <h3 class="h-2">{ct}</h3>
        <p class="lede" style="max-width:50ch;margin-inline:auto">{cd}</p>
        <div class="btn-row center" style="margin-top:1.5rem"><a class="btn btn-rose" href="/contact.html"><span>{cb}</span></a></div>
      </div>
    </div>
  </section>""")

    return f"""
<main id="main">

  <section class="page-hero">
    <div class="band-bg" style="background-image:url('/assets/img/service-hotel.webp');--bg-pos:70% 40%"></div>
    <div class="wrap">
      <div class="section-head reveal is-in">
        <p class="eyebrow">Our services</p>
        <h1 class="h-display">Concierge care for every recovery.</h1>
        <p class="lede" style="margin-top:1.5rem;max-width:56ch">A full range of private, concierge-level post-surgical nursing across Orange County, Los Angeles, San Diego, and the surrounding areas — designed around where you recover, how long you need care, and what your procedure requires.</p>
        <div class="btn-row" style="margin-top:2.25rem">
          <a class="btn btn-rose" href="/contact.html"><span>Reserve your recovery</span></a>
          <a class="btn btn-ghost" href="/recovery-packages.html"><span>See pricing</span></a>
        </div>
      </div>
    </div>
  </section>

  <nav class="subnav" aria-label="Services">
    <div class="wrap">
      <ul>
{subnav}
      </ul>
    </div>
  </nav>
{''.join(sections)}

  <section class="section cta-band">
    <div class="band-bg" style="background-image:url('/assets/img/hero.webp')"></div>
    <div class="wrap center stack-lg">
      <div class="reveal">
        <p class="eyebrow eyebrow-c">Ready when you are</p>
        <h2 class="h-1" style="max-width:22ch;margin-inline:auto">Tell us your surgery date and we will take it from there.</h2>
      </div>
      <div class="btn-row center reveal">
        <a class="btn btn-rose" href="/contact.html"><span>Submit a private inquiry</span></a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}"><svg width="15" height="15" aria-hidden="true"><use href="#i-phone"/></svg><span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </section>

</main>
"""
