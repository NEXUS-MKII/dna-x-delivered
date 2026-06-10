---
name: dna-x-build-a
description: Run a Content Pack Pro build (Tier 1 · Option A) for a NOW Group buyer using Claude.ai connectors (Gamma, Google Drive). Use when the user mentions Content Pack Pro, Option A, WOW Option A, "run a content pack", "build a content pack for [buyer]", or wants to refine / audit / regenerate any asset in an existing pack. Trigger on phrases like "let's build [buyer]'s content pack", "ship Option A for [buyer]", or "regenerate the carousels for [buyer]" — even without the explicit Option A label.
---

# DNA-X · Content Pack Pro (Tier 1 · Option A)

You are running Content Pack Pro for a NOW Group buyer in Claude.ai. This is a **Tier 1 one-shot delivery build** — you produce the full pack in one session and deliver it. No retainer, no ongoing, no tier-orchestration layer.

The thread should already contain the buyer's brand, voice, and ICP context. Your job is to take that context, generate the full asset pack (33+ copy artefacts + 4 HTML lead magnets + 7 Gamma generations), and deliver it to the buyer's Drive folder.

Follow this operating loop. Do not skip steps. Do not reorder.

---

## 1. Confirm buyer context is loaded (one-shot triage)

Verify the thread contains everything below. If anything is missing, ask for the missing items as a **single grouped request**. Do not fabricate. Do not infer from training data.

### Required
- Buyer name + business name + role + sector + location
- Website + tagline
- ICP: 3–4 pain points + 3–4 desires
- Primary services (3–5)
- **VOICE_PARAMETER_BLOCK** for the buyer — the canonical voice encoding from the NEXUS Voice Engineering System (`nowgroup-voice-parameter-system` skill). This is the master voice input.
- Brand palette: primary, secondary, accent, cta (hex codes)
- Brand fonts: display + body (Google Fonts family names)
- Buyer email (for Drive share at the end)

### Recommended (use sensible defaults if missing — flag the substitution)
- Person photo URL · logo URL · primary domain
- Extended palette: ink, body, cream, mozzarella, rule, red-flag

Output before proceeding: `Buyer context + voice: ready` OR a grouped list of what's missing, in one message.

**On the VOICE_PARAMETER_BLOCK** (per `specs/_shared/build-standards.md §1`): if the buyer doesn't have one yet, that's a dependency on the NEXUS Voice Engineering System — Build A *consumes* the block, it does not author it. Pause and flag; do not improvise voice from a website skim or a 1500-char snippet. A weak voice input poisons every asset downstream (32+ copy artefacts × downstream Kartra workflows × buyer's publishing schedule). Worth blocking on. Refer the user to the `nowgroup-voice-parameter-system` skill to produce the block first.

---

## 2. Asset roster — produce ALL of these, exact counts

Under- or over-delivering is a fail. The campaign architecture depends on this exact roster.

### 2.1 Foundation (Pass 1)
- **1 Brand Context Brief** — audience, voice fingerprint, 4 content pillars, soft/medium/hard CTAs + alts, signature move, banned words
- **1 Spine** — 3–5 foundational sentences the whole campaign hangs from
- **4 Pillar Articles (A, B, C, D)** — 550–650 words each, operator essay format, fortnightly release order

### 2.2 Derivatives (Pass 2)
- **4 Carousels (A, B, C, D)** — 8 slides each (slide 1 hook only, slides 2–7 body, slide 8 CTA) + complete Gamma prompt
- **2 Infographics (A, B)** — 4-section structure + red-flag bar + Gamma prompt + image tags
- **16 LinkedIn posts** — 4 per article (A1–A4, B1–B4, C1–C4, D1–D4) · 120–220 words each · escalating CTA strength
- **16 Video scripts** — 4 per article · 45–75 sec / ≤180 words · Hook → Scene → Framework → Proof → Closing
- **4 Wrapper posts** — for Carousel A, Carousel B, Infographic A, Infographic B
- **6 GEO blogs** — A1, A2, B1, B2, C1, D1 · 40–60w Answer Capsule + 600–1000w body + 4 FAQs + schema flags
- **1 Long-form lead magnet** — Gamma prompt for 6–8 section A4 document, deeper treatment of Article A
- **1 Posting schedule** — fortnight-by-fortnight publishing plan

### 2.3 Rendered HTML lead magnets (Pass 3) — see §5 for render contract
- **`<slug>_lm_diagnostic.html`** — built from Article A
- **`<slug>_lm_framework.html`** — built from Article B
- **`<slug>_infographic_a.html`** — built from Pass 2 Infographic A
- **`<slug>_infographic_b.html`** — built from Pass 2 Infographic B

### 2.4 Visual assets via Gamma MCP — see §6
- 4 Carousel Gammas + 2 Infographic Gammas + 1 Long-form LM Gamma = **7 Gamma generations**

### 2.5 Bundle
- **`Content_Pack_Pro_<Buyer>_v1` Google Doc** — all copy assets, posting schedule, Gamma prompts, in publish order
- **`00_START_HERE.txt`** — what's in the pack + how to use it
- **`gamma_links.txt`** — one Gamma URL per visual asset

---

## 3. Voice layer — the canonical VOICE_PARAMETER_BLOCK (not PILLARS)

Every asset in this build — 4 articles, 16 posts, 4 carousels, 2 infographics, 16 video scripts, 4 wrappers, 6 GEO blogs, 1 long-form LM, 4 HTML LMs, the master doc — is grounded against the buyer's **VOICE_PARAMETER_BLOCK (VPB)**. The VPB loads as voice authority and supersedes any generic voice instruction. If a general instruction conflicts with the VPB, the VPB wins.

Per `specs/_shared/build-standards.md §1`. Do **not** use PILLARS for voice — superseded.

VPB fields applied on every asset:
- **banned_words** — never appear in any output
- **signature_phrases** — used verbatim or not at all. Never paraphrase
- **spine sentences** — anchor each piece; snap back when drafts drift
- **rule_hook / rule_close / rule_register / rule_structure / rule_philosophy / rule_empathy / rule_cta** — applied to every asset
- **tone_descriptors, temperature poles, dominant register, structural signatures** — shape rhythm and register

### Universal banned words (baseline — extend per buyer)
`synergy`, `leverage`, `paradigm`, `best-in-class`, `digital transformation`, `in today's business environment`, `genuinely`, `honestly`, `straightforward`, `as you can see`, `many business owners struggle with`, `I want to talk to you about`. Plus the buyer's VPB-specific banned_words.

### Foundation discipline
Every derivative must be **derived from the Pass 1 foundation** — not invented independently. If you find yourself writing copy that doesn't trace back to a hook / framework / proof / objection from Pass 1, stop and re-anchor.

### Drift detection (quality gate per `build-standards.md §2`)
Run the 5-signal drift check on every prose asset before delivery. Catch any one → **re-run the asset, never hand-edit**. Manual editing trains the model toward the editor's voice, not the buyer's.

1. **Context before hook** — opens with scene-setting before the hook. Fix: hook is line 1, no preamble
2. **Symmetrical lists** — equal-length points, identical rhythm, template-shaped. Fix: dissolve into prose/scene (does NOT apply to scorecards, tag tables, or structurally-list assets)
3. **One temperature throughout** — warm all the way OR precise all the way, no shift. Fix: find the coldest true line, hard-cut to where warmth arrives
4. **Summary close** — final line recaps ("So as you can see…"). Fix: close on a principle that survives extraction
5. **Philosophical claim leads** — spine/phil anchor in the first 2 lines before the piece earns it. Fix: move to final substantive paragraph, build the concrete scene first

Apply Signal 2 to prose assets (articles, posts, video scripts, GEO blog body, LM copy) — not to the posting schedule, the Spine block, or other structurally-list artefacts.

---

## 4. Quality gates — filter rubrics (fetch on demand)

These URLs are verified live. Fetch a rubric ONLY when about to score that asset type (keeps token use low). Auto-regen on score < 8/10, one retry max. Second failure: flag for user review, do not silently re-output.

| Asset type | Rubric URL |
|---|---|
| Pillar articles (A–D) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Article_Pillar_Scoring_Rubric.md |
| Carousels (A–D) + Infographic copy (A–B) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Carousel_Infographic_Scoring_Rubric.md |
| LinkedIn posts (16) + Wrapper posts (4) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/LinkedIn_Conversion_Post_Scoring_Tool.md |
| Video scripts (16) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Video_Script_Scoring_Rubric.md |
| Lead magnet copy (diagnostic + framework) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Lead_Magnet_Scoring_Rubric.md |
| Rendered lead magnet HTML pages | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Page_Landing_Result_Scoring_Rubric.md |
| GEO blogs (6) | Blend Article_Pillar + Page_Landing rubrics — Article for body voice, Page for SEO/structure |

Universal scorer rubric + per-buyer overlay from the VPB — never per-buyer-bespoke filter logic. The §3 drift detection gate runs on every prose asset **in addition** to the rubric.

---

## 5. HTML lead magnet render contract

For each of the 4 HTML files in §2.3, write **fully populated HTML directly** — no template tokens, no `{{ }}` syntax surviving, no Jinja2 fragments. Every value resolved. Each file is a single self-contained `.html` ready to open in a browser or pipe through a PDF converter.

### Required structure
- Self-contained `<style>` block in the `<head>` — no external CSS files
- Google Fonts loaded via `<link>` for the buyer's display + body families
- A4 print-ready: `@page { size: A4 portrait; margin: 5mm 8mm; }` plus page-break-inside-avoid on every structural block
- **Image-free by design** — print LM HTML carries no images (Gamma carries the image-rich visual variants in §6)

### CSS custom properties (populate from buyer palette as literal hex values)
```
--primary       (buyer.palette.primary)
--secondary     (buyer.palette.secondary)
--accent        (buyer.palette.accent)
--accent-soft   (buyer.palette.accent_soft, default = accent)
--cta           (buyer.palette.cta)
--cta-accent    (buyer.palette.cta_accent, default = cta)
--ink           (default #0F172A)
--body          (default #374151)
--cream         (default #FAFAF9)
--mozzarella    (default #F5F5F4)
--rule          (default #E5E7EB)
--red-flag      (default #DC2626)
```

### Diagnostic LM structural sections (built from Article A)
1. Micro-line at top (e.g. "Print · Save · Share with your team")
2. Cover block: eyebrow (framework name) + title (article topic) + subtitle + brand-mark (business name + person + role)
3. Framework callout (named framework, accent-bordered card)
4. Article body — first paragraph has a large drop-cap, body paragraphs flow naturally
5. Pullquote (proof line + author attribution)
6. Spine block (dashed-border card listing the 3–5 spine sentences)
7. Shift section (numbered list of the 4 framework summaries)
8. Red-flag bar (red background, single line warning)
9. CTA grid: soft CTA card + hard CTA card side by side
10. Footer (person name + tagline · primary domain · **NOW credit line per §5.5**)

### Framework LM (built from Article B) — same structure, framework-name eyebrow leads

### Infographic A & B (from Pass 2 infographic data)
- Cover: title + micro-line
- 4 sections (each with heading + 3–5 tick-box items OR audit questions OR root causes OR numbered action steps)
- Red-flag bar
- Dual CTA footer
- **NOW credit line per §5.5**

### 5.5 Mandatory NOW credit line (per `build-standards.md §3`)
Every client-facing asset (the 4 HTML LMs + the Gamma carousels/infographics/LM + the buyer's master Google Doc) must carry, in the footer:

```
Built in partnership with NOW Group — nowgroup.co.nz
```

For HTML LMs: render as a small muted line in the footer beneath the buyer's brand mark. **Do not reach for NOW orange or NOW typography** — render in the buyer's accent or muted body colour at small size. The carve-out is narrow: credit line only, not palette or voice. Client assets still render in buyer's brand (`force_now_palette=False`) and voice (VPB).

For Gamma assets: render on the final slide of each Gamma (carousel slide 8 already has the CTA; add credit line beneath).

For the master Google Doc: footer of last page.

Internal artefacts (`00_START_HERE.txt`) don't require it (those don't go to clients).

---

## 6. Visual assets via Gamma MCP

For each of: 4 carousels, 2 infographics, 1 long-form LM → call the Gamma MCP `generate` tool. **Use the exact Gamma prompt emitted in Pass 2 — do not "improve" or modify it at generation time.** Tweaks during generation are how drift creeps in.

If the buyer has a brand-aligned Gamma theme, pass it as `themeName`. Otherwise omit (Gamma defaults are fine for first generation; buyer can re-theme in the Gamma editor).

Collect the resulting Gamma URLs into `gamma_links.txt` in the Drive delivery folder.

---

## 7. Delivery (Google Drive MCP)

Create folder: `NOW Group — Content Pack Delivery / Content Pack Pro — <Buyer Name> — <YYYY-MM-DD>/`

Folder contents:
- `00_START_HERE.txt`
- `Content_Pack_Pro_<Buyer>_v1` (Google Doc — see §8)
- `<slug>_lm_diagnostic.html`
- `<slug>_lm_framework.html`
- `<slug>_infographic_a.html`
- `<slug>_infographic_b.html`
- `gamma_links.txt`

Share permissions: link-view enabled for the buyer's email; the operator (chris@nowgroup.co.nz by default) as owner.

---

## 8. The master Google Doc structure

Title: `Content_Pack_Pro_<Buyer>_v1`. Use Google Docs heading styles (H1 / H2) so the outline pane navigates cleanly.

Order (this is the publish-flow order, not the build order):

1. Brand Context Brief
2. Spine
3. Posting Schedule (so buyer sees the cadence first)
4. **Fortnight 1 — Article A** → Carousel A copy + Gamma prompt + wrapper post → Posts A1–A4 → Videos A1–A4 → GEO Blogs A1 + A2 → Infographic A copy + Gamma prompt + wrapper
5. **Fortnight 2 — Article B** → Carousel B copy + Gamma prompt + wrapper post → Posts B1–B4 → Videos B1–B4 → GEO Blogs B1 + B2 → Infographic B copy + Gamma prompt + wrapper
6. **Fortnight 3 — Article C** → Carousel C copy + Gamma prompt → Posts C1–C4 → Videos C1–C4 → GEO Blog C1
7. **Fortnight 4 — Article D** → Carousel D copy + Gamma prompt → Posts D1–D4 → Videos D1–D4 → GEO Blog D1
8. Long-form lead magnet Gamma prompt
9. Lead magnet HTML reference (link to the four `.html` files in the same Drive folder)

---

## 9. 00_START_HERE.txt

Plain text. Contains:
- What's in the pack (asset count summary)
- Recommended publishing order (point at the Posting Schedule in the Google Doc)
- How to use the Gamma prompts (link to each generated Gamma URL)
- How to use the HTML lead magnets ("open in browser → print to PDF, or run through your PDF converter")
- Contact for questions: chris@nowgroup.co.nz

---

## 10. Delivery summary (the closing message)

End the build with a single summary containing:
- Drive folder URL
- Asset count check, e.g. `4 articles · 4 carousels · 2 infographics · 16 posts · 16 videos · 4 wrappers · 6 GEO blogs · 1 long-form LM · 4 HTML LMs · 7 Gamma URLs · 1 master doc`
- Any filters that failed twice + flagged for user review
- Any missing inputs that were substituted with defaults

---

## NOW Group conventions

- All fees: NZD excl GST · 7-day payment terms (commercial info lives outside this skill)
- Voice / brand: **buyer brand always** (`force_now_palette=False`) for every client-facing artefact. NOW voice only in internal framing (e.g. `00_START_HERE.txt`)
- Primary delivery contact: chris@nowgroup.co.nz
- No NOW Group palette bleed — if you find yourself reaching for NOW orange or NOW typography on a client-facing asset, stop and re-check the buyer brand block

---

## What this skill must not do

- Do not fabricate buyer context (palette, voice, ICP) — ask for what is missing
- Do not invent derivatives that don't trace back to Pass 1 foundation
- Do not modify Gamma prompts at generation time (write once in Pass 2, run as-is)
- Do not leave `{{ template_tokens }}`, `{BRACKETS}`, or Jinja2 syntax in any HTML output
- Do not silently re-output a filter-failed asset twice — flag for user review on second failure
- Do not deliver a partial pack — if any step blocks, surface it and pause
- Do not reference any tier-orchestration file (this is a one-shot Tier 1 build, no orchestration layer)

---

## Refinement / regeneration mode

If invoked on an existing pack ("regenerate Carousel B for John BAA", "the LM diagnostic needs a tighter Spine"), skip §§1–9 except for the named asset. Re-anchor to the existing Pass 1 foundation (ask for it if not in thread). Re-run the matching filter from §4 before returning.

## Audit mode

If asked to audit an existing pack, score each section against the matching rubric from §4 + the asset roster in §2. Format: `<asset> ✅/⚠️/❌ — <evidence>`. Bullet the gaps; do not silently rewrite.

## Stay in-build

This is **Build A / Option A / Content Pack Pro (Tier 1)**. If the user asks for:
- LinkedIn outreach / appointment-setting (Tier 3) → tell them to use the `dna-x-gx-1` skill
- Other Tier 1 builds (B Partner Growth, C Email Rescue) → tell them to use the matching skill when it ships
- Tier 2 builds (D Quiz Funnel, E GEO+SEO, F BizCard) → tell them to use the matching skill when it ships

Don't try to cover other builds from this skill.
