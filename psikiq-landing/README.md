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

## Favicon

`icons/` — gold psi on the void, rounded, hairline frame (16/32/48 .ico, 16 + 32 png,
180 apple-touch, 192/512). Regenerate from `psi-gold.webp` if the mark changes. Source
pages link them in `<head>`; on GHL the header script swaps GHL's default icon for
ours at load. Also set it in GHL: Sites → Settings → Favicon → `icons/favicon-32.png`.
The set is mirrored on nexus-mkii.github.io/psikiq/icons/ (what the GHL pages fetch).

## Logo

`logo/` — lockups cut from `psi-gold.webp` + Oswald SemiBold wordmark (PSIKI white/ink, Q gold):
square 512/1024 (void, rounded, hairline), `psikiq-calendar-logo-180.png` (GHL calendar cap),
square + wide on transparent in on-dark (white text) and on-light (ink text) variants,
`psikiq-mark-avatar-512.png` (mark only, for circle-cropped avatars). Regenerate from the
session script if the mark changes; the wordmark is rendered, not typeset, so it matches
the site's `.wordmark` tracking.

## Products (GHL catalogue)

`products/catalogue.json` is the source for the GHL product ladder — mirrors the
pricing page. `build_cards.py` renders one 1000x1000 card per product (steel ground,
gold psi, Oswald name, gold price) into `products/cards/`; push those to the psikiq
Pages repo under `products/`, then `sync_products.py` creates/updates the products in
the PsikiQSolutions location and attaches prices. Both are idempotent — a product is
matched by NAME, a price is only created if the product has none. Change a price on
the pricing page → change it here → re-run. Token comes from the AUBIT vault.

## Open items

- Contact page wiring (`contact.html`, top of the script): `FORM_ENDPOINT` (a GHL
  workflow Inbound Webhook URL — until set, the form opens a pre-filled email),
  `CONTACT_EMAIL`, `LINKEDIN_URL`, `BOOK_URL`. Empty values hide their line.

- Book CTAs (all pages + the Prognosis result screen) → the Business Diagnostic calendar,
  permanent link `book.psikiq.io/widget/booking/hilKmb9laNRnqffVwmSk` (wired 22 Sep 2026;
  survives slug changes — use this form, not the slug link).
- Fonts need internet at runtime. If an offline demo is ever a risk, self-host
  the four faces in `fonts/` and swap the `@import` for local `@font-face`.
- The flying seeker and HUD readouts are desktop-only by design (mobile perf).
  Show it on a laptop.
- `prefers-reduced-motion` is respected — leave that in.

## Brand spellings (deliberate, do not "correct")

PsikiQ (wordmark) · psikick.ai / psikick.io (domains) · Qollapsis (engine) ·
AUBIT · NOW Group
