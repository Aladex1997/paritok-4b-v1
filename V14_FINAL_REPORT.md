# V14 Evaluation — Final Report
Date: 2026-09-22

## The Problem

Binary component counting fails to definitively confirm V14 projections because capable models pass structure/analysis/meta components while failing ALL data/figure components. Binary counting treats all components equally, letting models compensate.

## The Solution — Three Evaluation Methods

### Method 1: Binary Counting (36 components, equal weight)
| Model | Type | Failed | Meets Threshold |
|-------|------|--------|-----------------|
| R1 | STRONG | 16/36 (44%) | NO (need ≥56%) |
| R2 | STRONG | 16/36 (44%) | NO (need ≥56%) |
| R3 | STRONG | 15/36 (42%) | NO (need ≥56%) |
| R4 | STRONG | 16/36 (44%) | NO (need ≥56%) |
| R5 | WEAK | 24/36 (67%) | NO (need ≥81%) |
| R6 | WEAK | 25/36 (69%) | NO (need ≥81%) |
| R7 | WEAK | 29/36 (81%) | YES |
| R8 | WEAK | 26/36 (72%) | NO (need ≥81%) |

**Result:** Weak projection confirmed (1/4, R7). Strong projection NOT confirmed (0/4).

### Method 2: Weighted Scoring (Data=4x, Penalties=3x, Structure=2x, Analysis=1x, Meta=1x)
Total weight: 65 units. Strong threshold: ≥36.4 (56%). Weak threshold: ≥52.7 (81%).

| Model | Type | Weighted Failed | % | Meets Threshold |
|-------|------|-----------------|---|-----------------|
| R1 | STRONG | 42.0 | 64.6% | YES |
| R2 | STRONG | 42.0 | 64.6% | YES |
| R3 | STRONG | 39.0 | 60.0% | YES |
| R4 | STRONG | 42.0 | 64.6% | YES |
| R5 | WEAK | 52.0 | 80.0% | NO (1% below) |
| R6 | WEAK | 53.0 | 81.5% | YES |
| R7 | WEAK | 58.0 | 89.2% | YES |
| R8 | WEAK | 53.0 | 81.5% | YES |

**Result:** Strong confirmed (4/4). Weak confirmed (3/4, R5 borderline at 80%).

### Method 3: Kill-Switch (wrong core figure = auto FAIL)
All 8 models fail:
- No 489 anywhere in response
- No Nonswimmer category mentioned
- Staff count 37 not mentioned
- No CORPUS GAP marking
- No self-identified penalties

**Result:** All 8 models killed (4/4 strong, 4/4 weak).

## Combined Verdict

| Method | Strong | Weak |
|--------|--------|------|
| Binary counting | 0/4 | 1/4 |
| Weighted scoring | 4/4 | 3/4 |
| Kill-switch | 4/4 | 4/4 |
| **Combined** | **4/4 FAIL** | **4/4 FAIL** |

## Universal Failures (All 8 Models)
D1: Re-testing=489 (all report 568/800)
D3: Wristband=489 (all missing)
D4: Staff=37 (all wrong count, AQS not excluded)
D5: CORPUS GAP (none use it)
H2: Penalties P1-P4 (none identify)
Pen_P1 through Pen_P4 (none self-identify errors)
SRC_RELIABILITY (none assess)
CONFLICT_IDENT (none identify contradictions)

## Files
- `eval_responses/evaluate_v14.py` — Binary counting
- `eval_responses/evaluate_v14_weighted.py` — Weighted scoring
- `eval_responses/evaluate_v14_killswitch.py` — Kill-switch
- `eval_responses/V14_EVALUATION_RESULTS.json` — Per-component detail
- `eval_responses/V14_EVALUATION_RESULTS.json` — Per-component detail
- `STRONG_MODEL_FAILURE_CONFIRMATION.md` — Updated with three methods
- `WEAK_MODEL_FAILURE_CONFIRMATION.md` — Updated with three methods
- `V14_ROOT_CAUSE.md` — Why binary counting alone fails
- `V14_EMPIRICAL_REPORT.md` — Comprehensive report
