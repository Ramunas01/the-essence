# Brief 01 — Fetch a TinyStories sample

**For:** the Code agent (implementer) instance, run on WSL.
**Depends on:** nothing. Independent of the schema work — safe to run now.
**Does NOT touch:** the schema, any representation/normalization/translation
code (those are gated by `docs/SCHEMA.md` and are out of scope here).

## Goal

Pull a clean, deduplicated sample of **200 stories** from the TinyStories
dataset and store them locally as JSONL, so the human has raw material ready
for a manual plot-sorting pass and the pipeline has a fixture later. Pure
fetch-and-store. No analysis, no transformation.

## Context

`the-essence` is in design phase; this is plumbing that doesn't wait on the
schema. The dataset is `roneneldan/TinyStories` on HuggingFace (synthetic
short stories in a ~1,500-word child vocabulary). The advisor requested a
~200-story sample as low-effort groundwork. Raw corpora stay out of the public
repo (see "Output"), so this is local + a reproducible script.

## Constraints

- Branch + PR; do not merge without human review.
- Keep it tiny — one small script, standard deps (`datasets` or a direct
  parquet/HTTP pull). Don't add a heavy framework.
- Deterministic sample: take the **first 200** unique stories from the train
  split (after dedup) so the sample is reproducible — do NOT random-sample
  without a fixed seed. If you use a seed, record it in the output metadata.
- Do not translate, normalize, or parse the stories. Raw text only.

## Files / paths

- Script: `src/data/fetch_tinystories.py` (create the dirs).
- Output: `data/tinystories/sample-200.jsonl` — **gitignored** (the repo's
  `.gitignore` already excludes `data/`). The script is committed; the data
  is reproduced by running it.
- If a README helps, `src/data/README.md` with the one-line run command.

## Expected output

`data/tinystories/sample-200.jsonl`, one JSON object per line:

```json
{"id": 0, "text": "<story text>", "n_chars": 412, "source": "roneneldan/TinyStories", "split": "train"}
```

- `id`: 0..199, the post-dedup ordinal.
- Dedup by exact normalized-text hash (strip surrounding whitespace); drop
  duplicates before numbering.
- Script prints a summary on completion: total fetched, duplicates dropped,
  final count (must be 200), output path.

## How to verify (run before opening the PR)

1. `python src/data/fetch_tinystories.py` exits 0 and prints the summary.
2. `wc -l data/tinystories/sample-200.jsonl` → `200`.
3. Each line parses as JSON and has all five keys; `id` runs 0–199 with no
   gaps; no two `text` values are identical.
4. `git status` shows the script (and README) staged but NOT the `.jsonl`
   (confirms the gitignore is working).

## Notes for the PR description

State the dataset revision/commit hash you pulled from (for reproducibility),
the dedup count, and whether you used streaming or a full download.
