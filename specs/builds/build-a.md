---
spec_version: 1.1
last_updated: 2026-06-08
build_letter: A
build_name: Content Pack Pro
tier: 1
tagline: 8 weeks of buyer-voice LinkedIn content in one delivery
status: live
source: nexus_wow_option_a.py (NEXUS MKII canonical builder) + lm_builder/templates/*
---

# Option A — Content Pack Pro (Tier 1)

> A complete 8-week LinkedIn content campaign in the buyer's brand and voice — 4 fortnightly pillar articles + every derivative asset (posts, carousels, videos, infographics, GEO blogs, lead magnets). Built in one delivery; the buyer publishes on schedule.
>
> Tier 1 one-shot delivery build. Reference asset structure for Options B and C.

## 1. Intent

Content Pack Pro produces a complete 8-week LinkedIn content campaign for one buyer in a single delivery. Four pillar articles drive everything; every derivative is built FROM the articles (not invented independently). Output is buyer-branded (palette, fonts, logo, person photo) and buyer-voiced (Voice Parameter Block applied throughout). Buyer publishes fortnightly per the included posting schedule.

## 2. Commercial structure

- **Setup**: $1,997 NZD excl GST · one-off · ~14-day turnaround
- **No ongoing** — pack is a finite deliverable; buyer can re-engage for next pack
- **Commercial terms** — NZD excl GST · 7-day payment terms (NOW Group standard)

## 3. Deliverables (one delivery)

The pack contains the following assets. Counts are exact — do not under- or over-deliver.

### 3.1 Foundation (Pass 1)

| Asset | Format | Notes |
|---|---|---|
| Brand Context Brief | Section in master .docx | Audience, voice fingerprint, pillars, CTAs (soft/medium/hard), signature move, banned words |
| Spine | 3–5 foundational sentences | The thread the whole campaign hangs from |
| **4 × Pillar Articles** (A, B, C, D) | 550–650 words each | Operator essay; hook → spine sentence → named framework → 1–2 proof vignettes → CTA. Fortnightly release. |

### 3.2 Derivatives (Pass 2)

| Asset | Count | Format |
|---|---|---|
| Carousels (A, B, C, D) | 4 | 8 slides each (1 hook + 6 body + 1 CTA) + full Gamma prompt |
| Infographics (A, B) | 2 | 4-section diagnostic + red-flag bar + Gamma prompt + HTML print-PDF |
| LinkedIn copy posts | 16 | 4 per article (A1–4, B1–4, C1–4, D1–4) · 120–220 words each · escalating CTA strength |
| Video scripts | 16 | 4 per article · 45–75 sec / ≤180 words · Hook → Scene → Framework → Proof → Closing |
| Wrapper posts | 4 | Carousel A · Carousel B · Infographic A · Infographic B |
| GEO blogs | 6 | A1, A2, B1, B2, C1, D1 · Answer Capsule (40–60w) + 600–1000w body + 4 FAQs + schema flags |
| Long-form lead magnet | 1 | Gamma prompt for 6–8 section A4 document, deeper treatment of Article A |
| Posting schedule | 1 | Fortnight-by-fortnight publishing plan across all 31+ assets |

### 3.3 Render-out HTML lead magnets (Pass 3)

These are the **canonical printable PDFs** — Claude renders the HTML directly, the buyer (or Chris) PDF-converts externally.

| LM | Built from | Template reference |
|---|---|---|
| `<slug>_lm_diagnostic.html` | Article A | `lm_builder/templates/type_lm_diagnostic/template.html` |
| `<slug>_lm_framework.html` | Article B | `lm_builder/templates/type_lm_framework/template.html` |
| `<slug>_infographic_a.html` | Pass 2 infographic A | `lm_builder/templates/type_infographic_audit/template.html` |
| `<slug>_infographic_b.html` | Pass 2 infographic B | `lm_builder/templates/type_infographic_audit/template.html` |

Render contract for the HTML LMs:

- **Self-contained** — inline `<style>` block, no external CSS, Google Fonts via `<link>` only
- **A4 print-ready** — `@page { size: A4 portrait; margin: 5mm 8mm; }` plus print-safe page-break rules
- **Brand variables** — populate CSS custom properties from buyer palette (`--primary`, `--secondary`, `--accent`, `--cta`, `--ink`, `--body`, `--cream`, `--mozzarella`, `--rule`, `--red-flag`)
- **Brand fonts** — buyer display + body families, loaded via Google Fonts URL
- **No images by design** — print-LM HTML is image-free (Gamma carries the image-rich web/social variants)
- **Defensive substitution** — never leave `{{ template_tokens }}` or `{BRACKETS}` in output; every value rendered, no Jinja2 syntax remaining

### 3.4 Master bundle

| Asset | Format |
|---|---|
| `WOW_OptionA_ContentPack_<Buyer>_v1.docx` | All 31+ copy assets pre-populated with Gamma prompts inline — single artefact buyer can scroll, edit, copy from |
| `00_START_HERE.txt` | Build-specific README pointing at delivery order + how to use Gamma prompts |
| Voice Encoder Pro PDF | If buyer has a Voice Parameter Block on record (else skip) |

### 3.5 Visual asset generation (Gamma MCP)

Run the Gamma MCP `generate` tool for each of: 4 carousels, 2 infographics (visual variants), 1 long-form LM. Use the exact Gamma prompts emitted in Pass 2 — do not modify or "improve" them at generation time. Gamma theme: match buyer brand if a brand-aligned Gamma theme exists; otherwise default.

## 4. Inputs required

- **Buyer profile** — name, business, role, sector, location, website, tagline, lead source, growth target, success definition
- **ICP detail** — 3–4 pain points, 3–4 desires, primary services, core values
- **Voice sample** — written content sample OR transcript excerpt (~1500 chars sufficient)
- **Voice Parameter Block** — if available (drives banned words, signature move, register)
- **Brand profile** — palette (primary, secondary, accent, cta, ink, body, cream, mozzarella, rule, red-flag), fonts (display + body), person photo URL, logo URL, primary domain, person name + role + tagline
- **From other builds** — none required; stacks with Build E (GEO authority) for blog distribution + Build D (Quiz Funnel) for inbound capture

For pre-existing customers, all of the above will already be in the thread context — skill verifies presence, asks for what is missing, never fabricates.

## 5. Voice + brand layer

- **Buyer brand** — `force_now_palette=False` (all client-facing assets render in buyer palette/fonts)
- **Voice Parameter Block** drives:
  - All article body copy + derivative copy
  - Hook patterns + signature move enforcement
  - Banned word list (hard reject)
- **NOW voice** appears only in the internal `00_START_HERE.txt` framing if NOW is delivering directly
- **Voice rules** (non-negotiable, from `nexus_wow_option_a.py:581`):
  - Plain English. Short sentences. No fluff.
  - Outcome-first: time saved, risk reduced, margin improved, decision speed
  - Confident, calm urgency. No panic. No hype.
  - Concrete examples — not overly technical
  - Auto-banned: synergy, leverage, paradigm, best-in-class, digital transformation (plus buyer's own banned list)

## 6. Quality gates

Fetch each rubric on demand (only when scoring the matching asset type — keeps token use low). Auto-regen on score < 8/10 (one retry max — second failure flags for human review, does not silently re-output).

| Asset type | Rubric URL |
|---|---|
| Pillar articles (A–D) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Article_Pillar_Scoring_Rubric.md |
| Carousels (A–D) + Infographic copy (A–B) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Carousel_Infographic_Scoring_Rubric.md |
| LinkedIn posts (16) + Wrapper posts (4) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/LinkedIn_Conversion_Post_Scoring_Tool.md |
| Video scripts (16) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Video_Script_Scoring_Rubric.md |
| Lead magnet copy (diagnostic + framework) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Lead_Magnet_Scoring_Rubric.md |
| Rendered lead magnet HTML pages | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Page_Landing_Result_Scoring_Rubric.md |
| GEO blogs (6) | Blend Article_Pillar + Page_Landing rubrics — Article for body voice, Page for SEO/structure |
| Long-form LM Gamma prompt | Lead_Magnet_Scoring_Rubric (apply to the prompt's intended output, not prompt syntax) |
| Posting schedule · Brand Brief · Spine | No rubric — structural correctness check only |

Universal scorer rubric + per-buyer overlay from the buyer's Voice Parameter Block — never per-buyer-bespoke filter logic.

**Python parity note:** the canonical Python build (`nexus_wow_option_a.py`) auto-wires only `article_filter` + `carousel_filter`. The Claude.ai skill applies more rubrics because in-thread serial scoring is cheaper than the Python pipeline's subprocess fan-out. To stay in strict Python parity, run only the first two rubrics.

## 7. Delivery structure (Google Drive)

```
NOW Group — Content Pack Delivery/
  └── Content Pack Pro — <Buyer Name> — <YYYY-MM-DD>/
        ├── 00_START_HERE.txt
        ├── WOW_OptionA_ContentPack_<Buyer>_v1.docx
        ├── <slug>_lm_diagnostic.html
        ├── <slug>_lm_framework.html
        ├── <slug>_infographic_a.html
        ├── <slug>_infographic_b.html
        ├── gamma_links.txt   (one Gamma URL per visual asset)
        └── (optional) <Buyer>_voice_encoder_pro.pdf
```

Share permissions: link-view enabled for the buyer's email; Chris (chris@nowgroup.co.nz) owner.

## 8. Refinement notes

- **Why 4 × 550–650w articles, not 2 × 1200w**: fortnightly cadence outperforms monthly on low-to-mid influence accounts; short articles get read in full + shared more readily. Locked since v1.
- **Why Pass 1 → Pass 2 separation**: derivatives MUST derive from the foundation (not be invented independently). Single-pass generation produces noticeably more drift between pillar voice and post voice.
- **Why image-free print LMs**: print PDFs are tactile + business-use artefacts; Gamma carries the image-rich web variants. Don't merge the two roles.
- **Open spec question** — should the GEO blog count scale with buyer's existing blog audience (currently fixed at 6)? Flag for review after 5 packs.
- **Open spec question** — long-form LM is currently a Gamma prompt only (no HTML render). Should it become a third HTML LM (`type_lm_longform`)? Flag for review after first buyer requests it.

## 9. Canonical Python build (reference)

This spec mirrors the Python pipeline at `NEXUS MKII/nexus_wow_option_a.py` — when drift between this spec and the Python is detected, the Python is canonical for asset shape (it ships the actual deliverable), and this spec is canonical for the asset roster + voice/brand rules (it's the human-readable contract). Reconcile by updating both.

Key Python entry points:
- `generate_foundation()` — Pass 1 prompt + asset schema
- `generate_derivatives()` — Pass 2 prompt + asset schema
- `_emit_lm_content_yamls()` — Pass 3 LM content YAML emission
- `_build_option_a_assets()` — Pass 4 lm_builder subprocess (Jinja2 + Playwright)

---
