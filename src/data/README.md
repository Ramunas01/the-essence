# src/data

Scripts that fetch and stage raw corpora locally. Output lands in `data/` (gitignored).

## TinyStories sample

```
python src/data/fetch_tinystories.py
```

Produces `data/tinystories/sample-200.jsonl` — 200 deduplicated stories from the
`roneneldan/TinyStories` train split. Requires `pip install datasets`.
