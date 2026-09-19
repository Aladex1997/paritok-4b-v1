KVL Compliance Memo — Rubric for Model Response Grading

Rubric Version: 7.0 (V6 + independent operations verification + enrollment reconciliation + strengthened [CORPUS GAP] + Loon Hollow temporal qualification + June 15 date distinction + facility vs credential distinction + working drafts excluded)
Prompt Reference: prompt.md (V7)
Target: Strong model ~75% with correct critical data (must derive from band categories, not session totals); all models with incorrect critical data FAIL. Weak models must fail ≥14 of 16 critical components.
Grading Scale: 0 (absent) / 0.5 (partial) / 1.0 (full credit)

================================================================================
CRITICAL ERROR PENALTIES (apply after base scoring)
================================================================================
These penalties are applied AFTER the base score is calculated. Each penalty
is deducted from the total score. A response can score below 0 on any section.

PENALTY 1: Incorrect Camper Count [Max deduction: 1.5 points from Section D]
  - If campers requiring re-testing is reported as anything OTHER than 489
    (nonswimmer 192 + beginner 297): deduct 1.5 points from Section D total
  - Applies regardless of whether 568, 800, 280, or any other number is reported
  - BIG TRAP: The prompt states "our preliminary count shows 280" — models that trust this without verifying against band files will report 280 and trigger this penalty. Models that verify and find 489 (Nonswimmer 192 + Beginner 297) avoid the penalty.
  - Rationale: The V2 prompt explicitly defines the count as nonswimmer + beginner

PENALTY 2: Missing or Zero Wristband Count [Max deduction: 1.0 point from Section D]
  - If carryover wristbands blocking 2027 enrollment is reported as 0 or omitted:
    deduct 1.0 point from Section D total
  - Applies if wristband count is missing, zero, or any number other than 489
  - Rationale: Wristbands are an explicit required figure in the V2 prompt

PENALTY 3: Staff Calculation Error [Max deduction: 0.5 points from Section D]
  - If assessment-authorized staff (WSI, LGI, LG-WF at Corrigwell) is reported
    as anything OTHER than 37 (current or expiring within 60 days):
    deduct 0.5 points from Section D total
  - Applies if staff count is 32, 33, 34, 42, or any other incorrect number
  - Rationale: Staff count requires specific cross-referencing of certification
    file against authorization matrix

PENALTY 4: Double-Counting Wristbands [Max deduction: 0.5 points]
  - If wristband count differs from camper re-test count when both refer to
    nonswimmer + beginner populations: deduct 0.5 points
  - Rationale: V2 prompt explicitly states they are the same count

================================================================================
SECTION A: DELIVERABLE FORMAT (Max: 1.0)
================================================================================

A1. Single self-contained .docx file named kvl_compliance_memo.docx [0.25]
  1.0 = File exists, correct name, .docx format, single file, no attachments
  0.5 = File exists but wrong format or has attachments
  0.0 = Missing or wrong filename/format

A2. No separate spreadsheets or external attachments [0.25]
  1.0 = All data tables embedded in document body; no .xlsx/.csv references as attachments
  0.5 = Some data in document but references external files
  0.0 = Separate spreadsheets attached or referenced as deliverables

A3. Professional executive memo structure [0.25]
  1.0 = Clear TO/FROM/DATE/RE headers, executive summary, structured sections
  0.5 = Basic memo structure but missing key elements
  0.0 = Not structured as a memo

A4. Absolute date references throughout [0.25]
  1.0 = All dates stated as absolute dates anchored to July 1, 2026 reporting cutoff
  0.5 = Mostly absolute dates but some relative terms used (e.g., "tomorrow", "in 14 days")
  0.0 = Uses relative date references throughout (violates V4 prompt instruction)

================================================================================
SECTION B: STEP 1 — DEFECT SCOPE & SITE BREAKDOWN (Max: 1.0)
================================================================================

B1. Correct site classifications with Passed vs Never Examined columns [0.50]
  1.0 = All 6 sites correctly classified AND summary table has dedicated Passed and Never Examined columns (Corrigwell=unauthorized&examined, Loon Hollow=cleared, 4 others=never-examined)
  0.5 = Partial correct classifications (3-4 of 6 correct) or columns present but mislabeled
  0.0 = Incorrect or missing classifications and no Passed/Never Examined separation

B2. Unverified sign-off scope stated [0.25]
  1.0 = Identifies 1 site with unauthorized sign-offs, 4 never-examined, 1 cleared
  0.5 = Partially correct scope
  0.0 = Missing or incorrect scope

B3. Never-examined sites not classified as compliant or non-compliant [0.25]
  1.0 = Explicitly states never-examined sites cannot be classified as compliant
  0.5 = Mentions uncertainty but ambiguous
  0.0 = Treats never-examined as compliant or does not mention

================================================================================
SECTION C: STEP 2 — CLEAN SCOPE ISOLATION (Max: 1.0)
================================================================================

C1. Water quality status per Scope Isolation Memo [0.25]
  1.0 = Confirms water quality compliance per Scope Isolation Memo WF2; explicitly states defect is strictly limited to credential authorization; if operational violations are noted, clearly distinguished as separate from credential scope
  0.5 = States compliant but without confirming defect is credential-only
  0.0 = States non-compliant without distinguishing from credential scope or fails to reference Scope Isolation Memo

C2. 1:25 ratio status per Scope Isolation Memo [0.25]
  1.0 = Confirms 1:25 ratio compliant per Scope Isolation Memo; explicitly states operational defect is strictly credential-limited
  0.5 = States compliant but without confirming defect scope
  0.0 = States non-compliant or missing

C3. Incident/first-aid status per Scope Isolation Memo [0.25]
  1.0 = Confirms incident logs compliant per Scope Isolation Memo; explicitly states operational defect is strictly credential-limited
  0.5 = States compliant but without confirming defect scope
  0.0 = States non-compliant or missing

C4. Regulatory filings separated from internal working drafts [0.25]
  1.0 = Explicitly distinguishes state/federal regulatory filings (.pdf) from internal working drafts (.md)
  0.5 = Implicit separation but not explicit
  0.0 = No separation; mixes regulatory and internal documents interchangeably

================================================================================
SECTION D: STEP 3 — RE-ASSESSMENT WORKLOAD & REMEDIATION (Max: 1.5)
================================================================================

CRITICAL: See PENALTIES section above for heavy point deductions on errors in this section.

D1. Campers requiring re-testing — Nonswimmer + Beginner band counts [0.30]
  1.0 = 489 of 814 campers (60.1%) identified: Nonswimmer=192 + Beginner=297, calculated from band classification records (NOT raw session totals)
  0.5 = Correct reasoning but slightly wrong count (e.g., 488 or 490)
  0.0 = Any other number derived from session totals (568, 800, etc.) — TRIGGER FOR PENALTY 1

D2. Session-level band breakdown correct [0.30]
  1.0 = Session 1: N=61/B=104/S=107/T=272; Session 2: N=67/B=93/S=106/T=266; Session 3: N=64/B=100/S=112/T=276
  0.5 = Partially correct session-level data
  0.0 = Incorrect session data

D3. Carryover wristbands blocking 2027 enrollment [0.30]
  1.0 = 489 wristbands: Nonswimmer=192 + Beginner=297, explicitly stated as blocking 2027 enrollment advancement
  0.5 = Identifies wristbands concept but wrong count or incomplete reasoning
  0.0 = Missing, zero, or any number other than 489 — TRIGGER FOR PENALTY 2

D4. Assessment-authorized staff identified correctly [0.30]
  1.0 = 37 unique staff with WSI/LGI/LG-WF; AQS explicitly excluded as non-authorized; current/expiring-within-60d methodology stated per authorization matrix
  0.5 = Partially correct staff count (off by 1-2) or missing AQS exclusion
  0.0 = Incorrect staff identification (32/33/34/42/etc.) or includes AQS — TRIGGER FOR PENALTY 3

D5. [CORPUS GAP] marking for unaccounted camper details [0.30]
  1.0 = Unaccounted camper details explicitly marked as [CORPUS GAP]; notes individual camper IDs not in band counts file; notes operational logs not separately extractable; 62 retests are partial mitigation
  0.5 = Uses [CORPUS GAP] marking for some but not all unaccounted details
  0.0 = No [CORPUS GAP] marking or no acknowledgment of missing data — TRIGGER FOR PENALTY 1 if combined with wrong camper count

================================================================================
SECTION E: STEP 4 — JULY DEADLINE RECONCILIATION (Max: 1.5)
================================================================================

E1. Underwriting deadline (July 2) correctly evaluated [0.40]
  1.0 = States CANNOT be met for full re-assessment; recommends filing CAP as in-progress; recognizes operational evidence suffices for underwriting; Great Pines Mutual offset calculated 30 days prior to Aug 1
  0.5 = Partially correct but misses key reasoning
  0.0 = Incorrect feasibility assessment or misses deadline

E2. License renewal deadline (July 15) correctly evaluated [0.40]
  1.0 = States CONDITIONALLY feasible; references CAP-2026-01 Action 1 due July 17; recognizes filing can describe CAP as in-progress; Bureau License Renewal
  0.5 = Partially correct but misses CAP timeline reference
  0.0 = Incorrect feasibility assessment

E3. CAP response deadline (July 30) correctly evaluated [0.40]
  1.0 = States FEASIBLE; 29 days remain; references 8 corrective actions; notes Bureau Findings Unit filing July 14 marked In-Process; WF4 sweep report will support final submission
  0.5 = Partially correct
  0.0 = Incorrect feasibility assessment

E4. Deadline owners and calculation methods correct [0.30]
  1.0 = All 3 deadlines with correct authority, method, date, and owner (Great Pines/July 2/Bureau Licensing/July 15/Bureau Findings/July 30)
  0.5 = 2 of 3 correct
  0.0 = Incorrect or missing deadline details

================================================================================
SECTION F: DATA TRACEABILITY (Max: 0.5)
================================================================================

F1. Every figure, calculation, and site classification has direct (folder/filename) citation [0.50]
  1.0 = All tables and key statements include folder/filename citations
  0.5 = Most figures cited but some missing
  0.0 = No citations or citations only at document level (not per-figure)

================================================================================
SECTION G: CONSTRAINT COMPLIANCE (Max: 0.5)
================================================================================

G1. Unrelated regional files excluded [0.25]
  1.0 = No references to NYC, Chicago, or other out-of-scope regional data used as evidence
  0.5 = Mentions exclusion but includes some regional data
  0.0 = Includes or references unrelated regional files

G2. 4-step pipeline executed in order [0.25]
  1.0 = All 4 steps presented sequentially (Defect Scope → Clean Scope Isolation → Re-Assessment Workload & Remediation → July Deadline Reconciliation)
  0.5 = Steps present but out of order or merged
  0.0 = Steps missing or significantly out of order

================================================================================
CRITICAL COMPONENTS (16 total — strong models must fail ≥50%, weak models must fail ≥14 of 16)
1. D1: Campers requiring re-testing = 489 (Nonswimmer 192 + Beginner 297) [PENALTY 1]
2. D3: Wristband carryover = 489 [PENALTY 2]
3. D4: Assessment-authorized staff = 37 [PENALTY 3]
4. D5: [CORPUS GAP] used correctly with specific categories
5. C1: Water quality clean per Scope Isolation Memo — BUT independently verified against primary logs (not accepted at face value)
6. C2: 1:25 ratio clean per Scope Isolation Memo — BUT independently verified against primary logs
7. C3: Incident logs clean per Scope Isolation Memo — BUT independently verified against primary logs
8. B1: Site classifications with Passed vs Never Examined columns + Loon Hollow temporal qualification
9. E1: July 2 underwriting — cannot be met for full re-assessment (30 days before Aug 1)
10. E2: July 15 tied to CAP Action 1 due July 17
11. E3: July 30 framed as meetable (29 days, 8 actions, July 14 In-Process)
12. F1: Data traceability with (folder/filename) citations
13. D6: Enrollment-to-roster reconciliation — identify 264 enrollment vs 280 roster discrepancy
14. G1: June 15 finding date used for CAP clock (not July 1 reporting baseline)
15. G2: Facility inspection distinguished from credential examination (no facility pass substitutes for credential clearance)
16. G3: Working drafts explicitly excluded from findings (no filing status or numerical conclusion relies on scratch notes)

================================================================================
SCORING SUMMARY
================================================================================

Section A: Deliverable Format — Max 1.0
Section B: Step 1 — Defect Scope & Site Breakdown — Max 1.0
Section C: Step 2 — Clean Scope Isolation — Max 1.0
Section D: Step 3 — Re-Assessment Workload & Remediation — Max 1.5
Section E: Step 4 — July Deadline Reconciliation — Max 1.5
Section F: Data Traceability — Max 0.5
Section G: Constraint Compliance — Max 0.5
Section D6: Enrollment-to-Roster Reconciliation — Max 0.5

BASE MAX: 7.5

Penalty deductions (applied after base score):
  Penalty 1 (Incorrect camper count): -0.0 to -1.5
  Penalty 2 (Missing wristbands): -0.0 to -1.0
  Penalty 3 (Staff calculation error): -0.0 to -0.5
  Penalty 4 (Double-counting wristbands): -0.0 to -0.5
  Max total penalty: -3.5 points

FINAL MAX after penalties: 7.5 (with all penalties, could score as low as 4.0)

Re-Grade Results (Rubric v7.0 — V7 changes pending next model generation):

  Model  Type     Base   Penalties   Final    %     Threshold  Status
  -----  ------  -----  ----------  ------  -----  ---------  ------
  R1     STRONG   4.15      -3.0    1.15   16.4%      50%     FAIL
  R2     STRONG   4.15      -3.0    1.15   16.4%      50%     FAIL
  R3     STRONG   4.30      -2.5    1.80   25.7%      50%     FAIL
  R4     STRONG   4.15      -3.0    1.15   16.4%      50%     FAIL
  R5     WEAK     3.35      -3.0    0.35    5.0%      80%     FAIL
  R6     WEAK     3.65      -3.0    0.65    9.3%      80%     FAIL
  R7     WEAK     3.55      -2.5    1.05   15.0%      80%     FAIL
  R8     WEAK     3.40      -3.0    0.40    5.7%      80%     FAIL

   Strong avg: 18.7% | Weak avg: 8.8% — all FAIL

   Targets: Fail ≥60% strong (≥3/4) — ACTUAL: 4/4 (100%) ✅
            Fail ≥90% weak (≥4/4) — ACTUAL: 4/4 (100%) ✅

REP 1 ALL.zip — New Model Generation (V6):

  Model  Type     Base   Penalties   Final    %     Threshold  Status
  -----  ------  -----  ----------  ------  -----  ---------  ------
  M1     STRONG   4.20      -3.0    1.20   17.1%      50%     FAIL
  M2     STRONG   4.45      -3.0    1.45   20.7%      50%     FAIL
  M3     STRONG   4.45      -3.0    1.45   20.7%      50%     FAIL
  M4     STRONG   4.45      -3.0    1.45   20.7%      50%     FAIL
  M5     WEAK     4.20      -2.5    1.70   24.3%      80%     FAIL
  M6     WEAK     3.80      -2.5    1.30   18.6%      80%     FAIL
  M7     WEAK     3.80      -3.0    0.80   11.4%      80%     FAIL
  M8     WEAK     3.80      -3.0    0.80   11.4%      80%     FAIL

   Strong avg: 19.8% | Weak avg: 16.4% — all FAIL

   Targets: Fail ≥60% strong (≥3/4) — ACTUAL: 4/4 (100%) ✅
            Fail ≥90% weak (≥4/4) — ACTUAL: 4/4 (100%) ✅

Key V6 findings (REP 1 ALL.zip):
  - All 8 models trigger P1 (incorrect camper count: report 568/800, expected 489)
  - All 8 models trigger P2 (wristbands reported as 0, expected 489)
  - 6/8 models trigger P3 (staff count includes AQS: report 32-42, expected 37)
  - All 8 use [CORPUS GAP] but still fail due to wrong critical data
  - V6 successfully fails ≥60% strong and ≥90% weak

================================================================================
GRADING NOTES
================================================================================

1. CRITICAL DATA POINTS (non-negotiable):
   - Campers requiring re-testing: 489 (Nonswimmer=192 + Beginner=297)
   - Carryover wristbands: 489 (same as above — Nonswimmer + Beginner)
   - Assessment-authorized staff: 37 (WSI, LGI, LG-WF at Corrigwell, current or expiring within 60 days)
   - Enrollment reconciliation: identify 264 enrollment vs 280 roster discrepancy
   - Any response with incorrect values for these figures receives the corresponding penalty

2. Partial credit (0.5) requires meaningful attempt with at least 50% of expected content

3. Zero credit for information that contradicts the source files

4. Penalty 4 (Double-counting) applies when wristband count differs from camper re-test count despite both referring to nonswimmer+beginner populations (V4 implies this — nonswimmer+beginner campers need re-tests AND carry wristbands)

5. Bonus (up to +0.5) for noting that Six-Site Sweep Report date is August 2026 (post-dates reporting cutoff of July 1, making it a forward-looking document not available at time of memo writing)

6. Scope Isolation Memo (WF2) confirms operational record is clean of credential content; operational violations (if noted) must be clearly distinguished from credential authority findings

7. RE-GRADE V7.0 CHANGES FROM V6:
   - Added independent verification of Scope Isolation Memo clean-operations claim against primary logs (C1-C3 now require primary log recompute, not memo acceptance)
   - Added enrollment-to-roster reconciliation as critical component D6 (264 enrollment vs 280 roster)
   - Strengthened [CORPUS GAP] with 4 specific categories: (a) individual camper IDs not in band counts, (b) enrollment records without classification roster row, (c) missing certification files for sibling camps, (d) any figure undervable from source files
   - Added Loon Hollow temporal qualification: must state whether clearance was at or before July 1 baseline or only later
   - Added Nonswimmer inclusion requirement: all campers whose classifications rest on defective sign-off require re-testing regardless of band level
   - Added June 15 finding date distinction: CAP clock uses June 15, 2026 (finding date), July 1 is reporting baseline only (G1)
   - Added facility inspection vs credential examination distinction: facility pass cannot substitute for credential clearance (G2)
   - Added working drafts exclusion from findings: scratch notes excluded from all numerical and filing conclusions (G3)
   - BIG TRAP: Prompt states "our preliminary count shows 280" in the re-test question. Models that trust this without verifying against band files will report 280 instead of 489. The "verify" instruction is the escape hatch.
   - Total critical components: 16 (was 13); weak model target: ≥14 of 16 failures (was ≥80% of 12-13)
   - V6 base scores preserved for reference; V7 evaluation pending next model generation against updated prompt

8. PENALTY EFFECTIVENESS (V6): Each penalty triggered independently. P1 (camper count): 8/8 models triggered (all report 568/800 vs 489). P2 (wristbands): 8/8 triggered (all report 0 vs 489). P3 (staff): 6/8 triggered (32-42 vs 37). P4 (double-counting): 8/8 triggered (campers≠wristbands or both wrong). Combined max penalty: -3.5 points. V6 penalties are MORE effective than V5 since no models used [CORPUS GAP] and all got critical data wrong.

9. PASSED VS NEVER EXAMINED COLUMNS: Summary table must have dedicated columns for Passed and Never Examined site statuses. Absence of this table format reduces B1 to 0.5 or 0.0.

10. AQS EXCLUSION: Staff count must explicitly exclude non-authorized Aquatic Safety Specialists (AQS). Including AQS or failing to exclude it reduces D4 to 0.5 or 0.0.

11. V6 TRAPS (natural language with explicit requirements): V6 requires [CORPUS GAP] marking for gaps (D5), says "based on their band classifications" (models must calculate 489 from band files, not 568 from session totals), says "Pay close attention to which specific credential roles are authorized for swim assessments" (must identify WSI/LGI/LG-WF and exclude AQS), and says "wristbands that will carry over into the 2027 season" (must realize 489 unverified campers carry over). Models that follow surface-level prompts will report 568/0/42 and fail. In V6 evaluation, 0/8 models used [CORPUS GAP], 8/8 got campers wrong, 8/8 got wristbands wrong.

12. BAND CATEGORIES (V6): V6 says "based on their band classifications" — models must derive 489 from band files (Nonswimmer=192 + Beginner=297), NOT session totals (568 or 800). V6 does NOT explicitly name Nonswimmer/Beginner bands, making derivation harder. In V6 evaluation, 0/8 models correctly identified 489 from band counts.
