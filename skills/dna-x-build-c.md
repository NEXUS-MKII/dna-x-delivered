---
name: dna-x-build-c
description: Run a Partner Growth Specialist build (Tier 1 · Option C) for a NOW Group buyer using Claude.ai connectors (Gamma, Google Drive). Use when the user mentions Partner Growth Specialist, Partner Pack, Option C, WOW Option C, "build a partner pack", "run partner growth for [buyer]", or wants to refine / audit / regenerate any asset in an existing partner pack. Trigger on phrases like "let's build [buyer]'s partner system", "ship Option C for [buyer]", or "regenerate the partner landing page for [buyer]" — even without the explicit Option C label.
---

# DNA-X · Partner Growth Specialist (Tier 1 · Option C)

You are running Partner Growth Specialist for a NOW Group buyer in Claude.ai. This is a **Tier 1 one-shot delivery build** — you produce the full partner activation system in one session and deliver it. Different audience to Build A (Content Pack Pro): Build A reaches the buyer's *clients*; Build C reaches the buyer's *partners* (other businesses, referral sources, complementary practitioners).

The thread should already contain the buyer's brand, voice, and ICP context. Your job: take that context, generate the full partner pack (landing page + 7 emails + 3 bios + partnership doc + ADD ONE lead magnet + Gamma generation), and deliver it to the buyer's Drive folder.

Follow this operating loop. Do not skip steps. Do not reorder.

---

## 1. Confirm buyer + partner context is loaded (one-shot triage)

Verify the thread contains everything below. If anything is missing, ask for the missing items as a **single grouped request**. Do not fabricate. Do not infer from training data.

### Required
- Buyer name + business name + role + sector + location
- Website + LinkedIn URL
- Primary audience (who the buyer's clients are — the partner will refer THESE people)
- Voice sample: written content excerpt OR transcript (~1500 chars)
- Brand palette: primary, secondary, accent, cta (hex codes)
- Brand fonts: display + body (Google Fonts family names)
- Buyer email (for Drive share)

### Strongly recommended — use directly if provided, derive from ICP if not
- **Hero tagline** with emphasis phrase highlighted (e.g. "You're already halfway a *buyer's agent*")
- **Reciprocal items list** — what the buyer offers in exchange for referrals
- **3 referral triggers** — scenarios where a partner should think of this buyer
- **4 differentiators** — what makes this partnership distinct
- **4 mutual commitments** — buyer's + partner's
- **Alignment Quiz URL** — the partner's first step

### Recommended (substitute defaults if missing — flag the substitution)
- Voice Parameter Block (banned words + signature move)
- Person photo URL · logo URL · primary domain
- Extended palette: ink, body, cream, mozzarella, rule, red-flag

Output before proceeding: `Buyer + partner context: ready` OR a grouped list of what's missing, in one message.

---

## 2. Asset roster — produce ALL of these, exact counts

Under- or over-delivering is a fail. The system architecture depends on this exact roster.

### 2.1 Partner landing page
- **1 `<slug>_partner.html`** — single self-contained file, see §5 for render contract

### 2.2 Partner Comms (master Google Doc — sections in publish order)
1. **Partner Onboarding overview** — the 4-step partnership flow + what the buyer does at each step
2. **Partnership Philosophy** — 3 paragraphs framing why referrals work in the buyer's voice
3. **3 Referral Triggers** — detailed scenarios with the trigger phrase + suggested conversation
4. **Internal Partner Management sequence** — buyer's CRM workflow: tag, task, follow-up cadence per partner stage
5. **ADD ONE Lead Magnet** — full asset content (4 sections + red-flag bar + Gamma prompt + recommended publishing format)
6. **Bio Library** — 3 formats: LinkedIn bio (~250 chars), Email signature (~120 chars), Spoken intro (~30 seconds when read aloud)
7. **Partnership Expectations Doc** — mutual commitments, 90-day success outcomes, escalation paths, communication cadence
8. **7-touch Email Templates** (see §2.3)

### 2.3 Email sequence (exactly 7 — Day-keyed)
| Day | Email | Purpose | CTA strength |
|---|---|---|---|
| 0 | Welcome | Partner signed up — set tone, link Alignment Quiz | Soft |
| 7 | Quiz follow-up | If completed: insights summary. If not: gentle re-prompt | Soft |
| 9 | PCD request | Ask for one high-value client scenario to anchor the relationship | Medium |
| 21A | Session booking (direct) | First joint client / intro call — direct CTA | Hard |
| 21B | Session booking (soft variant) | A/B for partners who didn't engage 21A | Medium |
| 30 | Referral log | Ask partner to log a referral attempt — successful or not | Medium |
| 60 | Re-engagement | Gentle restart with a new angle for stalled partners | Soft |

Each email: 120-300 words · subject line · 1 CTA · buyer's voice throughout.

### 2.4 ADD ONE lead magnet
- 1 complete asset: 4 sections + red-flag bar + intro + CTA
- 1 Gamma prompt for visual generation
- Format: diagnostic / self-assessment that the partner can hand to *their* client

### 2.5 Bundle
- **`Partner_Pack_<Buyer>_v1` Google Doc** — all 8 sections in publish order
- **`<slug>_partner.html`** — saved separately as raw HTML file on Drive
- **`00_START_HERE.txt`** — what's in the pack + how to deploy the landing page
- **`gamma_links.txt`** — the ADD ONE Gamma URL

---

## 3. Voice rules (non-negotiable)

Apply on every asset. Auto-reject any draft containing banned words.

- Plain English. Short sentences. No fluff.
- **Partnership-first framing**: "you'll send" / "you'll receive" — not "we offer" / "we provide"
- **Concrete commitments**: every commitment includes a timeframe or measurable signal (e.g. "We respond within 24 hours to any referral" not "We respond quickly")
- **Reciprocal energy**: equal weight on what the buyer GIVES and what the buyer GETS — never one-sided
- Universal banned: `synergy`, `leverage`, `paradigm`, `best-in-class`, `digital transformation`, `value-add`, `win-win`
- Plus the buyer's own banned-word list from their Voice Parameter Block (if present)

---

## 4. Quality gates — filter rubrics (fetch on demand)

These URLs are verified live. Fetch a rubric ONLY when about to score that asset type. Auto-regen on score < 8/10, one retry max. Second failure: flag for user review, do not silently re-output.

| Asset type | Rubric URL |
|---|---|
| Partner landing page HTML | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Page_Landing_Result_Scoring_Rubric.md |
| 7-email nurture sequence | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/EMBER_Universal_Filter.md |
| ADD ONE lead magnet copy | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Lead_Magnet_Scoring_Rubric.md |
| Bios + Partnership Expectations Doc | No rubric — structural correctness check (length caps, voice fingerprint, no banned phrases, paired commitments, measurable success criteria) |

Universal scorer rubric + per-buyer overlay from the buyer's Voice Parameter Block — never per-buyer-bespoke filter logic.

---

## 5. Partner landing page render contract

Write **fully populated HTML directly** — no template tokens, no `{{ }}` syntax surviving, no Jinja2 fragments. Every value resolved. Single self-contained `.html` ready to host (GitHub Pages, S3, Kajabi page, buyer's own server, anywhere).

### Required structure
- Self-contained `<style>` block in the `<head>` — no external CSS files
- Google Fonts loaded via `<link>` for the buyer's display + body families
- Responsive: mobile-first, breakpoints at 720px and 1080px
- Smooth-scroll on hash links
- Hero image slot reserved (use Gamma-generated if available, else skip cleanly)

### CSS custom properties (populate from buyer palette as literal hex values)
```
--primary       (buyer.palette.primary)
--secondary     (buyer.palette.secondary)
--accent        (buyer.palette.accent)
--cta           (buyer.palette.cta)
--ink           (default #0F172A)
--body          (default #374151)
--cream         (default #FAFAF9)
--mozzarella    (default #F5F5F4)
--rule          (default #E5E7EB)
--red-flag      (default #DC2626)
```

### Section stack (in order)
1. **Hero** — eyebrow micro-line (uppercase + letter-spacing) · tagline with emphasis phrase styled distinctly (italic + accent colour) · sub-headline · primary audience line
2. **Attention strip** — 4-step partnership flow as numbered cards in a 4-column grid (stacks on mobile). Default steps: "Alignment Quiz" · "Intro Call" · "First Referral" · "24h Response" (override if buyer's intake provides different)
3. **Reciprocal services list** — variable-length grid of what the buyer offers in exchange
4. **3 referral triggers** — each with icon (use emoji or simple SVG), title, situational description, suggested conversation phrase
5. **4 differentiators** — 2×2 grid with accent-bordered cards
6. **Pull quote** — large opening/closing quote glyphs, italics, attribution underneath — use a partner-perspective line if available, else the emphasis phrase from the hero tagline
7. **4 mutual commitments** — side-by-side "We commit to" / "You commit to" if pair-able, else 2×2 grid
8. **Quiz CTA** — prominent button linking to the Alignment Quiz URL + 4 small cover-preview cards beneath
9. **Practice card** — dark-backed footer card with buyer's intro (name + tagline), location, contact email or website, accent CTA
10. **Footer** — "Part of the NOW Group partnership ecosystem" line

### What must NOT remain in output
- No `{{ template_tokens }}` or `{BRACKETS}` or Jinja2 fragments
- No placeholder lorem ipsum
- No commented-out sections
- No external image references that haven't been resolved (Gamma URLs OK; broken `[PHOTO_URL]` not OK)

---

## 6. Visual asset via Gamma MCP

Build C uses Gamma for one asset: the **ADD ONE lead magnet visual**.

Call the Gamma MCP `generate` tool with the exact Gamma prompt produced in §2.4. **Do not "improve" or modify the prompt at generation time.** Tweaks during generation are how drift creeps in.

If the buyer has a brand-aligned Gamma theme, pass it as `themeName`. Otherwise omit (Gamma defaults are fine for first generation).

Collect the resulting Gamma URL into `gamma_links.txt` in the Drive delivery folder.

The partner landing page may optionally include a hero image — generate via Gamma if the buyer's brand wants it, or skip cleanly.

---

## 7. Delivery (Google Drive MCP)

Create folder: `NOW Group — Partner Pack Delivery / Partner Growth Specialist — <Buyer Name> — <YYYY-MM-DD>/`

Folder contents:
- `00_START_HERE.txt`
- `<slug>_partner.html` (the standalone landing page)
- `Partner_Pack_<Buyer>_v1` (Google Doc — see §8)
- `gamma_links.txt`

Share permissions: link-view enabled for the buyer's email; the operator (chris@nowgroup.co.nz by default) as owner.

---

## 8. The master Google Doc structure

Title: `Partner_Pack_<Buyer>_v1`. Use Google Docs heading styles (H1 / H2) so the outline pane navigates cleanly.

Order (publish-flow order, not build order):

1. Partner Onboarding overview
2. Partnership Philosophy
3. Referral Triggers (3)
4. Internal Partner Management sequence
5. ADD ONE Lead Magnet (full content + Gamma prompt + Gamma link from §6)
6. Bio Library (3 formats)
7. Partnership Expectations Doc
8. Email Templates (7 — Day 0 / 7 / 9 / 21A / 21B / 30 / 60 with subject lines + bodies)
9. Landing Page reference (link to the `.html` file in the same Drive folder)

---

## 9. 00_START_HERE.txt

Plain text. Contains:
- What's in the pack (asset count summary)
- **How to deploy the partner landing page** — three options:
  - Host on GitHub Pages (push the .html file)
  - Paste the HTML body into a Kajabi / Squarespace / Webflow page
  - Host on the buyer's own web server / S3 / Netlify
- How to send the 7-email sequence (load into the buyer's email tool — Kartra, Kajabi, ActiveCampaign, Mailchimp — as a 60-day sequence triggered when a partner completes the Alignment Quiz)
- How to use the Bio Library (LinkedIn About section, email signature, spoken intros at networking events)
- How to use the ADD ONE lead magnet (give to every partner — they hand it to THEIR clients)
- Contact for questions: chris@nowgroup.co.nz

---

## 10. Delivery summary (the closing message)

End the build with a single summary containing:
- Drive folder URL
- Asset count check: `1 landing page · 7 emails · 3 bios · 1 partnership doc · 1 ADD ONE asset (copy + Gamma) · 1 master doc · 1 deploy guide`
- Gamma URL for the ADD ONE asset
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

- Do not fabricate buyer context (palette, voice, ICP, reciprocal services) — ask for what is missing
- Do not invent partner referral triggers that don't trace back to the buyer's actual ICP — partners must recognise the trigger moments in their real client interactions
- Do not modify the Gamma prompt at generation time (write once in §2.4, run as-is)
- Do not leave `{{ template_tokens }}`, `{BRACKETS}`, or Jinja2 syntax in the HTML
- Do not silently re-output a filter-failed asset twice — flag for user review on second failure
- Do not deliver a partial pack — if any step blocks, surface it and pause
- Do not write partnership commitments without measurable signals — "we respond quickly" is a fail; "we respond within 24 hours" is the bar
- Do not reference any tier-orchestration file (this is a one-shot Tier 1 build, no orchestration layer)
- Do not push the landing page to any deployment surface — deployment is out of scope for the skill. Produce a clean .html file; the buyer / Chris deploys separately.

---

## Refinement / regeneration mode

If invoked on an existing pack ("regenerate the Day 21 emails for John BAA", "the Partnership Expectations doc needs a tighter cadence", "redo the landing page with Garth Lewis's new brand"), skip §§1–9 except for the named asset. Re-anchor to the existing context (ask for it if not in thread). Re-run the matching filter from §4 before returning.

## Audit mode

If asked to audit an existing pack, score each section against the matching rubric from §4 + the asset roster in §2. Format: `<asset> ✅/⚠️/❌ — <evidence>`. Bullet the gaps; do not silently rewrite.

## Stay in-build

This is **Build C / Option C / Partner Growth Specialist (Tier 1)**. If the user asks for:
- Content calendar for the buyer's own audience (Tier 1 Build A) → use `dna-x-build-a` skill
- LinkedIn outreach / appointment-setting (Tier 3) → use `dna-x-gx-1` skill
- Email rescue / sequence rewriting (Tier 1 Build B when shipped) → use the matching skill when available
- Tier 2 builds (D Quiz Funnel, E GEO+SEO, F BizCard) → use the matching skill when available

Don't try to cover other builds from this skill.
