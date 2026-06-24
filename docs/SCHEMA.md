# SCHEMA — the-essence (v0.1 DRAFT)

**Status:** v0.1 DRAFT, awaiting consultant + human review (morning of
2026-06-24+). Drafted by the PM against the decisions locked in
`docs/DECISIONS.md` (D-3, D-4, D-5, D-6, D-7, D-8, D-11) and validated by the
hand-encodings in `docs/encoding-trials.md`.

**Invariant (from `CLAUDE.md`):** no agent may collapse the three axes, change
the entity-state primitive, or alter the edge vocabularies without a recorded
human decision. Propose changes; do not enact them. This file is the canonical
home for the structure — do not invent a competing schema elsewhere.

---

## 1. The substrate

One **typed, directed multigraph** over three node families — *entities*,
*states*, and *concepts* — with typed, labelled edges. Genre is not a
different structure; it is a different *sampling density* along the axes:

- **Documentation** = one fat time-slice: many entities, dense relations, ~no time.
- **Narrative** = sparse relations, long in time: follow a worldline through states.

Both are the same graph. This was confirmed empirically in
`encoding-trials.md`, where the kidney's functions appeared *twice* — folded as
relations and unfolded as a state machine — without being forced.

---

## 2. Nodes

### 2.1 The primitive — entity-state (D-3)

A node is an **entity at one slice**:

```
EntityState = (
  entity_id,           # stable identity of the worldline this state belongs to
  state_index,         # ordinal position along that entity's time axis
  properties,          # {key: value} observed/asserted at this slice
  abstraction_level,   # the eolex Tier / generalisation level of this node
  provenance,          # (text_id, span) — see §5
  completeness         # observed | inferred | unknown — see §4
)
```

An **entity** is the worldline: the ordered sequence of its states. A
**relation** is a property stable across many slices (so stable the text
doesn't date it). An **event/transition** is the difference between two
adjacent states. "What is" and "what happens" are one structure sampled
differently — there is no event-vs-entity choice to make.

### 2.2 Setting as a first-class entity (D-11 #2)

The scene is **an entity with its own worldline**, not a special case.
`sun@shining → sky@dark`, `water@warm` are states on the *setting* entity's
time axis. Environmental change is just the setting's temporal edges.

### 2.3 Joint / n-ary states (D-11 #2)

A single state may attach to **two or more entities** when the state is
genuinely joint: `laughed(boy, kayak)`, `play-together(child, plaything)`.
This is an n-ary attachment, not a copy per entity.

### 2.4 Attitude / intentional nodes (D-11 #3)

A first-class node type for mental states: **believes / wants / fears /
intends**, held by an entity, whose **content is itself a slice** — usually a
*hypothetical or future* one.

```
Attitude = (
  holder_entity,       # who holds it
  mode,                # believes | wants | fears | intends | hopes ...
  content_slice,       # a (possibly hypothetical/future) EntityState or sub-graph
  provenance, completeness
)
```

This layer is load-bearing, not decorative: **a plot is the trajectory of
what an agent wants and whether they get it** (the attitude/goal layer sampled
along time). The kayak's "we will play again" is an `hopes` attitude pointing
at an `unknown-continuation` future slice (§4). Any future plot census
clusters primarily on this dimension (D-12).

### 2.5 Holes (D-5, D-11 #4)

Unknown/partial knowledge is explicit, never silently omitted. A worldline may
terminate in, or contain, an explicit hole. Represented via the `completeness`
flag (§4) and, for a worldline whose successor is unobserved, a dangling
temporal edge marked `unknown-continuation`.

---

## 3. Edges — the three axes (D-4) + reserved (D-7)

### 3.1 Relational (within one slice) — the documentation axis
Extensible, **registered** vocabulary: `is-a`, `part-of`, `has-property`,
`acts-on`, `produces`, `regulates`, … New relation types are added to the
registry, not invented ad hoc in data.

### 3.2 Temporal (between states of a worldline, or where worldlines meet) — the story axis
The **lifecycle four**: `introduces` → `functions/interacts` → `modifies` →
`removes/transforms`. Carries order and causality. Cross-worldline interaction
edges (two entities meeting at a slice, e.g. boy ⟷ kayak at play) live here.

### 3.3 Abstraction (between levels) — the lexicon axis
`instance-of` / `generalizes-to`, powered by the **eolex** Tier reduction. The
abstraction ladder *is* the Tier ladder. Climbing it merges entities
(`kidney` and `shark-rectal-gland` unify to `osmoregulatory-organ` at L2);
descending recovers the diff. This is what makes comparison and pruning work.

### 3.4 Reserved — merge / split (D-7, NOT implemented in v0.1)
A continuation edge crossing into another entity's worldline (boy's last state
→ `part-of` → wolf = merge; two outgoing continuation edges = split).
Mereology-over-time. Designed-for so the schema won't be torn up to add it; do
not build it now.

---

## 4. Completeness

`completeness ∈ {observed, inferred, unknown}` on every node and edge:
- `observed` — the text asserts it directly.
- `inferred` — we filled it from world knowledge / the lifecycle, not the text.
- `unknown` — named but undefined (`salt {undefined}`, `waste {undefined}`).

A worldline endpoint whose successor is unobserved carries an
`unknown-continuation` marker (the boy departs and we never learn his fate =
one observed state + an explicit unobserved continuation). The gap between an
expert's filled-in lifecycle and a novice's stubs is the **gradeable
quantity** for the examiner application.

---

## 5. Provenance (D-6)

Every node and edge records `(text_id, span)`. We never represent "the
kidney" — only **what a given text asserts** about it. Two texts about the same
real entity produce two provenance-tagged sub-graphs that are then *compared*,
not silently merged.

---

## 6. Out of scope — the lexical / metalinguistic layer (D-11 #1)

Facts about *words* — `adjective: renal`, `prefix: nephro-`, part-of-speech,
morphology — are **not** world-graph content. They route to **eolex** or a
thin lexical-annotation layer keyed by token. Keeping them out keeps the
essence graph about the world, not about language.

---

## 7. Open problem — identity across slices (D-8)

Worldlines assume trackable entity identity. Trivial in TinyStories
(coreference); philosophically real at the abstraction axis ("is the shark's
organ *the same as* a kidney one level up?"). **Entity resolution is a
first-class problem for the Code agent, not a detail.** v0.1 does not solve
it; it names it and requires that `entity_id` assignment be an explicit,
auditable step rather than an implicit assumption.

---

## 8. Notation (for hand-encoding and docs)

```
Node:             entity@state {props} ·level· (prov) [completeness]
Relational edge:  A --rel--> B
Temporal edge:    A@s0 ==functions(...)==> A@s1
Abstraction edge: A ~~generalizes-to~~> B
Attitude:         holder: mode → ⟨content slice⟩ [completeness]
```

(Worked examples: `docs/encoding-trials.md` §§1–3.)

---

## 9. Review checklist for the consultant + human

Open points I (PM) want a ruling on before v0.2 / before the Code agent builds
any representation:

1. **Causality**: is it a *property* of a temporal edge, or its own edge type?
   v0.1 treats it as carried by temporal edges — confirm.
2. **Relation registry**: who owns the relational-edge vocabulary, and is it
   frozen per-version or append-only at runtime?
3. **Attitude content**: should a hypothetical content-slice live in the same
   graph (tagged hypothetical) or a separate overlay? v0.1 keeps it in-graph,
   tagged.
4. **`state_index`**: total order per entity, or partial order (to allow
   uncertain/branching time)? v0.1 assumes total order; branching may be
   needed for hypotheticals.
5. Anything the three hand-encodings did NOT exercise that you expect real
   TinyStories (or a documentation paragraph you didn't write) to break.
