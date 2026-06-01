---
spec_version: 1.0
last_updated: 2026-06-02
tier: 3
tier_name: X-Ponential
tagline: Where the genome is expressed
source: _source/X-Ponential_Tier_3_Architecture_2026-05-30.docx
status: live
---

# Tier 3 — X-Ponential

> Managed channels · Partner-attributed · Ongoing-by-choice
>
> Cross-cutting orchestration spec for the X-Ponential tier. Per-product specs live at `specs/builds/gx-1.md`, `gx-2.md`, `gx-3.md` and reference this doc.

## 1. Commercial DNA

Tier 1 (WOW Essentials) and Tier 2 (DNAx Builds) are pure deliverables: NOW builds, client owns, no ongoing relationship. Yours forever, no retainer, no expiry.

**Tier 3 breaks that ethos — deliberately.** X-Ponential is the first DNA-X tier with built-in ongoing service. The buyer is no longer receiving assets; they're entering a managed deployment.

The structural difference:

- **Tier 1 & 2** — One-time price. Bespoke creative production. NOW builds and hands over. Client operates everything ongoing themselves.
- **Tier 3** — Setup fee + monthly retainer. NOW builds the foundation. A VA or third-party partner runs the channel ongoing. NOW oversees strategically and refreshes the asset library monthly.

### Why this works for the brand

- **Honest signalling** — Tier 3 is visually different (brushed gold vs warm orange) so buyers immediately understand the commercial structure has changed.
- **Partner amplification** — Each Tier 3 product channels demand to a NOW-vetted partner shortlist. NOW makes the partner. The partner runs the relationship. NOW stays in its lane: strategy and creative.
- **Ring-fenced economics** — Ad spend, software subscriptions, and third-party costs are paid directly by client to provider. NOW never marks up media or tooling. Clean P&L.
- **VA World attribution** — Every Tier 3 product has a VA World line baked into the price. Lifts the VA partnership into a new value tier where attribution is structural, not bolt-on.

## 2. Catalogue at a glance

| Product | Channel | Setup | Lite ongoing | Pro ongoing | Partner |
|---|---|---|---|---|---|
| GX-1 Acquisition | LinkedIn outreach 50/50 ICP/IPP | $2,000 one-off | $997/mo (60 convs · 6 mtgs) | $1,997/mo (120 convs · 12 mtgs) | VA World Channel Manager |
| GX-2 Amplification | Meta Ads + creative refresh | $2,997 one-off | $997/mo (creative refresh) | $1,997/mo (refresh + animations) | Ad partner shortlist + VA scheduling |
| GX-3 Anthology | Video library + monthly refresh | $4,997 (6-wk build) | $497/mo (4 new animations) | $997/mo (Lite + testimonial) | Video editor partner + VA scheduling |

### Risk reversal (per-product)

- **GX-1** — $100 credit per missed booked conversation
- **GX-2** — TBC (partner-run, NOW guarantees content delivery only)
- **GX-3** — Asset volume guarantee — TBC at launch

### Common terms (all Tier 3 products)

- 90-day performance review built into all engagements
- 30 days written notice after 90 days for either party to exit ongoing
- Setup fees non-refundable (cover Phase 1 work already completed)
- All fees NZD excl. GST · 7-day payment terms
- NOW manages all sub-contractor relationships — client never deals with sub-contractors directly

## 3. Naming system — GX-prefix + A-word

Tier 3 products use a dual-naming convention that signals both tier (via GX prefix) and product identity (via A-word, continuing the DNA-X tradition).

**Structure**: `[GX-N] ─ [A-word]    [Product description]`
**Example**: `GX-1 ─ Acquisition   LinkedIn Prospecting`

### Why GX-prefix

- 'G' is the 7th letter — naturally follows A–F (Tier 1 + Tier 2 builds), preserving alphabetical progression
- 'X' anchors the product in the X-Ponential tier — the X is the brand mark for managed-channel category
- Numerical suffix (1, 2, 3...) is launch order — simple, defensible, no hidden logic

### Why A-words

- Continues the Tier 1+2 naming tradition (Authority, Alliance, Activation, Answers, Algorithm, Architecture)
- Maintains the 'Done Now, [A-word]' tagline pattern across the entire DNA-X suite
- Each A-word is a verb-noun describing the channel's effect

### DNA progression maths still works

When a buyer owns Build C + Build E + GX-1, they're at DNA⁷ — seven products into the genome. The G-prefix doesn't break the count, it just signals which tier each product lives in. DNA¹ to DNA⁶ stays within Tier 1+2. DNA⁷ onwards opens the Tier 3 stack.

## 4. Visual treatment — brushed gold

Tier 3 sections on `nowgroup.co.nz/now-dna` use a brushed gold background graphic as the primary tier differentiator. This signals premium / managed category to buyers without needing copy to explain the commercial structure.

### Colour tokens

```css
--dnax-gold-primary:  #D8B162;   /* brushed gold accent */
--dnax-gold-glow:     #E8C17C;   /* hover/active */
--dnax-gold-deep:     #B48C48;   /* shadow depth */
--dnax-gold-light:    #F5E8C7;   /* light overlay */
```

### Background treatment

```css
background:
  /* Brushed texture (subtle horizontal lines) */
  repeating-linear-gradient(90deg,
    transparent 0px,
    rgba(232,193,124,0.04) 1px,
    transparent 2px,
    rgba(196,159,89,0.03) 3px,
    transparent 4px),
  /* Gold gradient overlay */
  linear-gradient(135deg,
    rgba(196,159,89,0.08) 0%,
    rgba(232,193,124,0.12) 25%,
    rgba(196,159,89,0.06) 50%,
    rgba(180,140,72,0.10) 75%,
    rgba(216,177,98,0.08) 100%),
  /* Base warm black */
  #0A0707;
```

### Card treatment within Tier 3

```css
.gx-card {
  border: 1px solid rgba(216,177,98,0.4);
  background: rgba(20,16,14,0.85);
  box-shadow: 0 0 24px -4px rgba(216,177,98,0.25);
}
.gx-card:hover {
  border: 1px solid rgba(232,193,124,0.7);
  box-shadow: 0 0 36px -4px rgba(232,193,124,0.4);
}
```

### Letter badges (GX-prefix display)

```css
.gx-badge {
  background: rgba(216,177,98,0.1);
  border: 1.5px solid rgba(216,177,98,0.4);
  color: #D8B162;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 4px;
}
```

### Tier separator on the page

Between the existing Tier 2 (DNAx Builds) section and the new Tier 3 (X-Ponential) section, add a thin gold rule with the tier-shift announcement:

```html
<hr style="height:2px; background: linear-gradient(90deg, transparent, #D8B162, transparent); border:none;" />
<p class="tier-shift">↓ TIER 3 — X-PONENTIAL — Managed channels begin here ↓</p>
```

## 5. Partner relationships — vetted shortlist model

Every Tier 3 product has at least one third-party partner running ongoing operations. **NOW maintains the shortlist; the client chooses** which partner suits their style and price point.

### Why a shortlist (not a single partner)

- **Negotiating leverage** — Multiple partners compete for client placements. NOW retains the kingmaker position.
- **Client fit** — Different partners suit different ICPs, geographies, and personality types. Letting the client choose increases conversion.
- **Risk distribution** — If one partner has a bad month, the other partners absorb the demand. No single point of failure.

### Universal partner vetting criteria

- Minimum 3 years specific channel experience (LinkedIn / Meta Ads / video editing)
- NZ or AU operating base (timezone alignment, NZBN, insurance verified)
- Reference check with 3+ active clients
- Willingness to operate inside NOW's content framework (no automation, no proprietary playbook conflicts)
- Commercial terms transparent — partner fees disclosed to client upfront
- Willingness to enter a NOW partner agreement (annual renewal)

(Per-product specs may add additional vetting criteria specific to that channel.)

### Commercial structure — three-way value flow

```
CLIENT ──→ pays NOW:     setup + ongoing tier
CLIENT ──→ pays PARTNER: market-rate retainer (direct)
CLIENT ──→ pays MEDIA:   ad spend (direct to Meta / LinkedIn)

NOW    ←── creates content monthly for PARTNER's clients
PARTNER ──→ pays NOW:    content subscription per active client

NOW handles:     Strategy, brand voice, creative production
PARTNER handles: Channel operations, optimisation, reporting
CLIENT handles:  Close, deliver, retain
```

### Partner-content subscription (the second revenue line)

Partners with multiple X-Ponential clients buy a monthly content refresh pack from NOW per active client. This is the recurring B2B revenue that **doesn't break the DNA-X 'yours forever' promise** to end clients.

- **Per-client subscription** — Partner pays NOW a per-client monthly fee for ongoing content production tied to that client's brand DNA. Pricing TBC — recommended $497–$1,497/mo range.
- **Why partners pay this** — Cheaper than hiring an in-house creative team. Faster than briefing freelancers. Higher quality than template libraries. NOW is the embedded creative arm.
- **Why this is sticky** — Once a partner has 3+ clients on the system, switching content suppliers means re-extracting brand voice for every client. Switching costs become structural.

## 6. Bundle math principles

Tier 3 creates new bundle opportunities by combining Tier 2 builds with Tier 3 launchpads. These bundles can be priced and marketed as 'full-stack' offerings.

| Bundle | Composition | Stand-alone | Bundled | Save |
|---|---|---|---|---|
| D + GX-1 | Quiz Funnel + Acquisition Setup | $4,497 | $3,997 | $500 |
| E + GX-1 | GEO/SEO + Acquisition Setup | $3,997 | $3,497 | $500 |
| F + GX-3 | BizCard 2026 + Anthology Setup | $6,994 | $6,497 | $497 |
| D+E+F + GX-1 | Complete Factory + Acquisition Setup | $7,997 | $7,497 | $500 |
| D+E+F + GX-1+GX-2+GX-3 | **THE COMPLETE GENOME** | $15,988 | $14,997 | $991 |

### Bundle pricing rationale

- Bundled price always saves $497–$991 vs stand-alone purchase
- Bundles include **Setup fees only** (ongoing tiers priced separately)
- Largest possible bundle (Complete Genome at $14,997) is the apex Tier 3 offer
- Bundle savings consistent with existing DNAx bundle pattern ($497 standard discount)

## 7. Roadmap — GX-4 and beyond

The X-Ponential tier architecture supports indefinite expansion. Each new managed channel takes the next available GX number and a fresh A-word.

### Candidate Tier 3 products (uncommitted)

- **GX-4 — Audience** — Community/membership channel. Setup + monthly community operations + content.
- **GX-5 — Atmosphere** — PR/podcast/earned-media channel. Setup + ongoing pitching + appearance management.
- **GX-6 — Approach** — Cold email channel. Setup + ongoing list management + sequence operations.
- **GX-7 — Apparatus** — Sales operations channel. Setup + CRM management + sales-cycle ops.
- **GX-8 — Ascension** — Client success / retention channel. Setup + onboarding + retention-call ops.

### Sequencing principles

- Don't launch a new GX product until the previous one has at least **3 active clients** (proves the partner model holds)
- Each new product needs a vetted partner shortlist before public launch
- Each new product needs an LOE template adapted from the GX-1 master
- Each new product needs a Kajabi setup with three offer SKUs (Setup + Lite + Pro)
- Each new product needs page copy matching the established voice and structure

### What to validate at the X-Ponential tier level

- Are the ongoing tier conversion rates from Setup buyers above 60%?
- What's the average customer lifetime value (LTV) across all Tier 3 products?
- Are partners renewing their content subscriptions year-over-year?
- What's the net revenue retention (NRR) on the recurring tiers?

---

## Refinement notes

- Source doc archived at `_source/X-Ponential_Tier_3_Architecture_2026-05-30.docx` for provenance
- **GX-2 is still skeleton-only** — open spec decisions listed in `specs/builds/gx-2.md`:
  - How many partners on the shortlist at launch (1, 3, or 5)?
  - Partner vetting criteria + commercial split (referral fee from partner to NOW, or pure introduction?)
  - Does the partner-content subscription branding stay invisible to end client, or is NOW co-branded?
  - Whether GX-2 includes any ad-account setup work
  - Creative refresh delivery cadence — monthly batch on the 1st, or weekly drops?
- Bundle math `D+E+F + GX-1+GX-2+GX-3` Complete Genome bundle is the **apex Tier 3 offer** — should anchor the page copy
- `tier-3` page graphic still TBD as production asset (brushed gold treatment is specced above)
