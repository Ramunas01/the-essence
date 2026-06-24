# Manual plot-sort — TinyStories sample-200 (T-12)

**Purpose (D-12, T-12):** by-eye gold-standard grouping of the 200 stories into
"same plot" piles. Two deliverables, of which the **second is the real prize**:
1. The piles themselves — the human reference any future automated clustering
   is measured against.
2. **The blind-spots log** — every time you judge two stories same/different
   using something the *schema can't currently represent*, that's a gap in the
   data structure. Catching those is the whole point of doing this by hand.

This file is the annotation overlay. The raw data
(`data/tinystories/sample-200.jsonl`) stays untouched; stories are referenced
by their `id` (0–199).

## How to read the stories

From the repo root, print them one per id (pipe to `less`):

```bash
python3 -c "import json;[print(f'\n===== id {json.loads(l)[\"id\"]} =====\n'+json.loads(l)[\"text\"]) for l in open('data/tinystories/sample-200.jsonl')]" | less
```

Or one at a time: change `== N` to the id you want:
```bash
python3 -c "import json;[print(json.loads(l)['text']) for l in open('data/tinystories/sample-200.jsonl') if json.loads(l)['id']==0]"
```

---

## Piles

Give each pile a short essence label (the shared skeleton, not the surface).
List the story ids in it, optionally a one-line gist. Start loose; merge/split
piles freely as you go.

### Pile A — <label, e.g. "loses object → grief, no return">
- ids:
- gist:

### Pile B — <label>
- ids:
- gist:

### Pile C — <label>
- ids:
- gist:

<!-- add piles as needed -->

### Unsure / singletons (don't fit a pile yet)
- ids:

---

## Blind-spots log  ← the important part

One line each time the same/different call rests on something the three axes
(time / relation / abstraction) + attitude nodes can't yet hold. Note the ids,
what feature you used, and whether the schema can represent it.

Example: `ids 12 vs 45 — I called these "the same" because both have a moral
lesson at the end; the schema has no "theme/moral" node — POSSIBLE GAP.`

1.
2.
3.

---

## Notes for the PM / consultant
- Roughly how many piles fell out, and at what altitude you were cutting
  (fine-grained "boy+kayak" vs coarse "friendship") — this is the census-curve
  question (D-12), useful even as a rough feel.
