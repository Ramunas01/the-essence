# DECISIONS — the-essence

Architectural and scientific decisions, with rationale. Sourced from the
Web Opus scientific consultant (transcript in
`start-private/Initial-conversations.DOCX`) and confirmed by the human.
The PM maintains this file; the core invariant in `CLAUDE.md` protects it.

Each entry: **D-n — decision** · *date* · status · rationale.

---

## D-1 — Standalone repository · 2026-06-07 · LOCKED
`the-essence` is a separate repo, not a branch of `esperanto-lexicon`.
Test applied: the new work *consumes* the lexicon, it does not *change* it,
and would never merge back. A branch would drag the lexicon's autonomy rules
onto unrelated code and pollute its history.

## D-2 — Lexicon consumed as `eolex` dependency, not copied · 2026-06-07 · LOCKED
Package the lexicon's read-side as a thin installable library `eolex`
(load db/inventory, Tier-1 reduction, root decomposition, lookups). Data
files ship as package data — exactly one versioned copy. Two copies would
drift and create a "which tier is authoritative" bug class. Build/decompose/
audit tooling stays in the lexicon repo (instrument internals, not for
consumers).

## D-3 — The primitive is the entity-state node · 2026-06-07 · LOCKED
Node = `(entity_id, state_index, {properties}, abstraction_level,
provenance, completeness)`. An entity is a *worldline* — a sequence of
states. A "state" is a snapshot. Collapses the false fork between
event-centric and entity-centric design (block-universe reframing): "what
is" and "what happens" are the same structure sampled along different axes.

## D-4 — Three implemented structural axes · 2026-06-07 · LOCKED
1. **Relational** (within-slice): `is-a`, `part-of`, `has-property`,
   `acts-on` — extensible registered vocabulary. (Documentation axis.)
2. **Temporal** (between states of a worldline) — the **lifecycle four**:
   `introduces` → `functions/interacts` → `modifies` → `removes/transforms`,
   carrying causality and order. (Story axis.)
3. **Abstraction** (between levels): `instance-of` / `generalizes-to`,
   driven by the `eolex` Tier-1 reduction. Enables comparison and
   simplification. (Lexicon axis.)

These three are the irreducible structural set. Everything else is a
property hanging on a node.

## D-5 — Holes are first-class · 2026-06-07 · LOCKED
Unknown/partial knowledge is represented explicitly: each node/edge carries
a completeness flag `observed | inferred | unknown-continuation`. "The boy
is happy and we never learn his fate" = a worldline with one observed state
and an explicitly unobserved continuation. Texts are sparse snapshots of
reality; the structure says so rather than hiding it.

## D-6 — Provenance on every node and edge · 2026-06-07 · LOCKED
Every node/edge records which text and which span it came from. We never
represent "the kidney" — only what a given text *asserts* about it.

## D-7 — Merge/split axis reserved, unimplemented · 2026-06-07 · LOCKED
Cross-worldline temporal edges (boy's last state → `part-of` → wolf's
state = merge; two outgoing continuation edges = split). Mereology-over-time
(international-trade goods classification, atoms/energy conversion) is
expressible without a new primitive. Flagged as a reserved edge class in the
schema so its existence constrains the design without costing build time.

## D-8 — Entity identity-across-slices is a named first-class problem · 2026-06-07 · OPEN
Worldlines assume trackable identity across states. Easy-ish in stories
(coreference); hard in docs and across abstraction levels (is a modified
kidney the same kidney?). Expect the hardest bugs here. Code agent must
treat entity resolution as first-class.

## D-9 — First deliverable is the schema spec + hand-encoding gate, NOT code · 2026-06-07 · LOCKED
Before any pipeline code, produce `docs/SCHEMA.md` and hand-encode three
artifacts in it on paper:
1. one TinyStory (tests the **time** axis);
2. a 3-sentence kidney paragraph (tests the **relation** axis);
3. the same entity at two abstraction levels — "kidney" vs "waste-removal
   organ", with a shark's mechanism beside it (tests the **abstraction**
   axis + that anti-unification lands where intuition says).

If the schema strains, we learn it in an hour. This gate must pass before
the translator / normalizer / graph builder are written.

## D-10 — Comparison model · 2026-06-07 · DIRECTION (not yet detailed)
Align worldlines/relation-sets after climbing to a shared abstraction level
(anti-unification / least-general generalization → yields shared skeleton +
differences together), then measure what's missing/different *per axis*.
Per-axis decomposition IS the importance model: a missing root-cause
transition matters more than a missing leaf property. Fractal/depth-weighting
= distance along the abstraction axis from the comparison point. Prior art to
stand on: Schank (Conceptual Dependency), Propp (functions), Greimas
(actantial roles), Sowa (conceptual graphs), AMR, graph/tree edit distance,
Weisfeiler–Leman canonical labeling, knowledge-component models in ITS.
NOTE: these theories are *registered type-sets that plug into the typed-graph
socket*, not the spine itself — do not bake any single one into the primitive.
