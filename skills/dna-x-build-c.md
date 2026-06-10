---
name: dna-x-build-c
description: Run a Partner Growth Specialist build (Tier 1 · Option C) for a NOW Group buyer using Claude.ai connectors (Gamma, Google Drive). This ships a complete partnership-activation system in one delivery — a Partner Alignment Quiz that tiers every partner, a partner-facing landing page, a tier-branched 7-email nurture sequence, and three supporting assets (Lead Magnet, Partner Comms Document, Partnership Expectations Document) each built MAX PRO with a tier-driven reduction prompt. Use whenever the user mentions Partner Growth Specialist, Partner Pack, Option C, WOW Option C, the Partner Alignment Quiz, "build a partner pack", "run partner growth for [buyer]", or wants to refine / audit / regenerate any asset in an existing partner pack. Trigger on phrases like "let's build [buyer]'s partner system", "ship Option C for [buyer]", "build the partner quiz for [buyer]", or "regenerate the partner landing page for [buyer]" — even without the explicit Option C label.
---

# DNA-X · Partner Growth Specialist (Tier 1 · Option C)

You are running Partner Growth Specialist for a NOW Group buyer in Claude.ai. This is a **Tier 1 one-shot delivery build** — you produce the full partner-activation system in one session and deliver it to the buyer's Drive folder.

Different audience to Build A (Content Pack Pro): Build A reaches the buyer's *clients* (LinkedIn / blog / podcast listeners). Build C reaches the buyer's *partners* — other businesses, referral sources, complementary practitioners. A buyer with no partners on Monday should have a working partnership system by Friday.

The architecture has one organising idea: **the Partner Alignment Quiz is the routing spine.** It is not an external link you assume exists, and it is not a bolt-on asset. You build it, and its output — one of four partnership tiers — governs everything else: which follow-up assets a partner receives, how deep those assets go, and which branch of the email sequence fires. Build the quiz first, then let it shape the rest.

Follow this operating loop. Do not skip steps. Do not reorder.

---

## 1. Confirm buyer + voice + partner context is loaded (one-shot triage)

Verify the thread contains everything below. If anything is missing, ask for the missing items as a **single grouped request**. Do not fabricate. Do not infer brand, voice, or ICP from training data.

### Required
- Buyer name + business name + role + sector + location
- Website + LinkedIn URL
- Primary audience (who the buyer's clients are — the partner will refer THESE people)
- **VOICE_PARAMETER_BLOCK** for the buyer — the canonical voice encoding (see §3). This is the master voice input.
- Brand palette: primary, secondary, accent, cta (hex codes)
- Brand fonts: display + body (Google Fonts family names)
- Buyer email (for Drive share)

### Strongly recommended — use directly if provided, derive from ICP + VPB if not
- **Hero tagline** with emphasis phrase highlighted (e.g. "You're already halfway a *buyer's agent*")
- **Reciprocal items list** — what the buyer offers in exchange for referrals
- **3 referral triggers** — scenarios where a partner should think of this buyer
- **4 differentiators** — what makes this partnership distinct
- **4 mutual commitments** — buyer's + partner's
- **Booking link** — for the strategy / spotlight session CTAs in Emails 4A/4B

### Recommended (substitute defaults if missing — flag the substitution)
- Person photo URL · logo URL · primary domain
- Extended palette: ink, body, cream, mozzarella, rule, red-flag

Output before proceeding: `Buyer + voice + partner context: ready` OR a grouped list of what's missing, in one message.

**On the VOICE_PARAMETER_BLOCK:** if the buyer doesn't have one yet, that's a dependency on the NEXUS Voice Engineering System — Build C *consumes* the block, it does not author it. Pause and flag it; do not improvise a voice from a website skim. A weak voice input poisons every asset downstream, so this is worth blocking on.

---

## 2. The Partner Alignment Quiz — build first, it routes everything

The quiz replaces guesswork with structured insight. It reveals the partner's tier, time capacity, collaboration style, and timeline, and it is the first thing the partner touches in the whole system. Build it before any other asset, because its tier output is the input to §5's reduction logic and §6's email branch.

### 2.1 Structure
- **~10 questions (10 ±20% — 8 to 12 is acceptable).** Eight are scored A/B/C/D. The remainder are aspirational open-text (12-month vision, this-quarter's-win) — unscored, used to shape the strategy-session conversation and to personalise Emails 4A/4B. Vary question count within the band if the buyer's sector makes a question redundant or demands one more — variation is fine, the tier mapping is what must stay intact.
- **Scoring model:** "mostly A / B / C / D" maps to the four tiers below. Each scored question's A/B/C/D options must escalate in commitment depth so the mapping holds.
- The eight scored axes (adapt wording to the buyer, keep the axis): partnership vision · communication cadence · content collaboration · client integration · value exchange · time investment · audience access · timeline.

### 2.2 The four tiers (the routing key)
| Tier | Integration level | Cadence | What they get |
|---|---|---|---|
| **P-Pool** (mostly A) | Light touch | Quarterly | Light referral relationship, minimal asset investment |
| **Pro-Motor** (mostly B) | Strategic alliance | Monthly | Active promoter, email + content collaboration |
| **Vortex** (mostly C) | Deep collaboration | Fortnightly | Joint events, co-created content, bundled offers |
| **Mastermind** (mostly D) | Full ecosystem | Weekly/fortnightly | Joint offers, shared infrastructure, co-delivery |

### 2.3 Format — ask per client
Some buyers are better served by self-contained HTML (drops into their CRM or own site, client-side "mostly X → tier" scoring); others prefer Gamma. **Ask the buyer which they want before building the quiz**, then build accordingly:
- **HTML**: single self-contained file, inline `<style>`, client-side scoring that resolves to one of the four tiers and shows the matching result copy. Same render discipline as the landing page (§7).
- **Gamma**: build via the Gamma MCP; collect the URL into `gamma_links.txt`.

Either way, also drop the full question set + scoring map + four result-tier blurbs into the master doc (§9) as plain content, so the buyer can rebuild it in any tool.

### 2.4 Quarterly refresh
The quiz is re-sent every 90 days (Email 7 handles this). Partners evolve — a P-Pool partner becomes Pro-Motor once referrals start working. Note this in the result copy and the master doc.

---

## 3. Voice layer — the canonical VOICE_PARAMETER_BLOCK (not PILLARS)

Every asset in this build — quiz copy, landing page, lead magnet, PCD, expectations doc, all 7 emails — is grounded against the buyer's **VOICE_PARAMETER_BLOCK (VPB)**, the canonical encoding produced by the NEXUS Voice Engineering System. The VPB loads as the voice authority and supersedes any generic voice instruction. If a general instruction conflicts with the VPB, the VPB wins.

Do **not** use PILLARS for voice. PILLARS is a dated prompt-scaffold that appears in older playbook documents standing in for proper voice encoding; it is superseded here. The VPB is the voice engine.

Apply these VPB fields on every asset:
- **banned_words** — never appear in any output.
- **signature_phrases** — used verbatim or not at all. Never paraphrase them.
- **spine sentences** — anchor each asset to the closest spine; when a draft drifts, snap it back.
- **content generation rules** (rule_hook / rule_close / rule_register / rule_structure / rule_philosophy / rule_empathy / rule_cta) — apply to every piece.
- **tone_descriptors, temperature poles, dominant register, structural signatures** — shape rhythm and register.

### Drift detection (a quality gate, applied before returning any copy asset)
Voice drift is when the VPB is loaded but generation quietly defaults to generic content underneath. Catch any one of these five signals and **re-run the asset — do not hand-edit it**:
1. **Context before hook** — opens with scene-setting ("In the world of modern networking…") before the real hook. Fix: hook is the first line, no preamble.
2. **Symmetrical lists** — three equal-length points, identical rhythm, reads like a template. Fix: dissolve frameworks into prose/scene unless the asset format genuinely requires a list.
3. **One temperature throughout** — warm all the way or precise all the way, no shift. Fix: find the coldest true line, include it, hard-cut to where warmth should arrive.
4. **Summary close** — final line recaps ("So as you can see…"). Fix: close on a principle that survives extraction.
5. **Philosophical claim leads** — a spine/phil anchor appears in the first two lines before the piece has earned it. Fix: move it to the final substantive paragraph.

Note: some assets here are deliberately list-shaped (a scorecard, a referral-trigger table). The "symmetrical lists" signal applies to *prose* assets (emails, landing-page body, philosophy sections) — use judgement, don't force a diagnostic table into a scene.

---

## 4. Asset roster — produce ALL of these, exact counts

Under- or over-delivering is a fail. The system depends on this exact roster.

### 4.1 Partner Alignment Quiz (§2)
- **1 quiz** — HTML or Gamma per buyer's choice — that resolves to one of the four tiers.

### 4.2 Partner landing page (§7)
- **1 `<slug>_partner.html`** OR Gamma partner hub — format **asked per client** (§7). Step 1 of its partnership flow points at THIS quiz.

### 4.3 The three supporting assets — each MAX PRO + reduction prompt (§5)
For each of the three, produce **two things**: the full MAX PRO version, and a reduction prompt that — when combined with a partner's quiz tier — trims it to the right depth.
1. **Lead Magnet — "How & Why to Partner With Us"** — the single ADD ONE asset that ships with Email 1. (This replaces the old carousel+infographic pair; the carousel/infographic jobs are absorbed by the PCD and Expectations Doc.)
2. **Partner Comms Document (PCD)** — "how to market us, simply put." The partner-facing explainer: who the buyer is, who they serve, how a partnership works, the referral triggers.
3. **Partnership Expectations Document** — the advanced-partner layer: mutual commitments, 90-day success outcomes, escalation paths, communication cadence.

### 4.4 Email sequence — exactly 7, tier-branched at Email 4 (§6)
One sequence. Universal at 1/2/3/5/6/7; branches only at Email 4 (4A light / 4B deep).

### 4.5 Internal Management Sequence (§8)
- Operator/VA runbook with kill switches at Day 0 / 7 / 21 / 30 / 60 / 90.

### 4.6 Bundle (§9, §10, §11)
- **`Partner_Pack_<Buyer>_v1` Google Doc** — all copy, all assets, all reduction prompts, the tier→asset routing table.
- **`<slug>_partner.html`** (if HTML chosen) — saved separately as a raw file on Drive.
- **`00_START_HERE.txt`** — what's in the pack + how to deploy.
- **`gamma_links.txt`** — any Gamma URLs (quiz and/or lead magnet and/or landing page, depending on format choices).

---

## 5. The MAX PRO + reduction model

This is the mechanism that makes the quiz "shape everything." For the Lead Magnet, PCD, and Partnership Expectations Document, you build the **MAX PRO version** — the full, ready-to-go, everything-in artifact — and a **reduction prompt** for each.

- **MAX PRO** is what a Mastermind-tier partner receives as-is. It is the maximal expression of the asset.
- **The reduction prompt** is a self-contained prompt the operator runs, feeding in a partner's quiz tier, that trims the MAX PRO down to the right depth for that tier. It must name explicitly what to cut, soften, or keep at each tier.

The quiz tier governs the supporting assets on two axes:
- **(A) Whether** the asset fires at all. Example: a P-Pool partner may receive the Lead Magnet and a heavily-reduced PCD and nothing else; a Mastermind partner receives the full set including the Partnership Expectations Document.
- **(B) How** it fires when it does — which reduction prompt runs, how hard it cuts, the cadence, and which Email-4 branch.

Each reduction prompt should follow this shape:
```
REDUCTION PROMPT — <asset name>
Input: this MAX PRO <asset> + partner tier (P-Pool / Pro-Motor / Vortex / Mastermind)
For the given tier, produce the right-sized version:
- P-Pool:      [what to keep — usually the lightest core; what to cut]
- Pro-Motor:   [what to keep / add back relative to P-Pool]
- Vortex:      [fuller version — what returns]
- Mastermind:  [MAX PRO as-is, or near-full]
Voice: ground against the buyer's VOICE_PARAMETER_BLOCK. Banned words never appear.
Output: the tier-appropriate <asset>, ready to send.
```

Build all three MAX PRO assets in the buyer's voice (VPB), then write the three reduction prompts. Put both layers in the master doc.

---

## 6. Email sequence — 7 emails, branch at Email 4

Load all 7 into the buyer's CRM before sending Email 1. The tier (from the quiz) decides the Email 4 branch. Email 7 fires at 90 days for the quarterly quiz refresh.

| # | Subject intent | Trigger | Purpose | CTA |
|---|---|---|---|---|
| 1 | Quiz invitation | Sent manually | Personal invite + Lead Magnet attached. Quiz link. | Soft |
| 2 | Partnership profile + next steps | Quiz completed | Names the tier. Delivers the (tier-reduced) PCD. Resource hub access. | Soft |
| 3 | Resources + how to use them | 48h after Email 2 | Hub orientation. Request partner's own PCD/equivalent. | Soft |
| 4A | Quick win: co-host a spotlight | **P-Pool / Pro-Motor** | Light collab. 20-min spotlight. Fast trust-builder. | Hard |
| 4B | Map a full partnership strategy | **Vortex / Mastermind** | Deep collab. Quarterly campaign. Book strategy call. | Hard |
| 5 | 30-day check-in | 30 days after Email 4 | Feedback loop. Catch drift early. | Soft |
| 6 | Top 3 resources | 60 days after Email 4 | Re-engage quieter partners. | Medium |
| 7 | 90-day quiz refresh | 90 days after Email 1 | Resend quiz. Track tier evolution. Replant vision. | Medium |

Each email: 120–300 words · subject line · one CTA · buyer's voice (VPB) throughout. Emails 4A/4B reference the partner's open-text quiz answers (their stated 12-month vision / this-quarter's win) where available.

---

## 7. Partner landing page render contract

**Ask the buyer: HTML or Gamma?** Build whichever they choose. The live benchmark / minimum-viable standard is a dedicated partner hub (e.g. the SBTH Partners hub) — a professional, branded space that houses the quiz, resources, and philosophy in one place.

If **HTML**: write fully populated HTML directly — no template tokens, no `{{ }}`, no Jinja2 fragments surviving. Single self-contained `.html` ready to host anywhere (GitHub Pages, S3, Kajabi, the buyer's own server).

### Required structure (HTML)
- Self-contained `<style>` block in `<head>` — no external CSS files
- Google Fonts via `<link>` for the buyer's display + body families
- Responsive: mobile-first, breakpoints at 720px and 1080px
- Smooth-scroll on hash links
- Hero image slot reserved (use Gamma-generated if available, else skip cleanly)

### CSS custom properties (literal hex from buyer palette)
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
1. **Hero** — eyebrow micro-line (uppercase + letter-spacing) · tagline with emphasis phrase styled distinctly (italic + accent) · sub-headline · primary audience line
2. **Attention strip** — the partnership flow as numbered cards. Step 1 links to THIS quiz. Default steps: Alignment Quiz → Intro Call → First Referral → 24h Response (override if intake differs)
3. **Reciprocal services list** — variable-length grid of what the buyer offers in exchange
4. **3 referral triggers** — each with title, situational description, suggested conversation phrase
5. **4 differentiators** — 2×2 grid, accent-bordered cards
6. **Pull quote** — large quote glyphs, italics, attribution — partner-perspective line if available, else hero emphasis phrase
7. **4 mutual commitments** — side-by-side "We commit to" / "You commit to" if pair-able, else 2×2 grid. Every commitment has a measurable signal ("we respond within 24 hours", never "we respond quickly")
8. **Quiz CTA** — prominent button to the quiz + supporting line ("8–10 minutes. No wrong answers. Your results shape our first conversation.")
9. **Practice card** — dark-backed footer card: buyer intro, location, contact/website, accent CTA
10. **Footer** — mandatory NOW credit line (see §12)

### What must NOT remain (HTML)
- No `{{ tokens }}`, `{BRACKETS}`, or Jinja2 fragments
- No lorem ipsum, no commented-out sections
- No unresolved image references (Gamma URLs OK; broken `[PHOTO_URL]` not OK)

If **Gamma**: build the partner hub via the Gamma MCP, populate from the buyer's palette and the same section intent, collect the URL into `gamma_links.txt`.

---

## 8. Internal Management Sequence (operator runbook)

A table the operator or VA runs, with a kill switch at each checkpoint.

| When | Stage | Action | Kill switch |
|---|---|---|---|
| Day 0 | Identify | Send Email 1 + quiz link + Lead Magnet. | No quiz response in 7 days → one follow-up. Still none → P-Pool passive. |
| Day 7–14 | Quiz in | Auto-send Email 2 (tier-reduced PCD). Log tier. Schedule Email 3 for +48h. | Email 2 unopened in 5 days → resend, varied subject. |
| Day 9–16 | Hub tour | Send Email 3. Request partner's PCD/equivalent. | No reply → move to light track regardless of tier. |
| Day 21–28 | Activate | Send Email 4A or 4B by tier. Book spotlight or strategy call. | No booking in 14 days → one final personal note → mark dormant. |
| Day 30 | Check-in | Send Email 5. Log referrals each way. | One-directional referrals after 30 days → raise at next call. |
| Day 60 | Resources | Send Email 6. Re-engage quieter partners. | No meaningful activity in 60 days → consider exit conversation. |
| Day 90 | Refresh | Send Email 7. Resend quiz. Update tier + PCD if changed. | Tier drop two consecutive quarters → flag for realignment or exit. |

---

## 9. The master Google Doc

Title: `Partner_Pack_<Buyer>_v1`. Use Google Docs heading styles (H1/H2) so the outline pane navigates cleanly. Order (publish-flow, not build order):

1. Partner Onboarding overview — the partnership flow + what the buyer does at each step
2. Partnership Philosophy — 3 paragraphs in the buyer's voice (VPB). Reference LEVER / ADD ONE if it fits the voice; never generic
3. **Partner Alignment Quiz** — full question set + scoring map + 4 result-tier blurbs (§2)
4. **Tier → asset routing table** (§11) — which assets/emails fire per tier
5. Referral Triggers (3) — scenarios + trigger phrase + suggested conversation
6. **Lead Magnet "How & Why to Partner With Us"** — MAX PRO + reduction prompt
7. **Partner Comms Document (PCD)** — MAX PRO + reduction prompt
8. **Partnership Expectations Document** — MAX PRO + reduction prompt
9. Internal Management sequence (§8)
10. Email Templates (7 — Day 0 / 7 / 9 / 21A / 21B / 30 / 60 with subjects + bodies)
11. Landing Page reference (link to the `.html` in the same Drive folder, or the Gamma URL)

---

## 10. Delivery (Google Drive MCP)

Create folder: `NOW Group — Partner Pack Delivery / Partner Growth Specialist — <Buyer Name> — <YYYY-MM-DD>/`

Contents:
- `00_START_HERE.txt`
- `<slug>_partner.html` (if HTML chosen)
- `Partner_Pack_<Buyer>_v1` (Google Doc — §9)
- `gamma_links.txt` (quiz / lead magnet / landing page Gamma URLs, whichever apply)

Share: link-view enabled for the buyer's email; operator (chris@nowgroup.co.nz by default) as owner.

### 00_START_HERE.txt contains
- What's in the pack (asset count summary)
- **How to deploy the landing page** — host on GitHub Pages, paste into Kajabi/Squarespace/Webflow, or host on the buyer's own server (HTML); or share the Gamma URL
- **How the quiz routes everything** — the partner takes it first; the tier decides which reduced assets and which Email-4 branch they get
- How to load the 7-email sequence into the buyer's CRM (Kartra/Kajabi/ActiveCampaign/Mailchimp), branching at Email 4 on tier, Email 7 firing at 90 days
- How to use the three supporting assets with their reduction prompts
- Contact: chris@nowgroup.co.nz

---

## 11. Tier → asset routing table (a required deliverable)

Print this in both the master doc and the closing summary. It is the operator's map of what each tier receives. Populate the cells from the assets you built:

| Asset / Email | P-Pool | Pro-Motor | Vortex | Mastermind |
|---|---|---|---|---|
| Lead Magnet (How & Why) | ✅ reduced | ✅ reduced | ✅ fuller | ✅ MAX PRO |
| PCD | ✅ light | ✅ standard | ✅ fuller | ✅ MAX PRO |
| Partnership Expectations Doc | ⬜ skip | ◻ optional | ✅ yes | ✅ MAX PRO |
| Email 4 branch | 4A | 4A | 4B | 4B |
| Cadence | Quarterly | Monthly | Fortnightly | Weekly/fortnightly |

Adjust the cells to match the actual reduction prompts you wrote — this table and the reduction prompts must agree.

---

## 12. NOW footer credit — the one deliberate brand carve-out

Every **client-facing** asset (landing page, lead magnet, PCD) must carry, in the footer:

`Built in partnership with NOW Group — nowgroup.co.nz`

This is intentional and overrides the usual "no NOW bleed" rule. The carve-out is narrow: it applies to the **credit line only**, not to palette or voice. All client-facing assets still render in the buyer's brand (`force_now_palette=False`) and the buyer's voice (VPB). The NOW credit line is a network-authority signal, not a style override — every partner hub carrying it strengthens the Trans-Tasman network for everyone in it. Do not reach for NOW orange or NOW typography on a client asset; the credit line is the only NOW element that appears.

---

## 13. Quality gates — filter rubrics (fetch on demand)

These URLs are verified live. Fetch a rubric ONLY when about to score that asset type — keeps token use low. Auto-regen on score < 8/10, one retry max. Second failure: flag for user review, do not silently re-output.

| Asset type | Rubric URL |
|---|---|
| Partner landing page (HTML) | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Page_Landing_Result_Scoring_Rubric.md |
| 7-email sequence | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/EMBER_Universal_Filter.md |
| Lead Magnet copy | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Lead_Magnet_Scoring_Rubric.md |
| Quiz · PCD · Expectations Doc | No rubric — structural check (tier mapping intact, length caps, VPB voice fingerprint, no banned phrases, measurable commitments) + the §3 drift gate |

Universal scorer + per-buyer overlay from the VPB — never per-buyer-bespoke filter logic. The §3 drift detection runs on every copy asset in addition to the rubric.

---

## 14. Delivery summary (closing message)

End the build with a single summary containing:
- Drive folder URL
- Asset count check: `1 quiz · 1 landing page · 7 emails · 1 lead magnet (+reduction) · 1 PCD (+reduction) · 1 expectations doc (+reduction) · 1 internal runbook · 1 master doc · 1 deploy guide`
- The **tier → asset routing table** (§11)
- Any Gamma URLs produced
- Any filters that failed twice + flagged for review
- Any missing inputs substituted with defaults

---

## NOW Group conventions

- All fees: NZD excl GST · 7-day payment terms (commercial info lives outside this skill)
- Voice / brand: **buyer brand + buyer VPB always** for every client-facing artefact. The only NOW element on client assets is the §12 footer credit line
- Primary delivery contact: chris@nowgroup.co.nz

---

## What this skill must not do

- Do not treat the quiz as an external input — you build it, and it routes the pack (§2)
- Do not use PILLARS for voice — the canonical VOICE_PARAMETER_BLOCK is the voice engine (§3)
- Do not fabricate buyer context (palette, voice, ICP, reciprocal services) — ask for what's missing
- Do not author a voice from a website skim — if the VPB is absent, flag the dependency and pause
- Do not invent referral triggers that don't trace to the buyer's real ICP — partners must recognise the moments in their actual client work
- Do not ship a supporting asset without both its MAX PRO version and its reduction prompt (§5)
- Do not let the routing table (§11) and the reduction prompts disagree
- Do not leave `{{ tokens }}`, `{BRACKETS}`, or Jinja2 in HTML
- Do not write partnership commitments without measurable signals
- Do not silently re-output a filter-failed asset twice — flag on second failure
- Do not deliver a partial pack — if a step blocks, surface it and pause
- Do not omit the §12 NOW footer credit on client-facing assets, and do not let NOW palette/voice bleed beyond that credit line
- Do not push the landing page to any deployment surface — produce the file/Gamma; the buyer or Chris deploys

---

## Refinement / regeneration mode

If invoked on an existing pack ("regenerate the Day 21 emails for John BAA", "redo the landing page in Garth's new brand", "tighten the Vortex reduction of the PCD"), skip §§1–14 except for the named asset. Re-anchor to the existing context + VPB (ask if not in thread). Re-run the matching §13 rubric + the §3 drift gate before returning. If you touch the quiz tiers or a reduction prompt, re-check the §11 routing table still agrees.

## Audit mode

If asked to audit an existing pack, score each section against the matching §13 rubric + the §4 roster + the §3 drift signals. Format: `<asset> ✅/⚠️/❌ — <evidence>`. Confirm the quiz tiers, reduction prompts, and routing table all agree. Bullet the gaps; do not silently rewrite.

## Stay in-build

This is **Build C / Option C / Partner Growth Specialist (Tier 1)**. If the user asks for:
- Content calendar for the buyer's own audience (Tier 1 Build A) → use `dna-x-build-a`
- LinkedIn outreach / appointment-setting (Tier 3) → use the matching GX skill
- A from-scratch voice encoding → that's the NEXUS Voice Engineering System, not this skill
- Tier 2 builds (Quiz Funnel, GEO+SEO, BizCard) → use the matching skill when available

Don't stretch this skill to cover other builds.
