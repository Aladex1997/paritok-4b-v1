# V6 Compliance Memo Evaluation — Summary

## Prompt
- File: prompt.md (V6)
- Key traps: [CORPUS GAP] required, wristbands carry to 2027, band-derived camper count (489), AQS exclusion (staff=37), no named locations, no explicit band-category naming, no "block enrollment" language

## Rubric
- File: rubric.md (V6)
- Base max: 7.0, Penalties max: -3.5 (P1=-1.5, P2=-1.0, P3=-0.5, P4=-0.5)

## Results (8 models graded against V6 rubric)

| Model | Type | Base | Penalties | Final | % | Threshold | Status |
|-------|------|------|-----------|-------|---|-----------|--------|
| R1 | STRONG | 4.15 | -3.0 | 1.15 | 16.4% | 50% | FAIL |
| R2 | STRONG | 4.15 | -3.0 | 1.15 | 16.4% | 50% | FAIL |
| R3 | STRONG | 4.30 | -2.5 | 1.80 | 25.7% | 50% | FAIL |
| R4 | STRONG | 4.15 | -3.0 | 1.15 | 16.4% | 50% | FAIL |
| R5 | WEAK | 3.35 | -3.0 | 0.35 | 5.0% | 80% | FAIL |
| R6 | WEAK | 3.65 | -3.0 | 0.65 | 9.3% | 80% | FAIL |
| R7 | WEAK | 3.55 | -2.5 | 1.05 | 15.0% | 80% | FAIL |
| R8 | WEAK | 3.40 | -3.0 | 0.40 | 5.7% | 80% | FAIL |

## Target Verification
- Fail ≥60% strong: Required ≥3/4 → Actual 4/4 (100%) ✅
- Fail ≥90% weak: Required ≥4/4 → Actual 4/4 (100%) ✅

## Penalty Triggers
- P1 (wrong camper count): 8/8 models (all report 568/800 vs 489)
- P2 (missing wristbands): 8/8 models (all report 0 vs 489)
- P3 (staff error): 6/8 models (report 32-42 vs 37)
- P4 (double-counting): 8/8 models
- D5 ([CORPUS GAP]): 0/8 models (none used it)

## V5 vs V6
- Strong avg: 21.1% → 18.7% (↓2.4pts)
- Weak avg: 13.4% → 8.8% (↓4.6pts)
- [CORPUS GAP] usage: some → 0/8

## Files
- prompt.md — V6 prompt
- rubric.md — V6 rubric with results
- eval_responses/response_texts.json — All 8 model response texts
- eval_responses/evaluate_v6.py — Evaluation script
