# V14 Evaluation: Root Cause Analysis
Date: 2026-09-22

## Why Empirical Results Don't Meet Projections

### Component-Type Breakdown (All 8 Models)

| Type | Components | Strong Pass Rate | Weak Pass Rate |
|------|-----------|-----------------|---------------|
| Data/Figures (D1-D7, Pen_P1-P4) | 11 | 0-1/11 | 0/11 |
| Structure/Format (A, B, G) | 6 | 3-5/6 | 0-3/6 |
| Analysis/Scope (C, E, F, H) | 14 | 9-12/14 | 4-5/14 |
| Meta/Qualitative (Scope_limit, Timeline, Risk, SRC, CONFLICT) | 5 | 5/5 | 2-3/5 |
| **Total** | **36** | **20/36 pass** | **16/36 pass** |

### Root Cause

**V14 counting does not weight component types.** Models that fail ALL data/figure components (0-1/11) compensate by passing structure, analysis, and meta components. Binary PASS/FAIL counting without severity weighting means:

- All 8 models fail D1, D3, D4, D5, B1, D6, D2, E4, H2, Pen_P1-P3 (universal failures)
- All 8 models get key figures WRONG (489, 37, 264, wristband=489, Nonswimmer counts)
- But strong models pass 5/6 structure + 9-12/14 analysis + 5/5 meta = enough to stay below 20 FAIL

**Example — R1:**
- Data/Figures: 1/11 passed
- Structure/Format: 5/6 passed  
- Analysis/Scope: 9/14 passed
- Meta/Qualitative: 5/5 passed
- Total: 20/36 passed → 16/36 failed (below ≥20 threshold)

### V6 vs V14 Difference

V6 applied penalties AFTER base scoring (P1=-1.5, P2=-1.0, P3=-0.5, P4=-0.5). Data failures reduced overall score. All 8 models failed V6 because penalties brought base scores below threshold.

V14 switched to binary component counting. Penalties no longer reduce failure count — they just mark additional failed components. But models compensate by passing non-data components. The total failure count stays at 15-16, below the ≥20 threshold.

### Why V14 Hardening Failed

V14 added: cross-reference mandate, characterization challenge, judgment under ambiguity, no named sources. These target Analysis/Scope components. But strong models PASS these components (9-12/14) even under V14 criteria.

The hardening didn't make DATA components harder — D1-D7 still fail universally because models can't derive correct figures from source data without explicit guidance. But the hardening also didn't make STRUCTURE or META components harder enough to offset data failures.

### Proposed Solutions

1. **Weighted evaluation**: Assign severity weights to components. Data/figure failures (D1-D7, Pen_P1-P4) should carry heavier weight than format/structure. Threshold should be weighted-fail, not binary-count-fail.

2. **Kill-switch criteria**: If ANY of {489, 37, 264, CORPUS GAP} is wrong, model FAILS regardless of other components. Core data accuracy should be a binary gate.

3. **V15 hardening**: Make structure/meta components harder by requiring deeper analysis (e.g., specific cross-references between components, not just mentions).

4. **Re-generate under V14 prompt**: Current responses are from V6/V8 prompts. V14 prompt may produce different responses with different failure patterns.

5. **Manual human evaluation**: Current automated evaluation has limitations (keyword matching, false PASS on cross-reference components). Human grading against V14 rubric may reveal more failures.

### Files
- V14_EMPIRICAL_REPORT.md — empirical results
- eval_responses/V14_EVALUATION_RESULTS.json — per-component detail
- eval_responses/evaluate_v14.py — evaluation script
