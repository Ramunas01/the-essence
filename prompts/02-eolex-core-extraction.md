# Brief 02 — Factor a thin `eolex` read-core (lexicon repo)

**For:** the Code agent working in the **`esperanto-lexicon`** repo
(`/home/ramunas/projects/esperanto-lexicon`) — NOT the-essence.
**Decision:** D-13 in the-essence `docs/DECISIONS.md` (Option A).
**Depends on:** nothing in the-essence; can proceed in parallel with all
the-essence work. No the-essence schema dependency.

## Goal

Carve the lexicon's **read-side** out of the existing `eolex_relevance`
package into a thin, installable core package **`eolex`**, so that BOTH
`eolex_relevance` and the new `the-essence` project depend on one copy of the
read machinery (no data duplication, no drift). Then extend it to expose the
**pedagogical Tier 1–4** data the-essence's abstraction axis needs, which the
current bundle does NOT carry.

## Context — what already exists

On branch `feat/eolex-relevance-package`, the package `src/eolex_relevance/`
already contains the machinery:
- `eo_decomposer.py` — `Decomposer.decompose / decompose_word / root_tier`;
  `Decomposition` (`.head`, `.is_compound`, `.roots`), `ContentRoot`.
- `resolver.py` — `Resolver.resolve` (multilingual text → content roots),
  `tokenize`, `TokenResolution`, `_lookup`.
- `bundle.py` — `Bundle`, a portable SQLite carrying `eo_root(root, tier,
  prod, gloss)`, `word_root(lang, word, root)`, `vocab`.
- `scorer.py` — `RelevanceScorer` (TF-IDF over roots → domain scores). This is
  relevance-specific and **stays in `eolex_relevance`**; the-essence does not
  need it.

## ⚠️ CRITICAL — two distinct tier systems, do not conflate

(Verified in `lexicon_v2.db` on 2026-06-24; this is the DOCX's standing warning.)

| System | Where | Values | Meaning | In bundle today? |
|---|---|---|---|---|
| **Inventory tier** | `concept_root.tier`, `eo_inventory` | core / extended / tail / modern | ESPDIC productivity band | ✅ yes (`eo_root.tier`) |
| **Pedagogical tier** | `concept_lang.tier` (+ `cefr_level`) | 1 / 2 / 3 / 4 | expertise / abstraction ladder (Tier 1 ≈ child) | ❌ NO |

the-essence's **abstraction axis** (its SCHEMA §3.3) runs on the **pedagogical**
tier, not the inventory tier. So `eolex` must expose **both**, under names that
can never be confused, and the bundle/build must be extended to carry the
pedagogical tier + CEFR (keyed by word+lang from `concept_lang`).

NB: `eolex` provides the abstraction *level label* only. It does NOT provide
semantic hypernyms (kidney→organ); that generalisation is the-essence's own
concern and no hypernym graph exists in the lexicon today. Do not invent one.

## Scope

**A. Factor the core** (`eolex`):
- Move the read-side — decomposer, resolver, bundle (load + query path) — into
  a new package `eolex/`. Keep the bundle *builder* (`build.py`) wherever it
  must read the source db/inventory; the downstream contract is "load a bundle,
  answer queries", so consumers never need the source db.
- Refactor `eolex_relevance` to `import` from `eolex` (scorer, cli stay there).
  `eolex_relevance`'s public behaviour and tests must be unchanged after the
  refactor (this is the regression guard).

**B. Extend the read-side with the pedagogical tier:**
- Add `concept_lang(word, lang, tier, cefr_level)` to the bundle schema and
  the builder, sourced from `lexicon_v2.db`.
- Expose it in the core API, named distinctly from the inventory tier.

## Target public API (sketch — adjust names with care)

```python
from eolex import Lexicon

lex = Lexicon.load()                       # default packaged bundle; or .load(path)

# morphology / inventory side (already exists)
lex.roots("akvo", lang="eo")               # -> ["akv"]            content roots
lex.decompose("akvobirdo", lang="eo")      # -> Decomposition(roots, head, is_compound)
lex.inventory_tier("akv")                  # -> "core"|"extended"|"tail"|"modern"|None
lex.gloss("akv")                           # -> "aquatic, of water, ..." | None

# expertise / abstraction side (NEW — the-essence abstraction axis)
lex.pedagogical_tier("akvo", lang="eo")    # -> 1|2|3|4|None        EXPERTISE ladder
lex.cefr("akvo", lang="eo")                # -> "A1".. | None
```

Keep `Decomposer` / `Resolver` / `Bundle` importable from `eolex` for advanced
use, but `Lexicon` is the thin facade the-essence will normally call.

## Constraints

- Branch + PR in the **esperanto-lexicon** repo; no merge without human review.
- This repo is the frozen *instrument* — do not change any entry's tier or the
  inventory data (the lexicon's own CLAUDE.md autonomy rule). This is a
  packaging/exposure refactor, not a data change.
- `eolex_relevance`'s existing tests must still pass unchanged.
- Data ships as package data inside `eolex` (D-2) so a `pip install` from git
  needs no separate db.

## Packaging / install target

```
esperanto-lexicon/
  eolex/             # NEW thin read core (own pyproject; ships the bundle as package data)
  eolex_relevance/   # depends on eolex; keeps RelevanceScorer
```
Consumable by the-essence as:
`pip install "eolex @ git+https://github.com/Ramunas01/esperanto-lexicon.git#subdirectory=eolex"`

## How to verify (before opening the PR)

1. `eolex_relevance`'s existing test suite passes unchanged (regression guard).
2. New `eolex` tests: `Lexicon.load()` then —
   - `inventory_tier` returns a core/extended/tail/modern value for a known root;
   - `pedagogical_tier("<a known Tier-1 word>", "eo")` returns `1`; a Tier-3
     word returns `3`; counts reconcile with the db (1550/3139/97 at 1/2/3);
   - `decompose` of a known compound returns the expected head + roots;
   - `gloss` returns a non-empty string for a core root.
3. A clean `pip install` of `eolex` alone (no source db present) can still
   answer all of the above — proves the bundle is self-contained.

## PR description should note

The bundle schema change (added `concept_lang`), the source db revision used,
and confirmation that `eolex_relevance` is unchanged behaviourally.
