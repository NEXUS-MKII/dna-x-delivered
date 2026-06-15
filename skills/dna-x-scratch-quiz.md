---
name: dna-x-scratch-quiz
description: >-
  Design a scratch-built, code-owned diagnostic quiz funnel — independent of any
  hosted quiz platform (ScoreApp, Typeform, Interact, etc.) — that scores
  respondents, identifies their dominant pain, and emits a config the DNA-X
  Scratch Quiz Substrate engine renders into a 100% personalised response
  booklet. Use this skill whenever the user wants to build, design, or scope a
  quiz, scorecard, assessment, diagnostic, profiler, or quiz-style lead magnet
  that will run on owned code rather than a hosted SaaS — for AUBIT, a standalone
  codebase, a NOW Group build, or a scratch build. Trigger on "build a quiz",
  "design a scorecard", "diagnostic quiz", "assessment funnel", "profiler quiz",
  "lead magnet quiz", "quiz config", "scratch quiz", or any request to turn quiz
  answers into a scored, routed, personalised result — even if the user doesn't
  name the engine. Do NOT use this for building inside a hosted platform's own UI
  (that is the scoreapp-quiz-builder skill); this skill is for quizzes you own
  the engine for.
---

# DNA-X Scratch Quiz Designer

This skill designs **scratch-built, engine-owned diagnostic quizzes**. The defining
trait: you own the engine, so you are free of every hosted-platform constraint
(score-before-email gates, plan-tier feature gating, custom-code limits). The
output is a **config** for the DNA-X Scratch Quiz Substrate engine, which renders
a 100% personalised booklet per respondent.

## Fetch the canonical spec FIRST (always — do not improvise from memory)

Before doing anything else, fetch the substrate spec:

- **Substrate spec**: https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_shared/scratch-quiz-substrate.md

If the fetch fails (404, network error, partial content), **STOP and tell the user** — do not improvise the schema from training data. Drift between live spec and the emitted config is the single thing this skill exists to prevent.

Cite the spec version in the first line of every response:

> `scratch-quiz-substrate.md` v<spec_version> · fetched <iso-date>

That spec is the **source of truth for the config schema**. This skill is the **design craft** — how to think a good quiz into existence — and ends by emitting spec-compliant config against the live schema.

---

## The governing split (never violate)

- **Config controls structure + routing** — questions, categories, scoring style,
  routing rules, gates, result-types. Declared as data.
- **Code controls math + safeguards** — scoring, derived calculations, send caps,
  spine writes. Deterministic and auditable.
- **Claude controls voice + resonance** — the booklet prose, personalised to the
  respondent, in the operator's voice. Claude personalises *language*, never
  *facts*. Every number comes from the engine, never from Claude.

If a design choice would put math in config, or let Claude invent a number, it is
wrong. Stop and re-place it.

---

## Why this is not a hosted-platform quiz

Hosted platforms (ScoreApp et al.) shape quizzes around *their* limits: the score
hides behind the email gate by default, per-answer reactivity is gated to a paid
tier, result pages can't run real per-respondent logic. **None of that applies
here** because you render with Claude over owned data. So design for what you
*want*, not what a platform allows:

- Reveal-then-capture or tease — your choice, declared in config.
- Routing on any answer pattern — you own the rules.
- A booklet that reads like a consultant spent two days on the respondent —
  because Claude writes it per-person from real computed figures.

Best-practice *question design* still borrows from hosted-platform craft (the
3-part structure, the inversion test). The `scoreapp-quiz-builder` skill is a
good reference for question-writing patterns — but ignore its platform
constraints; they are false here.

---

## STEP 1 — Elect the scoring style (do this FIRST)

Scoring style is the single most important decision and everything branches from
it. It determines what "the result" *means*, which sets how routing reads scores,
which calculations apply, and what emotional frame the booklet takes. Elect it
before writing a single question.

| Style | The result answers… | Routes on | Booklet frame | Typical use |
|---|---|---|---|---|
| `gap_to_benchmark` | "How far am I from where I should be?" | **lowest** category (the biggest gap = the leak) | "here's how far you are from the target, and the one leak costing you most" | a known aspirational target exists (e.g. 50% GP / 20% NP) |
| `exposure_count` | "How exposed / at-risk am I?" | **most-exposed** category | "here's where you're dangerously exposed" | risk, compliance, readiness — no aspirational target, just danger |
| `dominant_category` | "Which type am I?" | **highest** category (the type you are) | "here's who you are / what kind of X you are" | profiling, ICP-match, partner-type, "what kind of X are you" |

**How to elect:** ask what the respondent should *feel* at the end.
- A felt **gap from a standard** → `gap_to_benchmark`.
- A felt **danger they hadn't priced in** → `exposure_count`.
- A felt **recognition of their identity/type** → `dominant_category`.

If two seem to fit, pick the one whose booklet frame is the stronger sales setup
for the operator's offer. State the elected style and *why* before proceeding.

---

## STEP 2 — Scope the funnel and what the bands mean

Establish, in business terms:
- **Who** the quiz qualifies (the ICP).
- **What each outcome means** for *that* business and *this* operator's offer —
  each result-type must set up a next step the operator actually sells.
- **The inversion test (critical):** is a "good" score actually the best lead?
  Often it is NOT — high scorers already have it handled and don't convert. In
  `gap` and `exposure` styles, never let the top outcome be reachable by overall
  score alone; it must be a **gate** (all categories clear a threshold). A high
  scorer with one weak category gets *helped on that weakness*, not congratulated.
  This is the score-inversion guard. (See spec §2.4.)

---

## STEP 3 — Design questions in three parts

The proven structure. Keep it lean — every question costs completion rate.

1. **Capture + context** — name, business, email, and any *informational* fields
   that set scale or context for derived math (e.g. a revenue band whose midpoints
   feed a dollar calculation). These are `scored: false, capture: true`.
2. **Scored diagnostic** — the questions that produce the category scores. Each
   maps to exactly one category with points per answer.
3. **Emotional + intent** — usually *unscored, captured*. The respondent's stated
   stress and desired outcome. These do NOT move the routing — they steer the
   **booklet's voice** so it lands as personal ("you told us cashflow keeps you up
   at night…"). This split is what makes a scratch booklet feel seen.

### Question-writing craft

- **Plain, owner-facing language.** No jargon. Ask the felt problem in their words.
- **Single-select for any question that routes** — checkbox/multi-select can't
  drive clean per-answer logic.
- **Reward awareness, not just outcome, where it's on-philosophy.** "Yes, my
  number is bad" can legitimately score above "I don't know my number" — knowing
  beats not-knowing. Decide per quiz; make it deliberate.
- **Invert deliberately when the obvious scoring is wrong.** Sometimes the answer
  that *sounds* worst is closer to the real conversation (e.g. "too much work" as
  a *high* readiness signal, not a problem). Flag every inversion as a conscious
  judgment call for the operator to ratify.
- **Expose numerics for derived calcs.** If an answer feeds a calculation, give
  each option a `represents_value` (see spec §2.3) so the same answer always
  yields the same number. Code reads it; Claude never guesses it.

---

## STEP 4 — Build the scoring (declare, don't compute)

- Assign each scored answer to a **category** with **points**. Points are
  arbitrary positive integers; the engine normalises to a percentage per category,
  so scales need not match across categories.
- Every category must receive at least one scored answer (the engine rejects a
  category that can't be scored).
- **Derived fields** use **named calculation types** from the engine's library —
  config *selects and parameterises* a calc; it never contains a formula string.
  Pick from the library in spec §2.3 (`revenue_gap_annualised`, `gap_to_target`,
  `ratio`, `count_below_threshold`, `weighted_index`, `dominant_of`). If the quiz
  needs math the library lacks, that is a flagged code request — not a config
  hack.
- **Missing inputs (e.g. "no idea"):** declare `on_missing_input: suppress` to omit
  the dependent figure and let the booklet pivot ("not knowing this is itself the
  problem"), rather than fabricate. Never let Claude estimate a suppressed figure.
- **Headline weighting is a per-quiz decision.** Default to an unweighted mean of
  categories. Weight only when the headline genuinely needs it — and remember the
  AI render layer adds answer-specific annotation that often carries the nuance an
  unweighted number can't, so unweighted is frequently enough. Decide and state it.

---

## STEP 5 — Routing (style-aware, diagnosis-first)

Routing reads the elected style:
- `gap_to_benchmark` → primary = **lowest** category.
- `exposure_count` → primary = **most-exposed** category.
- `dominant_category` → primary = **highest** category.

Then:
- **Gates first.** Declare any gate conditions (e.g. top outcome = all categories
  ≥ threshold). First matching gate wins. Gates are how you enforce the inversion
  guard.
- **Then primary** → map the primary category to a result-type.
- **Secondary (recommend ON).** Also surface the *second* dominant category — the
  booklet leads on the primary and names the secondary as "and here's what's
  coming next." Two shots at resonance; nearly free once the category profile
  exists.
- **Tie-breaks** — declare a priority order over categories for ties.

Use only the engine's declared condition vocabulary (spec §2.4); no arbitrary
expressions.

---

## STEP 6 — Result-types → template + emphasis + CTA

For each outcome declare: a label, a colour, a **booklet template variant**, a
**render emphasis** (what this result's booklet should foreground), and a **CTA**
(the operator's actual next step). Each result-type is a *different document* with
a different frame and CTA — design them as such, not as cosmetic relabels of one
page.

---

## STEP 7 — The render boundary (lock it)

The engine builds a **frozen payload** (all computed facts) and hands it +
template + the operator's **voice block** to Claude. In the render:
- Claude personalises language, framing, emphasis, and order — to *this*
  respondent's numbers, stated stress, and desired outcome.
- Claude **never states a number not in the payload.** If a figure is needed and
  absent (suppressed), the claim is omitted, not estimated.
- **Headline facts are injected mechanically** (`{{placeholder}}` substituted
  before Claude sees them) so they cannot drift. Claude writes prose *around*
  locked facts.
- Output sections are fixed by the template — Claude fills them, never adds or
  drops them.
- All prose stays inside the operator's voice block (banned patterns enforced).

**Render path:** Gamma connector primary (rapid, high-quality); WeasyPrint
alternative where surgical HTML control or offline render is wanted.

---

## STEP 8 — Emit the config + deliver/ratify

Produce the quiz as **spec-compliant config** (the YAML shape in spec §2), plus:
- the full question set with scoring,
- the routing + gates,
- the result-types with templates/CTAs,
- every deliberate judgment call (inversions, awareness-rewards, suppress choices)
  flagged for the operator to ratify.

Then state what the engine does on completion (spec §7): deliver booklet → write
the lead to the shared prospect spine with the full category profile → enrol into
warming **under existing send safeguards** (quiz completion is a trigger, not a
bypass: daily caps, weekday gate, unsubscribe headers) → audit-log the full chain.

End every design with the operator's open decisions — the judgment calls that are
theirs, not yours (e.g. inversion ratification, suppress-vs-provoke on missing
inputs, weighting). Present options with trade-offs; do not pre-decide the
operator's growth/positioning choices.

---

## The replicability test (run before handing config to build)

The design is sound only if the **same engine** would run it untouched. Sanity-check:
- Does every routing rule use the declared style's vocabulary?
- Does every derived field select a library calc type (no formula strings)?
- Is every fact in the booklet sourced from the payload (nothing for Claude to
  invent)?
- Could a *structurally different* quiz (a different style) run on the same engine
  with only config changes? If your design needs a new engine construct, that is a
  flagged spec/code change — surface it, don't smuggle it into config.

If all four hold, the config is ready for the build environment.

---

## Worked reference

AUBIT-TMT's "Tradie Profit Score" quiz is the worked instance in spec §9 —
`gap_to_benchmark` style, five categories, four result-types with gates, a
`revenue_gap_annualised` derived headline with suppress-on-missing, and three
ratified scoring-judgment calls. Read it as the model for a complete design.
