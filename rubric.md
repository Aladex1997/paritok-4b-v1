KVL Compliance Memo — Rubric for Model Response Grading

Rubric Version: 5.0 (Heavy Penalties + [CORPUS GAP] + V5 natural language)
Prompt Reference: prompt.md (V5)
Target: Strong model ~75% with correct critical data (must derive from band categories, not session totals); all models with incorrect critical data FAIL
Grading Scale: 0 (absent) / 0.5 (partial) / 1.0 (full credit)

================================================================================
CRITICAL ERROR PENALTIES (apply after base scoring)
================================================================================
These penalties are applied AFTER the base score is calculated. Each penalty
is deducted from the total score. A response can score below 0 on any section.

PENALTY 1: Incorrect Camper Count [Max deduction: 1.5 points from Section D]
  - If campers requiring re-testing is reported as anything OTHER than 489
    (nonswimmer 192 + beginner 297): deduct 1.5 points from Section D total
  - Applies regardless of whether 568, 800, or any other number is reported
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
SCORING SUMMARY
================================================================================

Section A: Deliverable Format — Max 1.0
Section B: Step 1 — Defect Scope & Site Breakdown — Max 1.0
Section C: Step 2 — Clean Scope Isolation — Max 1.0
Section D: Step 3 — Re-Assessment Workload & Remediation — Max 1.5
Section E: Step 4 — July Deadline Reconciliation — Max 1.5
Section F: Data Traceability — Max 0.5
Section G: Constraint Compliance — Max 0.5

BASE MAX: 7.0

Penalty deductions (applied after base score):
  Penalty 1 (Incorrect camper count): -0.0 to -1.5
  Penalty 2 (Missing wristbands): -0.0 to -1.0
  Penalty 3 (Staff calculation error): -0.0 to -0.5
  Penalty 4 (Double-counting wristbands): -0.0 to -0.5
  Max total penalty: -3.5 points

FINAL MAX after penalties: 7.0 (with all penalties, could score as low as 3.5)

Re-Grade Results (Rubric v5.0 — [CORPUS GAP] + Heavy Penalties):

  Model  Type     Base   Penalties   Final    %     Threshold  Status
  -----  ------  -----  ----------  ------  -----  ---------  ------
  R1     STRONG   5.09      -3.50    1.59   22.7%      50%     FAIL
  R2     STRONG   5.49      -3.50    1.99   28.4%      50%     FAIL
  R3     STRONG   4.66      -3.50    1.16   16.6%      50%     FAIL
  R4     STRONG   5.09      -3.50    1.59   22.7%      50%     FAIL
  R5     WEAK     4.32      -3.50    0.82   11.7%      80%     FAIL
  R6     WEAK     4.95      -3.50    1.45   20.7%      80%     FAIL
  R7     WEAK     4.42      -3.50    0.92   13.1%      80%     FAIL
  R8     WEAK     4.03      -3.50    0.53    7.6%      80%     FAIL

  Strong avg: 21.1% | Weak avg: 13.4% — all FAIL

  Note: V5 reinstates [CORPUS GAP] requirement. Models not using [CORPUS GAP] get D5=0.0.

  Key V5 findings:
  - [CORPUS GAP] requirement explicitly stated in V5 prompt
  - Campers: ALL report 568/800 (must derive 489 from band files: 192+297)
  - Wristbands: ALL report 0 (must realize 489 carry over to 2027)
  - Staff: ALL report 32-42 (must exclude AQS to get 37)
  - Models with correct data + [CORPUS GAP] score 70-85%; all others FAIL

Threshold Rationale:
- Strong threshold (50%): Models with correct data + [CORPUS GAP] score ~75%, well above
- Weak threshold (80%): Models with correct data + [CORPUS GAP] score ~86%, above threshold
- V5 explicit requirements ([CORPUS GAP], band categories, AQS exclusion) ensure models that follow surface-level prompts will fail
- Models from folder.zip.zip (all using [CORPUS GAP]) score 56-66% — close but still FAIL due to wrong critical data

================================================================================
GRADING NOTES
================================================================================

1. CRITICAL DATA POINTS (non-negotiable):
   - Campers requiring re-testing: 489 (Nonswimmer=192 + Beginner=297)
   - Carryover wristbands: 489 (same as above — Nonswimmer + Beginner)
   - Assessment-authorized staff: 37 (WSI, LGI, LG-WF at Corrigwell, current or expiring within 60 days)
   - Any response with incorrect values for these three figures receives the corresponding penalty
   - [CORPUS GAP] marking is REQUIRED for unaccounted camper details

================================================================================
GRADING NOTES
================================================================================

1. CRITICAL DATA POINTS (non-negotiable):
   - Campers requiring re-testing: 489 (Nonswimmer=192 + Beginner=297)
   - Carryover wristbands: 489 (same as above — Nonswimmer + Beginner)
   - Assessment-authorized staff: 37 (WSI, LGI, LG-WF at Corrigwell, current or expiring within 60 days)
   - Any response with incorrect values for these three figures receives the corresponding penalty

2. Partial credit (0.5) requires meaningful attempt with at least 50% of expected content

3. Zero credit for information that contradicts the source files

4. Penalty 4 (Double-counting) applies when wristband count differs from camper re-test count despite both referring to nonswimmer+beginner populations (V4 implies this — nonswimmer+beginner campers need re-tests AND carry wristbands)

5. Bonus (up to +0.5) for noting that Six-Site Sweep Report date is August 2026 (post-dates reporting cutoff of July 1, making it a forward-looking document not available at time of memo writing)

6. Scope Isolation Memo (WF2) confirms operational record is clean of credential content; operational violations (if noted) must be clearly distinguished from credential authority findings

7. RE-GRADE V5.0 RESULTS: V5 explicitly requires [CORPUS GAP] marking (D5). Models not using [CORPUS GAP] get D5=0.0. Combined with heavy penalties for wrong critical data, all 8 models from RESPONSE 7.zip FAIL (campers 568/800, wristbands 0, staff 32-42, no [CORPUS GAP]).

8. PENALTY EFFECTIVENESS: Each penalty is triggered independently. Models reporting 568 or 800 campers (vs 489) trigger P1=-1.5. Models reporting 0 wristbands (vs 489) trigger P2=-1.0. Models reporting 32-42 staff (vs 37) trigger P3=-0.5. Double-counting P4=-0.5 when both campers and wristbands are wrong. Combined max penalty = -3.5 points, sufficient to drop any model below threshold.

9. PASSED VS NEVER EXAMINED COLUMNS: Summary table must have dedicated columns for Passed and Never Examined site statuses. Absence of this table format reduces B1 to 0.5 or 0.0.

10. AQS EXCLUSION: Staff count must explicitly exclude non-authorized Aquatic Safety Specialists (AQS). Including AQS or failing to exclude it reduces D4 to 0.5 or 0.0.

11. V5 TRAPS (natural language with explicit requirements): V5 requires [CORPUS GAP] marking for gaps, says "Base the calculation strictly on band categories...and not raw session totals" (models must calculate 489 from band files, not 568 from session logs), says "maintain clear distinctions between authorized matrix credentials (WSI, LGI, LG-WF) and unauthorized/other personnel (e.g., AQS)" (must exclude AQS), and says "wristbands that must be carried over to block enrollment for the 2027 season" (must realize 489 unverified campers carry over). Models that follow surface-level prompts will report 568/0/42 and fail.

12. BAND CATEGORIES (V5): V5 explicitly says "Base the calculation strictly on band categories (specifically combining Nonswimmer and Beginner band counts) and not raw session totals." This is a direct hint that the answer is 192+297=489, NOT session totals (568 or 800).
