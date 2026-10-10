# Marketing NOW — ALL-IN Page (Modular)
**v1.4** — Build D + E scope refinements, AUBIT funnel context, new "How it works" section.

## What changed in v1.4 (from v1.3)

| Change | Where | Why |
|---|---|---|
| **Build D repositioned** — quiz hosting is client CRM (preferred) or ScoreApp (fallback) | Block 04 | No more "Tally / Google Form" — quiz lives in client's system, fully white-labelled |
| **Build D ICP/brand emphasis** — "YOUR ICP, YOUR brand, YOUR system" | Block 04 | Makes explicit that the build is bespoke at the brand layer, not just deployed |
| **Build E repositioned** as foundation pack | Block 04 | 12 citations (was 50+) — partner-respectful starter, not full SEO program |
| **Build E "Done Now, Algorithm"** title shifted from "Authority" to "Foundation" | Block 04 | Reflects that this is the launchpad for SEO partner work, not the destination |
| **NEW Block 04.5** — "How the system works" funnel section | NEW file | Surfaces the two-step diagnostic mechanic for cold visitors and share-able context |
| **FAQ updates** — quiz hosting Q, "Is this a full SEO program?" Q, citation positioning Q | Block 06 | Aligns with new positioning |
| **FAQPage schema** updated to match | Block 06 | Schema reflects current FAQ |

## What changed in v1.3 (from v1.2)

| Change | Where | Why |
|---|---|---|
| **Primary hero CTA** repointed to `https://netsync.nowgroup.co.nz/brandkit/` | Block 01 | Diagnostic-first funnel — capture intent before product browsing |
| **CTA label** → "Begin X-traction — power your X-Factor" | Block 01 | Matches the X-Factor / X-traction brand voice |
| **Urgency line added** — "Brand Blueprint and AI Voice Encoder by the end of the week" | Block 01 | Concrete deliverable preview, 7-day commitment frame |
| **Tagline globally updated** to "Hand built by robots, imagined by humans." | Blocks 01, 07 | Single line, complete thought — keeps craft signal AND adds human-imagination resolution |
| **Secondary CTA removed** from hero | Block 01 | Single-purpose hero — no decision fatigue, brandkit gets full focus |
| **CTA microcopy** added: "FREE DIAGNOSTIC • 10 MINUTES • NO CARD REQUIRED" | Block 01 | Reduces friction, signals low commitment |

## What changed in v1.2 (from v1.1)

| Change | Why |
|---|---|
| **8 independent files instead of 1 blob** | Edit each section without touching others. Hand sections to different people. Refactor independently. |
| **11 sections → 5 visible movements** | Compressed scroll length ~50%. Less fatigue. |
| **3 horizontal carousels** (Tier 1 / DNAˣ / Bundles) | Tighter than vertical card stacks. Native swipe on mobile, arrow controls on desktop, dot indicators. |
| **All CTAs solid orange** | No more "blank/hollow" buttons (the old navy-on-navy `.now-btn-secondary` was invisible on dark sections). |
| **Dev-mode banner** | Yellow banner at top says *"⚠ Preview mode — Kajabi URLs not configured."* Auto-hides when all 12 placeholders in `NOW.offerMap` are real URLs. Console warns about each unconfigured offer. |
| **Click handler on unconfigured CTAs** | Clicking a button before URLs are wired shows an alert with the offer key — no silent failures. |
| **Apostrophes fixed** | "Stack the A's" / "Six A's" / "the A's" — proper plural-letter punctuation. |
| **Contrast audit** | `--text-light-dim` bumped from 0.6 → 0.78 alpha. All text/background pairs verified for WCAG AA. |

---

## Install order (Kajabi)

Create a new blank Kajabi page. Add **9 Custom Code blocks** in this order:

```
Page top
  ↓
[Block 00 — FOUNDATION]    ← MUST be first. Loads CSS, fonts, JS, dev banner.
[Block 01 — HERO]
[Block 02 — SYSTEM]
[Block 03 — TIER 1 CAROUSEL]
[Block 04 — DNAx CAROUSEL]
[Block 05 — BUNDLES CAROUSEL]
[Block 04.5 — HOW THE FUNNEL WORKS]   ← NEW in v1.4. Sits AFTER bundles.
[Block 06 — PROOF + FAQ]
[Block 07 — CLOSE + FOOTER]
  ↓
Page bottom
```

For each block:
1. Open the corresponding `.html` file in a text editor
2. Select all (Ctrl+A / Cmd+A)
3. Copy
4. Paste into the Custom Code block in Kajabi
5. Save

Order matters because Block 00 defines the CSS variables and `NOW.*` JS namespace that all other blocks depend on. Block 04.5 sits *after* Block 05 even though numbered between 04 and 05 — it visually flows: Hero → System → Products (3 carousels in 03/04/05) → Funnel reference → Proof → Close. The carousel cluster shouldn't be interrupted.

---

## Wiring Kajabi offer URLs (the 15-minute job)

All offer URLs live in **one place**: the `NOW.offerMap` object at the bottom of **Block 00**.

```javascript
NOW.offerMap = {
  'content-pack-pro':        '#REPLACE_KAJABI_OFFER_URL_PACK_A',
  'partner-growth':          '#REPLACE_KAJABI_OFFER_URL_PACK_B',
  'email-rescue':            '#REPLACE_KAJABI_OFFER_URL_PACK_C',
  'wow-bundle':              '#REPLACE_KAJABI_OFFER_URL_WOW',
  'build-d':                 '#REPLACE_KAJABI_OFFER_URL_BUILD_D',
  'build-e':                 '#REPLACE_KAJABI_OFFER_URL_BUILD_E',
  'build-f':                 '#REPLACE_KAJABI_OFFER_URL_BUILD_F',
  'bundle-pipeline':         '#REPLACE_KAJABI_OFFER_URL_PIPELINE',
  'bundle-conversion':       '#REPLACE_KAJABI_OFFER_URL_CONVERSION',
  'bundle-authority':        '#REPLACE_KAJABI_OFFER_URL_AUTHORITY',
  'bundle-complete-factory': '#REPLACE_KAJABI_OFFER_URL_COMPLETE_FACTORY',
  'calendly':                '#REPLACE_CALENDLY_FIT_CALL_URL'
};
```

Replace each `#REPLACE_*` string with the real Kajabi checkout URL. Format looks like:
```
'content-pack-pro': 'https://www.nowgroup.co.nz/offers/AbC123Xy/checkout',
```

Save Block 00. The yellow dev banner disappears automatically once all 12 are real URLs.

---

## How `<style>` tags work across multiple blocks

**Short answer:** They all combine. The browser concatenates every `<style>` tag on a page into one effective stylesheet. Order matters — later rules override earlier rules of equal specificity. Block 00 loads first defining base tokens; subsequent blocks extend or override what they need.

### What's in each block

```
Block 00 — Shared CSS (everything reusable):
  • CSS variables on :root  (colors, spacing, typography)
  • Reset rules
  • Base layout              (.now-section, .now-container)
  • Buttons                  (.now-btn, .now-btn-ghost, .now-btn-link)
  • Eyebrows + cards + carousel framework
  • Dev banner + animations

Blocks 01–07 — Section-specific styles only:
  • Hero gradient + corner counter         (Block 01)
  • Tier mini-cards + spine grid           (Block 02)
  • Tier 1 carousel + WOW hero treatment   (Block 03)
  • Dark-bg carousel overrides             (Block 04)
  • Bundles + Complete Factory hero        (Block 05)
  • Proof grid + FAQ accordion             (Block 06)
  • Final CTA doors + footer               (Block 07)
```

Section styles only override what's specific to that section. They reference the variables from Block 00's `:root`, so changing a brand color in Block 00 ripples to every section automatically.

### Why this works

- **CSS variables on `:root`** cascade globally — every section inherits, regardless of DOM position
- **Class names are namespaced** with `.now-` prefix to avoid collisions with Kajabi's own classes
- **Section selectors are scoped** (`.now-hero-section h1` not just `h1`) so sections don't bleed into each other
- **No `!important` arms races** — specificity stays consistent

### Kajabi compatibility note

Kajabi's Custom Code blocks support `<style>` tags by default. On standard plans this works as expected.

**However** — if your Kajabi instance has strict content security policies (rare; some enterprise configurations) `<style>` tags inside Custom Code blocks may get stripped on save. If that happens, you have three fallback options:

**Option A — Consolidate all CSS into Block 00**
Copy every `<style>` block from Sections 01–07 into Block 00's `<style>` block. Delete the `<style>` tags from Sections 01–07, leaving only HTML. Block 00 becomes ~600 lines instead of 300, but every section edit involving styles now lives in one file.

**Option B — Site-wide Header injection (recommended for multi-page deployments)**
Move all CSS to **Kajabi → Settings → Site Details → Code Injection → Header**. Wrap in a single `<style>` tag. Every page on your Kajabi site picks it up. Section blocks stay as pure HTML.

Best if you plan to reuse the Marketing NOW design system across multiple pages (per-product pages, NET_SYNC pages, etc.).

**Option C — External stylesheet**
Save the consolidated CSS as a `.css` file, host it (Kajabi file uploads, GitHub Pages, your own CDN), reference via `<link rel="stylesheet" href="..."/>` in Header injection. Most professional but adds a hosting dependency.

### Quick test — are styles loading?

1. Paste all 8 blocks into Kajabi, click **Preview**
2. Open preview in browser, right-click any orange button → **Inspect**
3. Look at the **Computed Styles** panel
4. If `background-color` reads `rgb(232, 76, 30)` — styles are loading correctly ✓
5. If `background-color` is white, transparent, or default browser blue — `<style>` tags are being stripped, switch to **Option B**

### Editing the design system

| What you want to change | Where to edit |
|---|---|
| Brand orange color | Block 00 → `:root` → `--now-orange` |
| Brand navy color | Block 00 → `:root` → `--now-navy` |
| Default font sizes | Block 00 → `.now-section` |
| Button styling | Block 00 → `.now-btn` rules |
| Specific section background | That section's `<style>` block |
| Hero gradient | Block 01 → `<style>` |
| Carousel arrow appearance | Block 00 → `.now-carousel-btn` |
| FAQ accordion behavior | Block 06 → `<style>` |

If you want to change something **globally** (brand colors, spacing scale, font choices) — edit Block 00. Every section inherits.

If you want to change something **for one section only** — edit that section's `<style>` block.

---

## File reference

| File | Purpose | Lines |
|---|---|---|
| `00_foundation.html` | CSS framework, fonts, dev banner, JS, offerMap | ~300 |
| `01_hero.html` | Hero section | ~110 |
| `02_system.html` | Problem + how-it-works + counting + 6-A's spine | ~180 |
| `03_tier1_carousel.html` | Pack A/B/C + WOW Bundle (4-card carousel) | ~210 |
| `04_dnax_carousel.html` | Build D/E/F (3-card carousel) | ~270 |
| `05_bundles_carousel.html` | Pipeline / Conversion / Authority / Complete Factory (4-card carousel) | ~250 |
| `06_proof_faq.html` | 6 vignettes + 17-question FAQ + FAQPage schema | ~330 |
| `07_close_footer.html` | 3-door CTA + footer | ~150 |

---

## Editing principles

**Each block is independently editable.** Change one without breaking others.

**Block 00 is the only place CSS variables and JS namespace are defined.** If you need to change brand colors site-wide, edit Block 00 only. Every other block inherits.

**Section-specific styles live inside that section's `<style>` block.** They won't leak into other sections because of the `.now-section` parent class scoping.

**To remove a section:** delete that block from the Kajabi page. The page still works — sections are independent.

**To rearrange sections:** drag blocks in Kajabi's section editor. Block 00 must stay first; otherwise order is flexible.

**To A/B test a section:** duplicate the block, edit the copy in one version, hide the other. Swap which is visible.

---

## Mobile behavior

- **Carousels** swipe naturally on touch devices (CSS scroll-snap)
- **Arrow buttons** hide on small screens (carousel works via swipe)
- **Dot indicators** show position
- **Cards** snap one-at-a-time on mobile (88% width with peek of next)
- **Counting animation** still cycles
- **FAQ accordion** uses native `<details>` — no JS dependency, works everywhere

---

## What to verify before going live

1. ☐ All 12 `NOW.offerMap` URLs replaced with real Kajabi checkout URLs
2. ☐ Calendly fit-call URL replaced
3. ☐ Yellow dev banner has disappeared
4. ☐ Click each CTA — verify it routes correctly
5. ☐ Test mobile (380px width) — no horizontal scroll, all sections collapse cleanly
6. ☐ Open browser console — no warnings about unconfigured offers
7. ☐ Run Google Rich Results Test on the live URL — Organization + FAQPage schemas validate
8. ☐ Replace 6 placeholder testimonials with real ones (Block 06) when available
9. ☐ Set Open Graph image (use `Marketing_NOW_Hero_OG.svg` exported to PNG)
10. ☐ Submit URL to Google Search Console for indexing

---

## Troubleshooting

**Carousel not scrolling smoothly:**
- Check Block 00 loaded first (CSS depends on `:root` variables)
- Verify Google Fonts loaded (Network tab in DevTools)

**Page renders but everything looks unstyled (no orange, default fonts, broken layout):**
- Most likely: Kajabi stripped your `<style>` tags. See **"How `<style>` tags work across multiple blocks"** above for fallback options (consolidate into Block 00, or use Site-wide Header injection).
- Run the quick test in that section to confirm before doing anything else.

**Buttons still look "blank" or unstyled:**
- Hard refresh (Ctrl+Shift+R / Cmd+Shift+R) to clear cached old CSS
- Verify Block 00 is the FIRST custom code block on the page
- If problem persists, run the "Quick test — are styles loading?" check in the styles section above

**Some sections styled, others not:**
- That specific section's `<style>` tag was stripped or moved
- Open the section's HTML in Kajabi's editor — verify `<style>...</style>` is intact
- If repeatedly stripped, move that section's CSS into Block 00 (Option A in the styles advisory)

**Dev banner won't disappear:**
- Open browser console — look for `[Marketing NOW]` warning listing unconfigured URLs
- Make sure replacement URLs don't start with `#REPLACE` (the auto-detection key)

**FAQ schema not validating:**
- Block 06 contains the FAQPage schema. If Kajabi wraps it weirdly, move the `<script type="application/ld+json">` block to Site Details → Code Injection (Header).

**Counter stops animating:**
- Element ID `mainCounter` only exists in Block 02. If Block 02 was removed, the counter JS gracefully exits.

---

*Hand built by robots. From your DNA.*
