---
spec_version: 1.0
last_updated: 2026-06-02
build_letter: GX-1
build_name: Acquisition
tier: 3
tagline: Done Now, Acquisition
status: live
references:
  - specs/tiers/tier-3.md
source: _source/X-Ponential_Tier_3_Architecture_2026-05-30.docx
---

# GX-1 — Acquisition

> LinkedIn appointment-setting. 50/50 ICP/IPP split. Manual, personalised outreach. Booked conversations — the close is yours.
>
> First Tier 3 product. Reference for every GX-N product that follows.

## 1. Intent

GX-1 is a managed LinkedIn outreach product for B2B operators who need a predictable flow of qualified conversations but can't run prospecting in-house. NOW builds the system (audit, ICP/IPP, lead lists, content factory, reporting), recruits and trains the VA Channel Manager who runs the daily outreach, then refreshes the content monthly. The client closes and delivers — that's the only piece they do. Outcome: 60–120 booked conversations a year, ICP-fit, with the buyer pre-diagnosed before the call.

## 2. Commercial structure

- **Setup**: $2,000 NZD excl GST · one-off · 3-week build
- **Ongoing Lite**: $997/mo · 60 conversations · 6 booked meetings/month
- **Ongoing Pro**: $1,997/mo · 120 conversations · 12 booked meetings/month + Content Factory
- **Risk reversal**: $100 credit per missed booked conversation against the tier guarantee
- **Common Tier 3 terms apply** — see `specs/tiers/tier-3.md` §2

## 3. Deliverables (Setup phase, 3 weeks)

| Name | Format | Where it lands | Voice / brand layer |
|---|---|---|---|
| SGT Audit | PDF | Client Drive folder + thank-you email | Buyer brand |
| ICP profile + IPP profile | Markdown + visual one-pager | Drive | Buyer brand |
| Lead enrichment list (50+ prospects/channel) | CSV via SerpAPI | Drive (encrypted) | n/a |
| Channel Manager recruitment + briefing + training | Internal NOW playbook + recorded onboarding | Internal Drive | NOW voice |
| LinkedIn Sales Navigator setup | Client account, billed direct to client | Client's LinkedIn | n/a |
| Outreach system build (sequences, message templates, response playbook) | Docs in client Drive | Drive | Buyer voice (DNA-derived) |
| Content factory setup (monthly content briefing template + asset library) | Template + first month's pack | Drive | Buyer voice |
| Weekly reporting framework | Google Sheet + Looker Studio (optional) | Shared Drive | NOW visual + buyer brand on metrics |
| Live walkthrough on handover | 45–60 min Zoom + recording | Recording in Drive | n/a |

## 4. Inputs required

- **From intake form** — buyer-side: company, ICP description (rough), industry, target geo, existing LinkedIn presence URL, NZ/AU/US/EU market focus
- **From brand discovery** — palette, logo, font, tone (for Drive asset branding + report theming)
- **From Voice Parameter Block** — tone-of-voice section, banned phrases, register, the "for example" tell pattern (or equivalent buyer tell)
- **From SGT Audit (NOW-produced during setup)** — Strengths / Gaps / Targets analysis, used to finalise ICP/IPP split
- **From other builds** — none required, but stacks naturally with **Build D (Quiz Funnel)** for inbound capture and **Build E (GEO+SEO Authority)** for credibility uplift on prospect research

## 5. Voice + brand layer

- **Buyer brand** — `force_now_palette=False` (Tier 3 is bespoke buyer brand)
- **Voice Parameter Block** drives:
  - Outreach message templates (1st message + 3 follow-up steps)
  - Content factory monthly briefings
  - Weekly report narrative section ("This week's signal")
- **NOW voice** appears only in:
  - Internal Channel Manager training docs
  - SGT Audit framing language

## 6. Quality gates

- **Outreach message templates** — `lm_filter` (Lead Magnet filter) — must pass tone + buyer-voice + no-template-cliché thresholds. Auto-regen on score < 8/10.
- **SGT Audit PDF** — `page_filter` — structural compliance (sections complete) + voice score
- **Monthly content factory pack** — `article_filter` + `carousel_filter` depending on asset format
- **Weekly reports** — manual NOW review on first 4 weeks of every engagement; thereafter spot-check monthly

## 7. Refinement notes

- **Channel Manager attribution to VA World** is structural — every GX-1 setup hands the operations to a VA World-recruited Channel Manager. Margin split + onboarding flow tracked in VA World partner agreement (see `AUBIT_for_Aaron/` registry).
- **SerpAPI** is the canonical lead enrichment source. If lead volume needs to scale beyond SerpAPI quotas, escalate to Aaron (AUBIT-TMT partner) for AUBIT Network lookup.
- **LinkedIn Sales Navigator billing** stays direct client → LinkedIn. NOW never marks up software. State this upfront in checkout copy to pre-empt confusion.
- **Open spec question** — should the Content Factory monthly briefing include AI-drafted post copy (faster, cheaper) or stay human-Channel-Manager-drafted (higher voice fidelity)? Current spec = human-drafted; flag for review after 3 active clients.
- **Open spec question** — should the 14-day clarification window after handover be 14 days or 21? GX-3 uses 14, but GX-1 systems take longer to start producing signal. Flag for 90-day review.

---

## 8. Kajabi SKU configuration

Three offers in Kajabi: Setup (single payment) + two ongoing tiers (monthly subscription).

### Offer 1 — Setup & Onboarding

| Field | Value |
|---|---|
| Internal offer name | NOW GX-1 — Acquisition Setup & Onboarding |
| Public offer name | GX-1 Acquisition — Setup & System Build |
| Offer type | Single payment |
| Price | $2,000 NZD (excl GST) |
| Tax setting | Exclusive of GST (B2B standard) |
| Recurrence | One-time payment |

### Offer 2 — Acquisition Lite (ongoing)

| Field | Value |
|---|---|
| Internal offer name | NOW GX-1 — Acquisition Lite (monthly) |
| Public offer name | Acquisition Lite — 60 conversations, 6 meetings |
| Offer type | Subscription — recurring monthly |
| Price | $997 NZD/month (excl GST) |
| Recurrence | Monthly · 30-day notice exit after 90-day review |
| Gating | Sellable only to clients who have paid GX-1 Setup |

### Offer 3 — Acquisition Pro (ongoing)

| Field | Value |
|---|---|
| Internal offer name | NOW GX-1 — Acquisition Pro (monthly) |
| Public offer name | Acquisition Pro — 120 conversations, 12 meetings + Content Factory |
| Offer type | Subscription — recurring monthly |
| Price | $1,997 NZD/month (excl GST) |
| Recurrence | Monthly · 30-day notice exit after 90-day review |
| Gating | Sellable only to clients who have paid GX-1 Setup |

### Checkout copy — Setup

```
HEADLINE:    GX-1 Acquisition — Setup & System Build
SUBHEAD:     LinkedIn outreach that diagnoses your buyer
             before the call. Manual. Personalised. Booked.
BULLETS:
  • SGT Audit + ICP / IPP profile finalisation
  • Lead enrichment via SerpAPI (50+ prospects per channel)
  • Channel Manager recruitment, briefing, and training
  • LinkedIn Sales Navigator setup (subscription billed direct)
  • Outreach system build + content factory setup
  • Weekly reporting framework deployed from week one
  • Three-week build · Live walkthrough on handover
GUARANTEE:   We aim for 90–95% execution on system build.
             14-day clarification window after handover.
             Setup is non-refundable but the 90-day exit
             clause protects your ongoing commitment.
CTA:         Start GX-1 Acquisition — $2,000
```

### Thank-you page after Setup purchase

```
HEADLINE:    You're in. GX-1 Acquisition begins now.
BODY:        Two things land in your inbox in the next
             hour. First — the NET_SYNC onboarding form
             (your ICP + IPP intake). Second — a Calendly
             link to book your 45-minute discovery call.
             Both emails come from chris@nowgroup.co.nz.
CTA:         Complete NET_SYNC before our discovery call.
             It cuts our session from cold-start to warm-start.
```

## 9. Partner orchestration

- **Partner type** — VA World Channel Manager (single partner, no shortlist for GX-1 — VA World is the canonical channel)
- **Vetting criteria** (in addition to universal Tier 3 criteria in `tiers/tier-3.md` §5):
  - Demonstrated LinkedIn-specific outreach experience (not generic VA work)
  - Native or fluent English (outreach voice depends on it)
  - Comfort operating LinkedIn Sales Navigator + Calendly + CRM-of-choice
  - Willing to follow NOW outreach playbook without injecting templates from prior work
- **Three-way value flow** (specialised from `tiers/tier-3.md` §5):
  - CLIENT pays NOW: $2k setup + $997/$1,997 monthly tier
  - CLIENT pays LinkedIn directly: Sales Navigator subscription (~$80–$160/mo)
  - VA World pays Channel Manager their hourly rate
  - NOW pays VA World a monthly Channel Manager fee per active client (recurring B2B revenue)
- **Partner-content subscription** — VA World may take a content refresh subscription from NOW once they have 3+ active GX-1 clients (per `tiers/tier-3.md` §5 partner-content model)

## 10. Ongoing tier structure

### Acquisition Lite — $997/month

- **Volume guarantee**: 60 booked conversations · 6 confirmed meetings per month
- **Content factory cadence**: 1 monthly content refresh pack (4 LinkedIn posts + 2 follow-up message variants)
- **Weekly reporting**: standardised dashboard, asynchronous
- **NOW oversight**: monthly check-in (30 min)

### Acquisition Pro — $1,997/month

- **Everything in Lite, plus**:
- **Volume guarantee**: 120 booked conversations · 12 confirmed meetings per month
- **Content factory cadence**: 1 weekly content refresh (vs Lite's monthly) + Channel Manager content suggestions reviewed by NOW
- **Weekly reporting**: dashboard + 15-min weekly synchronous review with Channel Manager
- **NOW oversight**: bi-weekly strategy call (45 min)
- **Performance-tied creative variants**: top-performing post templates auto-promoted into next month's pack

### Common terms

- 90-day performance review built in (formal review at month 3 — go/exit decision)
- 30 days written notice after the 90-day review for either party to exit ongoing
- Setup fee non-refundable
- All fees NZD excl GST · 7-day payment terms
- NOW manages VA World relationship — client never deals with Channel Manager admin issues directly

## 11. Bundle math

GX-1 is the most-bundled Tier 3 product (lowest-cost setup, broadest applicability).

| Bundle | Composition | Stand-alone | Bundled | Save |
|---|---|---|---|---|
| D + GX-1 | Quiz Funnel + Acquisition Setup | $4,497 | $3,997 | $500 |
| E + GX-1 | GEO/SEO + Acquisition Setup | $3,997 | $3,497 | $500 |
| D+E+F + GX-1 | Complete Factory + Acquisition Setup | $7,997 | $7,497 | $500 |
| D+E+F + GX-1+GX-2+GX-3 | **THE COMPLETE GENOME** | $15,988 | $14,997 | $991 |

Bundle pricing rules per `tiers/tier-3.md` §6:
- Bundled price always saves $497–$991 vs stand-alone
- Bundles include **Setup fees only** (ongoing tiers priced separately, sold after Setup completes)
