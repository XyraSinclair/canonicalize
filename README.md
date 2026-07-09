# canonicalize

Drive an artifact toward **book-shape** — Erdős's Book, applied to repos: the
form a demanding user would not want to change after a hundred hours of use,
not because it is finished, but because everything present is right and
everything absent is named.

Most pre-release effort is polish theater: reordering sentences while the
counts are stale, the claims unverified, the gaps hidden, and "done" declared
by fatigue. This repo is the counter-method — canonicalization as a
disciplined drive with gates:

1. read everything;
2. precommit an explicit **denominator** of what "canonical" means for this
   artifact (covered / named-gap / ruled-out — the oracle the drive is
   scored against);
3. **enforce truth** so staleness classes die by test, not by care;
4. rebuild the **stranger's path** (cold clone → real result in a minute,
   zero private context);
5. **scrape** to one voice, every sentence load-bearing;
6. **adversarial rounds** with disjoint lenses until a round finds nothing —
   convergence is a measurement, not a mood;
7. publish with **receipts**: gaps named, residue committed, rejections
   reasoned.

## What's here

- **[BOOK.md](BOOK.md)** — the target state: the seven checkable properties
  of book-shape, and the minimum-description-length soul underneath them
  (cut to the actual shape; never average it away).
- **[DRIVE.md](DRIVE.md)** — the procedure: passes 0–6, each with its gate,
  and the failure modes of the drive itself.
- **[skills/canonicalize/](skills/canonicalize/SKILL.md)** — the executable
  form: a self-contained agent skill that runs the whole drive against a
  target repo.
- **[templates/](templates/)** — the working parts: the
  [denominator template](templates/canonicality.md), the
  [consistency-test patterns](templates/consistency-tests.md), and the
  [reviewer prompts](templates/review-prompts.md) for every lens plus the
  convergence round — fire as written.
- **[receipts/](receipts/)** — the method's evidence: a full drive on a
  real repo that had already survived two frontier-model reviews, in which
  three adversarial rounds plus a convergence verdict still surfaced 34
  accepted defects (the session's triage tally) — including a false row in
  the target's own self-assessment. Plus this repo's own self-drive receipt.

## Sixty seconds

```bash
git clone https://github.com/XyraSinclair/canonicalize && cd canonicalize
python3 check.py        # the repo's own consistency, enforced (property 2, live)
```

Then read [BOOK.md](BOOK.md) and skim a
[receipt](receipts/ideonomy-2026-07-09.md) to see the yield shape.

## Install the skill

Claude Code, one command:

```
/plugin marketplace add XyraSinclair/canonicalize
```

Any other agent that reads `SKILL.md` files:

```bash
./install.sh            # copies the skill into ~/.claude/skills/
```

Then: "canonicalize this repo" / "make this book-shaped" / "square this away
for publication."

## Relation to ideonomy

This repo is the applied art; [ideonomy](https://github.com/XyraSinclair/ideonomy)
is the general theory of the moves it composes. The drive is, in ideonomy's
vocabulary: `prove-the-coverage-denominator` aimed at the artifact itself
(the canonicality file), `build-the-oracle-before-the-answer` (the
denominator precommitted in target state), `refute-your-own-answer-blind`
(the adversarial rounds), `preserve-the-target` (the scrape removes the
false, never the sharp), and `carry-the-residue-forward` (receipts and
rejection logs committed, not remembered). You do not need ideonomy to use
this; you will recognize it if you have it.

## Status

The doctrine, drive, templates, and skill are complete and self-applied —
this repo's own denominator is [docs/canonicality.md](docs/canonicality.md),
audited across its own adversarial rounds. The method has one full receipt;
the named gaps are evidence-shaped: corpus breadth (C4 — receipts from more
drives, on other people's artifacts, by other operators), the hundred-hour
claim about the method itself (C5 — unproven at n=1), and lens diversity
(C6 — this repo's own self-drive has had no cross-model pass yet). The
template set grows only from receipts — every prompt and pattern here earned
its place by catching something real.

MIT licensed.
