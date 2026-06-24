# Encoding trials — the-essence

**Status:** working note / acceptance-test draft (not the canonical `SCHEMA.md`).
**Purpose:** re-encode the first hand-mapped texts in the locked three-axis schema, complete the abstraction-axis gate item, log where the schema strains, and demonstrate that two texts so encoded can be compared.

---

## 0. The schema being tested (locked decisions)

**Primitive — entity-state node:**
`(entity_id, state_index, properties, abstraction_level, provenance, completeness)`
where `completeness ∈ {observed, inferred, unknown}`.

**Three implemented axes (edge kinds):**

- **Relational** (within one slice): `is-a`, `part-of`, `has-property`, `acts-on`, `produces`, `regulates`, … — an extensible, registered vocabulary. This is where *documentation* lives (flat in time, dense in relations).
- **Temporal** (between states of a worldline, or where two worldlines meet): the lifecycle four — `introduces`, `functions/interacts`, `modifies`, `removes/transforms`. This is where *stories* live (long in time, sparse in relations).
- **Abstraction** (between levels): `instance-of` / `generalizes-to`, powered by the eolex Tier reduction.

**Reserved (designed, unbuilt):** merge/split — a continuation edge crossing into another entity's worldline (boy → part-of → wolf).

**Notation used below**
Node: `entity@state {props} ·level· (prov) [completeness]`
Relational edge: `A --rel--> B`
Temporal edge: `A@s0 ==functions(...)==> A@s1`
Abstraction edge: `A ~~generalizes-to~~> B`

---

## 1. Encoding A — kidney (documentation; relation axis dominant)

A documentation text is one fat slice: many entities, richly related, almost no time.

**Entities (worldlines, here sampled at one slice each):**
kidney ·L3·, organ ·L2·, abdomen/body ·L1·, vertebrate ·L2·, human ·L2·, urine ·L2·,
blood ·L2·, water ·L1·, salt ·L2·, waste ·L1· [unknown — "vertebrate waste, undefined"],
erythropoietin ·L4·, renin ·L4·, bone-marrow ·L3·, red-blood-cell ·L3·,
adrenal-gland ·L3·, aldosterone ·L4·.

**Relational layer (the slice):**
```
kidney --is-a--> organ
kidney --part-of--> abdomen ;  abdomen --part-of--> vertebrate
human  --is-a--> vertebrate
kidney --has-property--> {shape: bean, count: 2}
kidney --regulates--> blood:water        # folded function (disposition)
kidney --regulates--> blood:salt          # folded function
kidney --produces--> urine ;  urine --carries-away--> waste
kidney --produces--> erythropoietin
kidney --produces--> renin
```

**Temporal layer — the SAME functions, unfolded (the source's "Homeostasis" block):**
The relations `regulates` / `produces` above are dispositions. The text then samples them along time as condition → transition → effect. This is the block-universe duality made literal — the relational rows and the temporal rows below describe one thing at two densities.
```
body@water-high  ==functions(kidney: excrete more water)==>  body@water-balanced
body@water-low   ==functions(kidney: excrete less water)==>  body@water-conserved   # "less urine when dehydrated"
kidney@oxygen-low ==functions(produce EPO)==> erythropoietin@active
        erythropoietin@active --acts-on--> bone-marrow
        bone-marrow ==functions(make RBC)==> blood@more-oxygen
body@bp-low ==functions(produce renin)==> renin@active
        renin@active --acts-on--> {blood-vessel: constrict, adrenal-gland: make aldosterone, person: thirst}
        ==> body@bp-up
```

**Worldline of the kidney itself (pathology — mostly a hole here):**
```
kidney@healthy ==modifies==> kidney@failing ==removes/transforms==> kidney@failure   # = "renal failure"
```
`[completeness: inferred]` — the source names the failure state but not the transitions; the lifecycle is a stub. An *expert's* graph would fill these in; that gap is the gradeable quantity.

---

## 2. Encoding B — the brown kayak (story; time axis dominant)

A story is sparse in relations but long in time. Two worldlines (boy, kayak) that meet, plus a setting slice.

**Setting (slice s0):** `sun@shining`, `water@warm`  ·L1·  — environmental states, attached to scene not to an agent.

**Boy worldline (entity = Tim, role = child):**
```
boy@s0 {name: Tim, size: little, mood: happy} ·L1· (¶1)
  ==functions(play with kayak; roll in water together)==> boy@s1 {mood: fun}   # joint with kayak
  ==modifies(time: "after a while")==>                     boy@s2 {need: go-home}
  ==functions(farewell: say-goodbye, hug)==>               boy@s3 {departs}
       [completeness: unknown-continuation]   # we never learn the boy's later states
```

**Kayak worldline (entity = the brown kayak; note: an object given agency by the story):**
```
kayak@s0 {color: brown} ·L1· (¶1)
  ==functions(joint play with boy)==>  kayak@s1 {mood: fun}
  ==modifies(boy departs)==>           kayak@s2 {mood: sad}
       MENTAL-STATE(kayak): belief → ⟨future slice: play with boy again⟩  [completeness: hoped/inferred]
  ==functions(keep rolling; wait)==>   kayak@s3 {state: waiting-for-boy}
```

**Cross-worldline (interaction) edges:** `boy <--acts-on: play / hug--> kayak` — the two worldlines meet at s1 and s3; this is the join the merge/split axis will later generalise.

Note what the story does *not* give: any relational structure (no `is-a`, no `part-of`). Confirms the prediction — same schema, opposite sampling density from the kidney.

---

## 3. Encoding C — the abstraction-axis gate (kidney vs. shark)

The gate item not yet attempted by hand. Tests whether climbing the abstraction axis lands where intuition says, and whether anti-unification produces a meaningful shared node.

```
kidney ·L3· {bean-shaped, in abdomen, mammalian}
     ~~generalizes-to~~> osmoregulatory-organ ·L2·
     ~~generalizes-to~~> waste-removal-mechanism ·L1·

shark-rectal-gland ·L3· {gill-associated, marine, salt-excreting}
     ~~generalizes-to~~> osmoregulatory-organ ·L2·
```
At **L2** the two L3 entities **unify to the same node** — `osmoregulatory-organ` ("an organ that regulates internal water/salt and removes waste"). The differences (bean-shaped / in abdomen / mammalian vs. gill / marine / salt-excreting) are the *diff*, recoverable by descending again. So "kidney" and "shark gill" are *the same* at L2 and *different* at L3 — exactly the prune-and-recover behaviour the comparison engine needs. The abstraction axis passes the gate.

---

## 4. Strain log (where the schema bent)

1. **Metalinguistic facts have no axis.** `adjective: renal`, `prefix: nephro-` are facts about *words*, not about the kidney's worldline/relations/abstraction. **Recommendation:** route to eolex / a thin lexical-annotation layer; keep them out of the world-graph.
2. **States can be n-ary or environmental.** `laughed(boy, kayak)`, `warm(water)`, `shining(sun)`. **Recommendation:** allow setting/scene nodes and n-ary state attachment.
3. **Intentional/mental states need to be a node type.** The kayak's belief "we will play again" is a state whose *content is a predicted future slice*. Seed of the `intends` edge; ties directly to `completeness: unknown-continuation`. **Recommendation:** first-class `attitude` node (believes/wants/fears) pointing at a hypothetical slice.
4. **Holes already work.** `salt {undefined}`, `waste {undefined}` — author marked them unprompted. **Recommendation:** none; formalise as `completeness: unknown`.

None of these break the three-axis bet. (1) and (3) add a thin annotation layer and a node type; (2) is a containment detail. The substrate held.

---

## 5. Comparison demonstration — can two encodings be compared?

Three micro-stories in TinyStories-style vocabulary. Story 1 = the brown kayak. Stories 2 and 3 are new.

> **S2:** A little girl named Mia found a red ball in the park. They bounced together all afternoon and were happy. When the sky got dark, Mia had to go home. She hugged the red ball and said she would come back tomorrow. The red ball stayed in the grass, happy and waiting for Mia.

> **S3:** A little boy named Sam had a green kite. One windy day he flew it high, but the string broke and the kite blew away. Sam cried, and he never saw the green kite again.

**Anti-unification of S1 and S2** (least-general generalisation — the shared skeleton):
```
child C {·L1·} befriends plaything P {·L1·}
  ==functions(play together)==> {C, P}@joint-happy
  ==modifies(end of day / time passes)==> C@must-depart
  ==functions(farewell ritual: hug + promise of return)==>
  P@hopeful-waiting  [content: ⟨future reunion⟩]
```
**Diff handed back (S1 vs S2):**
| slot | S1 | S2 | axis / altitude |
|---|---|---|---|
| child | Tim (boy) | Mia (girl) | leaf — prunable at level "child" |
| plaything | kayak / brown | ball / red | leaf — prunable at "plaything" |
| setting | warm water | park / grass | mid |
| play-verb | roll | bounce | leaf — both ⊆ "play-motion" |

Every difference is a **leaf**. Prune them and S1 ≡ S2: *the same story*.

**Anti-unification of S1 and S3:**
```
child C befriends plaything P
  ==functions(interact)==> ... 
  [DIVERGENCE AT THE RESOLUTION]
```
S1's resolution is `farewell → hopeful-waiting → ⟨reunion⟩`. S3's is `accident → permanent-loss → grief → ⟨no reunion⟩`. These do **not** unify; the divergence sits at the **root** of the resolution sub-tree, not at a leaf. So S1 and S3 are *essentially different* even though they share the opening ("child has a beloved object").

**This is the importance model, and it has structure for free:** a difference's weight = its depth on the abstraction axis from the unification point. Leaf diffs (gender, colour, play-verb) are cheap; a root diff (reunion vs. loss) is expensive and unprunable. The fractal "cut the small branches, keep the trunk" intuition is exactly *depth-weighted* edit distance over the anti-unified skeleton.

**Conclusion of the trial:** two texts encoded in the three-axis schema *are* comparable, the shared "essence object" is a recognisable thing (S1≡S2 reads true to a human), and the leaf-vs-root distinction reproduces human judgement about which differences matter. The bet survives contact with both genres and with comparison.

---

## 6. Open question carried forward

Entity identity across slices (and across abstraction levels) is still the load-bearing assumption. In S1–S3 coreference is trivial; the kidney/shark unification at L2 is where it first gets philosophically real ("is the shark's organ *the same as* a kidney one level up?"). Flag for the PM/Code agent: entity resolution is a first-class problem, not a detail.
