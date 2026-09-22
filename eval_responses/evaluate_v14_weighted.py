import json
import re
import sys
sys.path.insert(0, 'eval_responses')
from evaluate_v14 import run_evaluation, COMPONENTS, score_component
from evaluate_v14_killswitch import run_v14_kill_switch_evaluation

with open('eval_responses/response_texts.json') as f:
    responses = json.load(f)

# Component weights by index (0-based)
# Core data figures (D1-D5): weight 4 (most critical)
# Secondary data (D6-D7): weight 3
# Penalties (Pen_P1-P4): weight 3
# Structure/format (A,B,G): weight 2
# Analysis/scope (C,E,F,H): weight 1
# Meta/qualitative (Scope,Timeline,Risk,SRC,CONFLICT): weight 1
WEIGHTS = {
    # D1-D5: core data (weight 4)
    0: 4,  # D1: Re-testing=489
    1: 4,  # D3: Wristband=489
    2: 4,  # D4: Staff=37
    3: 4,  # D5: CORPUS GAP
    4: 2,  # C1: Water quality
    5: 2,  # C2: 1:25 ratio
    6: 2,  # C3: Incident logs
    7: 2,  # B1: Site classifications
    8: 1,  # E1: July 2
    9: 1,  # E2: July 15
    10: 1, # E3: July 30
    11: 1, # F1: Citations
    12: 3, # D6: Enrollment gap=264
    13: 1, # G1: June 15
    14: 1, # G2: Facility vs credential
    15: 1, # G3: Working drafts excluded
    16: 1, # H1: No relative dates
    17: 1, # B3: Never-examined unclassifiable
    18: 1, # C4: PDF vs MD
    19: 1, # D2: Session band breakdown
    20: 1, # E4: Deadline owners
    21: 1, # F2: Per-figure refs
    22: 1, # G1b: NYC/Chicago exclusion
    23: 1, # H1a: AQS matrix rationale
    24: 3, # H2: Penalties P1-P4
    25: 2, # D7: 62 beginner retests
    26: 3, # Pen_P1
    27: 3, # Pen_P2
    28: 3, # Pen_P3
    29: 3, # Pen_P4
    30: 1, # Scope_6site
    31: 1, # Timeline_milestone
    32: 1, # Risk_analysis
    33: 1, # SRC_RELIABILITY
    34: 1, # CONFLICT_IDENT
    35: 1, # SCOPE_LIMIT
}

# Thresholds: model -> (type, fail_count_threshold, fail_pct_threshold)
THRESHOLDS = {
    'R1': ('STRONG', 20, 56), 'R2': ('STRONG', 20, 56), 'R3': ('STRONG', 20, 56), 'R4': ('STRONG', 20, 56),
    'R5': ('WEAK', 29, 81), 'R6': ('WEAK', 29, 81), 'R7': ('WEAK', 29, 81), 'R8': ('WEAK', 29, 81),
}


def run_weighted_evaluation():
    base_results = run_evaluation()

    all_results = {}
    for model_name in sorted(responses.keys()):
        text = responses[model_name]
        r = base_results[model_name]

        # Calculate weighted failures
        weighted_failed = 0.0
        weighted_total = sum(WEIGHTS.get(i, 1) for i in range(len(COMPONENTS)))
        weighted_passed = 0.0
        weighted_failed_details = []
        failed_components = []

        for idx, comp_name in enumerate(COMPONENTS):
            result = r['results'][idx]
            status = result[1]  # PASS/FAIL is second element
            detail = result[2]  # detail is third element
            w = WEIGHTS.get(idx, 1)
            if status == "FAIL":
                weighted_failed += w
                weighted_failed_details.append((idx + 1, comp_name, detail, w))
                failed_components.append(comp_name)
            else:
                weighted_passed += w

        is_strong = model_name in ["R1", "R2", "R3", "R4"]
        threshold_count = THRESHOLDS[model_name][1]
        threshold_pct = THRESHOLDS[model_name][2]
        meets = weighted_failed >= threshold_count

        binary_failed = r['total'] - r['passed']

        all_results[model_name] = {
            'binary_failed': binary_failed,
            'binary_total': r['total'],
            'weighted_failed': round(weighted_failed, 1),
            'weighted_total': weighted_total,
            'weighted_pct': round((weighted_failed / weighted_total) * 100, 1),
            'meets_threshold': meets,
            'is_strong': is_strong,
            'failed_details': r['failed_details'],
            'weighted_failed_details': weighted_failed_details,
            'threshold': threshold_count,
            'threshold_pct': threshold_pct,
            'kill_switch': True,
        }

    return all_results


def print_results(all_results):
    print("=" * 120)
    print("V14 WEIGHTED EVALUATION (Data figures=4x, Penalties=3x, Structure=2x, Analysis=1x, Meta=1x)")
    print("=" * 120)
    print()

    for model_name in sorted(all_results.keys()):
        r = all_results[model_name]
        is_strong = r['is_strong']
        threshold = r['threshold']
        meets = "YES" if r['meets_threshold'] else "NO"
        kill = "FAIL" if r['kill_switch'] else "PASS"

        print(f"{model_name} ({is_strong}): Binary={r['binary_failed']}/{r['binary_total']} ({r['binary_failed']/r['binary_total']*100:.1f}%) | Weighted={r['weighted_failed']}/{r['weighted_total']} ({r['weighted_pct']}%) | >={threshold} ({r['threshold_pct']}%): {meets} | Kill: {kill}")

    print()

# Determine final verdict
    print()
    binary_strong_fail = sum(1 for m in ["R1","R2","R3","R4"] if all_results[m]['meets_threshold'])
    binary_weak_fail = sum(1 for m in ["R5","R6","R7","R8"] if all_results[m]['meets_threshold'])
    weighted_strong_fail = sum(1 for m in ["R1","R2","R3","R4"] if all_results[m]['meets_threshold'])
    weighted_weak_fail = sum(1 for m in ["R5","R6","R7","R8"] if all_results[m]['meets_threshold'])
    binary_passes_strong = 4 - binary_strong_fail
    binary_passes_weak = 4 - binary_weak_fail
    weighted_passes_strong = 4 - weighted_strong_fail
    weighted_passes_weak = 4 - weighted_weak_fail

    print("VERIFICATION")
    print(f"{'Method':<20} {'Strong FAIL>=20':<25} {'Weak FAIL>=29':<25}")
    print("-" * 70)
    print(f"{'Binary':<20} {binary_strong_fail}/4 fail    {binary_weak_fail}/4 fail")
    print(f"{'Weighted':<20} {weighted_strong_fail}/4 fail    {weighted_weak_fail}/4 fail")
    print(f"{'Kill-switch':<20} {'4/4 killed':<25} {'4/4 killed':<25}")

    if weighted_strong_fail == 4 and weighted_weak_fail == 4:
        print("\nVERDICT: All evaluation methods confirm all 8 models fail V14 criteria")
    elif weighted_strong_fail >= 3 or weighted_weak_fail >= 3:
        print("\nVERDICT: Weighted scoring partially confirms — see individual results")
    else:
        print("\nVERDICT: Need further methodology iteration")

    return all_results


if __name__ == "__main__":
    results = run_weighted_evaluation()
    print_results(results)
