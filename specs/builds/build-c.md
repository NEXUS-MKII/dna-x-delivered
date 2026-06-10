---
spec_version: 2.0
last_updated: 2026-06-09
build_letter: C
build_name: Partner Growth Specialist
tier: 1
tagline: A quiz-routed partnership system in one delivery — every partner tiered, every asset reduced to fit
status: live
source: nexus_wow_option_c.py (Python pipeline, needs alignment refactor — see specs/builds/build-c-python-alignment.md)
references:
  - specs/_shared/build-standards.md
  - skills/dna-x-build-c.md (Claude.ai expression)
  - https://raw.githubusercontent.com/NEXUS-MKII/nowgroup-skills/main/sources/voice/NOW_Voice_Parameter_System.md (voice authority dependency)
---

# Option C — Partner Growth Specialist (Tier 1) · v2.0

> A complete partnership-activation system for one buyer in a single delivery. Built around one organising idea: **the Partner Alignment Quiz is the routing spine.** Every partner takes it, the quiz output tiers them into one of four levels (P-Pool / Pro-Motor / Vortex / Mastermind), and that tier governs which assets they receive, how deep those assets go, and which branch of the email sequence fires.
>
> Different audience to Build A (Content Pack Pro). Build A reaches the buyer's **clients**; Build C reaches the buyer's **partners** — other businesses, referral sources, complementary practitioners. A buyer with no partners on Monday should have a working partnership system by Friday.
>
> Tier 1 one-shot delivery build. Mandatory adherence to `specs/_shared/build-standards.md` (VPB dependency · drift detection · NOW footer · MAX PRO + reduction · format ask · routing tables · internal management sequence with kill switches).

---

## 1 · Intent

The fragility most consultants face with referral partnerships: they treat every partner the same. The high-intent Mastermind-tier partner gets the same generic onboarding as the casual P-Pool referrer, so the Mastermind feels under-served and the P-Pool feels overwhelmed. Both disengage.

Build C fixes that with one mechanism — the **Partner Alignment Quiz**. Every partner answers ~10 questions before they touch the rest of the system. Their answers tier them. The tier routes everything downstream: which assets they receive, at what depth, on what cadence, with which email branch firing on Day 21.

The deliverable is a complete partnership-activation system, not just a set of files. The buyer ships partners through it on day one.

---

## 2 · Commercial structure

- **Setup**: same one-off Tier 1 fee as Builds A/B · ~14-day turnaround
- **No ongoing** — pack is a finite deliverable; buyer can re-engage for partnership refresh
- **Commercial terms** — NZD excl GST · 7-day payment terms (NOW Group standard)

---

## 3 · The Partner Alignment Quiz (the routing spine)

The quiz is built **first**, before any other asset, because its tier output is the input to §6's MAX PRO + reduction logic and §7's email branch.

### 3.1 Structure
- **~10 questions** (10 ±20% — 8 to 12 acceptable). Eight scored A/B/C/D; the remainder open-text aspirational (12-month vision, this-quarter's win) — unscored, used to shape the strategy-session conversation and personalise Emails 4A/4B
- **Scoring model**: "mostly A / B / C / D" → maps to the four tiers below. Each scored question's A/B/C/D options must escalate in commitment depth so the mapping holds
- **The eight scored axes** (adapt wording per buyer, keep the axis): partnership vision · communication cadence · content collaboration · client integration · value exchange · time investment · audience access · timeline

### 3.2 The four tiers (routing key)

| Tier | Integration level | Cadence | What they get |
|---|---|---|---|
| **P-Pool** (mostly A) | Light touch | Quarterly | Light referral relationship, minimal asset investment |
| **Pro-Motor** (mostly B) | Strategic alliance | Monthly | Active promoter, email + content collaboration |
| **Vortex** (mostly C) | Deep collaboration | Fortnightly | Joint events, co-created content, bundled offers |
| **Mastermind** (mostly D) | Full ecosystem | Weekly/fortnightly | Joint offers, shared infrastructure, co-delivery |

### 3.3 Format — asked per buyer
Per `specs/_shared/build-standards.md §5 Format Ask Per Client`, the buyer chooses HTML or Gamma. Either way, the full question set + scoring map + four result-tier blurbs go into the master doc (§9) as plain content so the buyer can rebuild in any tool.

### 3.4 Quarterly refresh
The quiz re-sends every 90 days (Email 7 handles this). Partners evolve — a P-Pool can become Pro-Motor once referrals start working. Note in result copy + master doc.

---

## 4 · Voice layer — VOICE_PARAMETER_BLOCK dependency (not PILLARS)

Every asset is grounded against the buyer's **VOICE_PARAMETER_BLOCK (VPB)** — the canonical voice encoding from the NEXUS Voice Engineering System (`nowgroup-skills/sources/voice/NOW_Voice_Parameter_System.md`). The VPB is the voice authority. Generic voice instructions are superseded.

**Do not use PILLARS.** PILLARS is a dated prompt-scaffold from older playbook documents standing in for proper voice encoding. Superseded here. The VPB is the voice engine.

VPB fields applied to every asset:
- `banned_words` — never appear in any output
- `signature_phrases` — verbatim or not at all (never paraphrase)
- `spine sentences` — anchor each asset; snap back when draft drifts
- `rule_hook` / `rule_close` / `rule_register` / `rule_structure` / `rule_philosophy` / `rule_empathy` / `rule_cta` — applied to every piece
- `tone_descriptors`, temperature poles, dominant register, structural signatures — shape rhythm and register

**VPB absent = dependency block.** If the buyer doesn't have a VPB yet, that's a dependency on the Voice Engineering System. Build C *consumes* the block, does not author it. Pause and flag. Do not improvise a voice from a website skim — a weak voice input poisons every asset downstream.

### 4.1 Drift detection (quality gate)
Per `build-standards.md §2 Drift Detection`, every copy asset runs the 5-signal check before delivery. Caught signal → re-run, never hand-edit:
1. Context before hook · 2. Symmetrical lists · 3. One temperature throughout · 4. Summary close · 5. Philosophical claim leads

Some assets here are deliberately list-shaped (scorecard, referral-trigger table). Drift Signal 2 applies to *prose* assets (emails, landing-page body, philosophy sections) — judgement, not blind enforcement.

---

## 5 · Asset roster (exact counts)

Under- or over-delivering is a fail.

### 5.1 Partner Alignment Quiz (§3)
- **1 quiz** — HTML or Gamma per buyer's choice — resolves to one of the four tiers

### 5.2 Partner landing page (§8)
- **1 `<slug>_partner.html`** OR Gamma partner hub — format asked per buyer. Step 1 of its partnership flow points at THIS quiz

### 5.3 Three supporting assets — each MAX PRO + reduction prompt (§6)
For each: build **MAX PRO** version + **reduction prompt** that trims it per tier.
1. **Lead Magnet — "How & Why to Partner With Us"** — single ADD ONE asset, ships with Email 1. Replaces old carousel+infographic pair (their jobs absorbed by PCD + Expectations Doc).
2. **Partner Comms Document (PCD)** — "how to market us, simply put." Partner-facing explainer: who the buyer is, who they serve, how a partnership works, the referral triggers
3. **Partnership Expectations Document** — advanced-partner layer: mutual commitments, 90-day success outcomes, escalation paths, communication cadence

### 5.4 Email sequence — exactly 7, tier-branched at Email 4 (§7)
One sequence. Universal at 1/2/3/5/6/7; branches only at Email 4 (4A light / 4B deep).

### 5.5 Internal Management Sequence (§8 of skill, §9 of spec — operator runbook)
Per `build-standards.md §7`, operator/VA runbook with kill switches at Day 0 / 7 / 21 / 30 / 60 / 90.

### 5.6 Tier → Asset routing table (§10)
Per `build-standards.md §6`, first-class deliverable showing which assets/emails fire per tier.

### 5.7 Bundle (§11, §12)
- `Partner_Pack_<Buyer>_v1` Google Doc — all copy, all assets, all reduction prompts, the tier→asset routing table
- `<slug>_partner.html` (if HTML chosen) — saved separately as raw file on Drive
- `00_START_HERE.txt` — what's in the pack + how to deploy
- `gamma_links.txt` — any Gamma URLs (quiz / lead magnet / landing page per format choices)

---

## 6 · MAX PRO + reduction model

The mechanism that makes the quiz "shape everything." For Lead Magnet, PCD, and Partnership Expectations Document, produce two artefacts:

- **MAX PRO**: the full, ready-to-go, everything-in version. What a Mastermind-tier partner receives as-is.
- **Reduction prompt**: self-contained prompt the operator runs, feeding in a partner's quiz tier, that trims the MAX PRO to the right depth.

The quiz tier governs on two axes:
- **(A) Whether** the asset fires at all — e.g. P-Pool may skip the Partnership Expectations Doc entirely
- **(B) How** it fires — which reduction prompt runs, how hard it cuts, the cadence, which Email-4 branch

### 6.1 Canonical reduction-prompt shape

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

Build all three MAX PRO assets in the buyer's voice (VPB), write the three reduction prompts. Both layers in the master doc.

---

## 7 · Email sequence — 7 emails, branch at Email 4

Load all 7 into the buyer's CRM before sending Email 1. The tier decides Email 4 branch. Email 7 fires at 90 days for quarterly quiz refresh.

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

Each email: 120–300 words · subject line · one CTA · buyer's voice (VPB) throughout. Emails 4A/4B reference the partner's open-text quiz answers (12-month vision / this-quarter's win) where available.

---

## 8 · Partner landing page render contract

Per `build-standards.md §5`, format asked per buyer. The live benchmark / minimum-viable standard is a dedicated partner hub (e.g. the SBTH Partners hub) — a professional, branded space housing the quiz, resources, and philosophy in one place.

If **HTML**: fully populated HTML directly — no template tokens, no `{{ }}`, no Jinja2 surviving. Single self-contained `.html` ready to host anywhere.

### 8.1 Required structure (HTML)
- Self-contained `<style>` block in `<head>` — no external CSS files
- Google Fonts via `<link>` for buyer's display + body families
- Responsive: mobile-first, breakpoints at 720px and 1080px
- Smooth-scroll on hash links
- Hero image slot reserved (Gamma-generated if available, else skip cleanly)

### 8.2 CSS custom properties (literal hex from buyer palette)
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

### 8.3 Section stack (in order)
1. **Hero** — eyebrow micro-line (uppercase + letter-spacing) · tagline with emphasis phrase (italic + accent) · sub-headline · primary audience line
2. **Attention strip** — partnership flow as numbered cards. Step 1 links to THIS quiz. Default: Alignment Quiz → Intro Call → First Referral → 24h Response
3. **Reciprocal services list** — variable-length grid of what the buyer offers in exchange
4. **3 referral triggers** — title, situational description, suggested conversation phrase
5. **4 differentiators** — 2×2 grid, accent-bordered cards
6. **Pull quote** — large quote glyphs, italics, attribution — partner-perspective if available
7. **4 mutual commitments** — side-by-side or 2×2. Every commitment has a measurable signal ("we respond within 24 hours", never "we respond quickly")
8. **Quiz CTA** — prominent button to the quiz + supporting line ("8–10 minutes. No wrong answers. Your results shape our first conversation.")
9. **Practice card** — dark-backed footer card: buyer intro, location, contact/website, accent CTA
10. **Footer** — mandatory NOW credit line per `build-standards.md §3`: `Built in partnership with NOW Group — nowgroup.co.nz`

If **Gamma**: build the partner hub via Gamma MCP, populate from buyer palette + same section intent, collect URL into `gamma_links.txt`.

---

## 9 · Internal Management Sequence (operator runbook)

Per `build-standards.md §7`. Operator/VA runs this table; kill switch at each checkpoint.

| When | Stage | Action | Kill switch |
|---|---|---|---|
| Day 0 | Identify | Send Email 1 + quiz link + Lead Magnet | No quiz response in 7 days → one follow-up. Still none → P-Pool passive |
| Day 7–14 | Quiz in | Auto-send Email 2 (tier-reduced PCD). Log tier. Schedule Email 3 +48h | Email 2 unopened in 5 days → resend, varied subject |
| Day 9–16 | Hub tour | Send Email 3. Request partner's PCD/equivalent | No reply → move to light track regardless of tier |
| Day 21–28 | Activate | Send Email 4A or 4B by tier. Book spotlight or strategy call | No booking in 14 days → one final personal note → mark dormant |
| Day 30 | Check-in | Send Email 5. Log referrals each way | One-directional referrals after 30 days → raise at next call |
| Day 60 | Resources | Send Email 6. Re-engage quieter partners | No meaningful activity in 60 days → consider exit conversation |
| Day 90 | Refresh | Send Email 7. Resend quiz. Update tier + PCD if changed | Tier drop two consecutive quarters → flag for realignment or exit |

---

## 10 · Tier → Asset routing table (required deliverable)

Per `build-standards.md §6`. Print in both the master doc and the closing summary. Adjust cells to match the actual reduction prompts written — table and prompts must agree.

| Asset / Email | P-Pool | Pro-Motor | Vortex | Mastermind |
|---|---|---|---|---|
| Lead Magnet (How & Why) | ✅ reduced | ✅ reduced | ✅ fuller | ✅ MAX PRO |
| PCD | ✅ light | ✅ standard | ✅ fuller | ✅ MAX PRO |
| Partnership Expectations Doc | ⬜ skip | ◻ optional | ✅ yes | ✅ MAX PRO |
| Email 4 branch | 4A | 4A | 4B | 4B |
| Cadence | Quarterly | Monthly | Fortnightly | Weekly/fortnightly |

---

## 11 · Master Google Doc structure

Title: `Partner_Pack_<Buyer>_v1`. Heading styles H1/H2 for outline-pane navigation. Order (publish-flow, not build-order):

1. Partner Onboarding overview — the partnership flow + what the buyer does at each step
2. Partnership Philosophy — 3 paragraphs in buyer's voice (VPB). Reference LEVER / ADD ONE if fits voice; never generic
3. **Partner Alignment Quiz** — full question set + scoring map + 4 result-tier blurbs (§3)
4. **Tier → asset routing table** (§10)
5. Referral Triggers (3) — scenarios + trigger phrase + suggested conversation
6. **Lead Magnet "How & Why to Partner With Us"** — MAX PRO + reduction prompt
7. **Partner Comms Document (PCD)** — MAX PRO + reduction prompt
8. **Partnership Expectations Document** — MAX PRO + reduction prompt
9. Internal Management sequence (§9)
10. Email Templates (7 — Day 0/7/9/21A/21B/30/60 with subjects + bodies)
11. Landing Page reference (link to `.html` in same Drive folder, or Gamma URL)

---

## 12 · NOW footer credit (the one deliberate brand carve-out)

Per `build-standards.md §3`. Every **client-facing** asset (landing page, lead magnet, PCD) must carry, in footer:

`Built in partnership with NOW Group — nowgroup.co.nz`

Intentional override of the usual "no NOW bleed" rule. Carve-out is **narrow**: credit line only, not palette or voice. Client-facing assets still render in buyer's brand (`force_now_palette=False`) and buyer's voice (VPB). The NOW credit is a network-authority signal, not a style override.

---

## 13 · Quality gates (filter rubrics)

Per `build-standards.md §2`. Universal scorer + per-buyer overlay from VPB. Drift detection runs in addition to rubric scoring.

| Asset type | Rubric |
|---|---|
| Partner landing page (HTML) | Page_Landing_Result_Scoring_Rubric.md |
| 7-email sequence | EMBER_Universal_Filter.md |
| Lead Magnet copy | Lead_Magnet_Scoring_Rubric.md |
| Quiz · PCD · Expectations Doc | No rubric — structural check (tier mapping intact, length caps, VPB voice fingerprint, no banned phrases, measurable commitments) + §4.1 drift gate |

URLs at `specs/_shared/filters/` (live, verified).

---

## 14 · Open spec questions

- **Quiz format default** — currently per-buyer-choice. After 10 packs, review whether HTML or Gamma wins by frequency and consider defaulting
- **Email 4 A/B split copy** — collect actual conversion data after 10 packs to validate the light/deep cut at Pro-Motor/Vortex boundary
- **Email 7 quiz refresh** — does partner engagement justify resending the full 10-question quiz, or a 3-question pulse?

---

## 15 · Refinement notes — why this architecture

- **Quiz as routing spine, not bolt-on** — the previous architecture treated the partner's profile as something to discover via early-call conversation. The quiz front-loads structured insight so every asset arrives at the right depth. Skill builders are not consultants — the system has to do the segmentation work
- **MAX PRO + reduction over multi-version authoring** — writing 4 separate versions per asset (one per tier) is 4× the work and 4× the drift risk. MAX PRO + reduction = one authored asset + a prompt that does tier-stratification at delivery time. Single source of truth
- **NOW footer credit** — the network effect. Every partner hub carrying "Built in partnership with NOW Group" strengthens the Trans-Tasman network authority for every operator in it. Mandatory carve-out is worth the brand cost
- **Email branch at 4, not 21A/21B** — earlier versions split Day 21 (booking call) A/B. The tier-branched 4A/4B is the same idea expressed against the routing key, with cleaner labelling and a 90-day refresh loop closing the partnership cycle

---

## 16 · Implementation status — skill ↔ Python parity

| Layer | Status against this spec |
|---|---|
| **Claude.ai skill** (`dna-x-build-c.md`) | ✅ aligned with v2.0 (this spec) — 379 lines, all 16 sections implemented |
| **Python pipeline** (`nexus_wow_option_c.py`) | ⚠️ aligned with v1.0 (previous spec) — needs refactor to v2.0. **See `specs/builds/build-c-python-alignment.md` for the punch list** |

The spec is canonical. Both lanes follow it. When the spec moves, both lanes follow with explicit roadmapping (see alignment doc for current Python catch-up).

---
