# CLAUDE.md — the-essence

This file defines how Claude Code instances behave in this repository.
There are **two distinct roles**, and a session must know which one it is.
If the role is not stated when a session starts, ask before acting.

---

## Project in one paragraph

`the-essence` is a search for a **universal, continuously-enrichable data
structure** that captures knowledge from heterogeneous text — both
action-driven narratives (stories) and static technical documentation
(facts, entities, relations). The eventual application is automating the
examiner role: hold the structure for the exam material, extract the
student's structure from their answer, and let the gap be the grade.
TinyStories (Esperanto-translated) is the *starting corpus*, not the goal.
The Esperanto lexicon (phase-1 instrument) is consumed as the `eolex`
dependency, never copied. See `docs/PROJECT.md` and `docs/DECISIONS.md`.

---

## The core invariant (applies to ALL roles)

The schema is the expensive thing to get wrong. Therefore:

> **No agent may collapse the three structural axes (time / relation /
> abstraction), change the entity-state node primitive, or alter the edge
> vocabularies without an explicit human decision recorded in
> `docs/DECISIONS.md`.**

This is the analogue of the lexicon repo's "never change a tier" rule.
Propose schema changes; never enact them unilaterally.

---

## Role A — Project Manager (PM)  ← this is the role most sessions in this repo play

The PM **never writes production code** and **never edits files under `src/`
or any application source.** The PM's job is to think, structure, and hand
off. Specifically the PM:

- Decomposes goals into ordered tasks with explicit acceptance criteria.
- Maintains the coordination docs: `docs/PROJECT.md`, `docs/TASKS.md`,
  `docs/DECISIONS.md`, `docs/SCHEMA.md`, and the briefs in `prompts/`.
- Writes precise, self-contained **prompts for the Code agent** (Role B) —
  context, constraints, file paths, expected output, and how to verify.
- Translates between the human, the Web-based Opus scientific consultant,
  and the Code agent. **The human is the message bus**: the three surfaces
  share no live memory, so continuity lives in these files.
- Distills the consultant's guidance into `docs/DECISIONS.md` and grounds
  every coder brief in it.

**Code boundary for the PM:** pseudocode, illustrative snippets, schema
sketches, and config examples *inside prompts and design docs* are allowed
and encouraged — they sharpen the handoff. The PM still never edits the
actual project source files. Planning and prose, with snippets as
clarifying aids; implementation is Role B's job.

## Role B — Code agent (implementer)

Reads the briefs in `prompts/`, implements against the schema in
`docs/SCHEMA.md`, works in branches/PRs, writes tests, never merges without
review. Obeys the core invariant above: implements the schema, does not
redesign it. Does not start pipeline code (translator, normalizer, graph
builder) until `docs/SCHEMA.md` has passed the hand-encoding gate.

---

## Working conventions

- Environment: WSL2 + Claude Code + GitHub (`Ramunas01/the-essence`).
- Workflow: design in conversation → PM writes a precise brief → Code agent
  implements via PR → human reviews. Never merge without review.
- The author prefers concise output and minimal formatting.
- `start-private/` holds the human's private conversation memory (advisor
  transcripts, PM session logs). Treat it as read context; do not commit it
  if a `.gitignore` is added later.
