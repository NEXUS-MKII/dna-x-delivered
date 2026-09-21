# PsikiQ — landing page

Single self-contained static page. No build step, no framework, no dependencies
beyond Google Fonts (Oswald, Chakra Petch, JetBrains Mono) loaded at runtime, off the
critical path (preconnect + preload + media-swap link; display=swap).

Deploy = the GHL site. Two pages, each ONE source file; run

    python3 build_ghl.py

and paste the matching `ghl/psikiq-*-ghl.html` into that GHL page's single Custom
Code element (full-width section):

| source         | GHL page path | paste                        |
|----------------|---------------|------------------------------|
| `index.html`   | `/`           | `ghl/psikiq-home-ghl.html`    |
| `pricing.html` | `/psikiq-pricing` | `ghl/psikiq-pricing-ghl.html` |
| `contact.html` | `/psikiq-contact` | `ghl/psikiq-contact-ghl.html` |

`ghl/psikiq-header-ghl.html` is the HUD pill on its own (fonts + tokens included) for
any GHL page built in GHL's own editor — paste at the top of that page. The generated
pages above already carry it.
The site header (bar, nav, mobile menu) lives in `partials/header.html`; the build
injects it into every page between the `HEADER:start/end` markers, so edit the
partial, never the injected copy. Page links are written as `pricing.html` /
`index.html#…` in source and rewritten to the GHL paths in the output. The build strips the document wrapper, lifts GHL's 1170px
row cap on that section, and points the psi images at nexus-mkii.github.io/psikiq/.
Never hand-edit the GHL copy — that is how the two drifted apart in Sep 2026.

## Structure

Everything for PsikiQ lives in this folder and nothing outside it is referenced,
so splitting into a standalone repo later is a clean operation:

    git subtree split --prefix=psikiq-landing -b psikiq-standalone
    git remote add psikiq git@github.com:NEXUS-MKII/psikiq.git
    git push psikiq psikiq-standalone:main

## Media

- The hero runs the 68s film (cinematic clips intercut with Pika/Riverside footage
  of Chris with Rob and Aaron) **behind** the steel/white split — muted, looping.
  Page loads with the clean split; after `--hero-hold` (2s) the film starts and the
  two panels veil down to `--hero-veil` (0.5). Both are CSS vars on `.hero`.
  Reduced-motion users keep the still split.
- Two renders live in the GHL Media Library, as `data-src-desktop` / `data-src-mobile`
  on `#heroFilm` (16:9 720p and a 3:4 crop). An inline script picks one before the
  browser fetches: ≤768px, Save-Data, or a 2g/3g connection gets the mobile file.
  Empty `data-src-mobile` falls back to desktop. Renders come from the stitch
  script (`build.py` in the cut session) with the Safari-safe encode flags
  (yuv420p, High@4.0, 48 kHz); the hero files are silent.

## Open items

- Contact page wiring (`contact.html`, top of the script): `FORM_ENDPOINT` (a GHL
  workflow Inbound Webhook URL — until set, the form opens a pre-filled email),
  `CONTACT_EMAIL`, `LINKEDIN_URL`, `BOOK_URL`. Empty values hide their line.

- CTA `Book the diagnostic` points at `href="#"` — swap for the GHL calendar /
  booking URL before it takes real traffic.
- Fonts need internet at runtime. If an offline demo is ever a risk, self-host
  the four faces in `fonts/` and swap the `@import` for local `@font-face`.
- The flying seeker and HUD readouts are desktop-only by design (mobile perf).
  Show it on a laptop.
- `prefers-reduced-motion` is respected — leave that in.

## Brand spellings (deliberate, do not "correct")

PsikiQ (wordmark) · psikick.ai / psikick.io (domains) · Qollapsis (engine) ·
AUBIT · NOW Group
