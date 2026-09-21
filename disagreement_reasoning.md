# Disagreement Reasoning

## The Finding

Reviewers observed that weak model responses met nearly every evaluation element in the CHD task when the numerical figures were correct. A weak model that happened to compute the right numbers could pass the task without understanding the governing documents.

## The Root Cause

The prompt explicitly stated the rules that the source documents contain. Rather than discovering rules from Standing Order 15-3, Tariff Resolution 2019-14, and Resolution 2022-06, models could follow the prompt's instructions and arrive at correct answers without ever opening those documents.

Specifically, the prompt spelled out:

1. **When a skip counts as documented**: "check whether contemporaneous proof exists per Standing Order 15-3 s.3.2-3.3 — a cover sheet alone doesn't count. Use review_date in skip_events as the assembly date; a skip has contemporaneous proof only if review_date is on or before the skip_date AND a corresponding justification PDF exists." — This is the verbatim rule from Standing Order 15-3 s.3.2-3.3. No need to open the document.

2. **Three priority levels**: "Priority 1 — skips with no supporting record... Priority 2 — skips where supporting records exist but review_date is after skip_date... Priority 3 — subledger arithmetic errors only." — These are the exact classifications from the documents. No need to discover them.

3. **Account join**: "join to slip_inventory via the slip ID embedded in the account number (e.g., AC-LP-0122 → LP-0122)." — The join logic is given explicitly. No need to discover the pattern from data.

4. **Billable length**: "determine covered vs open from slip_inventory_2026-08.csv using check-in LOA from the certificates." — The formula is stated. No need to find it in Tariff Resolution 2019-14.

5. **Rate source**: "apply rates from Resolution 2022-06." — The source is named. No need to find the rates document.

A model that reads these instructions and follows them reaches the correct answers through pure instruction-following, with zero document discovery. The numbers in the environment are correct, and the prompt tells the model exactly how to use them. Weak models that compute the right figures pass the task regardless of whether they understand any governing document.

## Why This Fails the Task

The CHD task is designed to test whether a model can discover and apply rules from source documents. When the prompt gives every rule explicitly, the task becomes a test of arithmetic and instruction-following instead of a test of document understanding.

This creates a paradox: models that compute figures correctly appear to understand the task, but they may have never opened Standing Order 15-3, Tariff Resolution 2019-14, or any source document. The evaluation confirms figures are correct but does not verify that the model discovered the governing rules.

Figure correctness alone is therefore insufficient evidence of task competence. A model that gets all numbers right but never opens a governing document should fail the task, because it demonstrated neither discovery nor verification.

## The Solution

Remove every explicit rule from the prompt. Force the model to discover each rule from its source document. The V15 prompt (chd_prompt_v15.md) replaces explicit instructions with discovery instructions:

| Element | Before (explicit rule) | After (discovery) |
|---------|----------------------|-------------------|
| Skip documentation | Full rule from SO 15-3 s.3.2-3.3 quoted | "Determine for yourself what Standing Order 15-3 says" |
| Priority levels | P1/P2/P3 definitions given | "Determine for yourself which exceptions are Priority 1, 2, 3" |
| Account join | "AC-LP-0122 → LP-0122" example | Removed — discover from data |
| Billable length | "using check-in LOA from the certificates" | "Determine from governing documents" |
| Rate source | "apply rates from Resolution 2022-06" | "Determine which rates apply to which periods" |

## Why the Files Support the Hardening

Every rule the model needs exists in the source documents:

- Standing Order 15-3 contains the documentation rule in sections 3.2-3.3
- Tariff Resolution 2019-14 contains the pre-adoption rates and billable length rule
- Resolution 2022-06 contains the post-adoption rates
- The data files contain all figures and the account identifiers that reveal the join pattern

Nothing is missing from the environment. The model simply needs to find the rules where they live rather than reading them from the prompt.

## Expected Outcome

When the 8 model responses are run against V15:

- Weak models that previously passed by computing figures correctly will now fail because they cannot discover the rules from documents.
- Strong models that already discovered rules from documents will still pass, because the rules are findable in the source documents.
- The gap between strong and weak model performance will widen because weak models relied on instruction-following rather than discovery.
- Figure errors will still be penalized, but figure correctness alone will no longer be sufficient to pass.

This aligns the task with its design intent: testing document discovery, not instruction-following.

## Conclusion

The hardening is necessary and well-supported. The CHD task should test whether a model can find and apply rules from source documents. V15 removes the shortcut that allowed weak models to pass without opening any document, while preserving the task's scope, deliverables, and solvability.
