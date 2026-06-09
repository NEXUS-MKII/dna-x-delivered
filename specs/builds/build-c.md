---
spec_version: 1.0
last_updated: 2026-06-09
build_letter: C
build_name: Partner Growth Specialist
tier: 1
tagline: A partnership system in one delivery — landing page, 7-email nurture, the ADD ONE lead magnet
status: live
source: nexus_wow_option_c.py (NEXUS MKII canonical builder)
---

# Option C — Partner Growth Specialist (Tier 1)

> A complete partnership-activation system for one buyer in a single delivery. A live partner-facing landing page + a 7-touch nurture sequence + bios for every surface + the ADD ONE lead magnet that powers reciprocal referrals. The buyer ships partners through it on day one.
>
> Tier 1 one-shot delivery build. Different audience to Build A (Content Pack Pro): Build A reaches the buyer's *clients* (LinkedIn / blog / podcast listeners); Build C reaches the buyer's *partners* (other businesses, referral sources, complementary practitioners).

---

## 1 · Intent

Buyers know they "should have a referral system" but don't have one. Build C ships that system end-to-end:

- A **partner-facing landing page** that converts other practitioners into reciprocal referrers
- A **7-email nurture sequence** that onboards a partner from connection → first referral → ongoing relationship
- A **bio library** the buyer can drop into LinkedIn, email signatures, and spoken introductions
- A **Partnership Expectations document** that sets mutual commitments + escalation paths up-front
- The **ADD ONE lead magnet** — a single high-value diagnostic / self-assessment the partner can hand to *their* clients to provoke a referral

A buyer with no partners on Monday should have a partnership system Friday.

---

## 2 · Commercial structure

- **Setup**: same one-off Tier 1 fee as Builds A/B · ~14-day turnaround
- **No ongoing** — pack is a finite deliverable; buyer can re-engage for a partnership refresh
- **Commercial terms** — NZD excl GST · 7-day payment terms (NOW Group standard)

---

## 3 · Deliverables (one delivery)

The pack contains exactly the following assets. Counts are exact — do not under- or over-deliver.

### 3.1 Partner landing page (HTML)

A single self-contained `<buyer>_partner.html` file ready to host (GitHub Pages, S3, the buyer's own site, anywhere). See §5 for render contract.

Structural sections (in order):
1. **Hero** — eyebrow + tagline (with emphasis phrase) + sub-headline + primary audience
2. **Attention strip** — 4-step partnership flow (Alignment Quiz → Intro Call → First Referral → 24h Response), each with label + description
3. **Reciprocal services list** — variable-length grid of what the buyer offers in exchange (income from finance fees + advisory + asset-side coordination + etc.)
4. **3 referral triggers** — when to refer · the trigger moment · the conversation
5. **4 differentiators** — what makes this partnership distinct from any other
6. **Pull quote** — partner-perspective testimonial or framing line
7. **4 mutual commitments** — what the buyer commits to + what the partner commits to
8. **Quiz CTA** — link to the Alignment Quiz with 4-card cover preview
9. **Practice card** — buyer's introduction, location, contact, website
10. **Footer** — "Part of the NOW Group partnership ecosystem" line

### 3.2 Partner Comms document (.docx — bundled into Drive)

Single Google Doc titled `WOW_OptionC_PartnerPack_<Buyer>_v1`. Sections in publish-order:

| Section | What |
|---|---|
| 1. Partner Onboarding overview | The 4-step flow described in the landing page + what the buyer does at each step |
| 2. Partnership Philosophy | The buyer's stated belief about why referrals work + 3-paragraph framing |
| 3. Referral Triggers (3) | Detailed scenarios — what the partner sees in their client's situation + the trigger phrase to surface a referral |
| 4. Internal Partner Management sequence | The buyer's internal CRM workflow when a new partner signs up — tag, task, follow-up cadence |
| 5. ADD ONE Lead Magnet | The full asset content — 4 sections + red-flag bar + Gamma prompt + recommended publishing format |
| 6. Bio Library | 3 formats: LinkedIn bio (~250 chars) + Email signature (~120 chars) + Spoken intro (~30 seconds when read aloud) |
| 7. Partnership Expectations Doc | Mutual commitments, 90-day success outcomes, what to escalate, communication cadence |
| 8. Email Templates × 7 | Day 0 / 7 / 9 / 21A / 21B / 30 / 60 (see §3.3) |

### 3.3 7-touch email nurture sequence

| Day | Email | Purpose |
|---|---|---|
| 0 | Welcome | Partner signed up — sets tone, points at the Alignment Quiz |
| 7 | Quiz follow-up | If quiz not completed; if completed, summary + insights |
| 9 | Partner Conversation Document (PCD) | Asks partner for a single high-value scenario for the buyer to anchor the relationship on |
| 21A | Session booking — direct CTA | The first joint client / introduction call |
| 21B | Session booking — soft CTA | A/B variant for partners who haven't engaged the direct version |
| 30 | Referral log | Asks the partner to log a referral attempt — successful or not — to start the data |
| 60 | Re-engagement | For partners who haven't moved — gentle restart with a new angle |

All 7 use the buyer's voice (Voice Parameter Block applied) and reference the buyer's actual service mix.

### 3.4 ADD ONE lead magnet (Gamma prompt + content YAML)

A single high-value asset the buyer can hand any partner to drop into their own client workflow. Format: 4-section diagnostic or self-assessment + red-flag bar. Delivered as:
- Full content (4 sections + red flag + intro + CTA) in the master doc
- Gamma prompt for visual generation
- YAML structured data for downstream lm_builder pipelines (optional)

### 3.5 Bundle

| File | Format |
|---|---|
| `<slug>_partner.html` | Standalone HTML — ready to host |
| `WOW_OptionC_PartnerPack_<Buyer>_v1` | Google Doc with all copy + emails + Gamma prompts |
| `00_START_HERE.txt` | What's in the pack + how to deploy the landing page |
| `gamma_links.txt` | One Gamma URL for the ADD ONE asset |

---

## 4 · Inputs required

The build prefers structured intake from the buyer; falls back to ICP-derived content if intake isn't available.

### 4.1 Required
- Buyer name + business / trading name + role + sector + location
- Website + LinkedIn URL
- Primary audience description (who the buyer's clients are)
- Voice sample: written content excerpt OR transcript (~1500 chars sufficient)
- Brand palette: primary, secondary, accent, cta (hex codes)
- Brand fonts: display + body (Google Fonts family names)
- Buyer email (for Drive share at the end)

### 4.2 Strongly recommended (used directly if provided)
Structured partner intake — the buyer's answers to:
- **Hero tagline** (before-phrase + emphasis-phrase split, e.g. "You're already halfway a *buyer's agent*")
- **Reciprocal items list** — what the buyer offers in exchange for referrals
- **3 referral triggers** — scenarios where a partner should think of the buyer
- **4 differentiators** — what makes this partnership different
- **4 mutual commitments** — buyer's + partner's
- **Quiz URL** — the Alignment Quiz the partner takes to start the flow

If intake not provided, the build derives all of the above from the buyer's ICP + services + Voice Parameter Block.

### 4.3 Recommended (use defaults if missing — flag the substitution)
- Voice Parameter Block (drives banned words + signature move + register)
- Person photo URL · logo URL · primary domain
- Extended palette: ink, body, cream, mozzarella, rule, red-flag

---

## 5 · Partner landing page render contract

Write **fully populated HTML directly** — no template tokens, no `{{ }}` syntax surviving. Single self-contained `.html` ready to host.

### 5.1 Required structure
- Self-contained `<style>` block in `<head>` — no external CSS files
- Google Fonts loaded via `<link>` for buyer's display + body families
- Responsive: mobile-first, breakpoints at 720px and 1080px
- Smooth-scroll behaviour on hash links
- Hero image optional (slot reserved — use Gamma-generated or skip)

### 5.2 CSS custom properties (populate from buyer palette as literal hex values)
```
--primary       (buyer.palette.primary)
--secondary     (buyer.palette.secondary)
--accent        (buyer.palette.accent)
--cta           (buyer.palette.cta)
--ink           (default #0F172A)
--body          (default #374151)
--cream         (default #FAFAF9)
--mozzarella    (default #F5F5F4)
--rule          (default #E5E7EB)
--red-flag      (default #DC2626)
```

### 5.3 Section style notes
- **Hero**: large display type, eyebrow micro-line above (uppercase + letter-spacing), pull-quote treatment for the emphasis phrase
- **Attention strip**: 4-column grid on desktop, stacks on mobile; each step numbered with accent-coloured pill
- **Differentiators**: 2×2 grid with accent-bordered cards
- **Pull quote**: cream-backed with large opening/closing quote glyphs, italics, attribution underneath
- **Mutual commitments**: side-by-side "Buyer commits to" / "Partner commits to" if pair-able, else 2×2 grid
- **Quiz CTA**: prominent button + 4 small cover preview cards beneath
- **Practice card**: dark-backed footer card with buyer's intro + location + website + accent-coloured CTA

### 5.4 No deployment in the skill
The Python pipeline auto-deploys via GitHub Pages to `https://netsync.nowgroup.co.nz/wow/<slug>.html`. The Claude.ai skill produces a clean self-contained HTML file — buyer or Chris deploys separately (paste into Kajabi page, push to operator's GitHub Pages, host on the buyer's own server, etc.).

---

## 6 · Voice + brand layer

- **Buyer brand** — `force_now_palette=False` (all client-facing assets render in buyer palette/fonts)
- **Voice Parameter Block** drives:
  - All landing page body copy
  - All 7 email bodies + subject lines
  - All 3 bio variants
  - The ADD ONE asset content
- **NOW voice** appears only in `00_START_HERE.txt` framing
- **Voice rules** (non-negotiable):
  - Plain English. Short sentences. No fluff.
  - Partnership-first: "you'll send" / "you'll receive" framing, not "we offer" / "we provide"
  - Concrete: every commitment includes a timeframe or measurable signal
  - Reciprocal energy: equal weight on what the buyer GIVES and what the buyer GETS
  - Auto-banned: synergy, leverage, paradigm, best-in-class, digital transformation, "value-add", "win-win" (plus buyer's own banned list)

---

## 7 · Quality gates

Fetch each rubric on demand (only when scoring the matching asset type — keeps token use low). Auto-regen on score < 8/10, one retry max.

| Asset type | Rubric URL |
|---|---|
| Partner landing page HTML | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Page_Landing_Result_Scoring_Rubric.md |
| 7-email nurture sequence | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/EMBER_Universal_Filter.md |
| ADD ONE lead magnet copy | https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/filters/Lead_Magnet_Scoring_Rubric.md |
| Bios (LinkedIn / email / spoken) | No rubric — structural correctness check only (length caps, voice fingerprint, no banned phrases) |
| Partnership Expectations Doc | No rubric — checklist: mutual commitments paired, escalation path clear, cadence stated, success criteria measurable |

Universal scorer rubric + per-buyer overlay from the buyer's Voice Parameter Block — never per-buyer-bespoke filter logic.

---

## 8 · Delivery structure (Google Drive)

```
NOW Group — Partner Pack Delivery/
  └── Partner Growth Specialist — <Buyer Name> — <YYYY-MM-DD>/
        ├── 00_START_HERE.txt
        ├── <slug>_partner.html
        ├── WOW_OptionC_PartnerPack_<Buyer>_v1   (Google Doc)
        └── gamma_links.txt   (one Gamma URL: ADD ONE asset)
```

Share permissions: link-view enabled for buyer's email; Chris (chris@nowgroup.co.nz) owner.

---

## 9 · Refinement notes

- **Why partner-facing landing page, not just copy** — partners are time-poor and skeptical; a polished landing page beats a Word doc for first impressions. Sacrifice nothing on substance but raise production value.
- **Why 7 emails, not more or fewer** — covers the full partner activation arc (welcome → quiz → PCD → first session → first referral → re-engagement) without becoming nurture-spam. A/B at Day 21 because that's the conversion choke point.
- **Why the ADD ONE asset** — partners refer faster when they have a *thing* to hand over. A high-value diagnostic the partner gives to *their* client triggers conversations the partner couldn't initiate alone.
- **Open spec question** — should the ADD ONE asset have a fixed structure (4-section diagnostic) or adapt to buyer's domain? Currently fixed; flag for review after 5 packs.
- **Open spec question** — should email Day 21 have ONE variant or A/B as currently specified? A/B doubles copy work; might consolidate after first 10 packs reveal which converts.

---

## 10 · Canonical Python build (reference)

This spec mirrors the Python pipeline at `NEXUS MKII/nexus_wow_option_c.py`. When drift between this spec and the Python is detected, the Python is canonical for asset shape, and this spec is canonical for the asset roster + voice/brand rules. Reconcile by updating both.

Key Python entry points:
- `generate_pass_1_context_frame()` — context frame + voice prompt prefix
- `generate_pass_2_docx_builder()` — emails + bios + partnership expectations + ADD ONE
- `resolve_option_c_content(profile)` — assembles the placeholder dict from 3-layer priority (intake → Pass 2 → ICP-derived → defaults)
- `fill_template(content)` — substitutes resolved content into the partner-page HTML template
- `run_partner_page_build(profile_id, db)` — orchestrates render + GitHub Pages push

---
