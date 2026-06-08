---
name: dna-x-build-a
description: Run a Content Pack Pro build for a pre-existing NOW Group buyer using Claude.ai connectors (Gamma, Google Drive, GitHub). Use when the user mentions Content Pack Pro, Build A, WOW Option A, "run a content pack", "build a content pack for [buyer]", or wants to refine / audit / regenerate any asset in an existing pack. Trigger on phrases like "let's build [buyer]'s content pack", "ship Content Pack Pro for [buyer]", or "regenerate the carousels for [buyer]" — even without the explicit Build A label.
---

# DNA-X · Build A — Content Pack Pro

You are running Content Pack Pro for a pre-existing NOW Group buyer. The user is in a thread that already has the buyer's brand, voice, and ICP context loaded. Your job is to take that context and produce the full pack deliverable: 31+ copy assets + 4 HTML lead magnets + 4 carousel Gammas + 2 infographic Gammas + 1 long-form LM Gamma, delivered to the buyer's Drive folder.

Follow this sequence on every invocation. Do not skip steps. Do not reorder.

## 1. Fetch canonical spec (always — do not skip, do not improvise from memory)

Fetch **before doing anything else**:

- **Build A spec**: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/builds/build-a.md
- **Tier 2 orchestration**: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/tiers/tier-2.md

If either fetch fails (404, network error, partial content), **STOP and tell the user** — do not improvise from training data. The spec is canonical for the asset roster + voice/brand rules. Drift between live spec and your output is what this skill exists to prevent.

## 2. Cite spec version at the top of every response

Start every reply with a one-line citation block:

> `build-a.md` v<spec_version> · `tier-2.md` v<spec_version> · fetched <iso-date>

This lets the user spot drift if you're operating on a stale spec.

## 3. Confirm buyer context is loaded (one-shot triage)

In a single response, verify the thread has all of the following. If any are missing, ask for them as a single grouped request — do not fabricate, do not infer, do not proceed.

**Required:**
- Buyer name + business name + role + sector + location
- Website + tagline
- ICP: 3–4 pain points + 3–4 desires
- Primary services (3–5)
- Voice sample: written content excerpt OR transcript (~1500 chars)
- Brand palette (primary, secondary, accent, cta) + display + body fonts
- Buyer email (for Drive share)

**Recommended (use defaults from spec if missing — note the substitution):**
- Voice Parameter Block (drives banned words + signature move) — if absent, use voice rules from spec §5
- Person photo URL + logo URL + primary domain
- Full extended palette (ink, body, cream, mozzarella, rule, red-flag) — if absent, use spec defaults

Output: `Buyer context: ready` OR a grouped list of what's missing, in one message.

## 4. Run Pass 1 — Foundation

Generate the foundation in a single Claude response. Match the exact JSON schema in `nexus_wow_option_a.py:628-679` (the spec references it; the Python is canonical for shape).

Produce:
- Brand Context Brief (audience_who, audience_context, audience_pains × 4, audience_desires × 4, voice_fingerprint, signature_move, banned_words, allowed_humour, 4 content pillars, soft/medium/hard CTAs + alts)
- Spine (3–5 sentences)
- 4 × Pillar Articles A/B/C/D (550–650 words each, exact structure per spec §3.1)
- Blocks: 10 hooks + 4 framework summaries + 5 proof lines + 5 objections
- 4 × keyword clusters (one per article, for GEO blogs in Pass 2)

**Voice rules are non-negotiable.** Apply spec §5 + buyer Voice Parameter Block. Auto-reject any draft containing banned words.

Before moving to Pass 2, run `article_filter` on each pillar article. If score < 8/10, regenerate ONCE. Second failure: flag for user review, do not silently re-output.

## 5. Run Pass 2 — Derivatives

Generate ALL derivative assets from the Pass 1 foundation. Schema: `nexus_wow_option_a.py:761-920`. Asset count is exact per spec §3.2 — under- or over-delivering is a fail.

Produce in one response (or chunked across responses if length-limited):
- 4 carousels (8 slides each + Gamma prompt + wrapper post for A & B)
- 2 infographics (4-section + red-flag + Gamma prompt + image tags + wrapper post for A & B)
- 16 LinkedIn posts (4 per article, escalating CTA strength per spec)
- 16 video scripts (4 per article, 45–75s / ≤180 words)
- 6 GEO blogs (A1, A2, B1, B2, C1, D1 — answer capsule + body + 4 FAQs + schema flags)
- 1 long-form lead magnet Gamma prompt
- Posting schedule (fortnight-by-fortnight)

Every derivative must be **derived from the foundation** — not invented independently. If you find yourself writing copy that doesn't trace back to a hook / framework / proof / objection from Pass 1, stop and re-anchor.

Run the matching filter from spec §6 on each asset type. Auto-regen on score < 8/10, one retry max.

## 6. Render HTML lead magnets (Pass 3 — replaces the Python Jinja2+Playwright lane)

For each of the 4 HTML LMs in spec §3.3:

1. **Fetch the canonical template** as a structural reference:
   - Diagnostic: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/lm_templates/type_lm_diagnostic.html *(if not present, fall back to: NEXUS MKII local path is canonical — request from user)*
   - Framework: same path, `type_lm_framework.html`
   - Infographic: same path, `type_infographic_audit.html`

2. **Write the populated HTML directly** — no Jinja2 tokens, no `{{ brand.palette.primary }}` syntax surviving. Every CSS custom property carries the literal buyer hex; every text content carries the literal copy.

3. **Render contract** (from spec §3.3):
   - Self-contained `<style>` block, no external CSS files
   - Google Fonts via `<link>` for buyer display + body families
   - A4 print-ready `@page` rules + page-break-inside-avoid on structural blocks
   - Image-free by design (Gamma carries the visual variants)
   - Every `{{ token }}` and `{BRACKET}` resolved — none surviving

4. **Save each HTML to Drive** via the Google Drive MCP into the buyer delivery folder (spec §7).

The user will run the HTML files through their own PDF converter — your job stops at clean HTML on Drive.

## 7. Generate visual assets via Gamma MCP

For each of:
- 4 carousels (Gamma prompts from Pass 2)
- 2 infographics (Gamma prompts from Pass 2)
- 1 long-form lead magnet (Gamma prompt from Pass 2)

Call the Gamma MCP `generate` tool. Use the **exact** Gamma prompt emitted in Pass 2 — do not "improve" or modify it at generation time. Tweaks during generation are how drift creeps in.

If the buyer has a brand-aligned Gamma theme, pass it as `themeName`. Otherwise omit (Gamma defaults are fine for first generation; user can re-theme in the Gamma editor).

Collect the resulting Gamma URLs into a `gamma_links.txt` (spec §7) and save to the Drive delivery folder.

## 8. Assemble the master .docx (or its Drive-native equivalent)

Create a single Google Doc in the buyer delivery folder titled `WOW_OptionA_ContentPack_<Buyer>_v1`. Structure:

1. Brand Context Brief (Pass 1 output)
2. Spine
3. Posting Schedule (so the buyer sees the cadence first)
4. Pillar Article A → Carousel A copy + Gamma prompt + wrapper post → Posts A1–A4 → Videos A1–A4 → GEO Blogs A1+A2
5. (Repeat structure for B, C, D — except C has 1 GEO blog, D has 1)
6. Infographic A copy + Gamma prompt + wrapper post · Infographic B same
7. Long-form Lead Magnet Gamma prompt
8. Lead Magnet HTML reference (link to the two HTML files in Drive)

Use Google Docs heading styles (H1 for article sections, H2 for derivative groups) so the buyer can navigate via the outline pane.

## 9. Write 00_START_HERE.txt + share the folder

Create a plain text `00_START_HERE.txt` in the delivery folder containing:
- What the pack contains (asset roster summary)
- Recommended publishing order (point at the posting schedule)
- How to use the Gamma prompts (link to each generated Gamma)
- How to use the HTML lead magnets (open in browser → print to PDF / convert)
- Contact for questions: chris@nowgroup.co.nz

Set Drive folder share permissions: link-view for the buyer's email, Chris as owner.

## 10. Return the delivery summary

End the build with a single summary message containing:
- Drive folder URL
- Asset count check (e.g., `4 articles · 4 carousels · 2 infographics · 16 posts · 16 videos · 4 wrappers · 6 GEO blogs · 1 long-form LM · 4 HTML LMs · 7 Gamma URLs · 1 master doc`)
- Any filters that failed twice + flagged for user review
- Any missing inputs that were substituted with spec defaults

## NOW Group conventions (carry into every artefact)

- **All fees**: NZD excl GST · 7-day payment terms
- **Voice / brand**: buyer brand (`force_now_palette=False`) for every client-facing artefact; NOW voice only in internal `00_START_HERE.txt` framing
- **Primary contact**: chris@nowgroup.co.nz
- **No NOW Group palette bleed** — if you find yourself reaching for NOW orange or NOW typography on a client-facing asset, stop and re-check the buyer brand block

## What this skill must not do

- Do not skip the spec fetch in step 1 — it is the single source of truth
- Do not fabricate buyer context (palette, voice, ICP) — ask for what is missing
- Do not invent derivatives that don't trace back to Pass 1 foundation
- Do not modify Gamma prompts at generation time (write once in Pass 2, run as-is)
- Do not leave `{{ template_tokens }}` or `{BRACKETS}` in any HTML output
- Do not silently re-output a filter-failed asset twice — flag for user review on second failure
- Do not deliver a partial pack — if any step blocks, surface it and pause

## Refinement / regeneration mode

If the user invokes you on an existing pack ("regenerate Carousel B for John BAA", "the LM diagnostic needs a tighter Spine"), skip steps 4–9 and operate only on the named asset. Re-anchor to the existing Pass 1 foundation (ask the user for it if not in thread). Re-run the matching filter before returning.

## Audit mode

If the user asks to audit an existing pack against the spec, score each asset section against the relevant filter + spec §3 deliverable rules. Format: `<asset> ✅/⚠️/❌ — <evidence>`. Bullet the gaps; do not silently rewrite.

## Spec-improvement mode

If during the work you notice the spec is unclear, contradictory, or has a gap, surface it inline:

> **[SPEC GAP]** §X.Y says A but the build needs B. Recommend updating spec to clarify <one-line proposal>.

If the user accepts the proposal, output the full updated `build-a.md` ready to paste into the repo (frontmatter + body), with `spec_version` bumped and `last_updated` set to today.

## Stay in-build

Build A is **Tier 2 · Content Pack Pro**. If the user asks for something clearly in another build:
- LinkedIn outreach / appointment-setting → `dna-x-gx-1`
- Partner Growth (Build B), Email Rescue (Build C), Quiz Funnel (Build D), GEO+SEO Authority (Build E), BizCard (Build F) — tell the user to use the matching skill, don't try to cover from this one
