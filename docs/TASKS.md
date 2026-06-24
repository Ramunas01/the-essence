# TASKS — the-essence

Maintained by the PM. Status: `TODO` / `DOING` / `BLOCKED` / `REVIEW` / `DONE`.
Each task has an owner and acceptance criteria. IDs are stable.

Owners: **PM** (this role) · **CODE** (implementer agent) · **HUMAN** ·
**CONSULTANT** (Web Opus).

Last updated: 2026-06-24 (PM session 3).

---

## Tonight — low-cognition / technical (human's energy is low)

### T-11 · CODE · Fetch TinyStories sample · REVIEW — PR #1 open, all checks pass
- Brief: `prompts/01-tinystories-fetch.md`. Done: 200 deduped stories,
  streaming fetch, gitignored JSONL, script committed. Dataset SHA
  `f54c09fd…`; 0 duplicates in first 200. Programmer also fixed `data/` →
  `/data/` so `src/data/` isn't wrongly ignored (correct).
- PM review: clean, minimal (80+/1-), MERGEABLE. **Recommend HUMAN merge.**

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

### T-4 · CODE · Provide `eolex` read API · TODO — RESCOPED (much already exists)
- **Finding (2026-06-24):** the read-side machinery the-essence needs already
  exists in `esperanto-lexicon`, branch `feat/eolex-relevance-package`, as the
  package **`eolex_relevance`** (pushed). It contains:
  - `Decomposer` (`decompose`, `decompose_word`, `root_tier`; ContentRoot /
    Decomposition with `.head`/`.is_compound`/`.roots`) — root decomposition
    + tier, exactly what SCHEMA §3.3 (abstraction axis) needs;
  - `Resolver` (text → content roots, multilingual) — word→root lookup;
  - `Bundle` — a portable SQLite carrying `eo_root(root, tier, prod, gloss)`
    and `word_root(lang, word, root)`; "build-once / load-many" already.
  BUT its **public API is relevance-scoring** (`RelevanceScorer`), which
  the-essence does NOT need; the read primitives are effectively internal.
- NOTE: GitHub `Ramunas01/esperanto-lexicon-knowledge` is NOT this work
  (empty: LICENSE+README). The work is local on the lexicon repo branch.
- **Open decision (human + consultant + lexicon Code agent):** how the-essence
  consumes the read-side — see the two options below. Was T-4 "extract from
  scratch"; now it's "expose / factor the existing read-side." Still no schema
  dependency, can proceed in parallel.
  - **Option A (clean, matches advisor intent):** factor `resolver` +
    `eo_decomposer` + `bundle` read-path into a thin core pkg `eolex` that BOTH
    `eolex_relevance` and `the-essence` depend on. One copy, two consumers.
  - **Option B (fast, coupled):** the-essence depends on `eolex_relevance`
    directly and imports its (non-public) `Decomposer`/`Bundle`. Quick but
    drags in a scorer it doesn't use and relies on internal API.
- Missing either way: an explicit **Tier-1 reduction / generalize-to-Tier-1**
  helper (the abstraction-axis op) on top of `root_tier` + bundle tiers.
- PM to write `prompts/02-eolex-*.md` once the option is chosen.

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
