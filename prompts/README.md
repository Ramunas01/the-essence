# prompts/ — Code-agent briefs

The PM writes self-contained briefs here for the Code agent (implementer)
instance to pick up. The human carries a brief from this folder to the Code
agent's session.

## Why this exists

The PM, the Code agent, and the Web Opus consultant share no live memory.
A brief must therefore stand alone: the Code agent should be able to execute
it without having seen this conversation.

## Brief template

Each brief is `NN-short-name.md` and contains:

- **Goal** — one sentence: what done looks like.
- **Context** — the minimum the implementer needs; link the relevant
  `docs/DECISIONS.md` entries by ID (e.g. "per D-2, D-3").
- **Constraints** — the core invariant (don't redesign the schema), branch/PR
  workflow, no-merge-without-review, any "do not touch" boundaries.
- **Files / paths** — where things live, what to create.
- **Expected output** — artifacts, interfaces, signatures (pseudocode/snippet
  sketches welcome here to pin the interface).
- **How to verify** — the acceptance test the implementer runs before opening
  the PR.

## Status

No briefs written yet. First will be `01-eolex-extraction.md` for task T-4
(lives logically against the esperanto-lexicon repo). It does not depend on
the schema gate, so it can run in parallel with the PM's SCHEMA.md work.
