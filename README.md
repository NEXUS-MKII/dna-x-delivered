# DNA-X Delivered

NOW Group's DNA-X suite — client deliverables, canonical build specs, and Claude app skill templates, all in one public repo.

## What's in here

This repo serves **three audiences** from one tree:

| Directory | Audience | What it is |
|---|---|---|
| `DNA-X/<client-slug>/` | Clients | The actual deliverable HTML files NOW Group ships. Browse live at the Pages URLs below. |
| `specs/` | NOW operators + Claude skills | Canonical build specs — the single source of truth for how every DNA-X build is shaped. Fetched at runtime by Claude app skills. |
| `skills/` | NOW operators | Tiny markdown templates to paste into the Claude app at **Settings → Skills**. Each skill fetches the matching spec, lets Chris refine outputs fast, and surfaces spec gaps. |
| `_source/` | NOW operators | Provenance — original source documents that the specs were derived from. |

## Live URLs

Deliverables (GitHub Pages):

- MyFuture Spending Planner — https://nexus-mkii.github.io/dna-x-delivered/DNA-X/myfuture/spending_planner_standalone.html
- NOW Group Spending Command Centre — https://nexus-mkii.github.io/dna-x-delivered/DNA-X/now-group/spending_command_centre.html

Specs (raw, fetched by Claude skills via `raw.githubusercontent.com`):

- Schema template — https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/_template.md
- Tier 3 orchestration — https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/tiers/tier-3.md
- GX-1 Acquisition — https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/builds/gx-1.md

## DNA-X suite at a glance

12 skills planned — one per build + one per tier orchestration. Each build skill fetches its tier orchestration spec plus its own build spec.

### Tier 1 — WOW Essentials (NOW aesthetic, one-time price)

| Letter | Build | NEXUS module | Spec | Skill |
|---|---|---|---|---|
| A | Content Pack Pro | `nexus_wow_option_a.py` | ⏳ pending | ⏳ pending |
| B | Partner Growth System | `nexus_wow_option_c.py --html` (partial) | ⏳ pending | ⏳ pending |
| C | Email Database Rescue | `nexus_wow_option_b.py` | ⏳ pending | ⏳ pending |

### Tier 2 — DNAx Builds (buyer brand, bespoke, one-time price)

| Letter | Build | A-word | Price | Spec | Skill |
|---|---|---|---|---|---|
| D | Quiz Funnel | Answers | $2,497 | ⏳ pending | ⏳ pending |
| E | GEO + SEO Authority | Algorithm | $1,997 | ⏳ pending | ⏳ pending |
| F | BizCard 2026 | Architecture | $1,997 | ⏳ pending | ⏳ pending |

### Tier 3 — X-Ponential (managed channel, setup + monthly retainer)

| Letter | Build | A-word | Setup | Ongoing | Spec | Skill |
|---|---|---|---|---|---|---|
| GX-1 | Acquisition (LinkedIn) | Acquisition | $2,000 | $997 / $1,997 mo | ✅ [gx-1.md](specs/builds/gx-1.md) | ✅ [dna-x-gx-1.md](skills/dna-x-gx-1.md) |
| GX-2 | Amplification (Meta Ads) | Amplification | $2,997 | $997 / $1,997 mo | ⏳ pending (skeleton in source doc) | ⏳ pending |
| GX-3 | Anthology (Video) | Anthology | $4,997 | $497 / $997 mo | ⏳ pending | ⏳ pending |

### Tier orchestration specs

| Tier | Spec | Skill |
|---|---|---|
| Tier 1 — WOW Essentials | ⏳ pending | ⏳ pending |
| Tier 2 — DNAx Builds | ⏳ pending | ⏳ pending |
| Tier 3 — X-Ponential | ✅ [tier-3.md](specs/tiers/tier-3.md) | ⏳ pending |

## How the skill system works

The Claude app can't read local files, so the skill ↔ spec sync uses public URLs:

```
1. Chris invokes /dna-x-gx-1 in the Claude app
2. The skill instructs Claude to fetch:
   - specs/tiers/tier-3.md (orchestration)
   - specs/builds/gx-1.md (build spec)
   ...both via raw.githubusercontent.com
3. Claude operates on the user's request using the freshly-fetched specs
4. Claude cites the spec_version at the top of every response
5. If Chris improves the spec, he pushes a new commit. Next invocation picks up the new version.
```

This is **single-source-of-truth, automatic-sync**. No version drift between skill and spec because the skill always re-fetches.

### To install a skill in the Claude app

1. Open the raw markdown for the skill (e.g. https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/skills/dna-x-gx-1.md)
2. Copy the full file contents (frontmatter + body)
3. Claude app → **Settings → Skills → Create new skill**
4. Paste, save
5. Invoke from any conversation with `/dna-x-gx-1`

## How the refine loop works

The skill exists so Chris can iterate on builds fast:

1. **Use it** — ask the skill to draft / refine / audit a deliverable
2. **Spot a gap** — skill will flag `[SPEC GAP]` inline if the spec is unclear
3. **Refine the spec** — ask the skill to output the full updated `gx-1.md` (it knows the schema)
4. **Push the update** — paste the new spec.md into the repo, commit, push
5. **Propagate to NEXUS Python** — refine the matching builder module (`nexus_wow_option_*.py` or Tier 3 equivalent) so its implementation matches the new spec

Spec is the **WHAT/WHY**. NEXUS Python is the **HOW**. Refine the spec first; let the implementation follow.

## Repo identity (future moves are easy)

- **Repo name** currently `dna-x-delivered` — accurate while deliverables dominated; now also holds specs + skills. Recommend renaming to `dna-x` when the DNA-X domain is registered. GitHub redirects old URL permanently.
- **Custom domain** — when DNA-X domain is live, add a `CNAME` file at repo root + DNS CNAME → `nexus-mkii.github.io`. Pages auto-issues HTTPS cert.
- **Org transfer** — if a `dna-x` GitHub org is created later, Settings → Transfer ownership. All URLs auto-redirect.

## Source-of-truth boundary

- **This repo** is source-of-truth for: spec shape, commercial structure, deliverable list, voice/brand layer rules, Kajabi SKU config, partner orchestration model.
- **NEXUS MKII** (private, local) is source-of-truth for: build implementation (Python modules), live profile state, intake data, ongoing delivery telemetry, Voice Parameter Blocks for live buyers.
- **Kajabi MCP** is source-of-truth for: live offer/contact/analytics state in Kajabi itself.

When they disagree about a Kajabi offer's current state, MCP wins. When they disagree about how the offer *should* be configured, this repo wins. When they disagree about implementation details, NEXUS Python wins.
