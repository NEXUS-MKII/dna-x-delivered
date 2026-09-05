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
