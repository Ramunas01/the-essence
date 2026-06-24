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

**GATE RESULT (2026-06-24): PASSED.** All three axes were hand-encoded by the
human and the consultant (see `docs/encoding-trials.md`): kidney = relation
axis, brown-kayak = time axis, kidney/shark = abstraction axis. The substrate
held; the relational/temporal duality fell out spontaneously (kidney functions
written once folded as relations, once unfolded as a state machine), and the
comparison demo distinguished leaf differences (prunable) from root
differences (essence) — giving the importance model for free. Four strain
findings were logged and resolved in **D-11**.

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

## D-11 — Fold all four strain findings into SCHEMA v0.1 · 2026-06-24 · LOCKED
Decided by human + consultant after the T-3 gate (D-9). The four findings
from `docs/encoding-trials.md` are folded into the schema now rather than
deferred:
1. **Metalinguistic facts** (`renal`, `nephro-`) live in eolex / a thin
   lexical-annotation layer, NOT the world-graph. Schema draws the boundary.
2. **Setting/environmental & n-ary states** → make **setting a first-class
   entity with its own worldline** ("sun shining" → "sky got dark" is just
   the setting's temporal axis, no special case), and allow a single state to
   attach to two or more entities (genuinely joint states, "boy and kayak
   laughed"). No new mechanism.
3. **Attitude / intentional node type** (believes / wants / fears) whose
   content is a (often hypothetical/future) slice. Folded NOW, not deferred,
   because a plot *is* the trajectory of what a protagonist wants and whether
   they get it — the attitude/goal layer sampled along time. Defer it and any
   future plot census has almost nothing to cluster on. (Ties to the
   completeness flag: a hoped-for reunion points at an unknown-continuation
   slice.)
4. **Holes** already worked; formalize as `completeness` flag. No change.

Merge/split stays reserved (D-7). Rationale that none expands scope: (1) and
(3) add a thin layer and one node type; (2) reuses the worldline mechanism.

## D-12 — Plot census is a capstone probe, not near-term build · 2026-06-24 · DIRECTION
The "how many plots are in TinyStories" question is reframed as a *curve, not
a scalar*: two stories are the same plot when their anti-unified skeleton
keeps its root structure and differences are leaf-level; climb the abstraction
axis and plots merge, descend and they split. The real object is the
dendrogram; "how many plots" is wherever you cut it. This is simultaneously
(a) the most honest "did we forget a dimension?" coverage test — clustering
failures point straight at missing/miscalibrated schema parts — and (b) a
plausible methods+corpus-characterization paper (TinyStories' own diversity
was measured only lexically; Reagan/Vonnegut emotional-arc work and folktale
motif indices cluster on different axes; typed worldline-graphs reduced by
anti-unification is a distinct instrument). It depends on the whole pipeline
being trustworthy, so it is the **capstone milestone, not near-term**. Its
requirements are allowed to *constrain* the schema (already did, via #3) but
must NOT pull design forward. A cheap manual precursor (hand-sort 50–100
stories into plot piles) gives the human gold-standard needed to validate any
future automated clustering, and surfaces blind spots for an afternoon's
reading.
