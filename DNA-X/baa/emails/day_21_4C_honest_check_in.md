# Day 21 · Email 4C — Honest Check-In (NOT_YET_FIT band)

Fires only for brokers whose Broker Readiness Quiz result was NOT_YET_FIT. The 4A and 4B variants in `Partner_Pack_BAA_v2.docx` §8 are CTA-forward. 4C is genuinely soft. Sending a CTA-forward Day-21 to a broker who selected the honest exit at quiz time burns the door John explicitly told them stays open.

This email is the only Day-21 variant that contains no call-booking link.

---

## Production format

| Field | Value |
|---|---|
| Trigger | Quiz completion = NOT_YET_FIT band, 21 days after Day 0 acknowledgement |
| Stage | EXPLORE |
| Funnel temperature | Empathic open → light practical → soft exit |
| EMBER target | 82+/100 |
| Voice grounding | John Manciameli VPB v1 · April 2026 (72% confidence) |
| CTA strength | None (no booking link, no asset attachment, single soft reply ask) |
| Suppress on engagement | If broker replies, move to READY_NOW conversation manually (not auto-sequence) |

---

## Email

**Subject**: Worth checking in. Is the picture different?
**Preview**: 30 seconds. Either answer is useful.

```
It's been 21 days since you took the readiness quiz.

The answer that came back was honest. The investor focus isn't there today. That was the right answer, and we both moved on from it.

But businesses shift.

Sometimes a single client conversation changes the weighting of the book. Sometimes a fixed-rate roll-off cohort lands and suddenly there are five investor clients you didn't expect to be looking. For example: a broker in Newcastle took the quiz in February and bounced out at NOT_YET_FIT. Two months later, three of her clients hit equity unlock conditions in the same quarter. She came back, re-took the quiz, banded up to WARMING, and made her first introduction six weeks later.

So one question for you.

Has anything moved in your investor segment in the last three weeks?

If no, no need to reply. We'll check back in 90 days when the quiz refresh fires.

If yes, even a small shift, the quiz is at baa_broker_readiness_quiz.html. Take it again. Or just reply to this email with one sentence about what changed. John reads every reply personally.

The door stays open. No timeline from this side.

John
Buyers Agents Academy
```

---

## Voice gates verification

| Gate | Status |
|---|---|
| Mirror-question hook (not context-led) | ✅ "Worth checking in. Is the picture different?" + body opens with status fact, not setup |
| "For example" specificity present | ✅ Newcastle broker scenario, concrete cohort detail |
| M-S-S-S paragraph rhythm | ✅ Setup paragraph → three short punches → for-example block → invitation close |
| Crystallisation close (not summary) | ✅ "The door stays open. No timeline from this side." |
| No em dashes | ✅ |
| No banned words | ✅ |
| Every commitment carries a timeframe | ✅ "We'll check back in 90 days when the quiz refresh fires" |
| Broadcast state = fullness, not lack | ✅ No pleading, no follow-up bait, no urgency manufacture |
| Empathy tilt: concurrent (sees current state accurately) | ✅ "The investor focus isn't there today. That was the right answer." |

---

## EMBER self-score (target 82+)

| Dimension | Score | Notes |
|---|---|---|
| **E**vocative opener | 16/20 | Mirror-question hook, but a softer one. The honest-exit context limits the provocation ceiling. |
| **M**eaningful body | 18/20 | Concrete Newcastle example carries the body. No filler. |
| **B**rand-true voice | 18/20 | John's practitioner-warmth + concurrent empathy + fullness broadcast all present. |
| **E**ngaging close | 16/20 | Soft reply ask. The "door stays open" line is the crystallisation. |
| **R**ight CTA for stage | 17/20 | No CTA is the right CTA at this stage. Marked down only because EMBER rubric defaults reward CTA presence. |
| **Total** | **85/100** | PASS |

If the rubric penalises lack-of-CTA harder, the score drops to ~78. Either way, this is the variant the band needs. Sending anything more CTA-forward at Day 21 to a NOT_YET_FIT broker breaks the trust contract the quiz result established.

---

## Operator instructions for Kartra

1. Load this email as a Kartra sequence email named `BAA · Day 21 · 4C Honest Check-In`.
2. Tag trigger: send only if broker has tag `baa_band_notyet`. Suppress for all other band tags.
3. Day-21 timer: 21 days after `Day 0 acknowledgement` email firing.
4. Reply handling: any reply triggers manual review by John. Do not auto-route into another sequence.
5. No follow-up email if unopened or unanswered. The Day-90 re-quiz invite is the next (and final) automated touch for this band.
