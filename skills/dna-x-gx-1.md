---
name: dna-x-gx-1
description: Build, refine, audit, or edit any artefact for GX-1 Acquisition (LinkedIn outreach managed channel — Tier 3). Use when the user mentions GX-1, Acquisition, LinkedIn outreach setup, Channel Manager, ICP/IPP, SGT Audit, or wants to draft/refine GX-1 Kajabi offers, checkout copy, partner specs, weekly reports, content factory packs, or the spec itself.
---

# DNA-X · GX-1 Acquisition

You are working on artefacts for **GX-1 Acquisition**, the first Tier 3 (X-Ponential) product in the DNA-X suite. Follow this sequence on every invocation.

## 1. Fetch canonical specs (always — do not skip, do not improvise from memory)

Fetch both of these in parallel **before doing anything else**:

- **Tier 3 orchestration**: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/tiers/tier-3.md
- **GX-1 build spec**: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/builds/gx-1.md

If either fetch fails (404, network error, partial content), **STOP and tell the user** — do not improvise from training data. Drift between live spec and your output is the single thing this skill exists to prevent.

## 2. Cite spec versions at the top of every response

Start every reply with a one-line citation block:

> `gx-1.md` v<spec_version> · `tier-3.md` v<spec_version> · fetched <iso-date>

This lets the user spot drift if you're operating on a stale spec.

## 3. Apply the spec to the user's request

The user will typically want one of:

- **Draft a deliverable** (checkout copy, weekly report, content factory pack, SGT audit section, Channel Manager briefing, etc.) — match the spec exactly. Do not invent fields or add sections not in the spec.
- **Refine an existing artefact** (user pastes it in) — preserve their voice and structural choices, tighten only against spec requirements. Don't rewrite for taste.
- **Audit an existing artefact for spec compliance** — score against the relevant spec sections (1–11), list gaps explicitly. Use this format: `Section X.Y ✅/⚠️/❌ — [evidence]`.
- **Improve the spec itself** — propose changes; if the user accepts, **output the full updated `gx-1.md` or `tier-3.md` ready to paste into the repo** (frontmatter + body), with `spec_version` bumped and `last_updated` set to today.

## 4. Flag spec gaps explicitly

If during the work you notice the spec is unclear, contradictory, or has a gap the user is asking about, surface it inline:

> **[SPEC GAP]** Section X.Y says Y but the user is asking Z. Recommend updating spec to clarify <one-line proposal>.

The point of this skill is that the user can refine the skill/spec and propagate refinements back to the NEXUS Python build that implements it. Spec gaps are the signal — surface them, don't paper over them.

## 5. Stay in-tier

GX-1 is **Tier 3** (managed channel, setup + monthly retainer, partner-run ongoing). If the user is asking about something that's clearly a Tier 1/2 build (A–F: Content Pack Pro, Partner Growth, Email Rescue, Quiz Funnel, GEO+SEO, BizCard), tell them to use the matching skill (`dna-x-build-a` through `dna-x-build-f`) — don't try to answer cross-tier from this skill. Cross-tier bundle questions (D+GX-1, full Genome bundle, etc.) are in scope here.

## 6. NOW Group conventions (carry these into every artefact)

- All fees: **NZD excl GST · 7-day payment terms**
- Voice/brand: **buyer brand** (`force_now_palette=False`) for any client-facing artefact; **NOW voice** only for internal Channel Manager training docs
- Primary contact for client comms: **chris@nowgroup.co.nz**
- Channel Manager is recruited via **VA World** (single canonical partner for GX-1, not a shortlist)
- LinkedIn Sales Navigator subscription is **billed direct client → LinkedIn** (NOW never marks up software)
