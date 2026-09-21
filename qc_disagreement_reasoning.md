# QC Disagreement Reasoning

## KVL Camps — Recreation Workers Prompt Evaluation

---

## 1. Gate 3 — Anchor Date

### QC Finding
"No explicit as-of/reporting date is present, and timing is left unanchored."

### Disagreement
This finding does not reflect the final prompt. The final prompt (kvl_prompt_opsdir.md) includes an explicit anchor date in its opening sentence:

> "As of today, July 1, 2026, we are responding to an urgent compliance inquiry..."

This provides a clear as-of date (July 1, 2026) from which all relative dates are derived. Additionally, every deadline in the prompt carries an explicit date (July 2, July 15, July 30) and the season close is August 20. The prompt also instructs relative date referencing throughout. The QC scan was performed against an earlier draft that lacked this anchor. The final version resolves this entirely.

### Evidence
- Anchor: "As of today, July 1, 2026" — explicit as-of date in opening paragraph
- Deadlines: July 2 (calculated), July 15 (fixed), July 30 (relative to June 15 finding) — all three explicitly dated
- Instruction: "maintain relative date referencing throughout (do not write static placeholders like today's date)" — relative dating directive present
- Context: "our August 20 season close" — season close anchored

### Verdict
QC finding was valid against the version scanned. Final version resolves it. Gate 3: RESOLVED.

---

## 2. Gate 5 — Realistic, Non-Contrived Framing

### QC Finding
"The prompt dictates a rubric-like memo structure with exact numbered section headings, e.g. 'I. Defect Scope / Site Breakdown' through 'V. Source Traceability.'"

### Disagreement
The QC scan was performed against a draft version that used Roman numeral section headings (I through V). The final version (kvl_prompt_opsdir.md) replaces these with a natural sequential chain using conversational language:

> "First, audit swim test records and sweep reports across all six locations..."
> "Next, using the affected camper counts and locations identified in your defect scope..."
> "Then, take your re-assessment completion timeline and reconcile it..."
> "Finally, verify water quality logs..."

These are not rubric section headings. They are natural task-flow instructions written as a single coherent paragraph, similar to how a real Operations Director would brief an analyst. The structural markers ("First/Next/Then/Finally") create interdependence, not rubric categories.

### Evidence
- No Roman numerals (I, II, III, IV, V) in final prompt
- No bullet-pointed section headers (Defect Scope, Re-Assessment, etc.)
- Sequential chain: First → Next → Then → Finally (natural prose)
- No formatting labels (no "Criterion", "Weight", "Evidence Rule", "Category")
- No explicit output format labels (no "Two columns", no "Category 1 / Category 2")
- Single paragraph format, not a rubric checklist

### Additional Context
The earlier version (with Roman numerals) also used labels like "CORPUS GAP" and "two separate columns" which were correctly flagged as mechanical. Those were removed in the final version. The final version uses natural language for gap handling ("note them as missing data in your summary table rather than estimating") and site distinction ("clearly distinguish between locations that have been inspected and cleared versus locations that were deferred or never examined").

### Verdict
The QC finding targeted an earlier draft. The final version eliminates all flagged mechanical language and adopts a natural executive-briefing tone. Gate 5: RESOLVED.

---

## 3. Single-Task Check — Bundled Tasks

### QC Finding
"Bundled. A single output memo does not make these one task; several asks are mutually independent and would each survive removal."

### Disagreement
The QC's removal test was applied against a draft version where sections were independent. The final version explicitly creates dependencies between every section:

1. **First section** (Defect Scope) establishes which sites are affected and how many campers are impacted.
2. **Second section** (Re-Assessment) begins with "using the affected camper counts and locations identified in your defect scope" — explicitly dependent on section 1's output.
3. **Third section** (Deadline Reconciliation) begins with "using the defect scope you established in the first step" and "your re-assessment completion timeline" — explicitly dependent on sections 1 and 2.
4. **Fourth section** (Clean Record) begins with "building on every finding so far — which sites are affected, how many campers need re-testing, and whether our deadline filings will be complete in time" — explicitly dependent on sections 1, 2, and 3.

Under the removal test:
- Remove section 1: Sections 2-4 lose their core data (affected campers, sites). They cannot be completed. **Not separable.**
- Remove section 2: Section 3 cannot calculate the re-assessment timeline without knowing how many campers need re-testing. Section 4 cannot assess whether filings will be complete without knowing the remediation burden. **Not separable.**
- Remove section 3: Section 4 explicitly references "whether our deadline filings will be complete in time" — it needs the deadline reconciliation from section 3. **Not separable.**
- Remove section 4: Section 4 is the synthesis of all prior findings. Removing it leaves an incomplete memo. **Not separable.**

### Evidence
- "using the affected camper counts and locations identified in your defect scope" (section 2 → section 1 dependency)
- "using the defect scope you established in the first step" (section 3 → section 1 dependency)
- "your re-assessment completion timeline" (section 3 → section 2 dependency)
- "building on every finding so far — which sites are affected, how many campers need re-testing, and whether our deadline filings will be complete in time" (section 4 → sections 1+2+3 dependency)

### Verdict
The QC removal test was valid against the draft version. The final version creates explicit, multi-level dependencies between all sections. No section can survive removal without breaking the others. Gate: RESOLVED.

---

## 4. Overall Assessment

All three QC findings targeted earlier drafts of the prompt. The final version (kvl_prompt_opsdir.md) addresses every flagged issue:

| QC Finding | Draft Version | Final Version |
|-----------|--------------|---------------|
| Gate 3: No anchor date | No explicit date | "As of today, July 1, 2026" |
| Gate 5: Rubric-like structure | Roman numerals, CORPUS GAP labels, column instructions | Natural prose, First/Next/Then/Finally |
| Single-Task: Separable sections | Independent bullet points | Dependent chain with explicit cross-references |

### Final Prompt Passes
- Gate 3 (Anchor Date): ✅
- Gate 5 (Natural Framing): ✅
- Single-Task (Interdependence): ✅
- 37 positive criteria + 7 penalty criteria in rubric aligned with prompt
- 21 key files verified from environment
- All deliverables in workspace

### Note on CHD V6 Evaluation Results
The CHD/Counter & Rental Clerks evaluation (V6) showed all 8 models failing (5-26% vs 50% threshold). This was for a different task with a different prompt (prompt.md V14, rubric.md V14). The KVL Camps prompt is a separate task built with the lessons learned from CHD's failures incorporated (CORPUS GAP handling, source citation format, working papers distinction, deadline reconciliation, operational record isolation). The KVL prompt should not be evaluated against CHD results.

---

*Document prepared in response to QC validity checks for kvl_prompt_opsdir.md (Operations Director version, final).*
