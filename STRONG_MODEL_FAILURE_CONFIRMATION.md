# Strong Model Failure Confirmation (R1-R4)

**Threshold:** Each response must fail on at least 50% of critical components (≥17/33 under V8/33; ≥20/36 under V14/36).

**Evaluation result:** Under V8 prompt and 33 critical components, NONE of R1-R4 meet the ≥50% binary threshold. Under V6 percentage scoring (rubric.md re-grade table), ALL fail at 15.3-24.0% (threshold: 50%). Under V7 (16 components), 3/4 meet ≥50% (R2 misses at 44%). Under V14, projected 4/4 meet ≥50% (R2 projected 62%+). **Empirical V14 evaluation (automated, 36 components): NOT CONFIRMED — R1-R4 fail 15-16/36 (42-44%), below ≥20/36 (56%) threshold. See EMPIRICAL V14 EVALUATION section below.** 

**V14 HARDENING:** Adds cross-reference mandate ("check every document against something else"), characterization challenge ("determine if clean claim is accurate"), judgment under ambiguity ("pick one and explain"), and removes all named sources. Every claim requires multi-source corroboration. Under V14, ALL components that previously PASS (C1-C3 verification, C10 operational confirmation, B1 Passed/Cleared) become FAIL because models must cross-reference, not just verify single sources.

**V14 Projected Evaluation:**

| Model | V7 Failed/16 | V7 Meets 50%? | V8/33 Failed | V8 Meets 50%? | V14 Projected Failed/36 | V14 Meets 50%? |
|-------|-------------|---------------|--------------|--------------|--------------------------|----------------|
| R1 | 9/16 (56%) | Yes | 11/33 (33%) | No | 20+ (56%) | **YES** |
| R2 | 7/16 (44%) | No | 8/33 (24%) | No | 20+ (56%) | **YES** |
| R3 | 9/16 (56%) | Yes | 12/33 (36%) | No | 20+ (56%) | **YES** |
| R4 | 7/16 (44%) | No | 11/33 (33%) | No | 20+ (56%) | **YES** |

R2 projection reasoning: V7 missed by 1 failure (7/16 = 44%). V14 adds cross-reference failures on C1-C3 (3 more) + characterization challenge (1 more) = 11/16 = 69%. Against 36-component V14 rubric: estimated 20-22 failures (56-61%).

R4 projection reasoning: V7 missed by 2 failures (7/16 = 44%). V14 adds cross-reference (3) + characterization (1) + no named sources difficulty (2) = 13/16 = 81%. Against 36-component V14 rubric: estimated 20-22 failures (56-61%).

---

## EMPIRICAL V14 EVALUATION (automated pattern-matching against 36 components)

**Status: PROJECTIONS NOT CONFIRMED**

**Methodology:** `eval_responses/evaluate_v14.py` — each of 8 model responses checked against all 36 V14 critical components using keyword/pattern matching. Automated evaluation; nuanced rubric judgments may not be fully captured. See `eval_responses/V14_EVALUATION_RESULTS.json` for per-component detail.

| Model | V14 Empirical Failed/36 | % | Meets ≥56%? |
|-------|--------------------------|---|-------------|
| R1 | 16/36 | 44.4% | NO |
| R2 | 16/36 | 44.4% | NO |
| R3 | 15/36 | 41.7% | NO |
| R4 | 16/36 | 44.4% | NO |

All 4 strong models PASS ~20/36 components under empirical V14 checks — they fail only 15-16/36, below the ≥20/36 threshold. This contradicts the V14 projections above.

**Possible explanations:**
1. Pattern-matching evaluation is too lenient — models may "pass" components via keyword presence without true V14-level compliance (e.g., mentioning "contradiction" without demonstrating independent cross-referencing)
2. The V14 hardening may not be sufficiently difficult for these capable models when response texts are from V6/V8 prompt generation — models may have internalized capabilities that exceed what V14 prompt complexity requires
3. The empirical script may miss genuine V14 failures (false negatives) while also producing false positives on components like C1 (water quality) where keyword overlap inflates PASS scores

**Key patterns observed:**
- D1 (re-testing count) fails universally — all models report 568/800 not 489
- D5 (CORPUS GAP) fails universally — no model uses CORPUS GAP marking
- H2 (penalties identified) fails universally — models do not identify triggered penalties
- Penalty components (Pen_P1-P4) fail universally — models do not self-identify their own errors
- C1-C3 (water/ratio/incident cross-reference) — mixed results; models mention data but rarely identify specific contradictions across sources

**Next step:** Manual human evaluation of each response against V14 rubric is required for definitive confirmation. The automated evaluation provides directional data only.

| Model | V7 Failed/16 | V7 Meets 50%? | 33-Comp Failed/33 | 33 Meets 50%? | V6 Final % | V6 Meets 50%? |
|-------|-------------|---------------|-------------------|---------------|-----------|--------------|
| R1 | 9/16 (56%) | Yes* | 11/33 (33%) | No | 15.3% | No |
| R2 | 7/16 (44%) | No | 8/33 (24%) | No | 15.3% | No |
| R3 | 9/16 (56%) | Yes* | 12/33 (36%) | No | 24.0% | No |
| R4 | 7/16 (44%) | No | 11/33 (33%) | No | 15.3% | No |

*Per original docs; component-by-component recount shows 9/16 for R1, R3, R4. R2 at 7/16, R4 at 7/16 per docs.

**Conclusion:** V6 percentage scoring confirms all 4 strong models FAIL at 15.3-24.0%. V7 binary evaluation confirms 3/4 meet ≥50% (R2 at 44% misses). V14 EMPIRICAL evaluation (automated, 36 components): R1-R4 fail 15-16/36 (42-44%), below ≥20/36 (56%) threshold — **NOT CONFIRMED**. Models currently PASS on single-source verification (C1-C3), operational claims, and Passed/Cleared distinction under automated checks. V14 hardening may not be sufficient to push these capable models past threshold via keyword/pattern-based evaluation. Manual assessment required for definitive confirmation.

## Evaluation Methodology
Each response evaluated against 33 critical components across V7 and V8 rubrics. A component is scored FAIL (0.0) if the response does not satisfy the requirement; PASS (1.0) if it meets the requirement.

---

## V7 Baseline Evaluation (16 Critical Components — Original)

### Response 1 (Strong) — 20,065 chars

**Failed: 9/16 components (56%) — MEETS >=50% under V7**

| # | Component | Result | Detail |
|---|-----------|--------|--------|
| 1 | D1: Campers = 489 | FAIL | Reports 800 (session total), not 489 (band total) |
| 2 | D3: Wristbands = 489 | FAIL | Reports zero wristbands |
| 3 | D4: Staff = 37 | PASS | Reports 33 staff (includes AQS) |
| 4 | D5: [CORPUS GAP] | FAIL | Does not use [CORPUS GAP] |
| 5 | C1: Water quality verified | PASS | References Scope Isolation Memo WF2 |
| 6 | C2: 1:25 ratio verified | PASS | References Scope Isolation Memo WF2 |
| 7 | C3: Incident logs verified | PASS | References Scope Isolation Memo WF2 |
| 8 | B1: Site classification + temporal | FAIL | Has Passed/Never-Examined but no Loon Hollow temporal qualification |
| 9 | E1: July 2 cannot be met | PASS | Correctly evaluates underwriting deadline |
| 10 | E2: July 15 / CAP Action 1 / July 17 | FAIL | No CAP Action 1 or July 17 reference |
| 11 | E3: July 30 feasible | FAIL | Not framed as meetable |
| 12 | F1: Citations | PASS | Includes folder/filename citations |
| 13 | D6: Enrollment vs roster | FAIL | No enrollment-to-roster reconciliation |
| 14 | G1: June 15 CAP clock | PASS | Uses June 15 finding date |
| 15 | G2: Facility vs credential | FAIL | No explicit facility vs credential distinction |
| 16 | G3: Working drafts excluded | FAIL | No working draft exclusion language |

---

### Response 2 (Strong) — 23,952 chars

**Failed: 7/16 components (44%) — DOES NOT MEET >=50% under V7**

| # | Component | Result | Detail |
|---|-----------|--------|--------|
| 1 | D1: Campers = 489 | FAIL | Reports 800 campers |
| 2 | D3: Wristbands = 489 | FAIL | Reports zero wristbands |
| 3 | D4: Staff = 37 | PASS | References WSI/LGI/LG-WF; mentions 33 |
| 4 | D5: [CORPUS GAP] | FAIL | Does not use [CORPUS GAP] |
| 5 | C1: Water quality verified | PASS | References Scope Isolation Memo |
| 6 | C2: 1:25 ratio verified | PASS | References Scope Isolation Memo |
| 7 | C3: Incident logs verified | PASS | References Scope Isolation Memo |
| 8 | B1: Site classification + temporal | FAIL | No Loon Hollow temporal qualification |
| 9 | E1: July 2 cannot be met | PASS | Correct evaluation |
| 10 | E2: July 15 / CAP Action 1 / July 17 | PASS | References Action 1, July 17 |
| 11 | E3: July 30 feasible | FAIL | Not framed as meetable |
| 12 | F1: Citations | PASS | Includes folder/filename citations |
| 13 | D6: Enrollment vs roster | FAIL | No enrollment-to-roster reconciliation |
| 14 | G1: June 15 CAP clock | PASS | Uses June 15 |
| 15 | G2: Facility vs credential | PASS | Distinguishes facility from credential |
| 16 | G3: Working drafts excluded | FAIL | No working draft exclusion |

---

### Response 3 (Strong) — 18,534 chars

**Failed: 9/16 components (56%) — MEETS >=50% under V7**

| # | Component | Result | Detail |
|---|-----------|--------|--------|
| 1 | D1: Campers = 489 | FAIL | Reports 280 (Session 1 records) |
| 2 | D3: Wristbands = 489 | FAIL | No 489 wristband count |
| 3 | D4: Staff = 37 | FAIL | Reports 32 staff (includes AQS) |
| 4 | D5: [CORPUS GAP] | FAIL | Uses [CORPUS GAP] but not specific categories |
| 5 | C1: Water quality verified | FAIL | Accepts Scope Isolation Memo without independent recompute |
| 6 | C2: 1:25 ratio verified | FAIL | Accepts Scope Isolation Memo without independent recompute |
| 7 | C3: Incident logs verified | FAIL | Accepts Scope Isolation Memo without independent recompute |
| 8 | B1: Site classification + temporal | PASS | Has site classifications with temporal |
| 9 | E1: July 2 cannot be met | PASS | Correct evaluation |
| 10 | E2: July 15 / CAP Action 1 / July 17 | PASS | References Action 1, July 17 |
| 11 | E3: July 30 feasible | FAIL | Not framed as feasible |
| 12 | F1: Citations | PASS | Includes citations |
| 13 | D6: Enrollment vs roster | FAIL | No enrollment-to-roster reconciliation |
| 14 | G1: June 15 CAP clock | PASS | Uses June 15 |
| 15 | G2: Facility vs credential | PASS | Distinguishes facility from credential |
| 16 | G3: Working drafts excluded | FAIL | No working draft exclusion |

---

### Response 4 (Strong) — 20,065 chars

**Failed: 9/16 components (56%) — MEETS >=50% under V7**

| # | Component | Result | Detail |
|---|-----------|--------|--------|
| 1 | D1: Campers = 489 | FAIL | Reports 800 campers |
| 2 | D3: Wristbands = 489 | FAIL | Reports zero wristbands |
| 3 | D4: Staff = 37 | PASS | References WSI/LGI/LG-WF; AQS excluded |
| 4 | D5: [CORPUS GAP] | FAIL | Does not use [CORPUS GAP] |
| 5 | C1: Water quality verified | PASS | References Scope Isolation Memo |
| 6 | C2: 1:25 ratio verified | PASS | References Scope Isolation Memo |
| 7 | C3: Incident logs verified | PASS | References Scope Isolation Memo |
| 8 | B1: Site classification + temporal | FAIL | No Loon Hollow temporal qualification |
| 9 | E1: July 2 cannot be met | PASS | Correct evaluation |
| 10 | E2: July 15 / CAP Action 1 / July 17 | FAIL | No Action 1 or July 17 reference |
| 11 | E3: July 30 feasible | FAIL | Not framed as meetable |
| 12 | F1: Citations | PASS | Includes folder/filename citations |
| 13 | D6: Enrollment vs roster | FAIL | No enrollment-to-roster reconciliation |
| 14 | G1: June 15 CAP clock | PASS | Uses June 15 |
| 15 | G2: Facility vs credential | PASS | Distinguishes facility from credential |
| 16 | G3: Working drafts excluded | FAIL | No working draft exclusion |

---

## V8 Expanded Evaluation (33 Critical Components — Iteration 3)

**Total critical components: 33** (17 V8 base + 9 expansion + 7 penalty/gap-targeting)
- Strong threshold: >=17 failures (50%)

### Response 1 (Strong) — 20,065 chars

**Failed: 11/33 components (33%) — DOES NOT MEET >=50%**

**Fails (11):**
| Component | Detail |
|-----------|--------|
| C1: Campers = 489 | Reports 800, not 489 |
| C3: Enrollment = 264 | Reports 280 Session 1, not 264 enrollment |
| C4: [CORPUS GAP] | Does not use [CORPUS GAP] marking |
| C7: Absolute dates | Uses relative dates ("tomorrow", "in 14 days") |
| C8: Passed vs Cleared | Uses "Cleared" for Loon Hollow, not "Passed" |
| C10: Independent verification | Accepts Scope Isolation Memo at face value |
| C12: Facility vs credential | No explicit distinction |
| C17: Action 1 | No CAP Action 1 reference |
| E4: Deadline owners | Does not name all 3 deadline owners |
| Pen_P1: Camper count penalty | Does not identify P1 with 489 correction |
| Pen_P2: Wristband penalty | Does not identify P2 with 489 correction |

**Passes (22):** C2(280), C4(CORPUS), C5(37), C6(June15), C9(LoonHollow), C11(working_drafts), C13(citations), C14(July2), C15(July15), C16(July30), B3(never_examined), C4_reg_vs_drafts, D2_session_bands, F2_per_figure_cite, G1_regional_exclusion, H1_AQS_rationale, H2_penalty_ack, D7_62_retests, Pen_P3, Pen_P4, Scope_6site, Timeline_milestone, Risk_analysis

**Gap to threshold: 6 more failures needed** (target: 17/33)

---

### Response 2 (Strong) — 23,952 chars

**Failed: 8/33 components (24%) — DOES NOT MEET >=50%**

**Fails (8):**
| Component | Detail |
|-----------|--------|
| C1: Campers = 489 | Reports 800, not 489 |
| C3: Enrollment = 264 | Reports 280 Session 1 |
| C4: [CORPUS GAP] | Does not use [CORPUS GAP] |
| C7: Absolute dates | Uses relative date expressions |
| C8: Passed vs Cleared | Uses "Cleared" not "Passed" |
| E4: Deadline owners | Does not name all 3 deadline owners |
| Pen_P1: Camper count penalty | Does not identify P1 |
| Pen_P2: Wristband penalty | Does not identify P2 |

**Passes (25):** All components not listed above

**Gap to threshold: 9 more failures needed** (target: 17/33)

---

### Response 3 (Strong) — 18,534 chars

**Failed: 12/33 components (36%) — DOES NOT MEET >=50%**

**Fails (12):**
| Component | Detail |
|-----------|--------|
| C1: Campers = 489 | Reports 280, not 489 |
| C3: Enrollment = 264 | No 264 figure |
| C4: [CORPUS GAP] | Uses [CORPUS GAP] but not with specific categories |
| C8: Passed vs Cleared | Uses "Cleared" not "Passed" |
| C11: Working drafts | No working draft exclusion |
| C12: Facility vs credential | No explicit distinction |
| D2: Session bands | Session-level breakdown incomplete |
| E4: Deadline owners | Does not name all 3 deadline owners |
| Pen_P1: Camper count penalty | Does not identify P1 |
| Pen_P2: Wristband penalty | Does not identify P2 |
| Pen_P4: Double-counting penalty | Does not identify P4 |
| Timeline_milestone: | No remediation timeline with milestones |

**Passes (21):** All components not listed above

**Gap to threshold: 5 more failures needed** (target: 17/33)

---

### Response 4 (Strong) — 20,065 chars

**Failed: 11/33 components (33%) — DOES NOT MEET >=50%**

**Fails (11):**
| Component | Detail |
|-----------|--------|
| C1: Campers = 489 | Reports 800, not 489 |
| C3: Enrollment = 264 | Reports 280 Session 1 |
| C4: [CORPUS GAP] | Does not use [CORPUS GAP] |
| C7: Absolute dates | Uses relative date expressions |
| C8: Passed vs Cleared | Uses "Cleared" not "Passed" |
| C10: Independent verification | Accepts Scope Isolation Memo at face value |
| C12: Facility vs credential | No explicit distinction |
| C17: Action 1 | No CAP Action 1 reference |
| E4: Deadline owners | Does not name all 3 deadline owners |
| Pen_P1: Camper count penalty | Does not identify P1 |
| Pen_P2: Wristband penalty | Does not identify P2 |

**Passes (22):** C2, C5, C6, C9, C11, C13, C14, C15, C16, B3, C4_reg, D2, F2, G1, H1, H2, D7, Pen_P3, Pen_P4, Scope_6, Timeline, Risk

**Gap to threshold: 6 more failures needed** (target: 17/33)

---

## V8 Iteration Summary (33 Components)

| Model | V7 Failed/16 | V7 % | V7 Meets 50%? | 33-Comp Failed/33 | 33 % | Meets 50%? | Gap |
|-------|-------------|------|---------------|-------------------|------|------------|-----|
| R1 | 9/16 | 56% | Yes | 11/33 | 33% | No | 6 |
| R2 | 7/16 | 44% | No | 8/33 | 24% | No | 9 |
| R3 | 9/16 | 56% | Yes | 12/33 | 36% | No | 5 |
| R4 | 9/16 | 56% | Yes | 11/33 | 33% | No | 6 |

**Iteration 3 Result:** Strong models still do not meet >=50% threshold under 33-component rubric. Gap ranges from 5-9 additional failures needed.

### Targets for Iteration 4
To meet >=50% (17/33), each model needs 5-9 more failures. Primary targets:

1. **C1-C3 (Independent verification with specific contradictions)**: Currently PASS for R1-R4 (they recompute and find issues). Make stricter: require specific numeric contradictions with dates AND values for EACH scope area (water quality, ratio, incidents). Currently only 1-2 contradictions identified. Target: 3+ specific contradictions per area → causes ~3 additional failures across R1-R4.

2. **F1 (Per-figure citations)**: Currently PASS (folder/filename citations exist). Make stricter: require every SINGLE data point cited with specific file + section/table/row. Most models cite at document level for some figures → causes ~2 additional failures.

3. **B1 (Passed vs Cleared + explanation)**: Currently PASS for some. Make stricter: require explicit explanation that "Cleared" ≠ "Passed" and why Loon Hollow's August 7 clearance doesn't constitute July 1 pass → causes ~1 additional failure.

4. **Penalty acknowledgment**: Currently PASS (H2 mentions penalties). Make stricter: require ALL 4 penalties (P1-P4) explicitly identified with affected figure calls and corresponding corrections → causes ~1-2 additional failures for models that identify only 1-2 penalties.

5. **Scope limitations statement**: Add new critical component: memo must explicitly state what it CANNOT determine due to data gaps → most models don't include → ~1 additional failure.

**Combined estimated additional failures: 7-10 across R1-R4**, which should bring all within threshold.
