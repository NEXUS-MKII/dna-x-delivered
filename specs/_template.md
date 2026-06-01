---
spec_version: 0.1
last_updated: 2026-06-02
build_letter: TEMPLATE
tier: 0
status: template
---

# [Build Letter] — [Build Name]

> Spec schema template. Every DNA-X build spec follows this shape.
> Tier 1 & 2 specs use Sections 1–7. Tier 3 specs add Sections 8–11.

## 1. Intent

One paragraph: what this build does, who it's for, the outcome it produces. Keep it under 80 words.

## 2. Commercial structure

- **Price (NZD excl GST)**:
- **Delivery time**:
- **Asset count**:
- **Risk reversal / guarantee**:
- **Tier 3 only**: setup fee + Lite tier + Pro tier monthly pricing

## 3. Deliverables

Every artefact this build produces. For each:

- **Name** —
- **Format** (HTML / PDF / docx / Drive folder / etc.) —
- **Where it lands** (Drive path / repo path / client portal) —
- **Voice + brand layer applied** (which sections of the Voice Parameter Block, brand palette source) —

## 4. Inputs required

- **From intake form**: which fields
- **From brand discovery**: palette, logo, type, tone source
- **From Voice Parameter Block**: which sections
- **From other builds (dependencies)**: if any

## 5. Voice + brand layer

- Voice Parameter Block sections referenced
- Brand DNA elements applied (palette, type, tone)
- **Tier 1**: forced NOW aesthetic — `force_now_palette=True`
- **Tier 2 & 3**: buyer brand — `force_now_palette=False`

## 6. Quality gates

- Which universal filter / scorer applies (`article_filter`, `carousel_filter`, `ember_filter`, `lm_filter`, `page_filter`, `video_filter`)
- Auto-regen rules (score < N → regen with adjustment)
- Manual review points

## 7. Refinement notes

Open spec questions, recent changes, known gaps. **Read this before suggesting changes** — it's where work-in-progress lives.

---

## Tier 3 only — additional sections

## 8. Kajabi SKU configuration

For each offer (Setup, Lite, Pro):

| Field | Value |
|---|---|
| Internal offer name | |
| Public offer name | |
| Offer type | Single payment / Monthly subscription |
| Price (NZD excl GST) | |
| Tax setting | Exclusive of GST (B2B standard) |
| Recurrence | One-time / Monthly + 30-day notice exit after 90-day review |
| Gating | Lite/Pro sellable only to Setup buyers |

Include checkout copy + thank-you page copy verbatim.

## 9. Partner orchestration

- **Which partner type** runs ongoing (VA World, Meta Ads operator, Video editor, etc.)
- **Vetting criteria** specific to this product (in addition to the universal Tier 3 vetting criteria in `tiers/tier-3.md`)
- **Three-way value flow** — client ↔ NOW ↔ partner ↔ media (if applicable)
- **Partner-content subscription** — per-client monthly fee, terms

## 10. Ongoing tier structure

- **Lite** — what's included, monthly cadence, deliverables, price
- **Pro** — what's added on top of Lite, price
- **Common terms** — 90-day performance review, 30-day notice exit after 90 days, setup fees non-refundable

## 11. Bundle math

Which Tier 1/2 builds combine with this Tier 3 product, at what price. Stand-alone vs bundled saving.
