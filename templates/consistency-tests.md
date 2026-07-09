# Consistency-test patterns: make staleness classes unrepresentable

The point is never the found instance; it is the class. A fixed
inconsistency recurs the next time anyone edits either side; an enforced one
dies. These patterns cover the classes that actually occur, in rough order
of yield. Implement them in the target's own runtime (a stdlib test file is
usually enough — see `check.py` in this repo for a minimal live example);
they must run offline and fast, or they will be skipped and then lie.

## 1. Counts derive from source

Any number the prose asserts about the artifact itself (N primitives, N
skills, N modules) is either computed in a test against the machine-readable
source, or removed from the prose. Grep-based: assert the doc contains
`f"{len(SOURCE)} things"`. The complementary rule: numbers outside the
enforced set are *avoided*, not asserted — "the offline test suite" ages
better than "18 tests".

Also enforce the negative: prose *inside code files* (docstrings, demo
output) must not hardcode catalog counts — the demo that prints "35" while
shipping 37 is this class.

## 2. Parallel forms of one catalog are one catalog

When an idea exists as both doc and data (a catalog in markdown ↔ a list in
code), test both directions: every key in the data appears in the doc with
its exact name; every key pattern in the doc exists in the data. Same for
routing tables (a dispatcher doc may only reference entries that exist).

## 3. Links resolve

Walk every tracked markdown file; every relative link target exists (strip
anchors). External links are a manual sweep at release — say so in the
denominator rather than pretending the test covers them.

## 4. Multi-file versions agree

Version asserted in more than one place (package manifest, plugin manifest,
marketplace entry) → one test asserting equality. Same for any other
duplicated scalar (minimum runtime version, license name).

## 5. Machine-readable contracts satisfy their spec

Frontmatter, manifests, schemas: name matches directory, required fields
present, length limits respected. Cheap to write, catches whole classes of
silent uninstallability.

## 6. The invariant the artifact's own logic claims

If the artifact states an invariant about itself ("a compression is never
worse than raw", "the classifier can't be satisfied without engaging prior
state"), encode the adversarial counter-case a reviewer found as a
permanent regression test. Reviewer findings make the best test fixtures:
each one is a proven blind spot.

## Meta

- Write the enforcement test in the same commit as the fix — the commit
  message then documents the class, not just the instance.
- The gate for the pass: the suite would have caught every consistency
  defect the full read found. If a class is unenforceable, that fact is a
  denominator row, not a silence.
