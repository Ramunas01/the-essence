# SCHEMA — the-essence

> **STATUS: STUB.** This is the canonical home for the data-structure spec.
> It is intentionally not yet filled — drafting it is task **T-2** (PM), and
> it must pass the hand-encoding gate **T-3** before any pipeline code is
> written. Do not invent a competing schema elsewhere. Do not change the
> primitive or axes without a recorded decision (see `CLAUDE.md` invariant).

## Planned contents (to be written in T-2)

1. **The substrate** — a typed directed multigraph over (entities, events,
   concepts).
2. **The node primitive** — entity-state: `(entity_id, state_index,
   {properties}, abstraction_level, provenance, completeness)`. (D-3)
3. **Edge vocabularies** — three implemented axes (D-4):
   - relational (within-slice)
   - temporal (lifecycle four)
   - abstraction (instance-of / generalizes-to)
   - reserved: merge/split cross-worldline edges (D-7), designed-for, unbuilt.
4. **Holes & provenance** — completeness flags and source spans (D-5, D-6).
5. **Identity** — entity-resolution stated as the load-bearing open problem
   (D-8).

## Hand-encoding acceptance test (T-3 — the gate)

Three artifacts to encode by hand in this schema and report strain:
- one TinyStory — exercises the **time** axis;
- a 3-sentence kidney paragraph — exercises the **relation** axis;
- "kidney" vs "waste-removal organ" with a shark's mechanism beside it —
  exercises the **abstraction** axis and tests anti-unification.
