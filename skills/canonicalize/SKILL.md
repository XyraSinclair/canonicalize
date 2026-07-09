---
name: canonicalize
description: >-
  Drive a repo, document, or tool toward book-shape: the canonical form a
  demanding user would not want to change after a hundred hours of use. A
  disciplined sequence of passes — read everything; precommit an explicit
  denominator of what "canonical" means; machine-enforce truth so staleness
  classes die; rebuild the stranger's entry path; scrape the prose to one
  voice; run fresh-eyes adversarial rounds until a round finds nothing;
  publish with committed receipts. The failure it prevents: polish theater —
  effort spent smoothing an artifact whose counts are stale, whose claims
  are unverified, whose gaps are hidden, and whose "done" was declared by
  fatigue. Triggers on "canonicalize this", "make this canonical /
  book-shaped / definitive", "square this away for publication", "get this
  repo ready to publish", and any pre-release quality drive.
---

# canonicalize

Book-shape is a conjunction of seven checkable properties (stated fully in
BOOK.md at the source repo; summarized here so this file executes alone):
the artifact **states its own denominator**; its **truth is enforced by
tests, not care**; it **works for a stranger in a minute and rewards the
hundredth hour**; it speaks in **one voice with every sentence
load-bearing**; it **survives motivated refutation from diverse lenses**;
its **gaps are named, residue committed, rejections reasoned**; and it
**applies to itself**. Underneath all seven: an artifact is understood to
the degree it is compressed — regenerable from invariants, not merely
enumerated. Canonicalization cuts to the actual shape; it never averages
the shape away.

## Procedure

1. **Read everything.** Every file, end to end; partial reads cannot see the
   defect classes that matter (stale counts, private-context leaks, register
   strata). Collect defects; fix nothing yet.

2. **Precommit the denominator.** Write `docs/canonicality.md` into the
   target: the explicit property list that "canonical" means for THIS
   artifact, grouped (truth / first-contact / depth / craft / stewardship),
   every row labeled covered / named-gap / ruled-out. Write it in target
   state and treat it as the oracle the rest of the drive is scored against.

3. **Enforce truth.** Fix each inconsistency, then make its class
   unrepresentable: counts derive from source; parallel forms of one catalog
   get a sync test; links get a resolution test; multi-file versions get an
   equality test. Offline, fast, no new dependencies. The suite must have
   caught everything step 1 found.

4. **Rebuild the stranger's path.** Cold-clone in a temp dir and follow the
   README literally — run it, don't simulate it. First screen says
   what/for-whom/why; one command produces a real result; install paths
   exercised; every private name removed or defined; notation legend-ed;
   orphans linked or deleted.

5. **Scrape to one voice.** Remove the internal-notes stratum, self-grading
   superlatives, honesty tics, and every sentence that changes nothing.
   Named specifics over vague impressives. One canonical statement per idea.
   The scrape removes the false and unearned — never the sharp.

6. **Adversarial rounds until dry.** Fan out fresh-context reviewers with
   distinct lenses: stranger-test (clone + README-literal + denominator
   audit row by row), prose audit, code review (concrete failure scenarios
   only), and a cross-model refutation pass. Triage every finding: accept
   and fix, or reject with a written reason — never silently drop. Repeat
   until a full round yields zero must-fix findings.

7. **Publish with receipts.** Packaging complete; tag + release notes that
   name what was reviewed AND what remains open; description/topics match
   reality; the denominator verified true at the tagged commit; surviving
   residue committed into the artifact. If it ships skills or tools, install
   them into your own environment as the final self-application.

## The gate

The drive is complete only when ALL of:

- the latest full adversarial round produced **zero must-fix findings**
  (convergence is a measurement — a reviewer round finding nothing — never
  the author's sense of enough);
- `canonicality.md` is **true at HEAD**: every "covered" row verifiable,
  every gap named, no row unlabeled, no row deleted to hide;
- review residue and rejected-findings-with-reasons are **committed into
  the artifact**, not left in the session;
- a **final cold-clone smoke test** passes at the tagged commit.

A drive that stops before this gate reports itself as partial, with the
remaining passes named — "mostly canonicalized" is not a state.

## Example

A skills repo looks finished: coherent docs, passing tests, two prior
reviews. The drive still finds: the flagship doc claims 35 primitives while
the code ships 37 (the demo prints both, disagreeing with itself); links
point to sibling repos that were never published; a top skill references the
author's private project by name twice; the review section is written in
operator slang ("the real Oracle, browser-background"); and the repo's own
self-assessment marks a release "covered" that was never tagged. Four
rounds: round 1 (stranger + prose) finds leaks and strata; round 2
(cross-model) refutes an engine invariant with a concrete two-item corpus
and forces a real fix; round 3 finds one leftover sentence contradicting the
fix; round 4 finds nothing — converged. Every class got a test; the gaps
that remain (no external-corpus receipts yet) are named in the release notes
rather than papered over. That is the difference between polished and
canonical: the second one stops moving.
