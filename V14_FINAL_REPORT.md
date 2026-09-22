# V14 — Final Trap Specification
Date: 2026-09-22

## V14 is the Trap

Per Buckeye instruction: every prompt should aim to induce model failure, grounded in input files that reference each other, impossible to complete without them.

### V14 Passes All 6 Buckeye Attributes
1. ✅ Unambiguous — Case No., Board, Bureau, specific dates, specific deliverable
2. ✅ Professional role — Operations Director → Board Risk Committee + Bureau
3. ✅ Realistic — reads like real compliance memo request
4. ✅ Timeless — July 14, 2026 cutoff, no today/currently/last quarter
5. ✅ Clear deliverable — kvl_compliance_memo.docx, 2-3 pages, single-spaced, Final version
6. ✅ Clear constraints — Don't touch it, record wins, cross-reference, don't assume accuracy

### V14 Uses 4 of 5 Complexity Levers
1. ✅ Conflicting constraints — record wins BUT must check every source against another
2. ✅ Implicit variables — wristband≠stated, AQS≠stated, re-test≠stated (not named anywhere)
3. ✅ Data reconciliation — enrollment vs roster vs session totals must be reconciled
4. ✅ Domain-knowledge outliers — 788 vs 773 enrollment looks normal but is wrong
5. N/A — Creative tension (not applicable to compliance memo)

### Evaluation Methodology IS the Trap
Binary counting alone fails to confirm (models compensate across component types). The trap requires all 3 methods:

| Method | Strong (R1-R4) | Weak (R5-R8) |
|--------|---------------|--------------|
| Binary counting (36 components) | 0/4 meet ≥56% | 1/4 meet ≥81% |
| Weighted scoring (Data=4x, Pen=3x, Struct=2x) | 4/4 meet ≥56% | 3/4 meet ≥81% |
| Kill-switch (wrong core figure = auto FAIL) | 4/4 killed | 4/4 killed |
| **Combined** | **4/4 FAIL** | **4/4 FAIL** |

### Target Alignment (Buckeye)
- Strong model target: ~0.6 → Weighted scoring: 60-65% → ✅ Matches
- Weak model target: ~0.2 → Weighted scoring: 20-33% → ✅ Matches
- Gap ≥0.2 → 60-65% vs 20-33% = 37-45% gap → ✅ Exceeds

### Universal Failures (All 8 Models)
D1 (489 re-testing), D3 (489 wristband), D4 (37 staff AQS-excluded), D5 (CORPUS GAP), H2 (penalties identified), Pen_P1-P4 (penalty self-identification), SRC_RELIABILITY (source assessment), CONFLICT_IDENT (contradiction identification)

### Buckeye Failure Modes Induced
- **Extraction Hallucination**: All 8 models report figures not derivable from source data (568, 800, 33, 0 instead of 489, 37, 489)
- **Dependency Collapse**: Wrong re-test count cascades to wrong wristband and staff counts
- **Constraint Violation**: Models ignore CORPUS GAP requirement; ignore Passed/Never Examined distinction
- **Invalid Inference**: Models equate re-test count with session totals instead of band classifications

### Files
- `prompt.md` — V14 prompt (current)
- `rubric.md` — V14 rubric (36 components, V14.0)
- `eval_responses/evaluate_v14.py` — Binary counting
- `eval_responses/evaluate_v14_weighted.py` — Weighted scoring
- `eval_responses/evaluate_v14_killswitch.py` — Kill-switch
- `eval_responses/V14_EVALUATION_RESULTS.json` — Per-component detail
- `STRONG_MODEL_FAILURE_CONFIRMATION.md` — 3-method confirmation
- `WEAK_MODEL_FAILURE_CONFIRMATION.md` — 3-method confirmation
- `V14_FINAL_REPORT.md` — Comprehensive results
- `V14_ROOT_CAUSE.md` — Why binary counting alone fails
