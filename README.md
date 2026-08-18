# Divine AfterCare

Marketing site for Divine AfterCare — concierge post-surgical nursing across
Orange County, Los Angeles, and San Diego.

Static HTML, CSS, and one small vanilla JS file. No framework, no build
toolchain, no runtime dependencies. Deployable to any static host as-is.

## Run it locally

```bash
npm run dev          # builds, then serves on http://127.0.0.1:4321
```

or without npm:

```bash
python3 src/build.py
python3 -m http.server 4321 --bind 127.0.0.1
```

## Layout

```
index.html  services.html  recovery-packages.html  contact.html  privacy-policy.html
sitemap.xml  robots.txt
assets/
  css/site.css        design tokens + all component styles
  js/site.js          header, drawer, scroll reveal, hour dials, inquiry form
  fonts/              self-hosted Fraunces + Inter (woff2)
  img/                optimized .webp used by the site
  img/_source/        untouched originals, not served
src/                  the page sources the HTML is generated from
```

### Editing content

The five HTML files are **generated**. Edit the matching file in `src/`, then
run `npm run build`.

| Edit this | To change |
|---|---|
| `src/partials.py` | header, footer, phone/email, `<head>` and meta tags |
| `src/page_home.py` | homepage — services, differences, scope, testimonials, FAQ |
| `src/page_services.py` | the three service sections |
| `src/page_packages.py` | package pricing and companion-care rates |
| `src/page_contact.py` | contact methods, inquiry form, service areas |
| `src/page_privacy.py` | privacy policy |
| `src/build.py` | page titles, meta descriptions, schema.org JSON-LD |

Phone and email live in one place (`src/partials.py`) and flow everywhere.

## Design system

Defined as CSS custom properties at the top of `assets/css/site.css`.

- **Display** — Fraunces, weight 300. **Body/UI** — Inter. Both self-hosted.
- **Palette** — porcelain `#FCFAF9`, linen `#F3EDEA`, espresso `#2B2124`,
  brand mauve `#A15576`, rose-gold `#C08A6C`.
  `--rose-text` is a darkened mauve used for small type so 11–13px labels
  clear WCAG AA on the linen bands.
- **Signature** — the arc, taken from the logo's overlapping circles: arched
  imagery (`.arch`), the hour dials on the pricing cards, and the leaf bullet
  on the scope-of-care lists.

Verified: WCAG AA contrast, single `h1` per page, no heading-level jumps,
labelled form fields, visible keyboard focus, `prefers-reduced-motion`
respected, no horizontal overflow at 390px.

## The inquiry form

`contact.html` has no backend. It validates, then opens the visitor's mail
client with the inquiry pre-filled to `info@divineaftercare.com`. To post to a
real endpoint instead, replace the `mailto:` hand-off at the bottom of
`assets/js/site.js` with a `fetch()`.

## Deploying

Any static host. The build emits **document-relative** links, so the site works
served from a domain root *or* from a subpath like GitHub Pages'
`/divineaftercare.com/`. Keep it that way: a leading `/` on an asset or page
link breaks the subpath deploy. `src/build.py:relativize()` enforces this.

Two related gotchas, both already handled:

- `url()` inside a CSS custom property resolves against the *stylesheet*, not
  the document. Band photos therefore sit on a real `.band-bg` element with an
  inline `background-image`, not on a `--var` consumed from `site.css`.
- `.nojekyll` is present so GitHub Pages serves `assets/img/_source/` paths
  literally rather than running the files through Jekyll.

## Images

Source images are archived in `assets/img/_source/` and are not served. The
site loads WebP only — 14 MB of originals compress to about 1 MB. To
regenerate after adding an image, re-run the conversion or export WebP
directly, keeping the same base filename.
