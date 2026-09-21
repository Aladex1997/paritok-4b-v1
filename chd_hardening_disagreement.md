# Disagreement Reasoning — CHD Task Hardening

## Background

Review finding: weak model responses met nearly every element of the CHD task when the figures were correct. The task was too easy to grade well on, even for weak models.

## The Problem

The current prompt (output/corrected_prompt.txt) spells out every rule the files contain:

1. **Skip documentation rule**: explicitly states "check whether contemporaneous proof exists per Standing Order 15-3 s.3.2-3.3 — a cover sheet alone doesn't count. Use review_date in skip_events as the assembly date; a skip has contemporaneous proof only if review_date is on or before the skip_date AND a corresponding justification PDF exists."

2. **Three priority levels**: explicitly defines Priority 1, Priority 2, and Priority 3 with specific criteria for each.

3. **Account join**: explicitly gives the example "AC-LP-0122 → LP-0122" showing how to extract the slip ID from the account number.

4. **Billable length**: explicitly states "determine covered vs open from slip_inventory_2026-08.csv using check-in LOA from the certificates."

5. **Rate source**: explicitly references Resolution 2022-06 for rates.

A model that reads these instructions and follows the steps reaches the correct answers without ever opening Standing Order 15-3, Tariff Resolution 2019-14, or the underlying data files. The prompt gives the analysis pathway directly. The numbers in the environment are correct and the prompt tells you exactly how to use them. Weak models that happen to compute the right figures pass.

## Why This Fails

The task is supposed to test whether a model can discover rules from source documents, not whether it can follow explicit instructions. When the prompt spells out every rule:

- **Verification is not tested**: The model never needs to check Standing Order 15-3 or Tariff Resolution 2019-14. It can skip all source documents and still produce correct answers.
- **Discovery is not tested**: The model never needs to determine for itself what constitutes a documented skip, what priority levels exist, or how accounts link to slips.
- **Figure correctness masks all other failures**: A weak model that computes the right numbers passes regardless of whether it understood the governing documents. The prompt makes figure computation a mechanical exercise rather than a discovery task.

This is the core reason V6 evaluation showed weak models scoring 5-15% while getting some figures right — the prompt rewards figure computation without testing document understanding.

## The Hardening Approach

The V15 prompt (chd_prompt_v15.md) removes every explicit rule from the prompt while preserving the task structure and deliverable format. Models must now discover each rule from the source documents themselves:

| Element | V14 (explicit) | V15 (discovery) |
|---------|----------------|-----------------|
| Skip documentation | "check whether contemporaneous proof exists per Standing Order 15-3 s.3.2-3.3 — a cover sheet alone doesn't count. Use review_date..." | "Determine for yourself what Standing Order 15-3 says about when a skip counts as documented and what proof is required." |
| Priority levels | "Priority 1 — skips with no supporting record... Priority 2 — skips where supporting records exist... Priority 3 — subledger arithmetic errors only." | "Determine for yourself which exceptions are Priority 1, Priority 2, and Priority 3." |
| Account join | "join to slip_inventory via the slip ID embedded in the account number (e.g., AC-LP-0122 → LP-0122)" | Removed entirely. Model must discover the relationship from the data. |
| Billable length | "determine covered vs open from slip_inventory_2026-08.csv using check-in LOA" | "Determine billable length from the governing documents — do not use a formula from this prompt." |
| Rate source | "apply rates from Resolution 2022-06" | "Determine the rates from the governing documents. Rates change at different points in time — determine which rates apply to which periods." |

## Why V15 Solves the Problem

1. **Verification becomes necessary**: The model cannot skip Standing Order 15-3, Resolution 2022-06, or Tariff Resolution 2019-14. Every rule must be found from these documents.

2. **Discovery becomes necessary**: The model must determine for itself what constitutes a documented skip, what priority levels exist, and how accounts link to slips. No pathway is given.

3. **Figure correctness alone is insufficient**: Even if a model computes the right figures, it must also demonstrate that it found the governing rules from the documents. A model that gets the numbers right but never opens Standing Order 15-3 will fail the discovery requirements.

4. **The files support the hardening**: All the rules the model needs are present in the source documents. The environment contains Standing Order 15-3 (with section 3.2-3.3 documentation rules), Tariff Resolution 2019-14 (with pre-adoption rates and billable length rules), Resolution 2022-06 (with post-adoption rates), and the data files with all the figures. Nothing is missing.

## What V15 Does Not Change

- **Task scope**: Same audit period, same deliverables, same quality bar.
- **File list**: Same source documents, same environment.
- **Deliverable format**: Same workbook and memo structure.
- **Date context**: Same audit date (August 1, 2026), same cutoff.
- **Evaluation criteria**: Same rubric (V14). Figures that are wrong are still wrong.
- **Critical data**: Same expected values (correct figures are still correct after hardening).

## Conclusion

The hardening makes the CHD task test what it was designed to test: whether a model can discover and apply rules from source documents, not whether it can follow explicit instructions. The V15 prompt removes all pathways that bypass document discovery while keeping the environment fully supported. Running the 8 model responses again against V15 should show significantly lower pass rates for weak models, bringing weak performance in line with the reviewer's finding that the task was previously too easy.
