# Reduction Prompt — Partnership Expectations Document

Per Build C spec §6.1. The Expectations Document is the advanced-partner layer: mutual commitments, 90-day success outcomes, escalation paths, communication cadence. MAX PRO content lives in `Partner_Pack_BAA_v2.docx` §7.

This is the asset that fires HARDEST on tier difference. READY_NOW brokers need the full mutual-commitment block before their first introduction. NOT_YET_FIT brokers should never see it — the commitments are operational reality and reading them at the wrong stage burns the open door.

---

## How to run

Paste the VOICE_PARAMETER_BLOCK (John Manciameli v1 · April 2026) first.
Then paste this prompt.
Then paste the MAX PRO Expectations content (from v2 docx §7).
Then state the band on the last line.

---

## Prompt body

```
REDUCTION PROMPT — Partnership Expectations Document

You are reducing the MAX PRO version of John Manciameli's Partnership
Expectations Document to fit one of four broker referral-readiness bands.
This document sets the operational frame for an active partnership.

Voice: ground against the loaded VOICE_PARAMETER_BLOCK. Practitioner-warmth,
specific timeframes mandatory (commitments without timeframes are intentions,
not commitments), no em dashes, "for example" specificity throughout.

INPUT FORMAT:
- MAX PRO Expectations (John commits / Partner commits / 90-day outcomes /
  Escalation path / Communication cadence)
- Band: one of READY_NOW / WARMING / BUILDING / NOT_YET_FIT

OUTPUT FORMAT: a partner-side document, sent with or just after the
post-intro-call activation pack per the routing table.

REDUCTION RULES:

READY_NOW (mostly A)
→ MAX PRO as-is. All five blocks. All seven of John's commitments.
  All five of the partner's commitments. The full 90-day outcomes block.
  The escalation path. The cadence table.
→ Add to header: "Effective from the date of your first introduction.
  Save this. Reference it if any expectation isn't being met."

WARMING (mostly B)
→ Keep John's commitments in full (all 7). The partner needs to see
  what they're being offered.
→ Reduce the partner's commitments from 5 to 4. Drop item 5 (the
  non-compete clause). Premature for a broker who hasn't sent their
  first deal yet. Restore it when the partnership moves to active.
→ Keep 90-day outcomes block as a single paragraph rather than the
  three-bullet list: "By the end of 90 days, John would expect at
  least one introduction in active property search, one deal in due
  diligence, or one deal settled with referral fee paid. If none of
  those has happened, John will initiate a realignment conversation
  to understand what's getting in the way."
→ Drop the escalation path block. Premature. Add it on the first
  active deal.
→ Keep cadence table.

BUILDING (mostly C)
→ Do not send the Expectations Document at this stage. The broker is
  still verifying fit. Sending commitments reads as preparing the
  paperwork for an agreement neither side has agreed to yet.
→ Instead: send a one-paragraph note in John's voice: "Once your
  database scan surfaces a client who's the right fit and we've had
  the intro call, we'll work through the partnership commitments
  document together. That document is what makes this a real
  partnership rather than a referral arrangement. We're not there
  today, and that's the right answer."

NOT_YET_FIT (mostly D)
→ Skip entirely. No expectations document. No partnership commitments.
  Reaching for this asset at this band breaks the honest exit John
  offered them at the quiz result.
→ If asked directly, send back: "We'd build the expectations document
  together if and when the focus shifts. Not before. The quiz is
  always there to re-take when the picture changes."

UNIVERSAL VOICE GATES:
- Every commitment has a timeframe or measurable signal. "We respond
  quickly" is a fail. "We respond inside 24 hours" is the bar.
- Banned words: leverage, synergy, paradigm shift, game-changer,
  Here's the thing, Let's dive in, In today's fast-paced world,
  unlock the power of, transform, revolutionise, holistic, seamless,
  robust, cutting-edge, best-in-class.
- No em dashes.
- "For example" wherever an abstract claim could land. Make every
  promise specific.

OUTPUT NOW:
```

---

## Routing reference

| Band | What fires | Email tag |
|---|---|---|
| READY_NOW | MAX PRO Expectations + effective-from line | `baa_exp_maxpro` |
| WARMING | Reduced (drop non-compete + escalation, soften 90-day) | `baa_exp_warming` |
| BUILDING | Skip. Send one-paragraph "build it together later" note | `baa_exp_deferred` |
| NOT_YET_FIT | Skip entirely. Reaching for this asset breaks the honest exit | `_` |
