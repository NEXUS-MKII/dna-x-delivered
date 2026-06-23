# Email Branch Selector

Per Build C spec §7. The 7-touch email sequence (Day 0/7/9/21A/21B/30/60) is universal at most touchpoints. Email 4 (Day 21) is where the sequence branches.

For BAA, the canonical 4A/4B split (Light vs Deep collab) maps to readiness, not relationship depth:

- **4A** — "Quick win: co-host a spotlight" — works for **WARMING** and **BUILDING**. Low-friction first move.
- **4B** — "Map a full partnership strategy" — works for **READY_NOW**. Direct strategy call invite.
- **4C** — "Honest check-in" — **NOT_YET_FIT** gets a different cadence. No 21-day push.

## Day-21 branch decision matrix

| Band | Day 21 fires | Subject | CTA strength | Reduction prompt also runs |
|---|---|---|---|---|
| READY_NOW | 4B (deep) | "Your first introduction. Let's make it this week." | Hard | Lead Magnet MAX PRO (Day 0), PCD MAX PRO (Day 2), Expectations MAX PRO (Day 21) |
| WARMING | 4A (light) | "Not ready to make an introduction yet? Here's what to do instead." | Medium | Lead Magnet WARMING (Day 0), PCD WARMING (Day 2), Expectations WARMING (Day 21) |
| BUILDING | 4A (modified) | "60 days. A database scan. One client." | Soft | Lead Magnet BUILDING (Day 0). PCD/Expectations deferred. |
| NOT_YET_FIT | 4C (honest) | "Worth checking in. Is the picture different?" | Soft | "When the focus shifts" one-pager only. No subsequent assets. |

## 4C — NOT_YET_FIT honest check-in (new variant)

Build C canonical doesn't carry a 4C. BAA needs one because the canonical 4A is still a CTA-forward email, and that breaks the honest exit John gave the broker at quiz time. 4C is genuinely soft.

```
Subject: Worth checking in. Is the picture different?
Preview: 30 seconds. Either answer is useful.

It's been 21 days since you took the readiness quiz.

The answer that came back was honest: the focus isn't there today. That
was the right answer, and we both moved on from it.

But businesses shift. Sometimes a single client conversation changes the
weighting of the book. Sometimes a fixed-rate roll-off cohort lands and
suddenly there are five investor clients you didn't expect.

So one question. Has anything moved in your investor segment in the last
three weeks?

If no, no need to reply. We'll check back in 90 days.

If yes, even a small shift, the quiz is at baa_broker_readiness_quiz.html.
Take it again. Or reply to this email with one sentence about what changed.
John reads every reply personally.

John
Buyers Agents Academy
```

This 4C is the only Day-21 email that does not contain a call booking link. Intentional. NOT_YET_FIT brokers were told the door stays open with no timeline from this side. 4C honours that.

## Voice gates on every Day-21 email

- Opens with a mirror-question or declaration (not context)
- "For example" appears at least once per 200 words
- M-S-S-S paragraph rhythm
- No em dashes
- Banned words list applies
- Crystallisation close

## Operator instruction

Load all four Day-21 variants into Kartra as separate emails tagged with the band. The Day 14 trigger checks the broker's `baa_band` tag (set by quiz submission) and fires the matching email. Suppress the others.
