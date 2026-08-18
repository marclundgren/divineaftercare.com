# -*- coding: utf-8 -*-
from partials import PHONE_DISPLAY, PHONE_TEL, EMAIL

SECTIONS = [
    ("Disclaimer",
     ["We take reasonable steps to safeguard the personal information shared by our website visitors, though no security system can be guaranteed completely foolproof, and we cannot promise the confidentiality of information transmitted over the internet.",
      "While we make every effort to keep the content on this site accurate, current, and trustworthy, we cannot guarantee that all information is free of error. Any health-related content found on this website is provided for general educational purposes only and should never replace personalized medical advice, diagnosis, or treatment from a qualified provider."]),
    ("Your privacy matters",
     ["We respect the privacy of everyone who visits our site and follow applicable laws regarding how personal information is handled. If you submit information through our contact form, we may occasionally use it to share relevant updates about our services. If you would rather not receive those, let us know and we will promptly remove or update your information.",
      "Any details you provide are treated with confidentiality and used solely for legitimate business purposes. We never share your personal information without your consent, except where required by law."]),
    ("What information we collect",
     ["Like most websites, we use analytics tools to understand how visitors interact with our site. This may include IP addresses, pages viewed, referral sources, browser type, and device or operating system information. This data helps us identify trends and improve the experience — it is not used to personally identify you.",
      "We do not collect personal details such as your name, email address, or physical address unless you voluntarily provide them through our contact form. Aside from working with a digital marketing partner who assists us in reviewing site analytics, we do not sell, rent, or disclose personal information to outside parties unless legally obligated to do so."]),
    ("Cookies",
     ["When you visit our website we may place a small file known as a cookie on your device. This helps the site recognize returning visitors and understand which pages are most useful, allowing us to refine the site over time.",
      "You are free to adjust your browser settings to block cookies altogether or approve them case by case. Disabling cookies may limit certain features or functionality."]),
    ("Links to other websites",
     ["Our site may occasionally include links to third-party websites for your convenience. We do not manage, monitor, or take responsibility for the content, policies, or practices of these external sites, and including such a link does not imply our endorsement. We recommend reviewing the privacy practices of any third-party site you visit."]),
]


def build():
    body = "\n".join(f"""
      <div class="stack">
        <h2 class="h-2">{h}</h2>
        {''.join(f'<p>{p}</p>' for p in ps)}
      </div>""" for h, ps in SECTIONS)

    return f"""
<main id="main">

  <section class="page-hero">
    <div class="wrap">
      <div class="section-head reveal is-in">
        <p class="eyebrow">Legal</p>
        <h1 class="h-display">Privacy policy.</h1>
        <p class="lede" style="margin-top:1.5rem;max-width:58ch">The privacy of everyone who visits this website matters to us, and you deserve to know what information we gather and how it is used. This policy may be updated from time to time.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap wrap-narrow">
      <div class="stack-lg reveal">
{body}

        <div class="stack">
          <h2 class="h-2">Contact us</h2>
          <p>Questions about this policy, or about information we hold?</p>
          <p>
            Email <a href="mailto:{EMAIL}" style="color:var(--rose-text)">{EMAIL}</a><br>
            Phone <a href="tel:{PHONE_TEL}" style="color:var(--rose-text)">{PHONE_DISPLAY}</a>
          </p>
        </div>
      </div>
    </div>
  </section>

</main>
"""
