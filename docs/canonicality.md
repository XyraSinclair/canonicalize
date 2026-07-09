# Canonicality: the coverage denominator for this repo

The method applied to itself (BOOK.md property 7). Labels: **covered** /
**named-gap** / **ruled-out**. The repo may not call itself finished while
any row is unlabeled.

Target property: *an operator or agent who has never seen this repo can run
a full canonicalization drive on their own artifact using only what is here,
and after a hundred hours of drives would not want to change the method —
only to add receipts.*

## A. Truth and internal consistency

| # | Property | Label |
|---|----------|-------|
| A1 | Structural counts (seven properties, passes 0–6) match the documents' own headings, test-enforced; other counts avoided | covered — `check.py` |
| A2 | The skill is a faithful compression of BOOK+DRIVE (no contradiction between the standalone summary and the full doctrine) | covered — verified in the self-drive review round |
| A3 | Every intra-repo link resolves, test-enforced; external links verified manually | covered — `check.py`; external links last verified 2026-07-09 |
| A4 | The receipt states only what actually happened in the ideonomy drive, checkable against that repo's public history | covered — commits/tags/ledger at XyraSinclair/ideonomy |
| A5 | No stale claims | covered — last swept 2026-07-09 (three review rounds); `check.py` guards the structural class |

## B. First contact

| # | Property | Label |
|---|----------|-------|
| B1 | One command after cold clone produces a real result | covered — `python3 check.py` |
| B2 | First screen states what/for-whom/why | covered |
| B3 | Checks run offline, one command, stdlib only | covered |
| B4 | The skill is installable, not just readable | covered — plugin manifest validated + `install.sh` exercised |
| B5 | Zero private context; the skill executes standalone (no repo-relative dependencies), test-enforced | covered — `check.py` |

## C. Depth

| # | Property | Label |
|---|----------|-------|
| C1 | The passes are load-bearing: each exists because skipping it cost something in a real drive | covered — receipts trace each pass to its yield |
| C2 | The method applied to itself; this file is the receipt, audited adversarially | covered |
| C3 | The drive's own failure modes documented as prominently as its passes | covered — DRIVE.md final section |
| C4 | Corpus breadth: receipts from multiple drives, on others' artifacts, by other operators | named-gap — one full receipt (ideonomy); the template set grows only from receipts |
| C5 | The hundred-hour claim about the *method itself* is empirical and unproven at one receipt | named-gap — honesty about the recursion: this repo's own C-row discipline applies |
| C6 | The self-drive's lens set matches what Pass 5 prescribes (four lenses, cross-model diversity) | named-gap — essence + stranger + convergence rounds ran, all one model family; no cross-model pass on this repo yet |

## D. Craft

| # | Property | Label |
|---|----------|-------|
| D1 | Zero dependencies; stdlib check only | covered |
| D2 | Every file has a stated reason; no orphans | covered — every file is referenced from the README; `check.py` catches orphaned links |
| D3 | Packaging complete; install paths exercised | covered — `claude plugin validate` + `install.sh` run |
| D4 | Skill frontmatter satisfies the spec, test-enforced | covered — `check.py` |
| D5 | One austere voice; no unearned adjectives | covered — scraped at birth; audited in the self-drive round |

## E. Stewardship

| # | Property | Label |
|---|----------|-------|
| E1 | License present | covered — MIT |
| E2 | Revision discipline stated: templates and doctrine change only from receipts — a prompt or pattern is added/edited when a drive proves it caught or missed something real | covered — README Status |
| E3 | Release tagged; public metadata accurate | covered when `v0.1.0` exists (created at publish, pointing at this revision) — on any commit where the tag does not yet exist, read this row as a named-gap; verify with `git tag` |
| E4 | Community scaffolding | ruled-out for now — single-operator method; revisit on the first external receipt |

## Summary

The method, doctrine, and tooling are covered; the named gaps are all
evidence-shaped (C4, C5, C6) — one deep receipt rather than a corpus, the
hundred-hour claim about the method itself unproven at n=1, and a self-drive
lens set narrower than the four lenses Pass 5 prescribes. The prose asserts
the method's yield on the receipt it has and nowhere claims the generality
only more receipts could prove.
