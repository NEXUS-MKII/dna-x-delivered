# Reduction Prompt — Partner Comms Document (PCD)

Per Build C spec §6.1. The PCD is the partner-facing explainer: who John is, who he serves, how the Acquisitions Desk partnership works, the referral triggers, the partner's role. The MAX PRO version draws on `Partner_Pack_BAA_v2.docx` §1 (Onboarding Overview) + §2 (Philosophy) + §3 (Referral Triggers) + §4 (Internal Management visible to partner).

Reduction here is about depth, not subject. The READY_NOW broker reads the full philosophy and the Scott story before the call. The BUILDING broker just needs the model on one page.

---

## How to run

Paste the VOICE_PARAMETER_BLOCK (John Manciameli v1 · April 2026) first.
Then paste this prompt.
Then paste the MAX PRO PCD content (compiled from v2 docx sections 1, 2, 3, plus a partner-facing version of section 4).
Then state the band on the last line.

---

## Prompt body

```
REDUCTION PROMPT — Partner Comms Document (PCD)

You are reducing the MAX PRO version of the BAA Partner Comms Document
to fit one of four broker referral-readiness bands. The PCD is partner-facing.
A broker reads it before or just after the intro call to understand the
Acquisitions Desk model and what the partnership produces.

Voice: ground against the loaded VOICE_PARAMETER_BLOCK. Practitioner-warmth,
85% concrete, "for example" specificity mandatory, mirror-question hook,
crystallisation close, M-S-S-S rhythm, no em dashes.

INPUT FORMAT:
- MAX PRO PCD (full 4-section document)
- Band: one of READY_NOW / WARMING / BUILDING / NOT_YET_FIT

OUTPUT FORMAT: a clean partner-side PDF or Google Doc, ready to attach to
the Day 2 (post-quiz) email per the routing table.

REDUCTION RULES:

READY_NOW (mostly A)
→ MAX PRO as-is. All four sections. The Scott story stays in full. The
  data methodology paragraph stays in full. The "what each side gives /
  receives" closing paragraph stays in full.
→ Add at the end: "Before our call this week, the most useful thing you
  can do is identify two clients you'd introduce first. We'll talk through
  both on the call."

WARMING (mostly B)
→ Keep Sections 1 (Onboarding Overview), 2 (Philosophy), and 3 (Referral
  Triggers). Drop Section 4 (Internal Management) — premature.
→ In Section 2, trim the Scott story to 3 sentences (set-up, what happened,
  the colleague outcome). Keep the philosophy paragraphs around it intact.
→ Add at the end: "If you'd like the broker-side activation checklist
  (ADD ONE) before our call, reply to the Day 2 email and John will send it."

BUILDING (mostly C)
→ Reduce to a one-page summary version. Structure:
  - Headline: "The Property Acquisitions Desk in 90 seconds"
  - Para 1: The structural problem (settlement, relationship goes quiet,
    investor goes elsewhere). 3 sentences max.
  - Para 2: The model (acquisitions arm inside your business, you write
    the loan, you keep the relationship). 3 sentences max.
  - Para 3: The three referral triggers as a bullet list, one sentence each.
  - Close: "When you have one client who fits any of those three triggers,
    that's the moment for an intro call. Until then, the readiness checklist
    is the right tool to keep on your desk."
→ Drop the Scott story, the data methodology paragraph, the mutual
  commitments. All premature.

NOT_YET_FIT (mostly D)
→ Do not send the PCD. Send John's "When the focus shifts" one-pager
  (see ADD ONE reduction prompt). The PCD is targeted to brokers who are
  at minimum considering the model. NOT_YET_FIT brokers haven't selected
  themselves in. Sending the PCD reads as a soft pitch and erodes the
  honest exit John offered them at result time.

UNIVERSAL VOICE GATES:
- Banned words: leverage, synergy, paradigm shift, game-changer,
  Here's the thing, Let's dive in, In today's fast-paced world,
  unlock the power of, transform, revolutionise, holistic, seamless,
  robust, cutting-edge, best-in-class.
- No em dashes.
- "For example" appears at least once per 200 words of partner-facing copy.
- Every claim followed by a named specific or process step.
- Crystallisation close. Not a summary.

OUTPUT NOW:
```

---

## Routing reference

| Band | What fires | Email tag |
|---|---|---|
| READY_NOW | MAX PRO PCD + two-clients prompt | `baa_pcd_maxpro` |
| WARMING | 3-section PCD (no internal mgmt) | `baa_pcd_warming` |
| BUILDING | 1-page summary PCD | `baa_pcd_building` |
| NOT_YET_FIT | Skip. "When the focus shifts" one-pager sent instead | `baa_lm_focusshift` |
