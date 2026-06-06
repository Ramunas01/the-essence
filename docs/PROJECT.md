# PROJECT — the-essence

**Status:** Design phase. No application code yet. Schema not yet drafted.
**Last updated:** 2026-06-07 (PM session 1)

## Goal

Find a **universal, continuously-enrichable data structure** that represents
knowledge extracted from heterogeneous text, where both genres are *special
cases of one structure*, not one-primary-one-bolted-on:

- **Narrative** (stories): long in time, sparse in relations — follow a
  worldline through many states.
- **Documentation** (technical/normative): flat in time, dense in relations
  — one slice, many entities, richly related.

## Driving application

Automated examiner. The exam material defines worldlines/relations at some
abstraction level with known holes. A student answer is extracted into the
same structure. **Depth of expertise = worldline completeness × relational
density × abstraction range** — a computable graph property, not a metaphor.
A novice has the static relations; an expert has reconstructed the
lifecycles (introduce → function/interact → modify → remove/transform).

## Scope discipline

- **Shrink the genre** (stories first, TinyStories corpus) — SAFE.
- **Do NOT shrink the structure to fit stories** — the trap. Design the
  universal layered structure *now*, with documentation explicitly in mind;
  implement only the narrative layer first. The static/relational layer is
  designed but stubbed until a documentation corpus arrives.

## Relationship to the Esperanto lexicon

The lexicon (phase 1, frozen) is the **instrument**. It is consumed as a
packaged read-only dependency `eolex`, **not copied** into this repo. It
provides the abstraction-axis machinery: Tier-1 root reduction, root
decomposition, lookups. `pip install "eolex @ git+https://github.com/Ramunas01/esperanto-lexicon.git"`

## The three roles

| Role | Surface | Job |
|------|---------|-----|
| Scientific consultant | Web Claude Opus (claude.ai) | Theory, schema soundness, prior-art anchoring. Reads repo via GitHub. |
| Project Manager | Claude Code (this repo, thinking mode) | Decompose, write coder briefs, maintain these docs, translate between roles. Never codes. |
| Code agent | Claude Code (this repo, implementer) | Implements against the schema via PRs. |

The human carries information between the three surfaces (no shared memory).
The files in `docs/` and `prompts/` are the durable continuity.

## Open / hard problems (named, not solved)

- **Entity identity across slices** — is the boy in slice 1 the boy in
  slice 5? Coreference in stories; philosophically hairy in docs and across
  abstraction levels. Treat entity resolution as first-class, not a detail.
- **Merge/split axis** (reserved, unbuilt) — one worldline ending to become
  part of another (boy eaten by wolf → part-of wolf). Expressible as
  cross-worldline temporal edges; designed-for but not implemented.
