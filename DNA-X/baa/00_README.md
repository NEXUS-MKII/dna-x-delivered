# BAA Partner Hub — Build C Delivery

Buyers Agents Academy · Property Acquisitions Desk · Broker Partner Programme
Built against `dna-x-delivered/specs/builds/build-c.md` v2.0
Voice grounded against John Manciameli Voice Parameter Block v1 · April 2026 (72% confidence)

---

## What this is

A complete Build C delivery for John Manciameli's Buyers Agents Academy, scoped tighter than canonical Build C:

- **Audience is one ICP only** — Australian mortgage brokers who could refer pre-approved investor clients to John's Acquisitions Desk.
- **Quiz is referral-readiness, not relationship depth** — 8 scored questions on whether/how-ready a broker is to actually refer, not which tier of partnership they belong in.
- **Landing page is universal** — single hub for all potential broker partners. Targeting happens post-page through quiz-banded asset reduction.
- **Four readiness bands** drive everything downstream: `READY_NOW`, `WARMING`, `BUILDING`, `NOT_YET_FIT`.

The architecture follows Build C §8 (landing page as universal hub) and §6 (MAX PRO + reduction). The quiz reframe is the one deliberate spec deviation, captured here.

---

## File map

```
baa/
├── 00_README.md                          # this file
├── baa_partner.html                      # universal partner landing page
├── baa_broker_readiness_quiz.html        # 8-question scorecard, client-side scored
├── routing_table.md                      # band → asset/email map (Build C §10)
├── emails/
│   └── day_21_4C_honest_check_in.md      # production 4C email for NOT_YET_FIT band
└── prompts/
    ├── reduction_lead_magnet.md          # ADD ONE checklist reducer (4 bands)
    ├── reduction_pcd.md                  # Partner Comms Doc reducer (4 bands)
    ├── reduction_expectations.md         # Partnership Expectations reducer (4 bands)
    └── email_branch_selector.md          # Day-21 4A/4B/4C selector spec
```

---

## Deploy guide

### Production = Kartra

The landing page and quiz are being rebuilt natively inside Kartra. That's the production surface. This GitHub repo is the canonical reference: the spec the Kartra version implements against, and the source-of-truth for the reduction prompts + 4C email + routing table that drive the post-page automation inside Kartra.

The quiz uses `localStorage` only when run from this repo as a preview — the Kartra version replaces that with a native Kartra form, which auto-tags the broker (`baa_band_*`) on submit. No webhook needed.

### Preview (this repo)

Both HTML files are self-contained: no external CSS or JS dependencies beyond Google Fonts. Open `baa_partner.html` locally in any browser to preview. The Hero CTA, attention-strip Step 01, the Quiz CTA section, and the Practice Card all route to the quiz via relative link.

### If a static GitHub Pages copy is ever wanted

```bash
git add DNA-X/baa/
git commit -m "Add BAA partner hub — Build C delivery v2"
git push origin main
```

Would go live at `https://nexus-mkii.github.io/dna-x-delivered/DNA-X/baa/baa_partner.html` (~60 seconds after push).

---

## Operator runbook (what John or his VA does)

### When a broker takes the quiz

1. Browser scores the quiz client-side and renders the result. Result + answers are saved to `localStorage` under key `baa_quiz_result`.
2. **Wire the email submission** (current quiz uses local-only capture). When ready for production, attach the submit handler to a Kartra form action or webhook.
3. Set the Kartra tag matching the band (`baa_band_ready_now` / `baa_band_warming` / `baa_band_building` / `baa_band_notyet`). See `routing_table.md` for full tag map.
4. Day 0 email auto-fires. The email body is universal per `Partner_Pack_BAA_v2.docx` §8. The attached **asset** differs per band.

### When generating the band-appropriate attachments

For each band, run the reduction prompts in `prompts/`:

1. Open a Claude conversation.
2. Paste the **VOICE_PARAMETER_BLOCK** from `BAA_John_Voice_Parameter_Block_v1_April2026.docx` as the first message.
3. Paste the relevant reduction prompt (`reduction_lead_magnet.md`, `reduction_pcd.md`, or `reduction_expectations.md`).
4. Paste the MAX PRO content (from `Partner_Pack_BAA_v2.docx`).
5. State the band as the last line: e.g. `Band: WARMING`.
6. Output is the asset, ready to attach.

Pre-generating all 4 versions per asset and storing as Kartra-uploaded files is the cleaner production setup. Run once, attach automatically by tag.

### Day-21 email branch selection

See `prompts/email_branch_selector.md`. Four Day-21 variants exist (4B / 4A / 4A-modified / 4C-honest). The broker's band tag fires the matching email and suppresses the others.

---

## Voice gates on every output

These apply to every asset generated through these prompts. They are non-negotiable.

- **Banned words**: leverage, synergy, paradigm shift, game-changer, "Here's the thing", "Let's dive in", "In today's fast-paced world", "unlock the power of", transform, revolutionise, holistic, seamless, robust, cutting-edge, best-in-class.
- **No em dashes** anywhere. Use commas, periods, or split into shorter sentences.
- **"For example" at least once per 150-200 words** in any prose asset. This is John's most distinctive device.
- **Mirror-question hook OR failure-mode declaration** to open. Never context or background.
- **Crystallisation close**. Principle or invitation. Never a summary.
- **M-S-S-S paragraph rhythm**. Medium setup, three short punches.
- **Every commitment carries a timeframe or measurable signal**. "We respond within 24 hours" is the bar.

The quality gate is `Page_Landing_Result_Scoring_Rubric.md` for the landing page, `Lead_Magnet_Scoring_Rubric.md` for ADD ONE, `EMBER_Universal_Filter.md` for emails, and the §4.1 drift signals for everything else.

---

## What's intentionally different from canonical Build C

| Canonical Build C | BAA delivery | Reason |
|---|---|---|
| 10±2 questions, 4 relationship-depth tiers (P-Pool / Pro-Motor / Vortex / Mastermind) | 8 scored + 2 open, 4 readiness bands (READY_NOW / WARMING / BUILDING / NOT_YET_FIT) | John's partner scheme is tighter than canonical. Single ICP (AU mortgage brokers). Tiering by depth doesn't fit. Tiering by referral readiness does. |
| Day-21 splits 4A (light) vs 4B (deep) | Day-21 splits 4A / 4B / 4C (honest check-in) | NOT_YET_FIT band needs a Day-21 that honours the honest exit John offered at result time. Canonical 4A is still CTA-forward. 4C is genuinely soft. |
| Partner landing page hub for any partner type | Single-ICP broker hub | Targeting is at post-page asset reduction, not at landing page intent. Landing speaks to ALL potential broker partners equally. |
| `Expectations Doc → P-Pool optional / Mastermind MAX PRO` | `Expectations Doc → READY_NOW MAX PRO / WARMING reduced / BUILDING deferred / NOT_YET_FIT skip` | Reaching for a commitments document at the wrong band burns the open door. Honest exit is a feature, not a default. |

All other Build C requirements honoured: VPB grounding, drift detection, NOW footer credit (`Built in partnership with NOW Group · nowgroup.co.nz`), §8.3 section stack on the landing page, §6.1-canonical reduction-prompt shape on every reducer, §10 routing table as a first-class deliverable.

---

## Status

| Asset | Status |
|---|---|
| Landing page (`baa_partner.html`) | ✅ Built — reference spec for the Kartra rebuild |
| Quiz (`baa_broker_readiness_quiz.html`) | ✅ Built — reference spec for the Kartra-native form |
| Routing table (`routing_table.md`) | ✅ Built |
| Reduction prompts (3 + email selector) | ✅ Built |
| Day-21 4C honest check-in (`emails/day_21_4C_honest_check_in.md`) | ✅ Built — EMBER self-score 85/100 |
| MAX PRO assets (ADD ONE / PCD / Expectations) | 📦 Source-of-truth = `Partner_Pack_BAA_v2.docx` — already scored 93/93/PASS in v2 |
| 7-touch email sequence | 📦 Source-of-truth = `Partner_Pack_BAA_v2.docx` §8 + the 4C in `emails/` here |

---

## Open items for the Kartra build-out

1. **Landing page + quiz** — rebuild as Kartra-native pages using these two HTML files as the visual + structural reference. The quiz form replaces the JS-only capture: Kartra auto-tags broker (`baa_band_ready_now` / `baa_band_warming` / `baa_band_building` / `baa_band_notyet`) on submit.
2. **Load all four Day-21 variants** into Kartra (4A and 4B already in `Partner_Pack_BAA_v2.docx` §8; 4C now in `emails/day_21_4C_honest_check_in.md`). Tag-trigger each on the matching band.
3. **Pre-generate all 4 band versions** of ADD ONE / PCD / Expectations once, upload to Kartra, attach by tag on Day 0 / Day 2 / Day 21.
4. **VPB v2 upgrade** — current grounding is v1 at 72% confidence. Upgrade path is in the VPB document itself (raw unscripted session recording + 4 unedited LinkedIn posts).
