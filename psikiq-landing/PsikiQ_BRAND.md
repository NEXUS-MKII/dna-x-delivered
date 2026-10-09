# PsikiQ — brand reference
**v1.0 · 2026-10-04 · canonical.** Everything here is taken from what is live, not from
intent. If the site and this document disagree, the site is right and this is stale —
fix it here and say so.

---

## 1 · What PsikiQ is

The **premium-positioning brand over the ELENCHUS engine**. Where AUBIT is the machinery
and NOW Group is the house, PsikiQ is the face a buyer meets: a consultancy that reads a
business's position and tells it something it could feel but not prove.

> **We see what your market can't.**

The product thesis and the marketing are the same object. The diagnostic demonstrates
the claim while making it — every answer returns a *reveal*, so the respondent moves
unaware → aware while they answer. Chris's framing, worth keeping:

> *"We say it's just a showcase of our skill — but it's a living catch-all uber-powered
> funnel too."*

**Never positioned as:** a scorecard, a quiz tool, a marketing agency. It returns a
**position on a curve**, not a score — position is actionable, a score is decoration.

---

## 2 · Names and spellings — never "correct" these

| Correct | Not |
|---|---|
| **PsikiQ** — capital P, capital Q, nothing in between | PsiKiQ · Psikiq · PSIKIQ (except as a set wordmark) |
| **ELENCHUS** — the engine | Qollapsis *(retired 2026-09-05)* · Elenchus in body copy is fine; caps in attribution |
| **Greiner** — Larry E. Greiner, whose growth model the diagnostic runs on | Griner |
| **AUBIT** · **NOW Group** | Aubit · Now Group |
| **PsikiQ Solutions** — the NZBN trading name, for console/app builds | |

**ELENCHUS** is named for the Socratic *elenchus*: the cross-examination that collapses
a belief its holder did not know was false. That is the method, not a flourish.

> ⚠️ **Trademark note.** Qollapsis was coined and registrable; Elenchus is a classical
> common noun and will be much harder to protect. Flagged, not resolved.

### Attribution lines, verbatim

- Site footer: *powered by the **ELENCHUS** engine · built by **AUBIT** · a **NOW GROUP** company*
- Commercial documents: *engineered and delivered by NOW Group*
- Console / app builds: **PsikiQ Solutions**
- White papers stay **NOW Group** — never PsikiQ.

---

## 3 · Voice

Declarative, unhurried, concrete. Short sentences that land, then one longer one that
opens the idea. It never sells by adjective; it sells by naming the thing the reader
already feels.

**It does:**
- Name the pain before the product. *"There's a market you can't see."*
- Show its working. *"The magic is real and the mechanism is honest."*
- Admit limits, which is where the authority comes from. *"An instrument that hides its uncertainty isn't an instrument."*
- Use the em dash to turn a sentence, and the lowercase mono kicker to label a beat.

**It never:**
- Opens on price. Pain → paradise first; the number goes in the investment section.
- Uses hype words — *revolutionary, game-changing, unlock, supercharge, 10x*.
- Claims magic without immediately explaining the mechanism.
- Puts a NOW Group solution inside a white paper.

**The spine** every long page follows, numbered in lowercase roman with a mono kicker:

`i · the question → ii · the measurement → iii · the answer → iv · the instrument → v · the engine`

---

## 4 · Colour

The whole palette is gold on near-black, with silver for data and one orange accent.
Defined once as CSS custom properties on `:root`.

| Token | Hex | Role |
|---|---|---|
| `--void` / `--ink` | `#17110A` | the ground — near-black, warm, never pure black |
| `--gold` / `--accent` | `#E6BE6A` | **the** brand colour: marks, rules, prices, emphasis |
| `--gold-deep` | `#B8912F` | the Q in the wordmark on light grounds |
| `--accent-ink` | `#A8801E` | gold that must pass contrast on white |
| `--accent-glow` | `rgba(230,190,106,.28)` | every glow and shadow bloom |
| `--warm` | `#E8912E` | secondary accent — mono kickers only, never large areas |
| `--silver` | `#C9CFD6` | data, readouts, secondary text on dark |
| `--silver-2` | `#9AA3AD` | quieter still |
| `--white` / `--white-2` | `#FFFFFF` / `#EEF0F3` | the light half of the split |
| `--mut-dark` / `--mut-light` | `#727E8E` / `#8A93A0` | body copy, muted |
| `--line-dark` / `--line-light` | `#1C232D` / `#E1E4E9` | hairlines |

**Rules.** Gold is for one thing at a time — if everything is gold, nothing is.
Orange labels, gold emphasises. No other hue enters the palette (cyan was removed
deliberately). Dark is the default; light is the *other half of the split*, not a theme.

---

## 5 · Type

| Role | Face | Weights |
|---|---|---|
| Display / headings | **Oswald** — tall, condensed, Impact-but-premium | 300 · 400 · 500 · 600 |
| Body | **Chakra Petch** | 300 · 400 |
| Data / kickers / HUD | **JetBrains Mono** | 500 |

Headings are uppercase with `letter-spacing: .01em`. Mono kickers are uppercase,
`.14–.16em` tracked, in `--warm`. Michroma was dropped (2026-09-22) — it had no usable
psi glyph and earned nothing.

Fonts load off the critical path: one `preconnect` to `fonts.gstatic.com`, `preload`,
then a `media="print" onload` stylesheet, `display=swap`. Only the weights listed above.

---

## 6 · The mark

**ψ** — the Greek psi. Gold, drawn as an image, never typeset (no reliable glyph).

| Asset | Use |
|---|---|
| `logo/psikiq-logo-square-512.png` · `-1024` | avatars, profile, square slots |
| `logo/psikiq-ghl-business-logo-350x180.png` | GHL Business Profile (their exact frame) |
| `logo/psikiq-calendar-logo-180.png` | GHL calendar header |
| `logo/psikiq-logo-wide-on-light.png` / `-on-dark` | email headers, wide slots |
| `logo/psikiq-mark-avatar-512.png` | mark only, for circle crops |
| `icons/` | favicon set — 16/32/48 `.ico`, 180 apple-touch, 192/512 |
| `psi-split.webp` · `psi-gold.webp` | the hero mark; split version has the gold/ink seam at x=60 |

Public host: `https://nexus-mkii.github.io/psikiq/` — images, icons and product cards.
Regenerate the lockups from `psi-gold.webp`; the wordmark is **rendered** in Oswald
SemiBold with the site's tracking, not typed, so it always matches the hero.

---

## 7 · Motifs — what makes a surface look PsikiQ

- **The split.** Dark half / light half with a gold seam down the middle. The brand's
  central image: superposition before measurement.
- **Brushed steel.** Vertical striations plus a diagonal gold sheen. The ground of every
  dark surface (`--steel-stripes` + `--steel-sheen`, `background-blend-mode: screen`).
- **The HUD.** Gold corner brackets, a mono readout (`ψ PSIKIQ // SUPERPOSITION`), a
  state line, a progress rail. The page knows what it is doing and says so.
- **Corner brackets** on every panel, pill and card — 2px gold, top-left and bottom-right.
- **The slow scan** — a faint gold band travelling down the header pill. The instrument
  is on.
- **Hairline rules**, never boxes. Columns are separated by 1px gold at low alpha.
- **The seeker** — a winged gold orb that flies the home page and lights what it passes.
  Desktop only, `prefers-reduced-motion` removes it.
- **The collapse** — the one scroll-driven set piece, where the split resolves into solid
  ground. The page performs its own thesis exactly once.

**Phase language** runs through the HUD and section labels:
`SUPERPOSITION → MEASUREMENT → COLLAPSE → RESOLVED`.

---

## 8 · Where things live

| | |
|---|---|
| Site | `psikiq.io` — GHL, pages at `/`, `/psikiq-pricing`, `/psikiq-contact` |
| Booking | `book.psikiq.io` — GHL branded domain (CNAME → `link.msgsndr.com`, DNS-only) |
| Diagnostic | `crisisquiz.nowgroup.co.nz/quiz/prognosis` — self-hosted, tunnelled; stays off marketing platforms because the scoring is the IP |
| Assets | `nexus-mkii.github.io/psikiq/` — repo `NEXUS-MKII/psikiq` |
| Source | `dna-x-delivered/psikiq-landing/` — `index.html`, `pricing.html`, `contact.html`, `partials/header.html`; `build_ghl.py` emits the GHL pastables |
| Products | `products/catalogue.json` → GHL catalogue, with rendered cards |
| CRM | GHL location `XmnnOgihSvpbtlApd8cN` (PsikiQSolutions) |

---

## 9 · The ladder, in brand terms

Free **Prognosis** (8 min, no gate — the generosity *is* the strategy) → **Guided
Business Diagnostic** ($1,500, credited) → **Quiz Endpoint Build** ($5,000) → **the
funnel, ad to booked** ($6,500) → **owned engine** ($8–12k, scoped).

Language discipline: the build is an **endpoint**, not a funnel. A funnel runs from the
ad to the booked conversation; the endpoint is where it lands. Only the package that
includes creative may be called a funnel.

---

## 10 · Known stale / open

- `psikick.ai` / `psikick.io` appear in older notes and in the engine's CORS allowlist.
  **Superseded by `psikiq.io`** (2026-09-21). Harmless but should be cleared out.
- Elenchus trademark exposure (§2).
- GST: location tax rate `NZ GST` 15% exists; products are not yet attached to it.

---

*Maintained in `dna-x-delivered/psikiq-landing/BRAND.md`. Bump the version stamp on
every change.*
