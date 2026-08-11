---
name: dna-x-go-private
description: Prepare the team and the DNA-X repo (dna-x-delivered) to flip from public to private without breaking the things that depend on it being public — the spec-fetching skills, GitHub Pages, and the opener install links. Use when the user wants to make DNA-X private, add a team member to DNA-X, land the X-Pipe (GX-1) engine into DNA-X, or asks "what breaks if we go private".
---

> v2026-08-11.1 · source-of-truth: dna-x-delivered/skills/dna-x-go-private.md — bump the .n and the date on every change; this repo is the canonical copy.

# DNA-X · Go-Private Playbook

You are helping NOW Group move **`NEXUS-MKII/dna-x-delivered`** (the DNA-X repo, Tier-3 product IP) from **public → private** *seamlessly*. This is the repo that holds GX-1 (X-Pipe) and the whole DNA-X build/skill suite.

**Do not just flip the visibility bit.** This repo's public-ness is load-bearing. Flipping it blind silently breaks the skills, the public site, and the client-facing opener install. Follow this sequence.

---

## The core tension (read first, every time)

Almost every DNA-X skill is architected to **fetch its own spec over a public raw URL** at runtime:

```
https://raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered/main/specs/...
```

`raw.githubusercontent.com` serves **private** repos only with a token in the request. A skill running in a plain Claude session has no token → the fetch **404s** the moment the repo is private. That is the single biggest breakage, and it's invisible until someone runs a skill and it silently drifts to training-data memory.

Three load-bearing public dependencies (verify live counts in Step 1 — do not trust these numbers blindly):

| Dependency | What relies on it | Breaks on private? |
|---|---|---|
| **Raw spec URLs** (`/specs/**`) | `dna-x-gx-1`, `dna-x-build-a`, `dna-x-build-c`, `dna-x-scratch-quiz`, `README` — they `fetch` specs at runtime | **Yes** — 404 unauthenticated |
| **GitHub Pages** (`nexus-mkii.github.io/dna-x-delivered/`) | Public site; `.nojekyll` legacy build from `main` `/` | **Yes** on GitHub Free — private repos can't publish Pages without Pro/Team/Enterprise |
| **Opener install** (`DNA-X/x-gen/*.html`, `INSTALL.md`) | VAs install openers by dropping the public raw link in Claude | **Yes** — raw links 404, VA install stops working |

---

## Step 0 — Snapshot current state

Run these and record the output before changing anything:

```bash
gh repo view NEXUS-MKII/dna-x-delivered --json visibility,isPrivate,url,diskUsage
gh api repos/NEXUS-MKII/dna-x-delivered/pages 2>/dev/null   # confirms Pages exists + public:true
gh api repos/NEXUS-MKII/dna-x-delivered/collaborators --jq '.[].login'
gh api orgs/NEXUS-MKII/teams --jq '.[].slug' 2>/dev/null    # teams that could be granted access
```

Confirm you (the operator) have **admin** on the repo (`viewerCanAdminister`) — you can't flip visibility or manage Pages without it.

## Step 1 — Discover the public dependencies (don't assume)

```bash
cd <dna-x-delivered clone>
# every file that fetches this repo over a public raw URL:
grep -rInc "raw.githubusercontent.com/NEXUS-MKII/dna-x-delivered" . \
  --include='*.md' --include='*.html' | grep -v '/.git/' | grep -v ':0'
# the opener install surface:
gh api "repos/NEXUS-MKII/dna-x-delivered/git/trees/main?recursive=1" --jq '.tree[].path' \
  | grep -Ei 'x-gen|opener|install'
```

Also check for **external** references you don't control: anything in other repos, artifacts already handed to VAs/clients, or Kajabi/site pages that embed `raw.githubusercontent.com/.../dna-x-delivered/...` or the Pages URL. Those you can only migrate or accept-as-broken — list them explicitly for the user.

## Step 2 — Choose the architecture (this is the real decision)

Present both to the user and let them pick. **Recommend Option A** — it keeps the load-bearing public URLs alive and puts only the IP behind the wall.

### Option A — Split (recommended)
Keep a **small PUBLIC surface** for the genuinely client-/VA-facing, must-be-public bits; move the **IP** private.

- **Stays public** (own public repo, e.g. `dna-x-public` — or leave the current repo public but stripped to just these): `DNA-X/x-gen/**` (openers + INSTALL) and any `specs/**` that skills fetch anonymously. Pages continues serving from the public repo.
- **Goes private** (this repo flipped, or a new `dna-x` private repo): the **X-Pipe (GX-1) engine** (`lib/enrichment_engine/**` + driver scripts + runbooks), internal build docs, anything IP.
- Skills that fetch specs keep working **only if their specs stay on the public side**. If a spec must go private, that skill must switch to authenticated fetch (Step 3d) or bundle the spec.

**Trade-off:** two repos to keep in sync, but zero breakage and the IP is actually protected. Best fit because the engine is the crown-jewel IP and the openers *must* stay publicly installable.

### Option B — Whole-repo private + migrate the public dependencies
Flip the entire repo private, then relocate everything that needed to be public:
- Move opener HTMLs + public specs to a public host (a separate public mirror repo, or Pages on a paid plan, or a CDN).
- Rewrite every raw URL in the skills to the new public host, **or** convert skills to authenticated fetch (Step 3d).
- Enable Pages on a paid GitHub plan (Pro/Team/Enterprise) if the site must survive.

**Trade-off:** one repo, but you must touch every consumer and either pay for Pages or drop it. More work, more breakage surface. Only choose if the user wants a single private repo and is fine migrating the public pieces.

> If the user is "not ready" (the usual state): **do Steps 3a–3c now** (team readiness is safe and reversible), **stage the engine landing** (Step 5) but DO NOT push IP into the still-public repo, and hold the actual visibility flip (Step 4) until they say go.

## Step 3 — Team readiness (safe to do anytime, before the flip)

**a. Confirm the access list.** Ask the user exactly who needs access once private: named humans, VAs, and any service/CI account. Default to **least privilege**.

**b. Grant via an org team, not per-repo collaborators.** Cleaner to manage and audit:
```bash
gh api -X PUT orgs/NEXUS-MKII/teams/<team-slug>/repos/NEXUS-MKII/dna-x-delivered \
  -f permission=push        # or 'pull' for read-only VAs, 'admin' for maintainers
# add members to the team:
gh api -X PUT orgs/NEXUS-MKII/teams/<team-slug>/memberships/<github-username> -f role=member
```
Do this **while the repo is still public** — access is a no-op until the flip, so nobody is locked out at the moment you flip.

**c. Each member sets up auth so `git` keeps working after the flip.** Public clones need no auth; private ones do. For each person:
- **Claude Code / gh CLI users:** `gh auth login` (or already org-authed) — `gh` carries the token, clones/pulls just work.
- **Plain git users:** either an **SSH key** added to their GitHub account (`git remote set-url origin git@github.com:NEXUS-MKII/dna-x-delivered.git`) or a **fine-grained PAT** with `repo` read scoped to NEXUS-MKII, used as the HTTPS password.
- **Existing local clones stay valid** — the remote URL doesn't change; only auth starts being required. Anyone who cloned anonymously just needs to authenticate on their next pull.

**d. (If any fetched spec goes private) switch that skill to authenticated fetch.** Replace the anonymous raw URL with a token'd request. Pattern for the skill body:
```
Fetch with the GitHub token in scope (gh api or an Authorization: Bearer <token> header):
  gh api repos/NEXUS-MKII/dna-x-delivered/contents/specs/builds/gx-1.md --jq '.content' | base64 -d
```
Prefer keeping specs public (Option A) so you don't have to touch every skill.

**e. Send the team a heads-up.** Short, factual — DO NOT send on anyone's behalf without the user's OK; draft it for them:

> **Heads-up: DNA-X repo going private on <date>.** If you work in `dna-x-delivered`, make sure you can authenticate to GitHub (run `gh auth login`, or add an SSH key / PAT). Existing clones keep working — you'll just need to be signed in on your next pull. You've been added to the `<team>` team. Public raw links and the Pages site are being handled separately; if a skill or an opener link stops fetching, flag it. Questions → chris@nowgroup.co.nz.

## Step 4 — Execute the flip (only when the user says go)

```bash
# 1. Final pre-flight: confirm team access is in place (Step 3b) so no one is locked out.
gh api repos/NEXUS-MKII/dna-x-delivered/collaborators --jq '.[].login'   # includes team-derived access
# 2. Flip visibility (this is the irreversible-feeling moment; confirm with the user first):
gh api -X PATCH repos/NEXUS-MKII/dna-x-delivered -f visibility=private -f name=dna-x-delivered
# 3. Pages: on GitHub Free the site auto-unpublishes when private. If it must survive, move it
#    (Option A public repo) BEFORE this step, or upgrade the plan and re-enable Pages after.
```

> **Confirm with the user before running the PATCH.** Going private is outward-facing and its side effects (dead public links, unpublished Pages) hit real people. Once public content has been indexed/cached/cloned, private-ing the repo does **not** retract those copies — say so.

## Step 5 — Land the X-Pipe (GX-1) engine (the reason we're here)

The engine (`lib/enrichment_engine/**` + `enrich_key_person.js`, `gx1_leadgen*.js`, `push_csv_to_sheet.js`, `smoke_enrichment.js`, `smoke_mode_b.js`, `runbooks/`) is the **IP**. It currently lives in the legacy `baa-booking-test` local project (no remote).

**Rule: never push the engine into the repo while it is public.** Land it into the **private** side only (private repo in Option A, or after the flip in Option B).

When landing:
- Export sterile with `git archive HEAD -- <paths>` from `baa-booking-test` (tracked-only = secret-free by `.gitignore`); exclude `.env`, `tokens/`, `cache/`, operator/client data.
- **Resolve the one cross-dependency:** `lib/enrichment_engine/modes/csv_import.js` imports `parseCsv` from `server/adapters/silos/sheets.js` (X-cal's tree). Bring `server/adapters/silos/` into the engine so it's self-contained, or inline `parseCsv`.
- Ship an **engine-only `package.json`**: `@anthropic-ai/sdk`, `apify-client`, `googleapis`, `p-queue`, `luxon`, `dotenv`, `axios` (drop express/stripe/handlebars/jwt — those are X-cal).
- Put it under a clear path (e.g. `x-pipe/` or `DNA-X/gx-1-engine/`) with a README. Keep `specs/builds/gx-1.md` + `skills/dna-x-gx-1.md` as the spec/skill layer that already exists.
- `node --check` the entry scripts before pushing to confirm the extraction resolves.

## Step 6 — Verify & rollback

**Verify after the flip:**
- Run `dna-x-gx-1` (and any spec-fetching skill) — its spec fetch must still succeed (public spec, or authenticated). If it 404s, its spec went private without Step 3d.
- Test an opener install raw link the way a VA would — must still resolve (Option A) or be pointed at the new public host (Option B).
- `curl -sI https://nexus-mkii.github.io/dna-x-delivered/` — 200 if Pages survived, 404 if it unpublished (expected on Free/Option B).
- A team member does a fresh authenticated `git clone` — succeeds.

**Rollback** (if something load-bearing broke and you need to buy time):
```bash
gh api -X PATCH repos/NEXUS-MKII/dna-x-delivered -f visibility=public -f name=dna-x-delivered
```
Re-public restores raw URLs + Pages immediately. It does **not** un-expose anything already exposed while public — so if the engine IP was (against the rule) pushed while public, re-publicing doesn't help; that IP is considered leaked and needs rotation/assessment, not a visibility toggle.

---

## One-line summary for the user
Going DNA-X private is safe **only after** you (1) decide split-vs-whole-private, (2) preserve or migrate the public raw-spec URLs + Pages + opener install, and (3) put every team member on org-team access with working git auth. The engine IP lands on the **private** side only — never into the repo while it's public.
