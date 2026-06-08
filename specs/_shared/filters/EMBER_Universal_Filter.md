# EMBER — Universal Email Quality Filter

A voice-agnostic diagnostic that scores any email against a universal quality rubric and gates whether it ships. Designed to compose with a per-client Voice Parameter Block at runtime — the rubric stays universal, the per-author specifics (banned words, signature phrases, funnel-stage labels) load as an overlay.

> Companion to: a per-client Voice Parameter Block (provides the WHO).
> This tool provides the QUALITY GATE.
> Generator companion: EMBER Universal Generator (separate file — writes from a brief).

---

## What this is

An email earns its place in an inbox by doing five jobs in sequence. EMBER names them:

- **E**dge — the hook that stops the scroll (subject + preview + first two lines)
- **M**ode — the named failure mode the reader sees themselves in
- **B**reak — the temperature swing that makes it sound human, not corporate or AI
- **E**vidence — real proof, not general claims
- **R**each — one earned CTA, last line

This filter scores an existing email against those five dimensions plus a universal voice-integrity check, and returns a 0–100 score with a PASS / HOLD / KILL gate.

**Use this when:**
- An email has been drafted (by human, AI, or generator tool) and needs a quality gate before send
- A campaign batch needs sweeping for AI-slop, weak hooks, stacked CTAs, or single-temperature drift
- A junior writer or VA submits a draft and the editor wants a structured second opinion before approving

**Do NOT use this for:**
- Generating emails from scratch (use the EMBER Universal Generator instead)
- Subjective taste calls — this is a structural quality gate, not a creative review

---

## Minimum ship score + gates

| Score | Verdict | Action |
|-------|---------|--------|
| **70+** | **PASS** | Publishable first draft. May still benefit from polish — but it ships. |
| **60–69** | **HOLD** | Specific edits needed. The Upgrade Pass section below shows where +10–15 typically comes from. |
| **<60** | **KILL** | Wrong premise. Do not edit — rewrite from scratch using the diagnostic notes. Editing a KILL trains the system toward the editor's voice, not the author's. |

The 70+ threshold is deliberate: it forces structural quality without demanding perfection. Lower thresholds let AI slop through. Higher thresholds discourage shipping.

---

## The EMBER rubric (100 points)

Score each dimension independently. Sum at the end.

### EDGE — does the opening earn the next 5 seconds? (20 pts)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Subject line | 0–5 | 4–7 words. Provokes or names rather than describes. Lowercase by default. Does not promise what the body can't deliver. |
| Preview text | 0–5 | 45–90 chars. Amplifies the subject, doesn't repeat it. Adds a second reason to open. |
| First two lines | 0–10 | Confession, scene, or provocation. NEVER a setup ("I want to talk to you about..."). NEVER a question the reader hasn't earned. The reader knows by line 2 whether this is for them. |

### MODE — is there a named failure the reader sees themselves in? (20 pts)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Failure mode is specific | 0–10 | The pain or problem named has specific contours — not "many business owners struggle with X." A specific role, situation, or pattern. |
| Coined or labelled | 0–5 | A two-or-three-word phrase compresses the failure into a memorable handle. Not required, but high-scoring emails usually have one. |
| Reader self-recognition | 0–5 | Within the first third of the email, the right reader thinks "that's me." Specific nouns from their world. Specific verbs from their day. |

### BREAK — is there ONE clear temperature swing? (25 pts — heaviest weight)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Temperature range exists | 0–10 | The email is not one temperature throughout. There is a colder line and a warmer line, or vice versa. Single-temperature emails fail this dimension entirely. |
| Swing is clean | 0–10 | One swing, not three. Hard-cut preferred — no transitional softening. The gap between cold and warm is what makes the email sound human. |
| Earned, not performed | 0–5 | The warm side is genuine — accountability, self-implication, real care. The cold side is precise diagnosis, not cruelty. Performed warmth ("I just want you to know...") and performed savagery ("Hot take:") both fail. |

**Why 25 points:** the Break is the structural feature most often missing in AI-generated and corporate email. Single-temperature output is the #1 tell. This dimension is weighted heaviest because if it fails, the email fails regardless of other strengths.

### EVIDENCE — is the proof real? (15 pts)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Specific over general | 0–10 | Numbers are real numbers. Names are real names. Moments are real moments. "We helped many clients increase X" → 0 pts. "Sarah ran her dormant 1,400-name list and booked 3 calls in 2 weeks" → full marks. |
| No invented outcomes | 0–5 | Every claim is one the author can verify. If the author doesn't have the proof, the claim should be cut. Inventing case studies, percentages, or quotes = automatic 0 on this dimension. |

### REACH — one earned CTA? (15 pts)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Single CTA | 0–5 | Exactly one primary action. PS may carry a softer secondary. Two or more primaries = automatic deduction. |
| Earned by the body | 0–5 | The action feels like the natural next step from what was just said, not a pivot. The body has done the work to make the action obvious. |
| Specific over vague | 0–5 | "Reply with the word X" / "Click this link to book a slot" / "Forward to one operator who needs this" — not "Get in touch" or "Let me know what you think." |

### VOICE INTEGRITY — universal + per-client (5 pts)

| Check | Points | What "good" looks like |
|-------|--------|------------------------|
| Universal banned words clean | 0–2 | Zero hits from the universal AI-slop list (below). One hit = -1. Two+ = 0. |
| Per-client banned words clean | 0–2 | Zero hits from this author's Voice Parameter Block `banned_words`. One hit = -1. Two+ = 0. |
| Signature phrases respected | 0–1 | If the email uses a phrase from the author's `signature_phrases`, it's used verbatim — not paraphrased. Paraphrased signature = automatic 0 on this sub-check. |

---

## Universal banned words (AI-slop list)

Delete on sight. Zero exceptions. These appear in the Voice Integrity check above.

```
leverage (unless referring to a physical lever)
synergy
paradigm shift
best-in-class
digital transformation
stakeholder (in marketing context)
value proposition
bandwidth (when used metaphorically)
low-hanging fruit
circle back
game-changer (unless ironic)
unlock the power of
"Here's the thing..."
"Let's dive in..."
"In today's fast-paced world..."
"At the end of the day..."
"Here's the truth..."
"It's not an X problem, it's a Y problem"   (overused — now an AI tell)
"Many [X]s struggle with..."
"As you can see..."
"I want to talk to you about..."
"In this email I'll share..."
"Hope this email finds you well"
```

---

## Universal banned structures

These are structural failures regardless of voice or industry.

- **Symmetrical triplets** — three parallel items of equal length and structure. Break the symmetry — make one shorter, one a question, one a single word.
- **Stacked CTAs** — two or more primary actions in the same email. Pick one. PS can carry a soft secondary; body cannot.
- **Corporate transitions** — "Therefore, it is evident that...", "In conclusion...", "Furthermore...", "Moreover...". Strip on sight.
- **Slab paragraphs** — any paragraph that runs more than three lines on a phone. Break it.
- **Question hooks the reader hasn't earned** — opening with "Have you ever wondered why..." or "What if I told you..." in a cold or low-trust context.
- **Promise-without-payoff** — subject line promises a specific framework or insight; body doesn't deliver one.

---

## Universal formatting rules

- Short paragraphs. Often one sentence. Sometimes two. Never a slab.
- Bold sparingly — one or two phrases per email maximum. Bolding everything bolds nothing.
- Emoji rare. Zero in offer-push emails. One max in casual nurture.
- Parenthetical asides welcome as the "whisper channel" — self-aware, occasionally self-deprecating, never academic.
- Phone test: if a paragraph runs more than three lines on a phone, break it.
- Sign-off: short. The author's name. Optional PS only when it earns its place — extra warmth, a genuine afterthought, or a soft secondary CTA.

---

## Per-client overlay — load at runtime

The filter is universal. The overlay is per-client and loads at scoring time from the buyer's Voice Parameter Block. The diagnostic prompt below references these by name; the runtime substitutes the buyer's values.

| Overlay field | Source in Voice Parameter Block | What the filter uses it for |
|---------------|----------------------------------|------------------------------|
| `banned_words` | Voice Parameter Block → `banned_words` | Voice Integrity check (per-client) |
| `signature_phrases` | Voice Parameter Block → `signature_phrases` | Voice Integrity check — verbatim or not at all |
| `tone_descriptors` | Voice Parameter Block → `tone_descriptors` | Context for the scorer; flagged in fail notes if tone obviously off |
| `funnel_stage_map` | Voice Parameter Block → `funnel_stage_calibration` (optional) | Adjusts dimension weighting per stage — see Calibration below |
| `voice_fingerprint` | Voice Parameter Block → `voice_fingerprint` | High-level reference for "does this sound like them" judgment in fail notes |

If the Voice Parameter Block is unavailable, the filter still runs on universal rules alone — Voice Integrity reduces to the 2-point universal-banned-words check, and per-client checks score 0 (with a flag noting the missing block).

---

## Calibration by funnel stage (generic ladder)

Different relationship stages need different EMBER weights. The default rubric scores all dimensions at the weights above. Calibrated mode rebalances per stage.

| Stage | Description | Weight shift |
|-------|-------------|--------------|
| **COLD** | First touch, re-engagement wake-up, cold list, prospecting | Edge +5, Break -5. Reader doesn't trust the author yet — full savage swing can feel aggressive. Hook does more work. |
| **WARM** | Active nurture, value drops, weekly cadence, returning audience | Default weights. Mode and Break both carry full load — reader is deciding whether the author is worth their continued attention. |
| **ENGAGED** | Community, partner activation, deeper-trust audience, premium content | Evidence +5, Edge -5. Engaged readers want depth, not hooks. Break can be quieter — half-turn often outperforms full swing. |
| **ADVOCATE** | Referral asks, testimonial requests, mutual moves, existing trust | Voice Integrity +5 (becomes 10 pts), Mode -5. Trust is pre-existing — don't re-prove what's already proven. Asks must honour the relationship. |

A buyer's Voice Parameter Block may include their own funnel-stage taxonomy (e.g. ATTENTION/ACTION/ASSOCIATION/ADVOCATE, AWARENESS/CONSIDERATION/DECISION/RETENTION, etc.). If a `funnel_stage_map` field is present in their block, map their stages to the generic ladder above before applying calibration.

If no calibration is requested, score against default weights.

---

## Copy/paste prompt

Universal. Substitute the bracketed values at runtime.

```
You are scoring an email against the universal EMBER quality rubric.

INPUTS:

The email to score:
[PASTE EMAIL HERE — include subject line, preview text, body, sign-off, PS if any]

The author's Voice Parameter Block (per-client overlay — values to apply during the Voice Integrity check):
[PASTE VOICE PARAMETER BLOCK HERE — or leave empty if unavailable]

Funnel stage (optional — calibrates dimension weights):
[ONE OF: COLD / WARM / ENGAGED / ADVOCATE — or leave blank for default weights]

Campaign context (optional — for fail-note specificity):
[BRIEF DESCRIPTION OF WHO THE READER IS AND WHAT THE CAMPAIGN IS DOING]

SCORE THE EMAIL ON THESE DIMENSIONS:

EDGE (20 pts) — Subject 4–7 words provoking not describing? Preview amplifies, 45–90 chars? First two lines confession/scene/provocation, never setup, never unearned question?

MODE (20 pts) — Specific failure named? Labelled with a two-three-word handle? Reader self-recognises in first third?

BREAK (25 pts — heaviest) — One clear temperature swing? Hard-cut preferred? Warm side genuine, cold side precise? Single-temperature emails fail this dimension entirely.

EVIDENCE (15 pts) — Numbers real, names real, moments real? Zero invented outcomes?

REACH (15 pts) — Exactly one primary CTA? Last-line position? Earned by the body, not a pivot? Specific not vague?

VOICE INTEGRITY (5 pts) — Universal AI-slop banned-words clean? Per-client banned_words from the Voice Parameter Block clean? Signature phrases used verbatim or not at all?

If a funnel stage was supplied, apply the matching weight shift before final scoring.

OUTPUT:

1. Total score out of 100
2. Per-dimension breakdown (Edge __/20, Mode __/20, Break __/25, Evidence __/15, Reach __/15, Voice __/5)
3. PASS / HOLD / KILL verdict (PASS 70+, HOLD 60–69, KILL <60)
4. The #1 reason this email will fail to convert in this stage — be specific and direct. No encouragement. Diagnosis only.
5. The #1 fix that would lift the score most — concrete, applicable, single change.
6. Rewrite the opening (subject + preview + first two lines) at PASS-level quality, in the author's voice as encoded in the Voice Parameter Block.
7. Banned-word and banned-structure hits — list every instance found, with the offending phrase quoted.

Be brutal. The author wants a diagnosis, not a pep talk.
```

---

## Upgrade Pass — turning HOLD into PASS

A HOLD (60–69) usually fails on one or two specific dimensions. The fastest +10–15 typically comes from:

- **Edge fail** (+5 to +10): rewrite the first two lines as confession or scene. Strip preamble. Cut the question if it hasn't been earned.
- **Mode fail** (+5 to +10): name the failure mode with specific nouns. Add a labelled handle if the context allows.
- **Break fail** (+10 to +15): introduce ONE clear temperature swing. Find the coldest true line in the topic, place it. Find where the warm should arrive, hard-cut to it.
- **Evidence fail** (+5 to +10): swap one general claim for one specific number, name, or moment. Cut anything you don't have proof for.
- **Reach fail** (+5 to +10): collapse stacked CTAs to one. Move the action to the last line. Make it specific.
- **Voice fail** (+1 to +3): delete every banned word. Replace paraphrased signature phrases with verbatim or remove.

Do not edit a KILL (<60). The structure is wrong. Rewrite from scratch using the diagnostic notes.

---

## Quality gate — before send

Run every email through this filter. PASS sends. HOLD gets the Upgrade Pass and re-scores. KILL goes back to the generator.

Manual editing of a KILL is forbidden. Editing trains the system toward the editor's voice, not the author's, and degrades every future generation. Re-generate, re-score.

---

*Universal EMBER Filter — voice-agnostic email quality diagnostic — v1.0*
*Composes with: any client's Voice Parameter Block — companions: EMBER Universal Generator, LinkedIn Universal Filter*
