# Disagreement Reasoning — Response to Review

## Acknowledging the Finding

The review correctly identified that weak responses met nearly every element when the figures were right. This means the task currently rewards figure computation over document discovery. A model that computes the right numbers can pass without ever consulting Standing Order 15-3, Tariff Resolution 2019-14, or any other governing document.

## The Core Problem

The prompt states the rules explicitly:

- When a skip counts as documented: the prompt quotes Standing Order 15-3 s.3.2-3.3 directly
- The three priority levels: the prompt defines Priority 1, Priority 2, and Priority 3 with specific criteria
- The account join: the prompt gives "AC-LP-0122 → LP-0122" as an explicit example
- Billable length: the prompt states "using check-in LOA from the certificates"
- Rate source: the prompt names Resolution 2022-06

A model that follows these instructions reaches correct answers through pure instruction-following. The prompt serves as a substitute for the source documents. Weak models that compute the right figures pass the task, regardless of whether they ever opened a governing document.

This undermines the task's purpose. The CHD task is designed to test whether a model can discover and apply rules from source documents. When the prompt gives every rule away, the test no longer measures discovery — it measures arithmetic and instruction-following.

## Proposed Hardening

Remove every explicit rule from the prompt and force discovery from the governing documents:

| Rule | Current (explicit) | Hardened (discovery) |
|------|-------------------|---------------------|
| Skip documentation | Prompt quotes SO 15-3 s.3.2-3.3 verbatim | Model finds it in Standing Order 15-3 s.3.2-3.3 |
| Priority levels | Prompt defines P1/P2/P3 criteria | Model discovers from the documents |
| Account join | "AC-LP-0122 → LP-0122" given | Model discovers from the data |
| Billable length | "using check-in LOA from certificates" | Model finds the rule in Tariff Resolution 2019-14 |
| Rate source | "apply rates from Resolution 2022-06" | Model determines which rates apply to which periods from governing documents |

## Why the Files Support This

Every rule the model needs exists in the source documents:

- Standing Order 15-3 s.3.2-3.3 contains the documentation rule — find it there
- Tariff Resolution 2019-14 contains the billable length formula — find it there
- Resolution 2022-06 contains the post-adoption rates — find them there
- The data files contain all figures and the account identifiers that reveal the join pattern — discover from the data

Nothing is missing. The environment fully supports the hardening.

## Why Weak Models Will Now Fail

Previously, weak models could pass by following the prompt's explicit instructions without discovering anything. With the hardening:

1. **No instruction pathway exists**: The prompt no longer states any rule. Every rule must be found from documents or data.
2. **Verification requires document access**: A model that skips Standing Order 15-3 will not know the documentation rule. A model that skips Tariff Resolution 2019-14 will not know the billable length formula.
3. **Figure correctness alone is insufficient**: Even if a model computes the right numbers, it must also demonstrate that it found the governing rules. A model that gets numbers right but never opens a governing document fails the discovery requirement.

This widens the gap between strong and weak model performance because strong models already discover rules from documents, while weak models relied on prompt instructions.

## What Does Not Change

- Task scope: same audit period, same deliverables (workbook + memo)
- File list: same source documents, same environment
- Deliverable format: same structure
- Date context: same audit date (August 1, 2026), same cutoff
- Evaluation criteria: same rubric — figures that are wrong are still wrong
- Expected values: correct figures remain correct after hardening

## Conclusion

The hardening is necessary and well-supported. The task should test document discovery, not instruction-following. V15 removes the shortcut that allowed weak models to pass without opening a single governing document, while keeping the environment fully solvable from the source materials.
