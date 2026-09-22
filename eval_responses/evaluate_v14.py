import json
import re

with open('eval_responses/response_texts.json') as f:
    responses = json.load(f)

COMPONENTS = [
    "D1: Re-testing=489 from band records",
    "D3: Wristband=489 inferred",
    "D4: Staff=37, AQS excluded",
    "D5: CORPUS GAP all 4 categories",
    "C1: Water quality cross-referenced",
    "C2: 1:25 ratio cross-referenced",
    "C3: Incident logs cross-referenced",
    "B1: Site Passed/Never Examined",
    "E1: July 2 underwriting infeasible",
    "E2: July 15 license conditionally feasible",
    "E3: July 30 CAP feasible",
    "F1: Citations + absolute dates",
    "D6: Enrollment vs 280 roster gap=264",
    "G1: June 15 CAP clock date",
    "G2: Facility vs credential distinction",
    "G3: Working drafts excluded",
    "H1: No relative dates",
    "B3: Never-examined unclassifiable",
    "C4: Regulatory(.pdf) vs working(.md)",
    "D2: Session band breakdown N/B/S/T",
    "E4: Deadline owners+methods+dates",
    "F2: Per-figure path+section refs",
    "G1b: NYC/Chicago exclusion",
    "H1a: AQS exclusion matrix rationale",
    "H2: Penalties P1-P4 identified",
    "D7: 62 beginner retests partial mitigation",
    "Pen_P1: P1 identified+corrected to 489",
    "Pen_P2: P2 identified+corrected to 489",
    "Pen_P3: P3 identified+corrected to 37",
    "Pen_P4: P4 double-counting identified",
    "Scope_6site: All 6 sites inspection+auth",
    "Timeline_milestone: Milestones+dates",
    "Risk_analysis: Risk per deadline",
    "SRC_RELIABILITY: Source reliability assessment",
    "CONFLICT_IDENT: Contradictions between sources",
    "SCOPE_LIMIT: What analysis cannot conclude",
]


def score_component(text, comp_idx):
    t = text.upper()
    tl = text.lower()

    if comp_idx == 0:
        has_489 = bool(re.search(r'\b489\b', text))
        has_nb = bool(re.search(r'Nonswimmer', text)) and bool(re.search(r'Beginner', text))
        has_band = bool(re.search(r'band', tl))
        has_800or568 = bool(re.search(r'\b(568|800)\b', text))
        if has_489 and has_nb and has_band and not has_800or568:
            return "PASS", "489 Nonswimmer+Beginner from band records"
        elif has_800or568 and not has_489:
            return "FAIL", "Reports 568/800 instead of 489"
        else:
            return "FAIL", "Missing 489 or band breakdown"

    if comp_idx == 1:
        has_489 = bool(re.search(r'\b489\b', text))
        has_wristband = bool(re.search(r'wristband', tl))
        has_inferred = bool(re.search(r'infer|derive|conclude|deduc|figure out|work out|connect|not stated|not mentioned|not in prompt', tl))
        if has_489 and has_wristband:
            return "PASS", "489 wristbands identified"
        else:
            return "FAIL", "Missing 489 wristband"

    if comp_idx == 2:
        has_37 = bool(re.search(r'\b37\b', text))
        has_aqs_excl = bool(re.search(r'AQS', text)) and bool(re.search(r'excl|not.*have|exclude|without|excluded', tl))
        has_matrix = bool(re.search(r'matrix', tl))
        if has_37 and has_aqs_excl and has_matrix:
            return "PASS", "37 staff, AQS excluded via matrix"
        elif has_37 and has_aqs_excl:
            return "FAIL", "37 staff, AQS excluded but no matrix rationale"
        elif has_37:
            return "FAIL", "37 identified but AQS not excluded"
        else:
            return "FAIL", "Staff count wrong or AQS not excluded"

    if comp_idx == 3:
        has_gap = bool(re.search(r'CORPUS GAP', text))
        has_ids = bool(re.search(r'camper.*ID|ID.*missing|missing.*ID|missing.*camper', tl))
        has_enroll = bool(re.search(r'enroll', tl))
        has_cert = bool(re.search(r'certif', tl))
        if has_gap and has_ids and has_enroll and has_cert:
            return "PASS", "CORPUS GAP all 4 categories"
        elif has_gap:
            return "FAIL", "CORPUS GAP but not all 4 categories"
        else:
            return "FAIL", "No CORPUS GAP marking"

    if comp_idx == 4:
        has_water = bool(re.search(r'water|chlorine', tl))
        has_contradict = bool(re.search(r'contradict|disagree|conflict|gap|differ|below|breach', tl))
        has_recompute = bool(re.search(r'recomput|recheck|verify|re-verif', tl))
        has_scope = bool(re.search(r'scope.*isol|isolat|WF2', tl))
        if has_water and has_contradict and has_recompute:
            return "PASS", "Water recomputed + contradictions"
        elif has_water and has_scope and has_contradict:
            return "FAIL", "Water + Scope Isolation but contradictions not verified"
        elif has_water and has_contradict:
            return "FAIL", "Water contradictions found but no recompute from logs"
        else:
            return "FAIL", "Water quality not verified"

    if comp_idx == 5:
        has_ratio = bool(re.search(r'1:25|ratio|buddy', tl))
        has_contradict = bool(re.search(r'contradict|disagree|conflict|gap|differ|breach|below|exceed', tl))
        has_recompute = bool(re.search(r'recomput|recheck|verify|re-verif', tl))
        if has_ratio and has_contradict:
            return "PASS", "1:25 ratio checked + contradictions"
        elif has_ratio and has_recompute and has_contradict:
            return "PASS", "1:25 recomputed + contradictions"
        elif has_ratio:
            return "FAIL", "1:25 ratio mentioned but no contradictions identified"
        else:
            return "FAIL", "1:25 ratio not addressed"

    if comp_idx == 6:
        has_incident = bool(re.search(r'incident|first.?aid|injur', tl))
        has_contradict = bool(re.search(r'contradict|disagree|conflict|gap|differ|without follow', tl))
        if has_incident and has_contradict:
            return "PASS", "Incident logs checked + contradictions"
        elif has_incident:
            return "FAIL", "Incidents mentioned but no cross-reference"
        else:
            return "FAIL", "Incident logs not addressed"

    if comp_idx == 7:
        has_passed = bool(re.search(r'\bPassed\b', text))
        has_never = bool(re.search(r'Never.?Examined|never.?examined', text))
        has_loon_temporal = bool(re.search(r'August.?7|post.?July|after.*July|later.*July', tl))
        has_6sites = all(s in text for s in ['Corrigwell', 'Loon', 'Tamarack', 'Bluegill', 'Heron', 'Otter'])
        has_cleared = bool(re.search(r'\bCleared\b', text))
        if has_passed and has_never and has_loon_temporal:
            return "PASS", "Passed+Never Examined+Loon temporal"
        elif has_passed and has_never and has_6sites and not has_cleared:
            return "FAIL", "All 6 sites but missing Loon temporal qualification"
        elif has_cleared and not has_passed:
            return "FAIL", "Uses 'Cleared' instead of 'Passed'"
        else:
            return "FAIL", "Missing Passed/Never Examined distinction"

    if comp_idx == 8:
        has_july2 = bool(re.search(r'July\s*2|July\s*0?2', text))
        has_infeasible = bool(re.search(r'infeasible|cannot.*full|not.*feasib|not.*complete|too.*late|insufficient.*time', tl))
        has_cap = bool(re.search(r'CAP|filing|file', tl))
        if has_infeasible and has_cap:
            return "PASS", "July 2 infeasible + CAP filing"
        elif has_july2 and has_infeasible:
            return "FAIL", "July 2 infeasible but no CAP filing"
        else:
            return "FAIL", "July 2 underwriting not addressed"

    if comp_idx == 9:
        has_july15 = bool(re.search(r'July\s*15|July\s*0?15', text))
        has_conditional = bool(re.search(r'condit|possible|may|could|potent', tl))
        has_cap_action = bool(re.search(r'CAP.*Action|Action.*1|action.*1|Action 1', tl))
        if has_july15 and has_conditional and has_cap_action:
            return "PASS", "July 15 conditional + CAP Action 1"
        elif has_july15 and has_conditional:
            return "FAIL", "July 15 conditional but no CAP Action 1"
        else:
            return "FAIL", "July 15 license not addressed"

    if comp_idx == 10:
        has_july30 = bool(re.search(r'July\s*30|July\s*0?30', text))
        has_feasible = bool(re.search(r'feasib|can|able|will have|remaining|days', tl))
        has_days = bool(re.search(r'\d+\s*days?|day.*remain|days.*left', tl))
        if has_feasible and has_days:
            return "PASS", "July 30 feasible + day count"
        elif has_july30 and has_feasible:
            return "FAIL", "July 30 feasible but no day count"
        else:
            return "FAIL", "July 30 CAP not addressed"

    if comp_idx == 11:
        has_citation = bool(re.search(r'\[.*S\d|Folder|folder', text))
        has_abs_date = bool(re.search(r'July \d+, 2026|August \d+, 2026|June \d+, 2026|September \d+, 2026', text))
        has_relative = bool(re.search(r'tomorrow|next week|in \d+ days|in \d+ week', tl))
        if has_citation and has_abs_date and not has_relative:
            return "PASS", "Citations + absolute dates"
        elif has_citation and has_abs_date:
            return "FAIL", "Citations + absolute dates but also relative"
        elif has_citation:
            return "FAIL", "Citations but no absolute dates"
        else:
            return "FAIL", "No per-figure citations"

    if comp_idx == 12:
        has_264 = bool(re.search(r'\b264\b', text))
        has_enroll = bool(re.search(r'enroll', tl))
        has_roster = bool(re.search(r'roster', tl))
        if has_264 and has_enroll and has_roster:
            return "PASS", "264 enrollment vs 280 roster gap"
        elif has_enroll and has_roster:
            return "FAIL", "Enrollment/roster mentioned but no 264 gap"
        else:
            return "FAIL", "Enrollment reconciliation missing"

    if comp_idx == 13:
        has_june15 = bool(re.search(r'June\s*15|June\s*0?15', text))
        if has_june15:
            return "PASS", "June 15 date identified"
        else:
            return "FAIL", "June 15 not identified"

    if comp_idx == 14:
        has_facility = bool(re.search(r'facilit|inspect|inspection', tl))
        has_credential = bool(re.search(r'credential|certif', tl))
        has_distinction = bool(re.search(r'distinguish|separate|different|not.*same|no.*substitut', tl))
        if has_facility and has_credential and has_distinction:
            return "PASS", "Facility vs credential distinguished"
        elif has_facility and has_credential:
            return "FAIL", "Both mentioned but not distinguished"
        else:
            return "FAIL", "Facility/credential distinction missing"

    if comp_idx == 15:
        has_draft = bool(re.search(r'draft|scratch|working', tl))
        has_exclude = bool(re.search(r'excl|exclude|not.*use|omit|not.*rely', tl))
        if has_draft and has_exclude:
            return "PASS", "Working drafts excluded"
        elif has_draft:
            return "FAIL", "Working drafts mentioned but not excluded"
        else:
            return "FAIL", "Working drafts not addressed"

    if comp_idx == 16:
        has_relative = bool(re.search(r'tomorrow|next week|in \d+\s*(day|week|month)', tl))
        if has_relative:
            return "FAIL", "Contains relative date expressions"
        else:
            return "PASS", "No relative dates"

    if comp_idx == 17:
        has_never = bool(re.search(r'Never.?Examined|never.?examined', text))
        has_unclassifiable = bool(re.search(r'unable.*classif|cannot.*classif|not.*classif|cannot.*compliant|not.*compliant|no.*determin', tl))
        if has_never and has_unclassifiable:
            return "PASS", "Never-examined stated as unclassifiable"
        elif has_never:
            return "FAIL", "Never-examined mentioned but not as unclassifiable"
        else:
            return "FAIL", "Never-examined not addressed"

    if comp_idx == 18:
        has_pdf = bool(re.search(r'\.pdf|pdf|regulatory.*fil', tl))
        has_md = bool(re.search(r'\.md|markdown|working.*draft|internal.*draft', tl))
        has_distinction = bool(re.search(r'distinguish|separate|different|not.*same|type', tl))
        if has_pdf and has_md and has_distinction:
            return "PASS", "Regulatory PDF vs working MD distinguished"
        elif has_pdf and has_md:
            return "FAIL", "Both types mentioned but not distinguished"
        else:
            return "FAIL", "File type distinction missing"

    if comp_idx == 19:
        has_session = bool(re.search(r'Session\s*\d', text))
        has_n = bool(re.search(r'N\s*=\s*\d+|N=\d+', text))
        has_b = bool(re.search(r'B\s*=\s*\d+|B=\d+', text))
        has_s = bool(re.search(r'S\s*=\s*\d+|S=\d+', text))
        has_t = bool(re.search(r'T\s*=\s*\d+|T=\d+', text))
        if has_session and has_n and has_b and has_s and has_t:
            return "PASS", "Session band breakdown N/B/S/T"
        else:
            return "FAIL", "Session band breakdown incomplete"

    if comp_idx == 20:
        has_owner = bool(re.search(r'Great Pines|Bureau|Licensing|Bureau Findings', tl))
        has_date = bool(re.search(r'July\s*\d', text))
        has_method = bool(re.search(r'calcul|method|determine|based.*on|derived', tl))
        if has_owner and has_date and has_method:
            return "PASS", "Owners + dates + methods"
        else:
            missing = []
            if not has_owner: missing.append("owners")
            if not has_date: missing.append("dates")
            if not has_method: missing.append("methods")
            return "FAIL", f"Missing: {', '.join(missing)}"

    if comp_idx == 21:
        has_path = bool(re.search(r'\[.*S\d|Folder|folder|/.*[/\.]', text))
        has_section = bool(re.search(r'section|row|table|page', tl))
        if has_path and has_section:
            return "PASS", "File path + section/row refs"
        elif has_path:
            return "FAIL", "File refs but no section/row detail"
        else:
            return "FAIL", "No per-figure path refs"

    if comp_idx == 22:
        has_excl = bool(re.search(r'excl|exclude|not.*use|omit|remove|irrelevant', tl))
        has_nyc = bool(re.search(r'NYC|New York|Chicago|regional', tl))
        if has_excl and has_nyc:
            return "PASS", "NYC/Chicago excluded"
        elif has_excl:
            return "FAIL", "Exclusion mentioned but no NYC/Chicago"
        else:
            return "FAIL", "No regional exclusion"

    if comp_idx == 23:
        has_aqs = bool(re.search(r'AQS', text))
        has_matrix_rat = bool(re.search(r'authorization.*matrix|matrix.*authorization|no.*swim.*assess|swim.*assess.*no', tl))
        if has_aqs and has_matrix_rat:
            return "PASS", "AQS excluded with matrix rationale"
        elif has_aqs:
            return "FAIL", "AQS mentioned but no matrix rationale"
        else:
            return "FAIL", "AQS not discussed"

    if comp_idx == 24:
        has_p1 = bool(re.search(r'P1|Penalty.*1|camper.*count.*wrong|wrong.*camper', tl))
        has_p2 = bool(re.search(r'P2|Penalty.*2|wristband.*miss|missing.*wristband', tl))
        has_p3 = bool(re.search(r'P3|Penalty.*3|staff.*count.*wrong|wrong.*staff', tl))
        has_p4 = bool(re.search(r'P4|Penalty.*4|double.*count|count.*double', tl))
        if has_p1 and has_p2 and has_p3 and has_p4:
            return "PASS", "All 4 penalties identified"
        else:
            missing = []
            if not has_p1: missing.append("P1")
            if not has_p2: missing.append("P2")
            if not has_p3: missing.append("P3")
            if not has_p4: missing.append("P4")
            return "FAIL", f"Missing: {', '.join(missing)}"

    if comp_idx == 25:
        has_62 = bool(re.search(r'\b62\b', text))
        has_beginner = bool(re.search(r'beginner', tl))
        has_mitig = bool(re.search(r'mitig|partial|partial.*mit|partial.*remed', tl))
        if has_62 and has_beginner and has_mitig:
            return "PASS", "62 beginner retests partial mitigation"
        else:
            return "FAIL", "62 beginner retests / mitigation not identified"

    if comp_idx == 26:
        has_p1 = bool(re.search(r'P1|Penalty.*1|wrong.*count|incorrect.*camper', tl))
        has_489 = bool(re.search(r'\b489\b', text))
        if has_p1 and has_489:
            return "PASS", "P1 identified + corrected to 489"
        else:
            return "FAIL", "P1 not identified or 489 correction missing"

    if comp_idx == 27:
        has_p2 = bool(re.search(r'P2|Penalty.*2|wristband.*error|missing.*wristband', tl))
        has_489 = bool(re.search(r'\b489\b', text))
        if has_p2 and has_489:
            return "PASS", "P2 identified + corrected to 489"
        else:
            return "FAIL", "P2 not identified or 489 correction missing"

    if comp_idx == 28:
        has_p3 = bool(re.search(r'P3|Penalty.*3|staff.*error|wrong.*staff', tl))
        has_37 = bool(re.search(r'\b37\b', text))
        if has_p3 and has_37:
            return "PASS", "P3 identified + corrected to 37"
        else:
            return "FAIL", "P3 not identified or 37 correction missing"

    if comp_idx == 29:
        has_p4 = bool(re.search(r'P4|Penalty.*4|double.*count|count.*double|overlap', tl))
        if has_p4:
            return "PASS", "P4 double-counting identified"
        else:
            return "FAIL", "P4 not identified"

    if comp_idx == 30:
        sites = ['Corrigwell', 'Loon', 'Tamarack', 'Bluegill', 'Heron', 'Otter']
        has_all = all(s in text for s in sites)
        has_insp = bool(re.search(r'examin|inspect|check|review|audit', tl))
        has_auth = bool(re.search(r'authoriz|credential|sign.?off|approval|qualif', tl))
        if has_all and has_insp and has_auth:
            return "PASS", "All 6 sites inspection+auth"
        elif has_all:
            return "FAIL", "All 6 sites but missing inspection/auth"
        else:
            missing_sites = [s for s in sites if s not in text]
            return "FAIL", f"Missing sites: {missing_sites}"

    if comp_idx == 31:
        has_mile = bool(re.search(r'milestone|timeline|schedule|target|deliverable', tl))
        has_date = bool(re.search(r'July\s*\d|August\s*\d|June\s*\d', text))
        has_remed = bool(re.search(r'remed|corrective|improv|fix|address', tl))
        if has_mile and has_date and has_remed:
            return "PASS", "Timeline with milestones+dates"
        else:
            missing = []
            if not has_mile: missing.append("milestone")
            if not has_date: missing.append("dates")
            if not has_remed: missing.append("remediation")
            return "FAIL", f"Missing: {', '.join(missing)}"

    if comp_idx == 32:
        has_risk = bool(re.search(r'risk|consequence|impact|danger|threat|expos', tl))
        has_dl = bool(re.search(r'deadline|July\s*\d|date', tl))
        if has_risk and has_dl:
            return "PASS", "Risk per deadline"
        else:
            missing = []
            if not has_risk: missing.append("risk")
            if not has_dl: missing.append("deadline")
            return "FAIL", f"Missing: {', '.join(missing)}"

    if comp_idx == 33:
        has_rel = bool(re.search(r'reliab|unreli|outdated|conflict|inaccurat|untrust|questionable|doubt', tl))
        has_assess = bool(re.search(r'assess|evaluat|determine|judg|decid', tl))
        if has_rel and has_assess:
            return "PASS", "Source reliability assessed"
        else:
            return "FAIL", "No source reliability assessment"

    if comp_idx == 34:
        has_contradict = bool(re.search(r'contradict|disagree|conflict|inconsist|mismatch|different.*sourc', tl))
        has_xref = bool(re.search(r'cross.?ref|verify.*against|compare|check.*against', tl))
        if has_contradict or has_xref:
            return "PASS", "Contradictions between sources identified"
        else:
            return "FAIL", "No conflict identification"

    if comp_idx == 35:
        has_gap = bool(re.search(r'cannot.*determin|not.*able|unable|does not.*answer|insufficient|incomplete|unknown|unanswer|not.*available', tl))
        if has_gap:
            return "PASS", "Scope limitations stated"
        else:
            return "FAIL", "No scope limitation section"

    return "FAIL", "Unknown"


def run_evaluation():
    all_results = {}
    for model_name, text in responses.items():
        results = []
        passed = 0
        failed = []
        for idx, comp_name in enumerate(COMPONENTS):
            status, detail = score_component(text, idx)
            results.append((comp_name, status, detail))
            if status == "PASS":
                passed += 1
            else:
                failed.append((idx + 1, comp_name, detail))
        all_results[model_name] = {
            "passed": passed,
            "total": len(COMPONENTS),
            "results": results,
            "failed_details": failed,
        }
    return all_results


def print_results(all_results):
    print("=" * 120)
    print("V14 EMPIRICAL EVALUATION — ALL 8 MODELS vs 36 CRITICAL COMPONENTS")
    print("=" * 120)
    print("Thresholds: Strong (R1-R4) fail >=20/36 (56%) | Weak (R5-R8) fail >=29/36 (81%)")
    print()

    for model_name in sorted(all_results.keys()):
        r = all_results[model_name]
        failed_count = r["total"] - r["passed"]
        fail_pct = (failed_count / r["total"]) * 100
        is_strong = model_name in ["R1", "R2", "R3", "R4"]
        threshold = 20 if is_strong else 29
        threshold_pct = 56 if is_strong else 81
        meets = "YES" if failed_count >= threshold else "NO"

        print(f"\n{'='*80}")
        print(f"{model_name} ({'STRONG' if is_strong else 'WEAK'}) — Failed: {failed_count}/{r['total']} ({fail_pct:.1f}%) — Meets >={threshold_pct}%? {meets}")
        print(f"{'='*80}")

        if r["failed_details"]:
            print(f"\n  FAILED COMPONENTS ({len(r['failed_details'])}):")
            for num, name, detail in r["failed_details"]:
                print(f"    {num:2d}. {name}: {detail}")

    print(f"\n{'='*120}")
    print("SUMMARY TABLE")
    print(f"{'='*120}")
    print(f"{'Model':<6} {'Type':<8} {'Failed':<8} {'/36':<5} {'%':<8} {'>=Threshold':<14} {'Meets?'}")
    print("-" * 80)
    for model_name in sorted(all_results.keys()):
        r = all_results[model_name]
        failed_count = r["total"] - r["passed"]
        fail_pct = (failed_count / r["total"]) * 100
        is_strong = model_name in ["R1", "R2", "R3", "R4"]
        threshold = 20 if is_strong else 29
        threshold_pct = 56 if is_strong else 81
        meets = "YES" if failed_count >= threshold else "NO"
        print(f"{model_name:<6} {'STRONG' if is_strong else 'WEAK':<8} {failed_count:<8} {r['total']:<5} {fail_pct:<8.1f} >= {threshold_pct}%     {meets}")

    print()

    strong_pass = all((r["total"] - r["passed"]) >= 20 for m, r in all_results.items() if m in ["R1", "R2", "R3", "R4"])
    weak_pass = all((r["total"] - r["passed"]) >= 29 for m, r in all_results.items() if m in ["R5", "R6", "R7", "R8"])
    print(f"{'='*120}")
    print("EMPIRICAL VERIFICATION")
    print(f"{'='*120}")
    print(f"Strong models all fail >=20/36 (>=56%): {'YES' if strong_pass else 'NO'}")
    print(f"Weak models all fail >=29/36 (>=81%): {'YES' if weak_pass else 'NO'}")
    if not strong_pass or not weak_pass:
        print("PROJECTIONS NOT CONFIRMED — methodology needs iteration")
    else:
        print("V14 EMPIRICAL EVALUATION CONFIRMS ALL PROJECTIONS")

    return all_results


if __name__ == "__main__":
    results = run_evaluation()
    print_results(results)
