#!/usr/bin/env python3
"""Assemble the static site. Run: python3 src/build.py"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from partials import head, header, FOOTER, PHONE_DISPLAY, PHONE_TEL, EMAIL
import page_home, page_services, page_packages, page_contact, page_privacy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.divineaftercare.com"

ORG_LD = json.dumps({
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "MedicalBusiness"],
    "name": "Divine AfterCare",
    "legalName": "Divine AfterCare, LLC",
    "url": SITE,
    "logo": SITE + "/assets/img/mark.webp",
    "image": SITE + "/assets/img/hero.webp",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "priceRange": "$$$",
    "description": "Concierge post-surgical aftercare delivered by licensed nurses to your home or hotel across Orange County, Los Angeles, and San Diego.",
    "address": {"@type": "PostalAddress", "addressRegion": "CA", "addressLocality": "Orange County", "addressCountry": "US"},
    "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in
                   ["Orange County", "Los Angeles County", "San Diego County"]],
    "sameAs": ["https://www.instagram.com/divineaftercare/",
               "https://www.facebook.com/profile.php?id=61592005871774"],
}, separators=(",", ":"))

FAQ_LD = json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in page_home.FAQS
    ],
}, separators=(",", ":"))


def relativize(html):
    """Rewrite root-relative asset/page links to document-relative ones.

    Every page lives at the deployment root, so plain relative links resolve
    correctly whether the site is served from a domain root or from a
    subpath like /divineaftercare.com/ on GitHub Pages. Absolute
    https:// URLs (canonical, og:*, JSON-LD) are deliberately left alone.
    """
    html = html.replace('="/assets/', '="assets/')
    html = html.replace("url('/assets/", "url('assets/")
    html = re.sub(r'href="/([a-z0-9-]+\.html)"', r'href="\1"', html)
    html = html.replace('href="/"', 'href="index.html"')
    return html


def ld(payload):
    return f'<script type="application/ld+json">{payload}</script>\n'


PAGES = [
    dict(file="index.html", active="home", build=page_home.build,
         title="Divine AfterCare | Concierge Post-Surgical Nursing in Orange County, CA",
         desc="Concierge post-surgical aftercare from licensed nurses, delivered to your home or hotel across Orange County, Los Angeles, and San Diego. 4 to 24-hour shifts, complete discretion.",
         canonical="/", extra=ld(ORG_LD) + ld(FAQ_LD)),

    dict(file="services.html", active="services", build=page_services.build,
         title="Post-Surgical Aftercare Services | Licensed In-Home Nursing | Divine AfterCare",
         desc="In-home aftercare, hotel and away recovery nursing, and personalized care plans from licensed nurses across Orange County, Los Angeles, and San Diego.",
         canonical="/services.html", extra=ld(ORG_LD)),

    dict(file="recovery-packages.html", active="packages", build=page_packages.build,
         title="Recovery Packages & Pricing | Post-Surgical Nursing | Divine AfterCare",
         desc="Transparent hourly pricing for concierge post-surgical nursing: 4, 6, 8, 12, and 24-hour recovery visits, transport, and ongoing companion care in Southern California.",
         canonical="/recovery-packages.html", extra=ld(ORG_LD)),

    dict(file="contact.html", active="contact", build=page_contact.build,
         title="Contact Divine AfterCare | Private Post-Surgical Nursing Inquiry | Orange County",
         desc="Reach Divine AfterCare by phone, email, or confidential inquiry form to arrange concierge post-surgical nursing across Orange County, Los Angeles, and San Diego.",
         canonical="/contact.html", extra=ld(ORG_LD)),

    dict(file="privacy-policy.html", active="", build=page_privacy.build,
         title="Privacy Policy | Divine AfterCare",
         desc="How Divine AfterCare collects, uses, and safeguards the information you share with us.",
         canonical="/privacy-policy.html", extra='<meta name="robots" content="noindex">\n'),
]


def main():
    for p in PAGES:
        html = head(p["title"], p["desc"], p["canonical"], p["extra"]) \
             + header(p["active"]) + p["build"]() + FOOTER
        html = relativize(html)
        out = os.path.join(ROOT, p["file"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  {p['file']:26} {len(html):>7,} bytes")

    # sitemap + robots
    urls = "".join(
        f"<url><loc>{SITE}{p['canonical']}</loc><changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if p['canonical'] == '/' else '0.8'}</priority></url>"
        for p in PAGES if "noindex" not in p["extra"])
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("  sitemap.xml, robots.txt")


if __name__ == "__main__":
    print("Building Divine AfterCare…")
    main()
    print("Done.")
