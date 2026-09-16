# KVL Camps — Recreation Workers

## Prompt

**Role**: You are a Senior Compliance Analyst at KVL Camps, a nonprofit operator of six aquatics-centered summer camps (Corrigwell, Loon Hollow, Tamarack Ridge, Bluegill Point, Heron Landing, Otter Run) serving ~4,800 campers per season across the mid-Atlantic lake country. The camp's waterfront operations are the core of the program — every camper meets the water on day one. The current season closes on 2026-08-20.

**Context**: The Bureau of Youth Camp Licensing issued a finding letter on 2026-06-15 (reference: CF-2026-KVL-014) identifying a **credential-authority defect** at Camp Corrigwell. The finding states that swim-ability assessments signed by a Corrigwell staff member since spring 2022 may not have been authorized under the camp's credential-authorization matrix. Specifically, the individual held a valid lifeguarding credential (LG-DW) but the matrix indicates the **AQS (Aquatics Supervisor)** track is not assessment-authorized — meaning the signer's credential track does not cover the duty of certifying swim-ability classifications. This is a credential-authority problem, not an operational one: water-quality logs, 1:25 guard ratios, and incident records are all in order for 2022–2025. The camp must respond with a corrective action plan and resolve the classification chain for affected campers before the season closes.

**Task**: Produce a **Compliance Response Memo** addressed to the Bureau of Youth Camp Licensing (findings unit) that:

1. **Identifies the scope of the defect**: Determine which campers at Camp Corrigwell were classified (nonswimmer / beginner / swimmer band assignment) by the unauthorized signer since spring 2022, using the Corrigwell Swim Classification Rosters (2022–2026) and the Corrigwell Lifeguard Certification Files to verify the signer's credential track and expiry status at each classification event. Report the total count of affected campers by year and by current band classification.

2. **Assesses re-assessment feasibility**: Using the Session Calendar and Enrollment workbook (2026), the Corrigwell Swim Test Summary (2026), and the Band Counts by Session (2026), determine how many currently-enrolled 2026 campers require re-assessment, how many 2025 swimmers carry bands that would gate 2027 enrollment, and what the re-assessment timeline would be given the season closes 2026-08-20. Note: re-assessment must be performed by credential-authorization-approved WSI/LGI staff — reference the Credential Validity Quick Reference for required credential codes and validity periods.

3. **Reconciles three conflicting July deadlines** and presents a unified action calendar:
   - **Underwriting documentation** (Great Pines Mutual): 30 days before the 08/01/2026 policy anniversary → due **2026-07-02**
   - **License renewal application** (Bureau Licensing Unit): fixed date **2026-07-15** — must describe CAP-2026-01 as in-progress with its action table
   - **Corrective action plan response** (Bureau findings unit): 45 days from the 2026-06-15 finding letter → due **2026-07-30**
   
   The renewal application must describe an in-progress CAP; do not delay filing for CAP closure. Present a day-by-day calendar for July showing which deliverable is due when, who owns each (Risk/Compliance for CAP, Licensing for application, Underwriting for UW packet), and escalation triggers for conflicts.

4. **Documents the operational record isolation**: Explicitly confirm that the operational record (water quality logs, ratio schedules, incident/first-aid logs for Corrigwell 2022–2026) contains no credential-content fields and therefore carries no finding. State clearly that the credential record and the operational record answer different questions and that the clean operational record cannot be inflated or dragged into the defect, nor can it be used to impeach the finding.

5. **Provides a six-site sweep summary**: Reference the Six-Site Credential Sweep Report (2026) and summarize findings across all six camps (Corrigwell, Loon Hollow, Tamarack Ridge, Bluegill Point, Heron Landing, Otter Run). Note which sites were examined and which were not (budget decision), and confirm whether the Corrigwell defect is isolated or systemic.

**Constraints & Deliverables**:
- Output as a structured memo with sections matching the five task areas above
- All dates must use relative dating consistent with the 2026 season timeline (do not assume a fixed current date; anchor to the 2026-08-20 season close)
- Any question the corpus cannot answer (e.g., specific camper identity, or details about the signer's hiring authority process) must be explicitly flagged as **[CORPUS GAP — not answerable from available documents]** rather than inferred
- Cite specific source files for each factual claim using the format: `(source: folder/filename)`
- The memo must distinguish between **confirmed findings** (data-supported), **operational status** (clean record), and **compliance gaps** (action required)

**What makes this hard**: The longest documents in the environment (annual confirmation batch, billing records) are not the ones that decide the answer. The key files are smaller, scattered across 7 folders, and some deliberately misleading files (public Federal Register documents, NYC/Chicago park data) look like they could be relevant but contain no camp-specific information. Models that skim will gravitate toward the wrong files. The second step (re-assessment feasibility) depends entirely on correctly completing the first step (identifying affected campers).

**Target difficulty**: Moderate. The answer requires joining 3–4 specific file types across different folders, reconciling conflicting deadline precision (relative vs. fixed dates), and flagging corpus gaps rather than inventing answers.
