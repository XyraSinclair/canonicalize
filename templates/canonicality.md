# Canonicality: the coverage denominator for <ARTIFACT>

<!-- Template. Copy into the target as docs/canonicality.md, adapt rows to
     the artifact, and write it in TARGET STATE before the drive: it is the
     precommitted oracle the drive is scored against. Labels: covered
     (holds, verified) / named-gap (does not hold; the gap is the work) /
     ruled-out (deliberately out of scope, with the reason). Rows may be
     relabeled with reasons, never deleted to hide. -->

"Canonical" is not a feeling; it is this labeled list. The artifact may not
call itself finished while any row is unlabeled.

Target property (name the single property the whole artifact must preserve —
e.g. *a stranger's agent and a demanding human can pick this up cold, get
first value in under a minute, keep finding value after 100 hours, and find
nothing they would need to change before trusting it*).

## A. Truth and internal consistency

| # | Property | Label |
|---|----------|-------|
| A1 | Load-bearing prose counts match the machine-readable source, test-enforced; counts outside the enforced set are avoided rather than asserted | |
| A2 | Parallel forms of one catalog (doc ↔ data structure) are sync-enforced | |
| A3 | Every intra-artifact link resolves (test-enforced); external links verified at release | |
| A4 | No stale claims — docs describing an earlier state | |
| A5 | Claims about external systems carry provenance | |

## B. First contact

| # | Property | Label |
|---|----------|-------|
| B1 | One command after cold clone produces a real, meaningful result | |
| B2 | First screen states what this is, for whom, why care | |
| B3 | Checks run offline, one command, no extra dependencies | |
| B4 | The artifact is installable/usable, not just readable | |
| B5 | Zero private context: no undefined internal names; notation carries its legend | |

## C. Depth (the 100-hour property)

| # | Property | Label |
|---|----------|-------|
| C1 | Core abstractions are load-bearing, not decorative | |
| C2 | The artifact applies to itself; the receipts are committed in-artifact | |
| C3 | Weaknesses documented as prominently as strengths | |
| C4+ | (the artifact's own empirical/depth claims, each as its own row) | |

## D. Craft

| # | Property | Label |
|---|----------|-------|
| D1 | Minimal dependency surface for what it does | |
| D2 | Every file has a stated reason to exist; no orphans, no dead code | |
| D3 | Packaging metadata complete; install paths exercised, not described | |
| D4 | Machine-readable contracts (frontmatter, manifests) satisfy their spec, test-enforced | |
| D5 | One austere voice; no slop registers, no unearned adjectives | |

## E. Stewardship

| # | Property | Label |
|---|----------|-------|
| E1 | License present and unambiguous | |
| E2 | The revision discipline is stated: how the artifact changes, what counts as evidence | |
| E3 | Release tagged; public metadata accurate | |
| E4 | Community scaffolding | (often ruled-out early: premature apparatus — state the revisit trigger) |

## Summary

State plainly what is covered and what the named gaps are. The prose of the
artifact must never assert what only the gaps could prove.
