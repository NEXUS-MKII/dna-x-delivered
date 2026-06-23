# Readiness Band → Asset Routing Table

Per Build C spec §10. Required deliverable. This table is the single source of truth for which asset, at what depth, on what cadence, fires for each readiness band.

Table and reduction prompts must agree. If you change a cell here, update the corresponding reduction prompt in `prompts/`.

---

## The four readiness bands

| Band | Quiz signature | What it means |
|---|---|---|
| **READY_NOW** | Mostly A | Investor-focused book, named pre-approval pipeline, advisory work happening, knows who to call. First introduction this month. |
| **WARMING** | Mostly B | Real investor potential in database, advisory instinct present, activation rhythm not running yet. First intro inside 30 to 45 days. |
| **BUILDING** | Mostly C | Adjacent fit. Investor segment thin or under-activated. Database scan needed before partnership conversation. 60 to 90 day cycle. |
| **NOT_YET_FIT** | Mostly D | Owner-occupier or FHB focus. Honest exit. Door stays open with no follow-up cadence. |

Tie-break: highest readiness wins (A > B > C > D).

---

## Asset routing

| Asset / Email | READY_NOW | WARMING | BUILDING | NOT_YET_FIT |
|---|---|---|---|---|
| **Day 0 — Quiz acknowledgement** | ✅ Send (full) | ✅ Send (full) | ✅ Send (full) | ✅ Send (warm honest variant) |
| **ADD ONE Lead Magnet** | ✅ MAX PRO + intent footer | ✅ MAX PRO minus fees objection | ✅ 2-section simplified | ⬜ Replaced by "When the focus shifts" one-pager |
| **Day 2 — Tier-reduced PCD** | ✅ MAX PRO PCD | ✅ 3-section PCD (no internal mgmt) | ✅ 1-page summary PCD | ⬜ Skip |
| **Day 9 — One scenario question** | ✅ Send | ✅ Send | ⬜ Skip (premature) | ⬜ Skip |
| **Day 21 — Email 4 branch** | 4B (deep, hard CTA) | 4A (light, medium CTA) | 4A modified (soft, 60-day frame) | 4C (honest check-in, no CTA) |
| **Day 21 — Expectations Document** | ✅ MAX PRO | ✅ Reduced (drop non-compete + escalation) | ⬜ Deferred ("build together later" note) | ⬜ Skip entirely |
| **Day 30 — Activity check-in** | ✅ Send | ✅ Send | ⬜ Skip | ⬜ Skip |
| **Day 60 — "Should we park this?"** | ✅ Send | ✅ Send | ✅ Send (rephrased as "what surfaced?") | ⬜ Skip |
| **Day 90 — Re-take quiz invite** | ✅ Send (quarterly refresh) | ✅ Send (quarterly refresh) | ✅ Send (the right cadence for this band) | ✅ Send (only quarterly touch for this band) |

---

## Cadence per band

| Band | Cadence between active touches | Quarterly review |
|---|---|---|
| READY_NOW | Weekly or fortnightly once first deal in flight | Yes (active partner) |
| WARMING | Fortnightly through Days 0–60. Monthly after Day 60. | Yes |
| BUILDING | One touch per fortnight through Day 60. Then quarterly. | At 90-day re-quiz |
| NOT_YET_FIT | Three touches: Day 0 acknowledgement + Day 21 4C honest check-in + Day 90 re-quiz invite. Nothing in between. | Quarterly re-quiz only |

---

## Kartra tag map

| Band | Set tag on quiz submit | Active tags during sequence | Suppress tags on completion |
|---|---|---|---|
| READY_NOW | `baa_band_ready_now` | `baa_partner_active` after Day 21 | `baa_band_warming`, `baa_band_building`, `baa_band_notyet` |
| WARMING | `baa_band_warming` | `baa_partner_warming` through Day 60 | other band tags |
| BUILDING | `baa_band_building` | `baa_partner_building` through Day 60 | other band tags |
| NOT_YET_FIT | `baa_band_notyet` | `baa_partner_dormant` after Day 0 | other band tags |

If a partner re-takes the quiz at Day 90 and bands up, the new tag overwrites the old. Operator manually moves them to the higher-band sequence at the Day-2 trigger.

---

## Operator kill switches (per Build C §9)

| When | Stage | Action | Kill switch |
|---|---|---|---|
| Day 0 | Quiz submission | Auto-send acknowledgement + Lead Magnet by band | No quiz response in 7 days → one follow-up. Still none → tag `baa_dormant` |
| Day 7 | PCD delivered | Auto-send tier-reduced PCD | Email 2 unopened in 5 days → resend with varied subject |
| Day 9 | One-scenario nudge | Personal-from-John email asking for one client situation | No reply → keep on cadence, do not chase |
| Day 21 | Email 4 branch | Send 4A/4B/4C per band | No engagement on 4B in 14 days → drop to WARMING cadence. No engagement on 4A in 14 days → tag `baa_dormant` |
| Day 30 | Activity check-in | Did the broker introduce anyone? | One-directional referrals raised at next intro call |
| Day 60 | "Should we park this?" | Honest re-engagement | Reply says "wrong fit" → close file, no further contact |
| Day 90 | Quarterly re-quiz | Re-send quiz link. Re-tag on completion | Band drop two consecutive quarters → realignment conversation or exit |

---

## Where each band's first email lands

The Day 0 email mentions the lead magnet differently per band. Operator must match.

- **READY_NOW** Day 0 reads: *"Attached is the broker activation checklist. You'll use it on the first call. Identify two clients who score 4 or 5 by the end of this week and reply with the situation."*
- **WARMING** Day 0 reads: *"Attached is the broker activation checklist. Print it. Use it on one client this week. Reply with what surfaced."*
- **BUILDING** Day 0 reads: *"Attached is the broker readiness checklist. Use it as a database scan over the next fortnight. When one client scores 4 or 5, that's the moment for the intro call."*
- **NOT_YET_FIT** Day 0 reads: *"Thanks for taking the quiz honestly. Attached is John's short note on what to watch for in your own book that might signal the picture is shifting. The door stays open. Re-take the quiz any time."*

All four Day-0 emails are universal in the canonical sequence per §7. The difference is the attached asset, generated by the reduction prompts, not the email body. The email body is the same template across all four bands.
