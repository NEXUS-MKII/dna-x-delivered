---
spec_version: 1.0
last_updated: 2026-06-10
references:
  - specs/builds/build-c.md (v2.0 spec — the target)
  - skills/dna-x-build-c.md (v2.0 skill — already aligned)
status: planned · not yet started
total_effort: ~11.5 hours focused refactor
canonical_python: NEXUS MKII/nexus_wow_option_c.py (2828 lines, currently on v1.0 architecture)
---

# Build C — Python Pipeline Alignment Roadmap

> Concrete refactor plan to bring `nexus_wow_option_c.py` (the automated production pipeline) into alignment with `build-c.md` v2.0 (the upgraded spec). The Claude.ai skill is already aligned; the Python is behind. This doc maps every spec section to the Python work needed with hour estimates so it can be scheduled as a focused session.

When this work completes, both lanes (skill + Python) implement the same spec and a buyer gets the same architecture whether the build is run bespoke through Claude.ai or auto-fired through `nexus_wow_ext.py`.

---

## 1 · Current Python state (v1.0 architecture)

`nexus_wow_option_c.py` implements:
- ✅ 3-pass pipeline (Pass 1 context frame → Pass 2 docx builder → Pass 3 YAML emit)
- ✅ Outputs: 1 partner landing page HTML + 1 docx (emails, bios, expectations, ADD ONE) + YAML
- ✅ Voice authority via `profile.voice_assets.parameter_block` (already references the VPB field)
- ✅ Brand applied via `force_now_palette=False` for client assets
- ⚠️ Tier 1 palette gate still pending (per memory `project_voice_encoder_promotion.md`)
- ❌ No quiz routing spine (treats partner profile as discovered via early call, not front-loaded structured insight)
- ❌ No MAX PRO + reduction prompts
- ❌ No tier-branched Email 4 (currently flat 7-email sequence)
- ❌ No tier→asset routing table generation
- ❌ No NOW footer credit on client assets
- ❌ VPB consumed as optional field, not enforced as dependency
- ⚠️ Internal Management Sequence in docx Section 4 but no kill-switch column
- ❌ 3 bios still in roster (LinkedIn / email sig / spoken intro) — Skill v2 absorbed these into the PCD; Python needs to follow

## 2 · Section-by-section refactor map

### 2.1 §3 of spec — Partner Alignment Quiz

**Spec requires**: build the quiz first; quiz output (4 tiers) routes everything else.

**Python today**: no quiz generation at all.

**Refactor work**:
- New function `generate_partner_alignment_quiz(profile, data)` — emits ~10 question set + scoring map + 4 tier blurbs
- New CLI flag `--quiz-format html|gamma` (default ask via operator config)
- For HTML quiz: extend the existing template-fill machinery to produce a second self-contained `.html` (client-side `mostly X → tier` scoring)
- For Gamma quiz: call `nexus_gamma_assets.py` with a new prompt type `partner_quiz`
- Store full question set in structured JSON so docx render can include it

**Effort**: 3 hours
**Blocks**: Pass 2 changes (the quiz tier is input to MAX PRO + reduction logic)

### 2.2 §4 of spec — VPB as enforced dependency

**Spec requires**: VPB absent = pause and flag; don't improvise.

**Python today**: reads `profile.voice_assets.parameter_block` if present; falls back to `encoder_lite`, then to Pass 2 inferred descriptors, then to profile context. Silent fallback chain.

**Refactor work**:
- Add pre-flight check in `_pre_build_assertions()` (or equivalent entry)
- If `profile.voice_assets.parameter_block` missing AND `--allow-improvised-voice` flag NOT set → exit with clear error message pointing at NEXUS Voice Engineering System
- Remove silent fallback to Pass-2-inferred voice descriptors (was a hack from v1)
- Update `nexus_wow_ext.py` (the Kajabi webhook dispatcher) to check VPB presence before firing the build — return error to buyer if absent

**Effort**: 30 minutes
**Blocks**: nothing (additive guard, easy to ship first)

### 2.3 §6 of spec — MAX PRO + reduction prompts

**Spec requires**: Lead Magnet, PCD, Expectations Doc each = MAX PRO version + reduction prompt block.

**Python today**: Pass 2 emits single-depth versions of each.

**Refactor work**:
- Refactor `generate_pass_2_docx_builder()` Claude API prompt to emit MAX PRO version + a `reduction_prompt` block per asset (4 named tiers: P-Pool / Pro-Motor / Vortex / Mastermind)
- JSON schema additions: each of LM, PCD, Expectations now has `max_pro_content` and `reduction_prompt` keys
- Docx render updates to include both layers per asset (MAX PRO above the fold, reduction prompt below as operator-facing)
- Master doc TOC update to reflect new structure

**Effort**: 3 hours
**Blocks**: tier→asset routing table generation (table cells reference the reduction prompts)

### 2.4 §7 of spec — Email sequence tier-branched at Email 4

**Spec requires**: 7 emails. Universal 1/2/3/5/6/7. Email 4 branches 4A (P-Pool/Pro-Motor light) / 4B (Vortex/Mastermind deep). Email 7 = 90-day quiz refresh.

**Python today**: 7 emails Day 0/7/9/21A/21B/30/60 (A/B at 21, no tier branching, no Day 90 quiz refresh).

**Refactor work**:
- Rewrite email Pass 2 schema: rename `email_21a/21b` to `email_4a/4b` with explicit tier routing labels
- Rewrite email 4A as "Quick win: co-host a spotlight" (light collab pattern)
- Rewrite email 4B as "Map a full partnership strategy" (deep collab pattern with strategy-call CTA)
- Add Email 7 at Day 90: "quiz refresh + tier evolution check" — references the quiz URL emitted in §2.1
- Update Pass 2 prompt to reference partner's open-text quiz answers (12-month vision / this-quarter's win) for 4A/4B personalisation hooks

**Effort**: 1 hour
**Blocks**: nothing (independent of §2.3 MAX PRO work, can ship in parallel)

### 2.5 §10 of spec — Tier→Asset routing table

**Spec requires**: explicit table showing which assets/emails fire per tier. First-class deliverable. Must agree with reduction prompts.

**Python today**: no routing table generated.

**Refactor work**:
- New function `generate_routing_table(generated, tiers, reduction_prompts)` — emits Markdown table
- Output: pure data dict that feeds the docx render
- Add to Pass 2 JSON schema output
- Render in master docx as a dedicated section (after the PCD section)
- Print in final summary log + the operator-facing 00_START_HERE-equivalent

**Effort**: 30 minutes
**Blocks**: nothing if §2.3 MAX PRO is done first (table cells reference reduction prompt names)

### 2.6 §12 of spec — NOW footer credit on client assets

**Spec requires**: `Built in partnership with NOW Group — nowgroup.co.nz` on every client-facing asset.

**Python today**: no NOW credit; partner landing page footer says `Part of the NOW Group partnership ecosystem` (pre-v2 language, close but not exact).

**Refactor work**:
- Update partner-page HTML template — change footer line to canonical credit
- Add NOW credit to docx footer on last page (python-docx `section.footer`)
- For ADD ONE Lead Magnet YAML → lm_builder rendering: ensure the template includes the credit
- Update wording on landing page: change `now_ecosystem_line` placeholder default

**Effort**: 10 minutes
**Blocks**: nothing

### 2.7 §9 of spec — Internal Management Sequence with kill switches

**Spec requires**: operator runbook table with explicit kill switch at every checkpoint.

**Python today**: Section 4 of docx has the sequence but no kill-switch column.

**Refactor work**:
- Update Pass 2 prompt for `internal_partner_management` section to require 4 columns: When · Stage · Action · Kill switch
- Render as proper 4-column docx table (currently single-column prose)
- Validate against 6 mandatory checkpoints: Day 0 / 7-14 / 9-16 / 21-28 / 30 / 60 / 90

**Effort**: 30 minutes
**Blocks**: nothing

### 2.8 Quiz format choice (HTML or Gamma)

**Spec requires**: ask per buyer.

**Python today**: no choice mechanism.

**Refactor work**:
- Add operator config field `wow_factor.option_c_content.quiz_format: 'html' | 'gamma'` (default `html`)
- Pre-build: if missing, log warning + use default
- Route to the right generator based on the field

**Effort**: 1 hour
**Blocks**: §2.1 quiz builder (depends on this for routing)

### 2.9 Routing table ↔ reduction prompt consistency check

**Spec requires**: table and prompts must agree.

**Python today**: no validation.

**Refactor work**:
- New function `validate_routing_consistency(routing_table, reduction_prompts)` — assertion that every tier mentioned in the table has a matching named branch in every reduction prompt
- Run after Pass 2 emit, before Pass 3 YAML write
- On failure: log loudly + abort (don't deliver a self-contradicting pack)

**Effort**: 30 minutes
**Blocks**: nothing once §2.3 and §2.5 done

### 2.10 Smoke tests

**Spec requires**: every pack is correct.

**Python today**: minimal smoke test infrastructure.

**Refactor work**:
- New `scripts/smoke_wow_option_c_v2.py`
- Synthesises a test profile with all required v2 inputs (including a stub VPB)
- Runs the full pipeline end-to-end
- Asserts:
  - Quiz output has 8-12 questions, 4 tier blurbs
  - Each of LM/PCD/Expectations has both MAX PRO and reduction prompt
  - Email 4 has both A and B branches with tier labels
  - Email 7 fires at Day 90 and references quiz refresh
  - Tier routing table exists, matches reduction prompts
  - NOW credit appears in HTML footer + docx footer
  - VPB-absent profile → pre-flight assertion fails cleanly

**Effort**: 1.5 hours
**Blocks**: all other refactor work done first

## 3 · Total effort & sequencing

| # | Task | Hours | Blocks / depends on |
|---|---|---|---|
| 1 | §2.6 NOW footer credit | 0.2 | nothing — ship first as quick warm-up |
| 2 | §2.2 VPB dependency gate | 0.5 | nothing — ship second, additive guard |
| 3 | §2.7 Kill switches in Internal Management | 0.5 | nothing |
| 4 | §2.8 Quiz format choice | 1.0 | nothing |
| 5 | §2.1 Quiz builder pass | 3.0 | depends on #4 |
| 6 | §2.3 MAX PRO + reduction prompts | 3.0 | depends on #5 (quiz tiers are input) |
| 7 | §2.4 Email tier-branching | 1.0 | nothing (parallel-able with #6) |
| 8 | §2.5 Routing table generator | 0.5 | depends on #6 |
| 9 | §2.9 Consistency check | 0.5 | depends on #6 + #8 |
| 10 | §2.10 Smoke tests | 1.5 | depends on all above |
| **TOTAL** | | **~11.5 hours** | |

Recommend two focused sessions:
- **Session 1 (~4h)**: #1, #2, #3, #4, #5 → quiz builder live + safety guards
- **Session 2 (~7.5h)**: #6, #7, #8, #9, #10 → MAX PRO + reduction + emails + table + tests

## 4 · Definition of "done"

The Python is aligned with v2.0 when:
1. A buyer who buys Option C via Kajabi webhook gets a pack that includes a Partner Alignment Quiz routing the rest of the deliverables
2. Lead Magnet, PCD, Expectations Doc each have a MAX PRO version + a reduction prompt
3. Email 4 branches 4A/4B by tier; Email 7 fires at Day 90 quiz refresh
4. Master docx contains the tier→asset routing table
5. Every client-facing asset carries the NOW credit footer line
6. VPB-absent buyers are blocked at pre-flight with a clear error pointing at the Voice Engineering System
7. The smoke test passes end-to-end on a synthetic profile
8. A spot-check delivery to a real test profile matches the structure of the v2.0 spec (manual review of one full pack)

## 5 · Parallel concerns

While this refactor is in flight:
- **Skill stays canonical for Claude.ai bespoke runs.** Buyers running Build C interactively get v2.0 immediately via the skill, regardless of Python catch-up state
- **Existing v1.0 packs in flight don't get retroactively upgraded.** They ship per v1.0 architecture. Document this in BUILD.md
- **`nexus_wow_ext.py` (the dispatcher)** stays untouched until §2.2 lands — at that point add the VPB pre-flight check there too so iframe-mode bookings don't fire builds against incomplete inputs

## 6 · After alignment

Once the Python catches up to v2.0:
1. Update `specs/builds/build-c.md` §16 "Implementation status" to mark Python as aligned
2. Run a parity audit: feed the same buyer profile through both lanes (skill + Python) and diff outputs — they should produce equivalent packs
3. Archive this alignment doc with `status: complete · python_aligned: <commit-sha>` in the frontmatter
4. Update `BUILD.md` in `baa-booking-test` repo to clear the Python ↔ Skill divergence concern for Build C
