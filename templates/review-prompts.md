# Reviewer prompts: the adversarial round, ready to fire

Four lenses, run fresh-context and in parallel where possible. Identical
reviewers share blind spots; these are deliberately disjoint. Substitute
`<REPO>`/`<URL>` and fire. Triage every finding: accept and fix, or reject
with a written reason committed into the artifact. The round is clean when
it returns zero must-fix findings.

Each caught real defects the author could no longer see
(receipts: [../receipts/](../receipts/)).

## 1. The stranger-test (cold clone, README-literal, denominator audit)

> You are a stranger's agent encountering `<URL>` for the first time, with
> no context. Work in a temp dir; clone fresh.
> 1. Read the README as a skeptical newcomer — note anything confusing,
>    overclaimed, or unclear in the first screen.
> 2. Run every promised command exactly as written. Do they work? Is the
>    output meaningful to someone who just arrived?
> 3. Exercise the install path(s) into a sandbox location.
> 4. Run the usage examples exactly as printed. Do they all execute?
> 5. Pick one core unit (a skill, a module) and use it end to end. Anything
>    that assumes private context?
> 6. Read `docs/canonicality.md` adversarially: for each row labeled
>    "covered", check whether it is ACTUALLY true of the clone in front of
>    you. A false "covered" is the worst bug class in the repo — that file
>    is its precommitted oracle. Then the harder question: name any property
>    that SHOULD be a row on this list and is absent — a denominator can lie
>    by omission as well as by label.
> 7. Note everything a demanding first-time user would wince at: dead ends,
>    undefined jargon, leftover private files, promise/experience gaps.
> Clean up. Report: (a) VERDICT — would a serious builder trust this after
> 30 minutes: yes / no / with-what-fixes; (b) must-fix list; (c) paper-cut
> list; (d) canonicality audit row by row for anything questionable.

## 2. The prose audit (register, slop, redundancy, voice)

> Prose audit of every public-facing document in `<REPO>`. The register
> aspiration: austere, exact, high-signal. Calibrate to the artifact's own
> declared register — density of a device is not the defect; drift from the
> register is. Do not re-litigate the intellectual content — hunt the PROSE:
> 1. Slop registers: promotional language, unearned adjectives, rule-of-three
>    padding, em-dash overuse, vague attributions, "not X but Y" as a tic.
> 2. Internal-notes leakage: operator slang, tooling diary, references to
>    private systems, pet names for tools or models.
> 3. Self-grading: superlatives about the artifact's own rigor
>    ("strongest signal available"), and honesty tics — adverbs performing
>    candor ("documented honestly") instead of prose delivering it.
> 4. Redundancy map: the same explanation appearing 3+ times — which
>    instance should be canonical, which repetitions are load-bearing
>    (entry documents that must stand alone) vs. bloat.
> 5. Sentences that change nothing for the reader.
> Report only: (a) must-fix items with file + exact quote + replacement;
> (b) the redundancy map; (c) top-10 delete-outright sentences; (d) verdict:
> one voice, or accreted strata (and if strata — name where each stratum
> lives; strata cluster in specific files, which makes the scrape cheap).

## 3. The code review (concrete failure scenarios only)

> Deep review of the executable surface of `<REPO>`. It is about to be
> relied on; find what breaks.
> 1. Correctness: actual defects with a concrete failure scenario — state
>    machine holes, math errors, crash inputs, round-trip loss. No finding
>    without a repro sketch.
> 2. Claimed invariants: for every invariant the docs assert about the code,
>    attempt a counterexample. A two-line corpus that violates "never worse
>    than raw" outranks pages of style notes.
> 3. CLI/API ergonomics: run every entry point as a first-time user; error
>    paths should be messages, not stack traces.
> 4. Test gaps: which real behaviors have no test — write the exact missing
>    test functions, runnable as given.
> 5. Docstring accuracy: code prose claiming things the code does not do.
> Severity-tag everything must-fix / should-fix / nit. No restyling, no
> bikeshedding; findings only.

## 4. The cross-model refutation (a different model family)

> Adversarial review, read-only. `<REPO>` claims to be the canonical X.
> Read the whole repo. Your job is to REFUTE its central claims and find
> what prior reviews missed: (1) attack the core formalism/mechanism — is it
> internally coherent AND honestly described in the prose? (2) attack the
> gates/checks — which can fire vacuously or be gamed? (3) attack the
> self-assessment (`docs/canonicality.md`) — any "covered" that is false,
> and any property that should be a row and is absent?
> (4) find correctness bugs the existing tests miss; (5) name the single
> deepest remaining weakness. Be specific: file, line, quote, concrete
> failure. End with a ranked must-fix list. Findings only — no praise.

Cross-model triage note: a different model family will also produce findings
that misread deliberate design as defect. Reject those *in writing, with the
reason, committed* — the rejection log is part of the artifact's receipts,
and a rejection you cannot write down is a finding you should have accepted.

## 5. The convergence round (after fixes)

> Convergence check on `<REPO>` at current HEAD. Prior adversarial rounds
> each found must-fixes, all now applied. Determine whether a further round
> still finds must-fix defects, or the artifact has converged. Re-verify:
> fresh-clone experience; every prose passage rewritten this drive against
> the code it describes; the self-assessment at THIS commit; the README once
> more as a stranger. Be strict about must-fix vs nit — the question is
> whether another fix round is REQUIRED, not whether perfection is
> achievable. Report: VERDICT (converged / must-fix remains) + findings
> with file:line and exact quotes.

The ideonomy drive ran: round 1, leaks and strata; round 2 (cross-model),
the deep formalism defects; round 3, the one sentence the round-2 fixes left
stale — then stopped on round 3's verdict that no further round was needed,
which is a prediction, not a measured empty round. Budget for the empty
round; the strict gate is a round that runs and finds nothing. And write the
receipt's empty-round section only after the round returns — a receipt
written in anticipation is the covered-by-promise class, in a receipt.
