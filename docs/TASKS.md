# TASKS — the-essence

Maintained by the PM. Status: `TODO` / `DOING` / `BLOCKED` / `REVIEW` / `DONE`.
Each task has an owner and acceptance criteria. IDs are stable.

Owners: **PM** (this role) · **CODE** (implementer agent) · **HUMAN** ·
**CONSULTANT** (Web Opus).

Last updated: 2026-06-24 (PM session 3).

---

## Tonight — low-cognition / technical (human's energy is low)

### T-11 · CODE · Fetch TinyStories sample · TODO ← hand this to the Code agent now
- Brief: `prompts/01-tinystories-fetch.md`. Pull 200 deduped stories from
  `roneneldan/TinyStories`, store as gitignored JSONL, commit the script.
- Independent of the schema — safe to run tonight.
- Acceptance: see brief (200 unique stories, valid JSONL, script reproducible).

## For your morning — full-capacity work

### T-2 · PM · Draft `docs/SCHEMA.md` · REVIEW ← drafted; awaiting your + consultant review
- v0.1 DRAFT written against D-3/4/5/6/7/8/11. Folds all four strain findings
  (setting-as-worldline + n-ary states, attitude node, lexical layer boundary,
  holes). Ends with a 5-point review checklist (causality, relation registry,
  attitude content, state_index ordering, untested gaps).
- Acceptance: consultant + human sign off, or return edits → PM does v0.2.

### T-12 · HUMAN · Manual plot-sort of the sample · TODO (needs T-11)
- Read the 200 (or 50–100) stories, sort into plot piles by eye. Produces the
  human gold-standard for any future automated clustering, and surfaces schema
  blind spots (any feature you use to judge same/different that the schema
  can't hold = a gap). Cheap precursor to D-12.
- Acceptance: a piles list + a note of any "can't-encode-this" moments.

### T-5 · CONSULTANT+HUMAN · Census altitude(s) decision · TODO
- Decide which abstraction level(s) the eventual plot census reports (it's a
  curve, not a scalar — see D-12). Feeds the comparison engine design later.

## Now — design backbone (in progress / parallel)

### T-1 · HUMAN · GitHub connection + setup commits · DONE
- Repo connected (`Ramunas01/the-essence`, `main`); `start-private/`
  gitignored; scaffold + `encoding-trials.md` pushed.

### T-3 · gate · Hand-encoding acceptance test · DONE — PASSED (2026-06-24)
- All three axes hand-encoded in `docs/encoding-trials.md`; substrate held;
  comparison demo gives the leaf-vs-root importance model. Strain findings
  resolved in D-11. See D-9 gate result.

### T-4 · CODE · Extract `eolex` read-only API · TODO (parallel — no schema dep)
- In the **esperanto-lexicon** repo: thin installable package exposing load
  db/inventory, Tier-1 reduction, root decomposition, lookups. Data ships as
  package data (D-2). PM to write `prompts/02-eolex-extraction.md` before
  handing off. Lower priority than T-11 for tonight (more cognition to review).

## Next — pipeline (BLOCKED until SCHEMA v0.1 is signed off, T-2)

### T-6 · CODE · Translator: TinyStories → Esperanto · BLOCKED-by-T2
Thin: ~50 stories, human-validated sample.

### T-7 · CODE · Normalizer (two layers) · BLOCKED-by-T2
entities → typed role placeholders; predicates → Tier-1 root via eolex.

### T-8 · CODE · Graph builder · BLOCKED-by-T2
story → labelled directed multigraph; canonical form; model separate from render.

### T-9 · CODE · Comparator · BLOCKED-by-T2
edit-distance baseline, then anti-unification (the research core).

### T-10 · CODE · Visualizer · BLOCKED-by-T2
last, lowest priority; pure rendering.

## Capstone (constrains design, must NOT pull it forward — D-12)

### T-13 · Plot census of TinyStories · FUTURE
Structural plot census via anti-unification over the abstraction ladder →
dendrogram ("how many plots" = where you cut it). Doubles as the coverage
probe and a possible methods+corpus paper. Requires the whole pipeline to be
trustworthy. T-12 (manual sort) is its cheap precursor / gold-standard.

## Done
- T-1 (GitHub connection), T-3 (hand-encoding gate — PASSED).
