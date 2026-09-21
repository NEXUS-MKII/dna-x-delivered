# PsikiQ — landing page

Single self-contained static page. No build step, no framework, no dependencies
beyond Google Fonts (Oswald, Michroma, Chakra Petch, JetBrains Mono) loaded at runtime.

Deploy = serve `index.html`. That's the whole job.

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
  two panels veil down to `--hero-veil` (0.28). Both are CSS vars on `.hero`.
  Reduced-motion users keep the still split.
- The mp4 lives in the GHL Media Library; `src` on `#heroFilm` is the filesafe CDN
  URL. Re-upload and swap that one URL to change the cut.

## Open items

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
