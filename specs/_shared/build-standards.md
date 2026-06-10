---
spec_version: 1.0
last_updated: 2026-06-09
applies_to: every DNA-X build (Tier 1 / Tier 2 / Tier 3)
referenced_by:
  - specs/builds/build-a.md
  - specs/builds/build-c.md
  - specs/builds/gx-1.md
---

# DNA-X Build Standards

> Seven cross-cutting patterns every DNA-X build must follow. Codified after the Build C v2.0 upgrade revealed that these patterns belong to the build SYSTEM, not to any individual build. Each build spec references this doc instead of restating these rules — single source of truth, zero drift.

The build skills (Claude.ai) and the Python builders (`nexus_wow_*.py`) both implement against these standards. When a build deviates, the deviation is documented in that build's spec — never silently.

---

## 1 · VOICE_PARAMETER_BLOCK as Voice Authority

**Every build that produces voice-bearing content consumes a buyer's VOICE_PARAMETER_BLOCK (VPB) as input.** The VPB is the canonical voice encoding produced by the NEXUS Voice Engineering System (see `https://raw.githubusercontent.com/NEXUS-MKII/nowgroup-skills/main/sources/voice/NOW_Voice_Parameter_System.md`).

### Rules
- The VPB **supersedes** any generic voice instruction. When they conflict, VPB wins
- **Do not use PILLARS.** PILLARS is a dated prompt-scaffold from older playbook documents — superseded
- VPB-absent = dependency block. Builds *consume* the VPB; they never author it. If absent, pause and flag — do not improvise voice from a website skim

### VPB fields applied to every asset
- `banned_words` — never appear in any output
- `signature_phrases` — verbatim or not at all (never paraphrase)
- `spine sentences` — anchor each asset; snap back when draft drifts
- `rule_hook` / `rule_close` / `rule_register` / `rule_structure` / `rule_philosophy` / `rule_empathy` / `rule_cta`
- `tone_descriptors`, temperature poles, dominant register, structural signatures

---

## 2 · Drift Detection Quality Gate (5 signals)

**Every copy asset runs the 5-signal drift check before delivery.** Catch any one → re-run the asset, never hand-edit it. Manual editing of AI output trains the model toward the editor's voice, not the buyer's.

| Signal | What it looks like | Correction prompt to add |
|---|---|---|
| **1. Context before hook** | Opens with scene-setting paragraph before the real hook | "The hook is the first line. No preamble, no context, no setup." |
| **2. Symmetrical lists** | Three equal-length points, identical rhythm, reads like a template | "Dissolve frameworks into prose or scene. No numbered lists unless the asset format genuinely requires one." |
| **3. One temperature throughout** | Warm all the way, or precise all the way. No register shift | "Find the coldest true line in this topic. Include it. Hard-cut to where warmth should arrive." |
| **4. Summary close** | Final line recaps ("So as you can see…") | "Close on a principle that survives extraction. Match the crystallisation register from the VPB." |
| **5. Philosophical claim leads** | A spine or phil anchor appears in the first two lines before the piece earns it | "Phil anchors close. Move to final substantive paragraph. Build the concrete scene first." |

### When drift signals don't apply
Signal 2 (symmetrical lists) does **not** apply to assets that are deliberately list-shaped — a scorecard, a referral-trigger table, a tier comparison. Judgement, not blind enforcement. Apply Signal 2 to **prose** assets only (emails, landing-page body, philosophy sections, articles, posts).

---

## 3 · NOW Footer Credit (the one brand carve-out)

**Every client-facing asset must carry, in the footer:**

```
Built in partnership with NOW Group — nowgroup.co.nz
```

### Why
Network-authority signal. Every buyer's hub carrying this strengthens the Trans-Tasman network for every operator in it. The compound effect requires it on every asset.

### Narrow carve-out
- Applies to the **credit line only** — never palette, never typography, never voice
- Client-facing assets still render in buyer's brand (`force_now_palette=False`) and buyer's voice (VPB)
- The NOW credit is a network signal, not a style override
- **Do not reach for NOW orange or NOW typography on a client asset.** The credit line is the only NOW element that appears

### Where it goes
- Landing pages: footer
- Lead magnets: footer of the rendered HTML/PDF, or the last slide of a Gamma
- Emails: signature line beneath the buyer's sign-off (smaller, muted)
- PCDs / printed docs: footer of last page
- Internal docs (operator runbooks, START_HERE files): not required (these don't go to clients)

---

## 4 · MAX PRO + Reduction Model (for tier-stratified builds)

Where a build has tier-stratified audiences (Build C: 4 partner tiers via Alignment Quiz), build assets at **MAX PRO** + **reduction prompts** rather than authoring N versions in parallel.

### MAX PRO
The full, ready-to-go, everything-in version of an asset. What the top-tier audience receives as-is.

### Reduction prompt
A self-contained prompt the operator runs, feeding in a tier identifier, that trims the MAX PRO to the right depth for that tier. Must name explicitly what to cut, soften, or keep per tier.

### Canonical reduction-prompt shape

```
REDUCTION PROMPT — <asset name>
Input: this MAX PRO <asset> + <segmentation key value>
For the given <tier/segment>, produce the right-sized version:
- <Tier A>: [what to keep — usually the lightest core; what to cut]
- <Tier B>: [what to keep / add back relative to A]
- <Tier C>: [fuller version — what returns]
- <Tier D>: [MAX PRO as-is, or near-full]
Voice: ground against the buyer's VOICE_PARAMETER_BLOCK. Banned words never appear.
Output: the tier-appropriate <asset>, ready to send.
```

### Why MAX PRO + reduction over multi-version authoring
- Writing N versions per asset = N× the work and N× the drift risk
- MAX PRO + reduction = one authored asset + a prompt that does segmentation at delivery
- Single source of truth — when the asset changes, you change one thing
- Reduction logic can be audited, versioned, and improved without re-writing assets

### When NOT to use MAX PRO + reduction
- When the audience is uniform (Build A reaches a buyer's whole client audience — single depth)
- When the segments need fundamentally different content (not just less of the same)

---

## 5 · Format Ask Per Client (HTML vs Gamma)

When a deliverable has both a **HTML lane** and a **Gamma lane** (landing pages, lead magnets, quiz assets), **ask the buyer which they want** before building. Build accordingly.

### Why
- Some buyers host on their own CRM / Squarespace / Webflow — HTML drops in
- Some buyers want client-side polish from Gamma's render engine — Gamma is easier
- Default-to-one creates friction for buyers in the other camp

### What to ship either way
Even when the buyer picks one format, drop the **plain-content version** of the asset (full copy + structural spec) into the master doc so the buyer can rebuild in any tool if needed.

### When format is NOT asked
- Email sequences (always plain text + HTML, no Gamma option)
- Master docs (always Google Docs)
- Internal runbooks (always plain Markdown or Google Doc)
- Operator-facing artefacts (one canonical format only)

---

## 6 · Routing Tables as Required Deliverables

When a build has multiple paths (tiers, segments, branches), the **map** of which asset/email goes to which path is a first-class deliverable. Not optional. Not buried. Print in both the master doc AND the closing summary.

### Required columns
- Asset / Email name (row label)
- One column per segment/tier
- Cell content: depth indicator (✅ MAX PRO / ✅ reduced / ⬜ skip / ◻ optional) + meaningful detail

### Required consistency
- The routing table and the reduction prompts must agree. If the table says "Vortex gets MAX PRO of the PCD" but the reduction prompt for Vortex says "trim by 30%" — that's a bug
- When the table changes, the reduction prompts change with it (and vice versa)

### Example (from Build C)

| Asset / Email | P-Pool | Pro-Motor | Vortex | Mastermind |
|---|---|---|---|---|
| Lead Magnet | ✅ reduced | ✅ reduced | ✅ fuller | ✅ MAX PRO |
| PCD | ✅ light | ✅ standard | ✅ fuller | ✅ MAX PRO |
| Partnership Expectations Doc | ⬜ skip | ◻ optional | ✅ yes | ✅ MAX PRO |
| Email 4 branch | 4A | 4A | 4B | 4B |
| Cadence | Quarterly | Monthly | Fortnightly | Weekly/fortnightly |

---

## 7 · Internal Management Sequence with Kill Switches

For any build that the buyer runs over time (Build C's 90-day partner activation; Build A's 8-week content rollout; GX-1's monthly retainer), produce an **operator/VA runbook** with explicit kill switches at every checkpoint.

### Why
- A system that fires forever without checkpoints generates spam and churn
- The kill switch is what makes the system humane and operator-controlled
- Operators / VAs need explicit "stop firing X when Y happens" rules, not vague "monitor for drop-off"

### Required structure

| When | Stage | Action | Kill switch |
|---|---|---|---|
| Day X | Stage label | What the operator/VA does | The specific condition under which to STOP firing this asset/email |

### Kill switch criteria
Every checkpoint has a kill switch. Every kill switch is:
- **Time-bounded** (e.g. "no response in 7 days")
- **Observable** (operator can check, no judgement calls)
- **Action-specific** (says what stops, not "investigate")

### Examples
- "No quiz response in 7 days → one follow-up. Still none → P-Pool passive"
- "Email 2 unopened in 5 days → resend with varied subject"
- "No booking in 14 days → one final personal note → mark dormant"
- "Tier drop two consecutive quarters → flag for realignment or exit"

---

## Cross-cutting reminders

### Skill ↔ Python parity
Every build has two implementations: the **Claude.ai skill** (bespoke runs) and the **Python pipeline** (automated production). Both implement against the build's spec. When the spec moves, both follow — never the skill or the Python alone. Each build's spec has a §"Implementation status — skill ↔ Python parity" section tracking divergence and pointing at the alignment roadmap if one exists.

### Filter rubrics (universal, never per-buyer-bespoke)
All scoring rubrics live at `specs/_shared/filters/`. Universal logic + per-buyer overlay from VPB. Never write a per-buyer-bespoke filter — overlay via the VPB instead.

### Skill body self-containment
Skills should be self-contained where possible — fetch their spec for canonical reference but execute even if fetch fails. Filter URLs inline. HTML render contracts described inline. No mandatory external dependency at session start except the spec fetch and the VPB.

### When deviating
Any build that deviates from these standards documents the deviation in its spec under a "Deviations" section with the reason. Silent deviation creates drift between builds and undermines this doc's purpose.
