# TASKS — the-essence

Maintained by the PM. Status: `TODO` / `DOING` / `BLOCKED` / `REVIEW` / `DONE`.
Each task has an owner and acceptance criteria. IDs are stable.

Owners: **PM** (this role) · **CODE** (implementer agent) · **HUMAN** ·
**CONSULTANT** (Web Opus).

---

## Now (design phase — the schema gate is the critical path)

### T-1 · HUMAN · Two setup commits to the repo · TODO
- `docs/` exists (done locally) and `CLAUDE.md` exists (done locally) — once
  reviewed, commit/push to `Ramunas01/the-essence`.
- Acceptance: repo on GitHub has `CLAUDE.md` + `docs/` so the consultant can
  pull current state and both agents attach to a canonical home.

### T-2 · PM · Draft `docs/SCHEMA.md` · TODO (next PM action)
- Write the typed-graph substrate: entity-state node primitive (D-3), the
  three edge vocabularies (D-4), reserved merge/split class (D-7), holes &
  provenance (D-5/D-6), identity stated as open (D-8).
- Acceptance: a reader can encode a node/edge without inventing structure;
  every field traces to a decision in DECISIONS.md.

### T-3 · PM (+HUMAN+CONSULTANT review) · Hand-encoding acceptance test · TODO
- In/alongside SCHEMA.md, hand-encode the three artifacts from D-9
  (TinyStory, kidney paragraph, two-abstraction-levels+shark). Flag every
  place the schema strains.
- Acceptance: all three fit one schema, OR strain points are documented for
  human+consultant review. **This is the gate.** Nothing in T-6+ starts
  until this passes.

### T-4 · CODE · Extract `eolex` read-only API · TODO (parallel — no schema dep)
- In the **esperanto-lexicon** repo: carve out a thin installable package
  `eolex` exposing load db/inventory, Tier-1 reduction, root decomposition,
  lookups. Data files ship as package data. (D-2)
- Acceptance: `pip install "eolex @ git+…"` then `import eolex` gives
  word→root/tier/gloss. Build/audit tooling NOT included. Tests + PR, no
  merge without review.
- NOTE: PM to write this brief into `prompts/` before handing to CODE.

### T-5 · CONSULTANT+HUMAN · Confirm essence-theory anchoring · TODO
- Confirm D-10 stance (theories are pluggable type-sets, not the spine) is
  the bet, and which type-sets seed the narrative layer first.
- Acceptance: recorded as a DECISIONS.md update; gates the edge vocabularies
  in SCHEMA.md if it changes anything.

## Next (only after the T-3 gate passes)

### T-6 · CODE · Translator: TinyStories → Esperanto · TODO/BLOCKED-by-T3
- Thin: ~50 stories, human-validated sample. Don't over-engineer.

### T-7 · CODE · Normalizer (two layers) · TODO/BLOCKED-by-T3
- entities → typed role placeholders (Peter → Boy-1); predicates → Tier-1
  root via eolex. Most reusable long-term component.

### T-8 · CODE · Graph builder · TODO/BLOCKED-by-T3
- story → labelled directed multigraph; canonical form for
  equality-up-to-relabeling. Keep model separate from rendering.

### T-9 · CODE · Comparator · TODO/BLOCKED-by-T3
- edit distance baseline, then anti-unification (the research core).

### T-10 · CODE · Visualizer · TODO/BLOCKED-by-T3
- last, lowest priority; pure rendering of the graph (triangle=protagonist,
  square=secondary, arrows/colors=relation types).

## Done
- (none yet)
