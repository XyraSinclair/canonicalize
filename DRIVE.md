# The drive: how to move an artifact toward book-shape

Canonicalization is a sequence of passes over a target artifact (usually a
repo), each with an explicit gate. The passes are ordered because each one
changes what the next can see: you cannot scrape a voice you have not fully
read, and you cannot measure convergence before enforcement has killed the
mechanical defect classes. Run them in order; commit and push at every pass
boundary — canonicalization that evaporates with the session is churn.

The seven target properties are defined in [BOOK.md](BOOK.md). This file is
the procedure. The agent-executable form is
[skills/canonicalize/SKILL.md](skills/canonicalize/SKILL.md); battle-tested
reviewer prompts are in [templates/review-prompts.md](templates/review-prompts.md).

## Pass 0 — Read everything

Every file, end to end. Not a sampling, not a skim: the defect classes that
matter most (stale counts, private-context leaks, strata of register) are
invisible to partial reads because each instance looks fine locally. Build
the defect list as you go, but fix nothing yet — fixes before the
denominator exists aim at symptoms.

**Gate:** you can state, from memory, what every file is for. Any file you
cannot justify goes on the defect list as a removal candidate.

## Pass 1 — Write the denominator

Create the artifact's `canonicality.md` from
[templates/canonicality.md](templates/canonicality.md): the explicit list of
properties that "canonical" means *for this artifact*, grouped (truth,
first-contact, depth, craft, stewardship), each labeled covered / named-gap /
ruled-out. Write it in **target state** — rows you intend to make true — and
treat it as a precommitted oracle: at publish, every "covered" must be true
at HEAD, and the reviewers will check.

**Gate:** the file exists, is committed into the target, and no row is
unlabeled. Rows you cannot label are themselves named gaps.

## Pass 2 — Enforce truth

Kill the found inconsistencies, then make their *classes* unrepresentable:

- counts in prose derive from the machine-readable source, or are avoided;
- parallel forms of one catalog get a sync test;
- intra-artifact links get a resolution test;
- versions asserted in more than one file get an equality test.

The test suite must run offline, fast, with no dependencies beyond the
artifact's own runtime. See
[templates/consistency-tests.md](templates/consistency-tests.md) for the
patterns; `check.py` in this repo is a minimal live example.

**Gate:** the suite exists, passes, and would have caught every consistency
defect found in Pass 0. If a defect's class is unenforceable, that fact goes
in the denominator.

## Pass 3 — Stranger surfaces

Rebuild the entry path as if you had never seen the artifact:

- first screen of the README says what it is, for whom, why care;
- one command after cold clone produces a real result;
- install paths actually work, and are exercised, not described;
- every private reference is removed or defined — project pet names,
  internal tool names, unexplained notation (add legends);
- orphan files are linked or deleted; leftover state is ignored or removed.

**Gate:** a fresh clone in a temp dir, following the README literally,
succeeds at every promised step. Run it; do not simulate it.

## Pass 4 — The scrape

One voice. Remove the internal-notes stratum (operator slang, tooling
diary, references to "the mission"), the self-grading superlatives
("strongest signal available"), the honesty tics (adverbs performing candor
instead of prose delivering it), and every sentence that does not earn its
place. Prefer the named specific to the vague impressive: "a three-persona
panel (Feynman, von Neumann, Grothendieck)" over "a diverse genius-style
panel." Deduplicate across files: one canonical statement per idea, pointers
elsewhere — except where each entry document must stand alone, and then vary
the phrasing deliberately.

**Gate:** an independent prose audit (see review-prompts) reports the corpus
reads as one voice, and its must-fix list is empty or applied.

## Pass 5 — Adversarial rounds until dry

Fan out fresh-eyes reviewers, each with a distinct lens and no context from
your session: the cold **stranger-test** (clone, follow README literally,
audit the denominator row by row), the **prose audit** (Pass 4's gate), the
**code review** (concrete failure scenarios only), and a **cross-model
pass** (a different model family, prompted to refute the central claims —
diversity catches what redundancy cannot). Triage adversarially: findings
are accepted, or *rejected with a written reason* — never silently dropped.
Fix, commit, and run another round. Loop until a round produces **zero
must-fix findings**. Two or three rounds is typical; declaring convergence
after one is the tell that you graded your own homework.

**Gate:** the latest round found nothing that must change. Residue from all
rounds — surviving objections, deferred items, rejected-with-reason calls —
is committed into the artifact, not left in the conversation.

## Pass 6 — Publish with receipts

Squared away is public: complete packaging metadata; a tagged release whose
notes state what was reviewed and what remains open; repository description
and topics that match the artifact as it now is; and the denominator
verified one final time at the tagged commit — every "covered" true, every
gap named. If the artifact carries skills or tools, install them into your
own environment as the last self-application: the installer working for you
is the first receipt that it works at all.

**Gate:** tag exists, release notes name the gaps, `canonicality.md` is true
at the tagged commit, and a final fresh-clone smoke test passes.

## Failure modes of the drive itself

- **Polish theater** — reordering sentences while the counts are stale.
  Enforcement (Pass 2) before beauty (Pass 4), always.
- **Averaging the shape away** — smoothing distinctive structure into
  generic professionalism. The scrape removes what is *false or unearned*,
  never what is sharp.
- **Convergence by fatigue** — stopping because you are tired, labeled as
  stopping because it is done. The gate is a reviewer round finding nothing,
  not your sense of enough.
- **Receipts in the conversation** — the session knows what was reviewed and
  rejected, but the artifact does not. If it is not committed, it did not
  happen.
- **Denominator drift** — quietly editing the property list mid-drive so the
  artifact passes. Rows may be relabeled with reasons, never deleted to
  hide.
