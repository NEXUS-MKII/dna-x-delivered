---
spec_version: 1.1
last_updated: 2026-06-16
applies_to: every DNA-X scratch-built quiz (any consuming system — AUBIT, standalone codebases, scratch builds)
status: live
companion_skill: skills/dna-x-scratch-quiz.md
referenced_by:
  - skills/dna-x-scratch-quiz.md (design craft that emits configs against this schema)
  - aubit-tmt/config/quizzes/tradie_profit_score.yaml (first worked instance — Aaron Kemp's Tradie Profit Score)
  - aubit-tmt/aubit_tmt_quiz_engine.py (reference implementation of the engine)
  - aubit-tmt/aubit_tmt_quiz_render.py (reference renderer)
---

# DNA-X — Scratch Quiz Substrate
### Engine spec v1.1 — config-heavy, hosted-platform-independent quiz→personalised-booklet engine

> **What this is:** the DNA-X engine for **scratch-built, code-owned diagnostic quizzes** — quizzes you build and run on your own engine, independent of any hosted quiz platform (ScoreApp et al.). It turns any quiz (declared as config) into a 100% personalised response booklet per respondent. The quiz is data. The engine is code. Claude renders. Every quiz across every consuming system (AUBIT, standalone codebases, scratch builds) runs through this untouched — only its config + templates change.
>
> **Worked instance inside this spec:** AUBIT-TMT's "Tradie Profit Score" quiz (Aaron Kemp) — §9. It is one instance of the substrate, not its owner. The engine is engine-agnostic; AUBIT is a consumer.
>
> **Companion skill:** `skills/dna-x-scratch-quiz.md` (the design craft that produces configs for this spec). This spec is the canonical schema source-of-truth the skill emits against.
>
> **v1.1:** scoring-style is a first-class declared concept (§2.0) — three styles: `gap_to_benchmark`, `exposure_count`, `dominant_category`. Routing is style-aware. All seven design decisions resolved (§10). Render: Gamma connector primary, WeasyPrint alternative.
>
> **Design law:** *config controls structure + routing; code controls math + safeguards; Claude controls voice + resonance.* Three layers, each owning exactly one thing. Do not let them bleed.

---

## 0. The one-paragraph version

A respondent answers a quiz. The engine scores their answers deterministically (code), routes them to a diagnosis using rules declared in the quiz config (data), computes any derived figures via named calculation types (code), assembles a frozen per-respondent **payload**, and hands that payload + a booklet template + a voice block to Claude, which renders a personalised booklet. Facts come from the payload; Claude personalises only language and framing. The booklet is delivered and the lead is written to the shared prospect spine with its full category profile attached, so downstream warming and human follow-up know the diagnosis. Swap the config + templates → new quiz, zero engine code change.

---

## 1. Architecture — five layers

```
[1] QUIZ CONFIG (YAML, data)
        questions · answers · points · categories · routing rules · gates ·
        derived-field declarations · result-type→template mapping
              │
              ▼
[2] CAPTURE  (code)  ── respondent answers ingested, validated, stored
              │
              ▼
[3] SCORING  (code, deterministic, audit-logged)
        per-category % = points earned ÷ points possible
        overall benchmark score
              │
              ▼
[4] ROUTING  (code executing config rules)
        primary leak (lowest category) · secondary leak · gates · result-type
        derived fields computed via named calc types
              │
              ▼
        PAYLOAD  (frozen object — the contract between engine and renderer)
              │
              ▼
[5] RENDER  (Claude API — voice block + payload + template)
        personalises prose ONLY · never invents facts
              │
              ▼
   DELIVER booklet (PDF) + WRITE lead to prospect spine (full category profile)
              + enrol into warming under existing send safeguards
```

**Ownership boundaries (enforced in code review):**

| Layer | Owner | Never does |
|---|---|---|
| Config | Data (YAML) | Never contains executable logic; declares only |
| Scoring | Code | Never calls Claude; never reads config rules beyond category maps |
| Routing | Code executing declared rules | Never hardcodes a quiz-specific result name |
| Derived fields | Code (named calc types) | Never evaluates arbitrary formula strings from config |
| Render | Claude | Never computes a number; never overrides a payload fact |

---

## 2. Layer 1 — Quiz config schema

A quiz is a single YAML file. The engine reads it; nothing about a specific quiz is hardcoded.

### 2.0 Scoring style — the first-class concept (elect this FIRST)

Before questions, before routing, a quiz declares its **scoring style**. Style is not cosmetic — it determines what "the result" *means*, which determines how routing reads the scores, which calc types apply, and what emotional frame the booklet takes. The skill's design process elects style as **step one**; everything downstream branches from it.

```yaml
quiz:
  scoring_style: gap_to_benchmark   # gap_to_benchmark | exposure_count | dominant_category
```

**v1 ships three real styles:**

| style | "what's the result?" | routes on | typical calc types | booklet frame |
|---|---|---|---|---|
| `gap_to_benchmark` | distance from a known target | **lowest** category (the biggest gap = the leak) | `revenue_gap_annualised`, `gap_to_target`, `ratio` | "here's how far you are from where you should be" |
| `exposure_count` | how many critical areas you're exposed on | **most-exposed** (highest count / lowest-safety) | `count_below_threshold`, `weighted_index` | "here's where you're dangerously exposed" |
| `dominant_category` | which profile/type wins | **highest** category (the type you are) | `dominant_of`, `weighted_index` | "here's who you are / what kind of X you are" |

**Why style is first-class, not emergent from routing rules:** a `gap` booklet and an `exposure` booklet are *different documents* — different CTAs, different voice, different "good." Making style a declared concept lets the engine's routing executor and the design skill branch the whole experience (questions → routing → result-types → booklet tone) off one field. The engine stays neutral; the quiz declares its shape.

**Routing reads style (engine behaviour):**
- `gap_to_benchmark` → `primary_leak` = lowest category; `benchmark.targets` required.
- `exposure_count` → `primary_exposure` = most-exposed category; `benchmark.targets` optional/absent.
- `dominant_category` → `dominant` = highest category; gates rarely used; `benchmark` absent.

Style also sets which routing keys are valid (§2.4) and which `default.map` semantics apply. Config-load validates that the declared style's required fields are present and its forbidden ones absent — fail loudly.

**Aaron's Tradie Profit quiz is `gap_to_benchmark`** (target 50/20, route on the leak). The Back Office "Are You At Risk?" validation sketch (§9.1) is `exposure_count`. A future "What Kind of Networker Are You?" / partner-type / ICP-match quiz is `dominant_category`.

### 2.1 Top-level shape

```yaml
quiz:
  id: tradie_profit_score
  version: 1
  title: "What's Your Tradie Profit Score?"
  estimated_minutes: 3
  scoring_style: gap_to_benchmark    # §2.0 — elected FIRST; drives routing + frame
  voice_block: aaron_kemp.voice_assets.parameter_block   # ref to encoder output
  operator: AUBIT-TMT

  capture:
    # which respondent fields to collect, and WHEN
    fields: [first_name, business_name, email]
    gate: tease            # tease | reveal_then_capture  (see §6)

  categories:              # the scored diagnostic dimensions
    - id: gp_margin
      label: "Gross Profit & Margin Discipline"
    - id: np_gap
      label: "Net Profit / Benchmark Gap"
    - id: cash_runway
      label: "Cash Runway"
    - id: pricing
      label: "Pricing Maturity"
    - id: owner_scale
      label: "Owner & Scale Readiness"

  benchmark:               # the headline target this quiz measures against
    targets: { gp_pct: 50, np_pct: 20 }

  questions: [ ... ]       # §2.2
  derived:   [ ... ]       # §2.3
  routing:   { ... }       # §2.4
  result_types: [ ... ]    # §2.5
```

### 2.2 Questions

Each question declares its type, whether it is scored, whether it is captured for the payload, and (if scored) the category + points per answer.

```yaml
questions:
  - id: q1_revenue
    text: "Last month, how much work did your business complete?"
    type: single_select
    scored: false
    capture: true                # value carried into payload, not scored
    capture_as: revenue_band     # payload key
    options:
      - { value: "under_20k",  label: "Under $20k",     midpoint: 15000 }
      - { value: "20_50k",     label: "$20–50k",        midpoint: 35000 }
      - { value: "50_100k",    label: "$50–100k",       midpoint: 75000 }
      - { value: "100_250k",   label: "$100–250k",      midpoint: 175000 }
      - { value: "250k_plus",  label: "$250k+",         midpoint: 300000 }

  - id: q2_cost_ratio
    text: "Out of every $100 earned, roughly how much goes to materials, labour and subcontractors?"
    type: single_select
    scored: true
    category: gp_margin
    options:
      - { value: "under_40", label: "Under $40", points: 10 }
      - { value: "40_50",    label: "$40–50",    points: 8 }
      - { value: "50_60",    label: "$50–60",    points: 4 }
      - { value: "over_60",  label: "Over $60",  points: 1 }
      - { value: "no_idea",  label: "No idea",   points: 0 }

  - id: q7_stress
    text: "Which causes you the most stress?"
    type: single_select
    scored: false
    capture: true
    capture_as: biggest_stress   # emotional driver — steers booklet voice, not routing
    options:
      - { value: "cashflow",   label: "Cashflow" }
      - { value: "pricing",    label: "Pricing jobs" }
      - { value: "team",       label: "Team performance" }
      - { value: "admin",      label: "Too much admin" }
      - { value: "profit",     label: "Not enough profit" }
```

**Rules the engine enforces:**
- `scored: true` requires `category` + `points` on every option.
- `scored: false` + `capture: true` requires `capture_as`.
- A question may be `scored: false` and `capture: false` (pure UX, e.g. a transition) — rare.
- `points` are arbitrary positive integers; category % normalises them (§3), so scales need not match across categories.

### 2.3 Derived fields — **named calculation types** (NOT formula strings)

Derived figures (e.g. "dollars on the table") are computed by **code-provided calculation types** that config *selects and parameterises*. The engine ships a library of calc types; config never contains an evaluable expression. This keeps the math-in-code boundary clean and avoids building an interpreter inside a config file.

```yaml
derived:
  - id: dollars_on_table
    calc: revenue_gap_annualised      # name of a code-provided calc type
    inputs:
      revenue_source: q1_revenue       # uses the option midpoint
      current_pct: np_gap              # respondent's net-profit category %→ mapped value
      target_pct: 20                   # from benchmark.targets.np_pct
    output_as: dollars_on_table        # payload key
    rounding: nearest_1000
```

**Calc-type library (code-owned, versioned), grouped by the scoring style that typically uses each. v1 ships:**

| calc type | used by style | signature | what it computes |
|---|---|---|---|
| `revenue_gap_annualised` | gap | (revenue_source, current_pct, target_pct, rounding) | (target_pct − current_pct) × annualised revenue. Negative clamped to 0. |
| `gap_to_target` | gap | (current, target) | target − current, floored at 0 |
| `ratio` | gap / any | (numerator, denominator) | simple ratio, guards div/0 |
| `count_below_threshold` | exposure | (categories[], threshold) | count of categories scoring below threshold — "exposed on N of M areas" |
| `weighted_index` | exposure / dominant | (inputs[], weights[]) | normalised weighted sum |
| `dominant_of` | dominant | (categories[]) | the highest-scoring category id + its margin over second |

**Adding a new calc type = a code change + a doc entry, deliberately.** Config authors pick from the library; they cannot invent math. This is the boundary. If a future quiz needs a calculation the library lacks, that is a reviewed code PR — not a config edit. The library is *meant* to grow as new quiz types are designed; v1 covers all three shipped scoring styles.

**Important — current_pct mapping:** a respondent's net-profit *answer* (Q4: lost / <10 / 10–20 / 20%+ / no idea) must map to a representative numeric for the calc. Declare that mapping on the scored question:

```yaml
  - id: q4_net_profit
    text: "After paying everything (including yourself), what Net Profit did you keep last month?"
    type: single_select
    scored: true
    category: np_gap
    represents: net_profit_pct        # exposes a numeric for derived calcs
    options:
      - { value: "lost",    label: "Lost money", points: 0,  represents_value: -5 }
      - { value: "under_10",label: "Under 10%",  points: 4,  represents_value: 7 }
      - { value: "10_20",   label: "10–20%",     points: 8,  represents_value: 15 }
      - { value: "20_plus", label: "20%+",       points: 10, represents_value: 22 }
      - { value: "no_idea", label: "No idea",    points: 0,  represents_value: 0 }
```

The calc reads `represents_value` of the chosen option. Same answer → same number, always.

**`no_idea` / missing-input handling (RESOLVED — suppress-and-pivot):** when a respondent answers "no idea" (or any answer with no real numeric, e.g. Q4 `no_idea`), the engine **suppresses the dependent derived figure** rather than fabricating one. Declared per derived field:

```yaml
derived:
  - id: dollars_on_table
    calc: revenue_gap_annualised
    on_missing_input: suppress        # suppress | fallback
    # if suppress: the figure is omitted from the payload; the template's
    # {{dollars_on_table}} block is replaced by the result_type's suppress_pivot copy.
```

When suppressed, the booklet **pivots**: "you told us you're not sure of your net profit — that's the first problem, and here's why not knowing is costing you." The not-knowing *becomes* the diagnosis hook. Claude must **never** estimate a suppressed figure. (`fallback` mode remains available per-field for cases where a conservative declared value is genuinely better than suppression — but Aaron's `dollars_on_table` uses `suppress`.)

### 2.4 Routing — declared, style-aware

Routing is **style-aware and diagnosis-first**: the scoring style (§2.0) sets *which* category the primary route reads. For `gap_to_benchmark` (Aaron's), the diagnosis is the *lowest* category — the biggest leak. The example below is the `gap` style; `exposure_count` routes on most-exposed, `dominant_category` routes on highest. Declared as data:

```yaml
routing:
  # rule keyword resolves per scoring_style:
  #   gap_to_benchmark  → primary = lowest_category (the leak)
  #   exposure_count    → primary = most_exposed_category
  #   dominant_category → primary = highest_category (the type)
  primary:
    rule: lowest_category            # valid for gap style; engine validates vs scoring_style
    tie_break: [gp_margin, np_gap, cash_runway, pricing, owner_scale]
                                     # order = priority when categories tie
  secondary:
    rule: second_lowest_category     # "and here's what's coming next" — two-factor (v1: ON)
    enabled: true

  gates:                             # evaluated BEFORE primary; first match wins
    - id: profit_machine
      when: all_categories_at_or_above: 75      # % threshold across EVERY category
      result_type: tradie_profit_machine
    - id: busy_but_stuck
      when:
        all_of:
          - category_at_or_above: { gp_margin: 60 }
          - category_at_or_above: { np_gap: 60 }
          - any_category_below: { threshold: 50, in: [pricing, owner_scale] }
      result_type: busy_but_stuck

  default:                           # if no gate matches, route by primary
    map:
      gp_margin:   margin_leak
      np_gap:      margin_leak
      cash_runway: cashflow_crunch
      pricing:     busy_but_stuck
      owner_scale: busy_but_stuck
```

**Engine routing algorithm (fixed code, reads the above):**
1. Compute all category %.
2. Resolve `primary.rule` against `scoring_style` — reject at config-load if the rule is invalid for the declared style (e.g. `lowest_category` on a `dominant_category` quiz).
3. Evaluate `gates` in order. First whose `when` is satisfied → that `result_type`. Stop. (Gates are most common in `gap` and `exposure` styles; rare in `dominant`.)
4. If no gate matches → take `primary` (per style) → look up `default.map` → `result_type`.
5. Compute `secondary` if enabled (independent of result_type; carried for the booklet — the "something is bound to resonate" second shot).

**The gate-not-band principle (gap/exposure styles):** the top outcome is reachable ONLY via an all-categories gate, never as "highest overall score." A high scorer with one weak category gets *helped on that category*, not congratulated. This is the score-inversion guard, in our own code where we control it.

**`when` condition vocabulary (code-supported, the only operators config may use):**
`all_categories_at_or_above: N` · `category_at_or_above: {cat: N}` · `category_below: {cat: N}` · `any_category_below: {threshold: N, in: [...]}` · `all_of: [...]` · `any_of: [...]` · `overall_at_or_above: N`. No arbitrary expressions. New operators = code change.

### 2.5 Result types → template + render emphasis + CTA

```yaml
result_types:
  - id: margin_leak
    label: "Margin Leak"
    colour: red
    template: booklet_margin_leak        # template variant id (§5)
    render_emphasis: "pricing, job costing, GP control"
    cta: { text: "Book a 15-minute Profit Snapshot", action: book_call }

  - id: cashflow_crunch
    label: "Cashflow Crunch"
    colour: orange
    template: booklet_cashflow_crunch
    render_emphasis: "invoicing rhythm, cash systems"
    cta: { text: "See your Cashflow Scorecard", action: book_call }

  - id: busy_but_stuck
    label: "Busy But Stuck"
    colour: yellow
    template: booklet_busy_but_stuck
    render_emphasis: "systems, leadership, pricing"
    cta: { text: "Get the 50/20 Growth Plan", action: book_call }

  - id: tradie_profit_machine
    label: "Tradie Profit Machine"
    colour: green
    template: booklet_profit_machine
    render_emphasis: "scale, remove owner dependency"
    cta: { text: "Apply for advanced coaching", action: apply }
```

---

## 3. Layer 3 — Scoring (deterministic, code)

- For each category: `category_pct = round(100 × Σ(points earned) ÷ Σ(points possible))`.
- `points possible` = the max-points option per scored question assigned to that category, summed.
- **Overall benchmark score** = mean of category % by default; **weighting is a per-quiz design decision** (config-declared `weights`, default equal). Some quizzes need a weighted headline (e.g. margin weighted heavier); others are fine unweighted *because the AI render layer adds answer-specific annotations that carry the nuance the raw number doesn't*. The schema supports weights (present, optional, default equal); the design skill prompts the decision per quiz. Used for the headline, not for routing.
- Scoring is **pure**: identical answers always produce identical scores. No Claude in this path. Every scoring run is audit-logged: respondent id, quiz id+version, raw answers, per-category points, per-category %, timestamp, engine version.
- A category with no answered scored questions is invalid for this engine (every category must receive ≥1 scored answer) — validate at config-load, fail loudly.

---

## 4. Layer 4 — The payload (the contract)

The single frozen object handed to the renderer. Engine builds it; renderer consumes it; it is **immutable** once built. The headline number is computed here, in code — never by Claude.

```json
{
  "engine_version": "1.0",
  "quiz": { "id": "tradie_profit_score", "version": 1 },
  "respondent": {
    "first_name": "…", "business_name": "…", "email": "…",
    "revenue_band": "100_250k"
  },
  "benchmark": {
    "targets": { "gp_pct": 50, "np_pct": 20 },
    "overall_score": 48,
    "gap_to_target": { "np_pct_points": 13 }
  },
  "categories": {
    "gp_margin": 40, "np_gap": 35, "cash_runway": 70,
    "pricing": 55, "owner_scale": 60
  },
  "diagnosis": {
    "result_type": "margin_leak",
    "result_label": "Margin Leak",
    "primary_leak": "np_gap",
    "secondary_leak": "gp_margin",
    "matched_gate": null
  },
  "emotional": {
    "biggest_stress": "profit",
    "desired_outcome": "scale_business"
  },
  "derived": {
    "dollars_on_table": 39000
  },
  "cta": { "text": "Book a 15-minute Profit Snapshot", "action": "book_call" }
}
```

**Contract rules:**
- Every value in `categories`, `benchmark`, `derived`, `diagnosis` is engine-computed and **locked**.
- `emotional.*` and `respondent.*` are captured verbatim.
- The renderer may read any field; it may write none.
- Swap the quiz → the payload's *keys* may differ (different categories/derived) but its *shape* (these top-level sections) is stable. The renderer template references payload keys by name; mismatched keys fail at render-validation, not silently.

---

## 5. Layer 5 — Render (Claude inline, personalisation)

Claude receives: **voice block** (operator's parameter block) + **payload** + **booklet template** (the result_type's variant) + **render prompt**.

**The render prompt's governing constraints (verbatim intent for the system prompt):**
- Personalise *language, framing, emphasis, and order-of-emphasis* to this respondent.
- Reference their real numbers (`categories`, `derived.dollars_on_table`, `benchmark`), their stated stress (`emotional.biggest_stress`), and their desired outcome (`emotional.desired_outcome`).
- **Never state a number, percentage, or dollar figure not present in the payload.** If a figure is needed and absent, omit the claim — do not estimate.
- Stay inside the operator voice block (banned patterns enforced).
- Honour the `render_emphasis` for this result type.
- Output the fixed template's sections, filled — never add or drop sections.

**Template = fixed shell per result_type** (sections, order, brand, CTA slot). Claude fills prose into the shell. Four variants for this quiz, one shell family. The template references payload keys via `{{double_brace}}` placeholders for *facts* (so facts are injected mechanically, not paraphrased by Claude) and leaves *prose blocks* for Claude to write around them.

**Fact-injection vs prose split (critical):**
- Facts (`{{dollars_on_table}}`, `{{categories.gp_margin}}`, names) → mechanically substituted into the template *before* Claude sees it, OR passed as locked values Claude must reproduce exactly. Prefer mechanical substitution for the headline number so it is impossible to drift.
- Prose (the "here's what this means for you" connective tissue) → Claude writes, in voice, around the injected facts.

**Render path (RESOLVED — Gamma primary, WeasyPrint alternative):** default render is via the **Gamma connector** — rapid and high-quality, leveraging the existing connector setup. WeasyPrint is offered as the alternative where surgical HTML control, base64-embedded assets, or offline/self-contained rendering is wanted (the established lead-magnet build method). The template format accommodates both: Gamma consumes the structured content + template; WeasyPrint consumes the same content as self-contained HTML. Output → PDF either way.

---

## 6. The capture gate (§2.1 `capture.gate`)

Two modes, declared in config. This engine is custom, so both are buildable — but they have different conversion shapes:

- **`tease` (recommended default):** respondent completes the quiz; the headline (e.g. "Your Tradie Profit Score is ready — we've calculated what your margin gap is costing you per year") is *promised* on the capture form; booklet (with the real `dollars_on_table` reveal) is delivered after capture. Curiosity gap drives opt-in.
- **`reveal_then_capture`:** show the score headline (and the dollar figure) *before* the form. Higher perceived honesty, but spends the curiosity asset before the ask.

Both are config; the engine supports each. Default `tease`. (This replaces the platform-specific gate constraint that would have applied on a hosted scorecard — we own the flow, so it is a config choice, not a tool limitation.)

---

## 7. Delivery, spine write, and safeguards

On render completion:
1. **Deliver** the booklet (PDF link + optional email send).
2. **Write the lead to the shared prospect spine** — the Lead/Prospect class, GHL/Kajabi-consistent — carrying the **full category profile + result_type + derived fields**, so warming and human follow-up know the diagnosis, not just "completed a quiz."
3. **Enrol into warming** under the existing AUBIT send safeguards — quiz completion is a *trigger*, not a bypass: 5/day default cap, 50/day absolute, weekday-only gate, `EARLIEST_SEND_DATE` floor, auto-injected `List-Unsubscribe` headers, unsubscribe-status excluded from warming.
4. **Audit-log** the full chain: capture → score → route → derived → render → deliver, each with inputs, outputs, timestamp, engine + config version. Auditor-defensible, consistent with the rest of AUBIT.

**Spine discipline:** the quiz writes through the same staging/validation gate as all spine writes — no direct unvalidated writes to the master store.

---

## 8. Replicability — what changes per new quiz

| Artefact | Per-quiz? | Notes |
|---|---|---|
| Quiz config YAML | **New** | questions, categories, routing, gates, derived selections, result-types |
| Booklet template(s) | **New** | one shell family + per-result variants |
| Render prompt emphasis | **New (in config)** | `render_emphasis` per result_type |
| Voice block | **New (ref)** | operator's parameter block |
| Engine (scoring/routing/derived/payload/render-orchestration) | **Unchanged** | the substrate |
| Calc-type library | **Unchanged** unless a new math type is genuinely needed | new type = reviewed code PR |
| Safeguards / spine write | **Unchanged** | |

**The replicability test (run before code lock):** the schema must express Aaron's quiz (§9) AND sketch a second, structurally different quiz (§9.1, a Back Office "Are You At Risk?" quiz) with **no new construct**. If the second quiz needs a feature the first didn't, extend the schema now, in YAML, before the engine is written.

---

## 9. Worked instance — Aaron's "Tradie Profit Score" quiz

Full config mapping of the 10-question quiz. Categories, scored/informational split, derived field, four result-types with gates.

**Question → category map:**

| Q | Question (abbrev) | scored | category / capture |
|---|---|---|---|
| 1 | Revenue last month | no | capture → `revenue_band` (midpoints for derived calc) |
| 2 | Cost ratio (mat/lab/sub per $100) | yes | `gp_margin` |
| 3 | Know your GP %? | yes | `gp_margin` (awareness) |
| 4 | Net profit kept | yes | `np_gap` (+ `represents: net_profit_pct`) |
| 5 | Weeks of cash | yes | `cash_runway` |
| 6 | How you price jobs | yes | `pricing` |
| 7 | Biggest stress | no | capture → `biggest_stress` (emotional driver) |
| 8 | Overrun handling | yes | `gp_margin` (margin discipline) |
| 9 | Biggest growth blocker | yes | `owner_scale` |
| 10 | What hitting 50/20 would mean | no | capture → `desired_outcome` (outcome selling) |

**Scoring style:** `gap_to_benchmark`. **Benchmark targets:** GP 50%, NP 20%.

**Full answer scoring (build-ready):**

| Q | Category | Answer options → points |
|---|---|---|
| 2 | `gp_margin` | Under $40 (10) · $40–50 (8) · $50–60 (4) · Over $60 (1) · No idea (0) |
| 3 | `gp_margin` | Yes 50%+ (10) · Yes 40–49% (6) · Yes <40% (3) · Not sure (0) |
| 4 | `np_gap` | Lost money (0 / rep −5) · Under 10% (4 / rep 7) · 10–20% (8 / rep 15) · 20%+ (10 / rep 22) · No idea (0 / **suppress**) |
| 5 | `cash_runway` | <1wk (0) · 1–2wk (3) · 2–4wk (6) · 1–3mo (8) · 3+mo (10) |
| 6 | `pricing` | Fixed price system (10) · Hourly + margin (8) · Competitor pricing (4) · Gut feel (2) · Estimate and hope (0) |
| 8 | `gp_margin` | Raise a variation (10) · Margin absorbs it (6) · Wear the cost (2) · Not sure (0) |
| 9 | `owner_scale` | No clear numbers (2) · Cashflow (3) · Team issues (5) · Not enough work (6) · Too much work (8) |

*Capture-only (unscored):* Q1 `revenue_band` (midpoints 15k/35k/75k/175k/300k) · Q7 `biggest_stress` · Q10 `desired_outcome`.

**Three deliberate scoring-judgment calls (ratified):**
- **Q9 inverted** — "too much work" scores highest on `owner_scale`: a tradie drowning in work but unable to scale is closer to the real coaching conversation than one with "no clear numbers" (a more fundamental problem). On Aaron's thesis.
- **Q3 rewards awareness even when the number's bad** — "Yes <40%" (3) > "Not sure" (0): knowing your bad GP beats not knowing. On-philosophy.
- **Q4 "No idea" → suppress** the `dollars_on_table` headline and pivot ("not knowing your net profit is the first problem") rather than fabricate a figure.

**Derived:** `dollars_on_table` via `revenue_gap_annualised` (revenue_band midpoint × (20 − net_profit_pct)/100, annualised, nearest $1000, clamped ≥0, `on_missing_input: suppress`).
**Routing:** `gap_to_benchmark` → primary = lowest category, tie-break `[gp_margin, np_gap, cash_runway, pricing, owner_scale]`; `secondary` ON.
**Gates:** `profit_machine` = all categories ≥75; `busy_but_stuck` = gp_margin ≥60 AND np_gap ≥60 AND (pricing OR owner_scale <50).
**Result-types:** Margin Leak (red), Cashflow Crunch (orange), Busy But Stuck (yellow), Tradie Profit Machine (green) — per §2.5.
**Voice block:** Aaron's encoder output. **Gate:** `tease`. **Render:** Gamma (connector).
**Headline pattern:** "Most tradies think they need more work. Usually they need better numbers. {{first_name}}, you're leaving ~${{dollars_on_table}}/year on the table." *(Suppressed → "{{first_name}}, you told us you're not sure what you're keeping — that's the first problem, and it's costing you more than you'd think.")*

### 9.1 Replicability validation sketch — "Are You At Risk?" (Back Office lane)

Stubbed in the SAME schema to prove no new construct is needed — and to exercise a *different scoring style*. (Not for build now — validation only.)

- **Scoring style:** `exposure_count` (no aspirational benchmark; route on most-exposed). Different style → proves §2.0 is real.
- **Categories:** `compliance`, `process_maturity`, `people_hr`, `governance`.
- **Scored questions:** contracts/policies current? · processes documented or in-your-head? · staff-issue readiness? · payroll/bookkeeping cleanliness?
- **Informational capture:** most-hated admin task (emotional driver); industry (context).
- **Derived:** `exposure_areas` via `count_below_threshold` (v1 calc type); optional `risk_index` via `weighted_index`.
- **Routing:** `primary = most_exposed_category`; gate `locked_down` = all categories ≥75.
- **Result-types:** High Risk / Exposed / Mostly Covered / Locked Down.
- **Verdict:** expressible with existing constructs and a *second* scoring style. ✅ Schema passes the second-quiz test across styles. A future `dominant_category` quiz ("What Kind of Networker Are You?") exercises the third style — `dominant_of` calc, route on highest, no gates.

---

## 10. Resolved decisions (all seven locked)

1. **Booklet render path — RESOLVED: Gamma primary, WeasyPrint alternative.** Gamma connector is set up → rapid + high quality; WeasyPrint offered where surgical HTML control / offline render is wanted. (§5)
2. **Capture gate default — RESOLVED: `tease`.** The "$X/year on the table" figure is the curiosity asset; promise it on the form, reveal in the booklet. A/B-testable later since we own the flow. (§6)
3. **Scoring-style as first-class concept — RESOLVED (reframed from calc-library coverage).** Scoring style is now a declared, first-class config field (§2.0). v1 ships **three** real styles: `gap_to_benchmark`, `exposure_count`, `dominant_category`. Calc library grows under styles; v1 ships six calc types covering all three. The design skill elects style as design-step-one. (§2.0, §2.3)
4. **Missing-input handling — RESOLVED: suppress-and-pivot (default), `fallback` available per-field.** No fabricated numbers. Suppressed figures pivot the booklet to "not knowing is itself the diagnosis." Claude never estimates. (§2.3)
5. **Two-factor routing — RESOLVED: ship `secondary` in v1.** Nearly free; the second shot that makes "something is bound to resonate" real. (§2.4)
6. **Fact-injection — RESOLVED: mechanical `{{placeholder}}` substitution.** The headline number is computed in code and injected mechanically; impossible to drift. Claude writes prose around it. (§5)
7. **Benchmark weighting — RESOLVED: per-quiz design decision.** Schema supports `weights` (present, optional, default equal). Some quizzes need weighting; others ride unweighted because the AI render layer adds answer-specific annotations carrying the nuance. The design skill prompts the decision per quiz — not hard-and-fast. (§3)

---

## 11. Build sequence (pilot)

1. Engine core: config loader + validator (fail loudly on schema violations §2/§3; validate `scoring_style` required/forbidden fields and that routing rules are valid for the declared style).
2. Scoring (deterministic, audit-logged).
3. Derived-field calc-type library (v1 six types across three styles).
4. Routing executor — style-aware: resolve `primary` per style → gates → `default.map`; compute `secondary`.
5. Payload builder (frozen, validated against template key references; honour `on_missing_input: suppress`).
6. Render orchestration (voice block + payload + template + render prompt → Claude → Gamma/WeasyPrint → PDF), mechanical fact-injection for headline number.
7. Delivery + spine write + warming enrol under safeguards + full audit chain.
8. Load Aaron's quiz config (§9, `gap_to_benchmark`) end-to-end; produce one head-turning Margin Leak booklet against a real respondent's answers. Prove it. Then the engine is done and every future quiz — across all three scoring styles — is config.

---
*DNA-X Scratch Quiz Substrate v1.1. Hosted-platform-independent; you own the engine. Scoring-style is a first-class concept (gap / exposure / dominant). All seven decisions resolved. Companion skill: `skills/dna-x-scratch-quiz.md`. This substrate is the engine behind every DNA-X scratch-built diagnostic quiz across all consuming systems; AUBIT-TMT's Tradie Profit Score (§9) is one worked instance.*
