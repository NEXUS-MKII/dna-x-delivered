# X-Gen (GX-1) Opener Engines — VA Install Advisory

Per-client opener engines, part of NOW Group's **X-Gen (GX-1)** lead-gen product and **provisioned by NOW Group** (provider of both the leads and the software). A VA installs one by dropping a short message into a **fresh Claude thread** (claude.ai) — Claude fetches the engine, rebuilds it as an artifact in the VA's own gallery, and briefs them on use. The engine runs on the **VA's own Claude/API access**, so generation is billed to their account.

**Files (public, served from the DNA-X repo):**
| Client | Fetch URL (installer uses this) | Live preview |
|---|---|---|
| Farhad — Dream Websites | `https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/farhad_opener_engine.html` | https://nexus-mkii.github.io/dna-x-delivered/DNA-X/x-gen/farhad_opener_engine.html |
| Tawanda — Kieser Mosman | `https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/tawanda_opener_engine.html` | https://nexus-mkii.github.io/dna-x-delivered/DNA-X/x-gen/tawanda_opener_engine.html |
| Zoltan — Marksmen IT | `https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/marksmen_opener_engine.html` | https://nexus-mkii.github.io/dna-x-delivered/DNA-X/x-gen/marksmen_opener_engine.html |

---

## 1. Installer messages (what the VA pastes)

The VA opens a **new claude.ai thread** and pastes the block for their client. Nothing else.

### Farhad — Dream Websites (website-rebuild outreach)
```
Please install my NOW Group X-Gen Opener Engine.
1. Fetch the file at this URL: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/farhad_opener_engine.html
2. Reproduce it EXACTLY as a single HTML artifact — byte for byte. Do not edit,
   summarise, restyle, or add any commentary inside the artifact.
3. After it renders, give me a 5-line quick-start for using it.
This is a NOW Group tool; the file is complete and self-contained.
```

### Tawanda — Kieser Mosman (medical referral outreach)
```
Please install my NOW Group X-Gen Opener Engine.
1. Fetch the file at this URL: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/tawanda_opener_engine.html
2. Reproduce it EXACTLY as a single HTML artifact — byte for byte. Do not edit,
   summarise, restyle, or add any commentary inside the artifact.
3. After it renders, give me a 5-line quick-start for using it.
This is a NOW Group tool; the file is complete and self-contained.
```

### Zoltan — Marksmen IT (managed-IT outreach)
```
Please install my NOW Group X-Gen Opener Engine.
1. Fetch the file at this URL: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/DNA-X/x-gen/marksmen_opener_engine.html
2. Reproduce it EXACTLY as a single HTML artifact — byte for byte. Do not edit,
   summarise, restyle, or add any commentary inside the artifact.
3. After it renders, give me a 5-line quick-start for using it.
This is a NOW Group tool; the file is complete and self-contained.
```

---

## 2. Usage guide (Claude relays this; also here for reference)

1. **First run only — if "Generate" shows `Failed to fetch`:** the tool needs Claude API access. Re-grant it in the artifact's permission/connector UI, then try again. (One-time setup gotcha.)
2. **Get leads:** open the client's NOW Group lead sheet, copy the rows you're working today (copying from the sheet is tab-separated — the tool handles that).
3. **Paste** into the **Batch** tab, one lead per line. Leave **"Auto-find owner / clinician"** ticked.
4. **Angle + Sender:** pick the angle and set the sender name.
5. **Generate.** For each lead: 3 email variants (A/B/C) + rationale, a LinkedIn connection note, subject lines, and a quality-gate check.
6. **Read the badge** at the top of each card:
   - ◆ green **"found"** — a named owner/clinician was located; the opener is addressed to them.
   - ○ amber **"No confident … found"** — none found online; you get a company/practice-level opener (never a made-up name). Normal for some leads (more common for trades, rarer for medical).
   - ○ amber **"Enrichment unavailable"** — the runtime blocked web search; use the manual LinkedIn/Website fields, or ask NOW Group for pre-enriched rows.
7. **Copy** the variant you want and send. Follow the **Day 0 → 21 channel sequence** shown in the LinkedIn tab.

---

## 3. Notes for the VA
- **Runs on your Claude.** Generation and any web-search enrichment bill your account, not NOW Group's.
- **It never invents a person.** No confident match = no name. By design (a wrong name is unrecoverable, especially in medical referrals).
- **Voice + rules are baked in** (NOW Group / Chris White register; no em dashes; the medical version blocks testimonials per AHPRA). Don't override them.
- **Updates:** NOW Group maintains the engine. If a new version ships, re-run the installer message to rebuild the artifact from the latest file.

---

## 4. For NOW Group (maintainer notes)
- Source of truth: `baa-booking-test/openers/` (private); published copies here in `dna-x-delivered/DNA-X/x-gen/` (public) for VA fetch.
- Model pinned `claude-sonnet-4-6`; bump to `claude-sonnet-5` once confirmed in the artifact runtime.
- Batch enrichment fallback: `scripts/enrich_key_person.js --profile trades|medical` pre-fills `decision_maker_name` so the opener reads names directly — use when in-artifact web search isn't available.
- New client = clone an engine, swap ICP/voice/enrichment profile, drop the file here, add an installer block above.
