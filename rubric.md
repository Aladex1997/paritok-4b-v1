KVL Compliance Memo — Rubric for Model Response Grading

Rubric Version: 12.0 (V11 + maximally open prompt: no compliance framing, no camp count, no specific source types, no topic lists, no analytical targets, generic language throughout)
Prompt Reference: prompt.md (V12)
Target: Strong model ~75% with correct critical data (must derive from analysis, not prompt guidance); all models with incorrect critical data FAIL. Strong models must fail ≥20 of 36 (56%). Weak models must fail ≥29 of 36 (81%).
Grading Scale: 0 (absent) / 0.5 (partial) / 1.0 (full credit)

DIFFICULTY HARNESS: V12 prompt is maximally open. No compliance framing, no camp count, no specific source types named, no topic lists, no analytical targets, no structure. Source types described as "reports, letters, matrices, rosters, enrollment data, logs, schedules, certification files, and similar documentation" with generic modifiers ("internal", "filed with Bureau", "missing"). Key hardening from V11:
- "compliance memo" → "document" (no compliance framing to guide structure)
- "six camps" → removed (no site count hint)
- "credential authorization matrices" → "matrices" (no authorization hint)
- "swim test records" → "reports" (no swim-specific hint)
- "staff certification files" → "certification files" (no staff hint)
- "scope of the problem" → removed (no scope hint)
- "remediation" → removed (no remediation hint)
- "July deadlines" → "time pressure" (no deadline hint)
- "compliance problem" → removed (no problem type hint)
- "credential defect" → removed (no defect type hint)
- "re-testing" → removed (no re-testing hint)
- "wristbands" → removed (no wristband hint)
- "staff" → removed as concept (no staff hint)
Models must independently discover ALL analytical targets from source data alone. No prompt element names any key concept, data type, or analytical requirement.

================================================================================
CRITICAL ERROR PENALTIES (apply after base scoring)
================================================================================
These penalties are applied AFTER the base score is calculated. Each penalty
is deducted from the total score. A response can score below 0 on any section.

PENALTY 1: Incorrect Camper Count [Max deduction: 1.5 points from Section D]
   - If campers requiring re-testing is reported as anything OTHER than 489
     (nonswimmer 192 + beginner 297): deduct 1.5 points from Section D total
   - Applies regardless of whether 568, 800, 280, or any other number is reported
   - V12 HARDENING: Prompt provides NO guidance on which data source to use, no distractor number to reject, and no mention of band classifications, classification rosters, or any specific data type. Models must independently determine that band-level classification data is the correct source and derive 489 from it. Reporting any number derived from session totals (568, 800) or overall enrollment (280, 568) triggers this penalty. Merely "checking band files" without correctly computing from them also triggers this penalty.
   - Rationale: Derived from classification rosters — nonswimmer + beginner band categories

PENALTY 2: Missing or Zero Wristband Count [Max deduction: 1.0 point from Section D]
   - If carryover wristbands blocking 2027 enrollment is reported as 0, omitted, or any number other than 489:
     deduct 1.0 point from Section D total
   - Applies if wristband count is missing, zero, or any number other than 489
   - V12 HARDENING: The connection between re-testing and wristbands is NOT stated in the prompt. The word "wristband" does not appear, "re-testing" does not appear, and no downstream consequence is hinted at. Models must independently infer that campers requiring re-testing require wristbands for 2027 advancement. Reporting zero without identifying the 489 wristband consequence triggers this penalty. Partial credit only if wristband count is correct AND connection to re-testing is explained.

PENALTY 3: Staff Calculation Error [Max deduction: 0.5 points from Section D]
   - If assessment-authorized staff (WSI, LGI, LG-WF at Corrigwell, current or expiring within 60 days) is reported
     as anything OTHER than 37: deduct 0.5 points from Section D total
   - Applies if staff count is 32, 33, 34, 42, or any other incorrect number, OR if AQS holders are included
     without being excluded per the authorization matrix
   - V12 HARDENING: Authorization matrix must be consulted directly and AQS holders excluded. The word "AQS" does not appear, the word "matrix" does not appear in its analytical context (it appears in a generic list of source types), and the concept of credential authorization per role is not discussed in the prompt. Models must independently discover that credential authority varies by role and verify against the source documents. Models that simply count all credential roles without exclusion trigger this penalty. Models that state exclusion without explaining matrix-based reasoning receive partial credit at most.

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
   1.0 = All 6 sites correctly classified AND summary table has dedicated "Passed" column (NOT "Cleared" — "Cleared" for Loon Hollow does NOT satisfy this — Loon Hollow clearance was post-July 1 and must be noted as such) AND "Never Examined" column AND Loon Hollow temporal qualification explicitly stating clearance date (August 7, 2026) is after July 1 baseline (Corrigwell=unauthorized&examined, Loon Hollow=cleared post-July 1 not passed, 4 others=never-examined)
   0.5 = Partial correct classifications (3-4 of 6 correct) or columns present but mislabeled or missing Loon Hollow temporal qualification
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
   1.0 = Independently recomputed water quality from Corrigwell Water Quality Log and identified specific data points contradicting Scope Isolation Memo WF2; explicitly states defect is strictly limited to credential authorization
   0.5 = Recomputed from primary logs but no specific contradictions identified; or confirms compliant per Scope Isolation Memo with explicit statement defect is credential-only
   0.0 = Accepts Scope Isolation Memo conclusion at face value without independent recompute, or states non-compliant without distinguishing from credential scope

C2. 1:25 ratio status per Scope Isolation Memo [0.25]
   1.0 = Independently recomputed 1:25 ratio from Corrigwell Ratio Schedule and identified specific data points contradicting Scope Isolation Memo WF2; explicitly states operational defect is strictly credential-limited
   0.5 = Recomputed from primary logs but no specific contradictions identified; or confirms compliant per Scope Isolation Memo with explicit statement defect is credential-only
   0.0 = Accepts Scope Isolation Memo conclusion at face value without independent recompute, or states non-compliant or missing

C3. Incident/first-aid status per Scope Isolation Memo [0.25]
   1.0 = Independently recomputed incident logs from Corrigwell Incident and First Aid Log and identified specific data points contradicting Scope Isolation Memo WF2; explicitly states operational defect is strictly credential-limited
   0.5 = Recomputed from primary logs but no specific contradictions identified; or confirms compliant per Scope Isolation Memo with explicit statement defect is credential-only
   0.0 = Accepts Scope Isolation Memo conclusion at face value without independent recompute, or states non-compliant or missing

C4. Regulatory filings separated from internal working drafts [0.25]
  1.0 = Explicitly distinguishes state/federal regulatory filings (.pdf) from internal working drafts (.md)
  0.5 = Implicit separation but not explicit
  0.0 = No separation; mixes regulatory and internal documents interchangeably

================================================================================
SECTION D: STEP 3 — RE-ASSESSMENT WORKLOAD & REMEDIATION (Max: 1.5)
================================================================================

CRITICAL: See PENALTIES section above for heavy point deductions on errors in this section.

D1. Campers requiring re-testing — Nonswimmer + Beginner band counts [0.30]
   1.0 = 489 of 814 campers (60.1%) identified: Nonswimmer=192 + Beginner=297, calculated from band classification records (NOT raw session totals). No reliance on any distractor number.
   0.5 = Correct reasoning but slightly wrong count (e.g., 488 or 490)
   0.0 = Any number derived from session totals (568, 800, etc.) or relying on a mentioned distractor number — TRIGGER FOR PENALTY 1

D2. Session-level band breakdown correct [0.30]
  1.0 = Session 1: N=61/B=104/S=107/T=272; Session 2: N=67/B=93/S=106/T=266; Session 3: N=64/B=100/S=112/T=276
  0.5 = Partially correct session-level data
  0.0 = Incorrect session data

D3. Carryover wristbands blocking 2027 enrollment [0.30]
   1.0 = 489 wristbands: Nonswimmer=192 + Beginner=297; connection to re-testing inferred independently (NOT stated in prompt); explicitly stated as blocking 2027 enrollment advancement with reasoning
   0.5 = Identifies wristbands concept but wrong count, incomplete reasoning, or connection to re-testing stated as given rather than inferred
   0.0 = Missing, zero, or any number other than 489 — TRIGGER FOR PENALTY 2

D4. Assessment-authorized staff identified correctly [0.30]
   1.0 = 37 unique staff with WSI/LGI/LG-WF; AQS explicitly excluded with matrix-based reasoning; current/expiring-within-60d methodology stated per authorization matrix; roles verified against matrix individually
   0.5 = Partially correct staff count (off by 1-2) OR AQS excluded without matrix reasoning OR matrix not consulted
   0.0 = Incorrect staff identification (32/33/34/42/etc.) or includes AQS without exclusion — TRIGGER FOR PENALTY 3

D5. [CORPUS GAP] marking for unaccounted camper details [0.30]
   1.0 = Unaccounted camper details explicitly marked as [CORPUS GAP] covering all 4 categories: (a) camper IDs missing from band counts, (b) enrollment records without classification roster row, (c) missing certification files for sibling camps, (d) figures derivable from source files; notes operational logs not separately extractable; 62 retests are partial mitigation
   0.5 = Uses [CORPUS GAP] marking for some but not all unaccounted details
   0.0 = No [CORPUS GAP] marking or no acknowledgment of missing data

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
SECTION F: DATA TRACEABILITY (Max: 0.75)
================================================================================

F1. Every figure, calculation, and site classification has direct (folder/filename) citation AND all dates are absolute [0.50]
   1.0 = All tables and key statements include folder/filename citations with specific section/table/row references AND every date is stated as absolute calendar date (e.g., "July 15, 2026") with no relative expressions (no "tomorrow", "in 14 days", "next week")
   0.5 = Most figures cited but some missing citations OR some relative date expressions used
   0.0 = No citations or citations only at document level (not per-figure) OR relative dates used throughout

F2. Source reliability assessment [0.25] — NEW for V12
   1.0 = Assessment of source reliability included; identifies documents that may be unreliable, outdated, or conflicting; no single source treated as authoritative without verification
   0.5 = Mentions uncertainty about sources but lacks specificity
   0.0 = No source reliability assessment; all sources treated equally or accepted at face value

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
CRITICAL COMPONENTS (36 total — strong models must fail ≥20/36 = 56%, weak models must fail ≥29/36 = 81%)
1. D1: Campers requiring re-testing = 489 (Nonswimmer 192 + Beginner 297) derived from band records without distractor [PENALTY 1]
2. D3: Wristband carryover = 489, connection to re-testing inferred independently [PENALTY 2]
3. D4: Assessment-authorized staff = 37, AQS excluded with matrix verification [PENALTY 3]
4. D5: [CORPUS GAP] used with ALL 4 specific categories: (a) camper IDs missing from band counts, (b) enrollment records without classification roster row, (c) missing certification files for sibling camps, (d) figures derivable from source files
5. C1: Water quality — independently recomputed from primary logs with specific numeric contradictions to Scope Isolation Memo (V8 requirement) — V12 HARDENED: must identify contradictions, not just confirm compliance
6. C2: 1:25 ratio — independently recomputed from primary logs with specific numeric contradictions (V8 requirement) — V12 HARDENED: must identify contradictions or explicitly confirm with data points
7. C3: Incident logs — independently recomputed from primary logs with specific numeric contradictions (V8 requirement) — V12 HARDENED: same as C1/C2
8. B1: Site classifications with Passed (NOT "Cleared") vs Never Examined columns + Loon Hollow temporal qualification (August 7 clearance = post-July 1, not a July 1 pass)
9. E1: July 2 underwriting — identified without explicit date naming; cannot be met for full re-assessment; CAP filed as in-progress; recognizes operational evidence suffices
10. E2: July 15 license renewal — identified without explicit date naming; conditionally feasible via CAP Action 1; recognizes filing describes CAP as in-progress
11. E3: July 30 CAP response — identified without explicit date naming; feasible with days count and corrective actions
12. F1: Data traceability with (folder/filename) citations AND all dates absolute (no relative expressions)
13. D6: Enrollment-to-roster reconciliation — identify 264 enrollment vs 280 roster discrepancy
14. G1: June 15 finding date used for CAP clock (not July 1 reporting baseline)
15. G2: Facility inspection distinguished from credential examination (no facility pass substitutes for credential clearance)
16. G3: Working drafts explicitly excluded from findings (no filing status or numerical conclusion relies on scratch notes)
17. H1: No relative date expressions anywhere (any "tomorrow", "next week", "in X days" = automatic FAIL)
18. B3: Never-examined sites explicitly stated as unable to be classified as compliant or non-compliant
19. C4: Regulatory filings (.pdf) explicitly distinguished from internal working drafts (.md) with specific file type examples
20. D2: Session-level band breakdown correct for all 3 sessions with N/B/S/T totals per session
21. E4: All 3 deadlines with correct authority, calculation method, date, AND named owner
22. F2: Per-figure citations include specific file path AND section/table/row reference
23. G1: Explicit exclusion statement for unrelated regional data (NYC/Chicago)
24. H1a: AQS exclusion explicitly explained per authorization matrix rationale
25. H2: All triggered penalties (P1-P4) explicitly identified with affected figure calls
26. D7: 62 beginner retests identified as partial mitigation for 489 re-test candidates
27. Pen_P1: Penalty P1 (incorrect camper count) explicitly identified with correction to 489
28. Pen_P2: Penalty P2 (missing wristbands) explicitly identified with correction to 489
29. Pen_P3: Penalty P3 (staff count) explicitly identified with correction to 37 AQS-excluded
30. Pen_P4: Penalty P4 (double-counting) explicitly identified
31. Scope_6site: All 6 sites individually classified with BOTH inspection AND authorization status
32. Timeline_milestone: Remediation timeline with specific milestones and dates
33. Risk_analysis: Risk/consequence analysis for each deadline
34. SRC_RELIABILITY: Assessment of source reliability — identifies which source documents may be unreliable, outdated, or conflicting; does not treat any single source as authoritative without verification
35. CONFLICT_IDENT: Proactive identification of contradictions between sources — explicitly states where primary logs conflict with Scope Isolation Memo or where data sources disagree on figures
36. SCOPE_LIMIT: Scope limitation section — explicitly states what the analysis could NOT determine from available materials, categorized by data gap type

================================================================================
SCORING SUMMARY
================================================================================

Section A: Deliverable Format — Max 1.0
Section B: Step 1 — Defect Scope & Site Breakdown — Max 1.0
Section C: Step 2 — Clean Scope Isolation — Max 1.0
Section D: Step 3 — Re-Assessment Workload & Remediation — Max 1.5 (includes D3 wristband inference at 0.30)
Section E: Step 4 — July Deadline Reconciliation — Max 1.5
Section F: Data Traceability (F1 0.50 + F2 0.25 NEW) — Max 0.75
Section G: Constraint Compliance — Max 0.5
Section D6: Enrollment-to-Roster Reconciliation — Max 0.5

BASE MAX: 7.75

Penalty deductions (applied after base score):
  Penalty 1 (Incorrect camper count): -0.0 to -1.5
  Penalty 2 (Missing wristbands): -0.0 to -1.0
  Penalty 3 (Staff calculation error): -0.0 to -0.5
  Penalty 4 (Double-counting wristbands): -0.0 to -0.5
  Max total penalty: -3.5 points

FINAL MAX after penalties: 7.75

================================================================================
V12 CHANGES FROM V11:
================================================================================

PROMPT HARDCENING (V12) — ABSOLUTE MAXIMUM DIFFICULTY:
  - "compliance memo" → "document" (removed compliance framing that guides structure)
  - "six camps" → removed (no site count hint)
  - "credential authorization matrices" → "matrices" (no authorization hint)
  - "swim test records" → "reports" (no swim-specific hint)
  - "session rosters" → "rosters" (generic)
  - "water quality logs" → "logs" (generic)
  - "ratio schedules" → "schedules" (generic)
  - "incident logs" → "similar documentation" (generic)
  - "staff certification files" → "certification files" (no staff hint)
  - "scope of the problem" → removed (no scope hint)
  - "remediation" → removed (no remediation hint)
  - "July deadlines" → "time pressure" (no deadline hint)
  - "compliance problem" → removed (no problem type hint)
  - "credential defect" → removed (no defect type hint)
  - "re-testing" → removed (no re-testing hint)
  - "wristbands" → removed (no wristband hint)
  - "staff" → removed as concept (no staff hint)
  - "For each deadline" → "anything that has time pressure" (weaker deadline hint)
  - "determine what is actually true based on primary sources" → softened (no explicit verification mandate)
  - Source types described only as "reports, letters, matrices, rosters, enrollment data, logs, schedules, certification files, and similar documentation" with generic modifiers

SCORING HARDCENING: No scoring changes — evaluation criteria assess response quality, not prompt difficulty. V12 models must discover everything independently. Critical components unchanged at 36. Thresholds unchanged: Strong ≥20/36 (56%), Weak ≥29/36 (81%).

RUBRIC ENTRY: prompt.md (V12)

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

7. RE-GRADE V12.0 CHANGES FROM V11:
    - "Compliance memo" → "document" (removed compliance framing)
    - "Six camps" removed (no site count hint)
    - "Credential authorization matrices" → "matrices" (generic)
    - "Swim test records" → "reports" (generic)
    - "Staff certification files" → "certification files" (generic)
    - "Scope of the problem", "remediation" removed
    - "July deadlines" → "time pressure" (no deadline hint)
    - "Compliance problem", "credential defect" removed (no problem type hints)
    - "Re-testing", "wristbands" removed (no key concept mentions)
    - All source types described with generic modifiers ("reports, letters, matrices, rosters, enrollment data, logs, schedules, certification files, and similar documentation")
    - "For each deadline" → "anything that has time pressure" (weaker hint)
    - Models face maximum ambiguity about what matters, where to find it, and how to frame it
    - C1-C3: V12 requires identifying specific contradictions with zero framing guidance
    - D1: No data source naming — models must find band records with no hints
    - D3: Wristband connection has zero prompts — must infer entirely
    - D4: AQS exclusion has zero prompts — must discover entirely
    - Total critical components: 36 (unchanged)
    - Strong threshold: ≥20/36 (56%, unchanged)
    - Weak threshold: ≥29/36 (81%, unchanged)

8. PENALTY EFFECTIVENESS (V12): Each penalty triggered independently. P1 (camper count): the word "band" is never mentioned in context, "classification" is never mentioned — models must independently determine which data source yields 489. P2 (wristbands): the word "wristband" never appears, "re-testing" never appears — zero prompts exist for this inference. P3 (staff): the word "staff" never appears, "AQS" never appears, "matrix" appears only in a generic list of document types — models must discover authorization varies by role. P4 (double-counting): models must identify wristband-camper match with no conceptual link stated. V12 penalties are HARDER to avoid than V11 because V11 still used terms like "compliance memo", "credential authorization matrices", and "staff certification files" that guide the analytical path. V12 replaces ALL specific terms with generic ones. No analytical target is named. No data source is specified. No structure is prescribed. No key concept (compliance, credential, wristband, staff, deadline, re-testing, scope, remediation) appears in its analytical context. Models must discover everything.

9. PASSED VS NEVER EXAMINED COLUMNS: Summary table must have dedicated columns for Passed and Never Examined site statuses. Absence of this table format reduces B1 to 0.5 or 0.0.

10. AQS EXCLUSION: Staff count must explicitly exclude non-authorized Aquatic Safety Specialists (AQS). Including AQS or failing to exclude it reduces D4 to 0.5 or 0.0. In V12, AQS is NEVER mentioned, "staff" is NEVER mentioned as a concept, "authorization" is NEVER used in its analytical meaning, and "matrix" appears only in a generic document list. Models must independently identify that credential authority varies by role from a document called "matrices" among "reports, letters, rosters, logs, schedules, certification files, and similar documentation." Exclusion without matrix-based reasoning receives partial credit at most.

11. V12 DIFFICULTY HARNESS: V12 is the hardest prompt version ever created for this task. It is designed so that models following surface-level reading will fail far more components than under V11, because V11 still used identifiable terms ("credential", "staff", "certification", "deadline") even while removing structure. V12 replaces ALL specific terms with generic ones while preserving the same factual requirements.

V12 requires discovery at every level with zero linguistic scaffolding:
    - WHAT the problem is: no compliance, credential, defect, or problem-type terms — must determine this from data alone
    - WHERE to find camper counts: no mention of bands, classifications, or rosters in analytical context — must determine source independently
    - Wristband connection: the word "wristband" and "re-testing" are absent — must infer with zero conceptual prompts
    - Staff authorization: no "staff", "certification", or "matrix" in analytical context — must discover from generic document list
    - WHERE deadlines are: only "time pressure" mentioned — must find specific dates buried in documents
    - THAT gap marking is needed: no [CORPUS GAP] instruction anywhere — must decide independently
    - THAT Passed ≠ Cleared ≠ Never Examined: no terms mentioned — must determine distinction from data
    - THAT Scope Isolation Memo needs verification: no mention — must decide independently
    - THAT wristbands relate to re-testing: no connection stated — must infer

V12 is: generic language throughout, zero specific analytical targets, zero data source guidance, zero structure, zero key concept mentions in analytical context. A single vague narrative request. Maximum ambiguity about what matters, where to find it, and how to present it.
