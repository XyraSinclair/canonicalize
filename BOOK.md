# Book-shape: what canonical means

Erdős said God keeps a book of the perfect proofs — not the first proof
found, not the most exhaustive, but the one where every line is forced, and
after reading it you cannot imagine the theorem any other way. "Straight from
The Book" is the highest compliment a proof can earn.

Artifacts have book-shape too. A repo, a document, a tool, a spec is
**book-shaped** when a demanding user, after a hundred hours of real use,
would not want to change it — not because it is finished, but because
everything present is right and everything absent is named. That is the
target state this repo exists to drive artifacts toward. Not polish. Not
completeness. *Form so right it stops moving.*

Book-shape is a conjunction of seven properties. Each is checkable; none is
a feeling.

## 1. It states its own denominator

Canonical is not an adjective; it is a labeled list. The artifact carries an
explicit inventory of the properties it claims — each marked **covered**
(holds, verified), **named-gap** (does not hold; the gap is the work), or
**ruled-out** (deliberately out of scope, with the reason) — and refuses the
word "done" while any row is unlabeled. The list is written *before* the
work, as a precommitted oracle: the properties are the expected values, the
drive is the run, and a row you wrote optimistically that turns out false is
the most valuable find of the whole exercise.

## 2. Its truth is enforced, not attended to

Every claim that can be machine-checked is. Counts derive from the source
instead of being asserted in prose; parallel forms of one catalog (the doc
and the data structure) are one catalog, sync-enforced; links resolve or the
build fails. The point is not the instance but the class: a fixed
inconsistency recurs, an enforced one dies. Care does not scale. Tests do.

## 3. It works for a stranger in a minute and rewards the hundredth hour

Cold-clone executable: one command after arrival produces a real result.
Zero private context — no pet names, no unexplained internal vocabulary, no
references a stranger cannot chase; every notation carries its legend. And
the other end of the axis: the deep structure is load-bearing enough that
use deepens it rather than exhausting it. A README that oversells dies in an
hour; a structure that only its author can navigate dies in a week.

## 4. One voice, every sentence load-bearing

Artifacts accrete strata — the public prose, then the operator's log
register, then the notes-to-self — and the strata never scrape themselves.
Book-shape is one austere voice throughout. No unearned adjectives: the
claim to depth is carried by demonstrated structure, never by "powerful" or
"striking" or "deeply." A sentence that does not change what the reader
knows or does is deleted, and deletion is the edit that most often improves
an artifact.

## 5. It survives motivated refutation from diverse lenses

Book-shape is adversarially earned. Reviewers who *want* to find defects —
each holding a different lens, because identical reviewers share blind
spots: the stranger who cold-clones and follows the README literally; the
prose auditor hunting register breaks and slop; the code reviewer with
concrete failure scenarios; a different model entirely, refuting the central
claims. The loop runs until a round finds nothing that must change.
**Convergence is a measurement, not a mood.**

## 6. Its gaps are named, its residue committed, its rejections reasoned

The honest form of incompleteness: what is not proven is labeled, never
implied. What resisted resolution is carried forward visibly — in the
artifact, not in the author's memory. And review findings that were
*rejected* are recorded with their reasons, because a rejection you cannot
defend in writing is a finding you should have accepted.

## 7. It applies to itself

The method that made the artifact is visible in the artifact, and the
artifact is its own first receipt. A style guide written in violation of its
own style, a test framework without tests, a canonicalization method that
was never used to canonicalize itself — each fails the cheapest check it
proposes. Self-application is not a flourish; it is the honest first proof,
because if the method cannot close its own case it will not close anyone
else's.

## The soul of it: minimum description length

Underneath the seven properties is one principle. An artifact is understood
to the degree it is *compressed*: regenerable from a small set of invariants
rather than merely enumerated. Book-shape is the drive's fixed point — the
form where nothing can be removed without losing coverage and nothing needs
adding to explain what exists. Canonicalization is not smoothing; most
editing that calls itself polish is averaging, and averaging destroys shape.
The work is the opposite: find the actual shape, and cut everything that is
not it.

Which is why the hundred-hour test is the right test. Novelty survives an
hour. Thoroughness survives ten. Only *rightness of form* survives a
hundred, because by then the user has pushed on every wall, and every wall
that was decoration has fallen.

One scope line, said once: these properties certify form, not worth. The
hundred-hour test presumes an artifact someone should use for a hundred
hours; whether it deserves the drive is a prior judgment the method does
not make for you.
