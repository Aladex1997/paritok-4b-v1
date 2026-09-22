import json
import re

with open('eval_responses/response_texts.json') as f:
    responses = json.load(f)

REASONING_TRAP_CHECKS = [
    {
        "name": "CONTRADICTORY_CLAIMS",
        "description": "Response makes contradictory claims about the same figure",
        "check": lambda text: _check_contradictory_claims(text),
    },
    {
        "name": "MULTIPLE_NUMBERS",
        "description": "Response gives multiple different values for the same figure",
        "check": lambda text: _check_multiple_numbers(text),
    },
    {
        "name": "UNRESOLVED_REFERENCES",
        "description": "References sources it cannot find or verify",
        "check": lambda text: _check_unresolved_refs(text),
    },
    {
        "name": "VAGUE_ANALYSIS",
        "description": "Uses vague language where specific is required",
        "check": lambda text: _check_vague(text),
    },
    {
        "name": "SECTION_CONTRADICTION",
        "description": "Different sections contradict each other",
        "check": lambda text: _check_section_contradiction(text),
    },
]


def _check_contradictory_claims(text):
    """Check if response contradicts itself on key figures."""
    numbers_489 = len(re.findall(r'\b489\b', text))
    numbers_800 = len(re.findall(r'\b800\b', text))
    numbers_568 = len(re.findall(r'\b568\b', text))
    numbers_280 = len(re.findall(r'\b280\b', text))

    has_489_and_800 = numbers_489 > 0 and numbers_800 > 0
    has_489_and_568 = numbers_489 > 0 and numbers_568 > 0
    has_280_and_800 = numbers_280 > 0 and numbers_800 > 0

    if has_489_and_800 or has_489_and_568:
        return True, f"Reports both 489 and {800 if numbers_800 > 0 else 568} — contradictory"
    if has_280_and_800 and numbers_280 > 1:
        return True, f"Reports 280 in conflicting contexts — contradictory"
    return False, "No contradictory claims on key figures"


def _check_multiple_numbers(text):
    """Check if response gives different numbers for same concept."""
    patterns = {
        're-test count': [r'\b(489|568|800|280)\b', r're.?test|re.?assess|swimmer.*test'],
        'staff count': [r'\b(37|33|34|42)\b', r'staff|personnel|people.*credential'],
        'wristband count': [r'\b(489|0)\b', r'wristband|carry.?over|band.*forward'],
    }
    for concept, (number_pat, context_pat) in patterns.items():
        numbers = re.findall(number_pat, text)
        if len(set(numbers)) > 1 and len(numbers) > 1:
            return True, f"Multiple {concept} values: {numbers}"
    return False, "No conflicting numbers for same concept"


def _check_unresolved_refs(text):
    """Check for references to unverifiable sources."""
    issues = []
    # References to files that don't exist in common locations
    suspicious = re.findall(r'\([A-Z][^/]*?/\w+[^)]*\)', text)
    if suspicious:
        issues.append(f"References to unusual paths: {suspicious[:3]}")
    # References to data not traceable
    if re.search(r'see.*note|refer.*memo|per.*internal|based.*verbal|according.*verbal', text, re.I):
        issues.append("References unverifiable verbal/internal sources")
    return bool(issues), "; ".join(issues) if issues else "All references resolvable"


def _check_vague(text):
    """Check for vague analysis where specifics required."""
    issues = []
    if len(re.findall(r'some|several|various|multiple|different|a number of', text)) > 3:
        issues.append("Overuse of vague quantifiers (some/several/various)")
    if re.search(r'etc\.|and so on|and others', text):
        issues.append("Uses 'etc.' or similar hand-waving")
    if re.search(r'complicated|complex|difficult to determine|hard to say', text, re.I):
        issues.append("Admits inability to analyze rather than analyzing")
    return bool(issues), "; ".join(issues) if issues else "Specific analysis throughout"


def _check_section_contradiction(text):
    """Check if different sections disagree."""
    sections = re.split(r'(?:^|\n)\d+\.|(?:^|\n)[A-Z]\.|(?:^|\n)Section\s*\d', text)
    if len(sections) < 3:
        return False, "Not enough distinct sections to compare"

    # Check if key figures differ across sections
    key_figures = {}
    for i, section in enumerate(sections):
        for pattern in [r'\b489\b', r'\b800\b', r'\b37\b', r'\b33\b']:
            matches = re.findall(pattern, section)
            if matches:
                if pattern not in key_figures:
                    key_figures[pattern] = set()
                key_figures[pattern].add((i, len(matches)))

    for figure, locations in key_figures.items():
        if len(locations) > 1:
            counts = [count for _, count in locations]
            if len(set(counts)) > 1:
                return True, f"Figure {figure} appears inconsistently across sections: {locations}"
    return False, "No cross-section contradictions"


def run_trap_evaluation():
    results = {}
    for model_name, text in responses.items():
        model_results = []
        trap_trips = 0
        for check in REASONING_TRAP_CHECKS:
            triggered, detail = check["check"](text)
            model_results.append({
                "name": check["name"],
                "description": check["description"],
                "triggered": triggered,
                "detail": detail,
            })
            if triggered:
                trap_trips += 1

        results[model_name] = {
            "trap_trips": trap_trips,
            "total_checks": len(REASONING_TRAP_CHECKS),
            "results": model_results,
        }
    return results


def print_results(results):
    print("=" * 100)
    print("REASONING TRAP EVALUATION — Does the model's analysis get STUCK while reading?")
    print("=" * 100)
    print()
    print("Each check detects a specific reasoning breakdown pattern during analysis.")
    print("If triggered, the model's reasoning process malfunctioned while processing source data.")
    print()

    for model_name in sorted(results.keys()):
        r = results[model_name]
        status = "TRAPPED" if r["trap_trips"] >= 3 else "PARTIALLY TRAPPED" if r["trap_trips"] >= 1 else "NOT TRAPPED"
        print(f"{model_name}: {r['trap_trips']}/{r['total_checks']} reasoning traps triggered — {status}")
        for res in r["results"]:
            trigger = "TRIGGERED" if res["triggered"] else "ok"
            print(f"  [{trigger}] {res['name']}: {res['detail']}")
        print()

    print("=" * 100)
    print("TRAP SUMMARY")
    print("=" * 100)
    trapped = sum(1 for r in results.values() if r["trap_trips"] >= 3)
    partially = sum(1 for r in results.values() if 1 <= r["trap_trips"] < 3)
    not_trapped = sum(1 for r in results.values() if r["trap_trips"] == 0)
    print(f"Fully trapped (3+ breakdowns): {trapped}/8")
    print(f"Partially trapped (1-2 breakdowns): {partially}/8")
    print(f"Not trapped (0 breakdowns): {not_trapped}/8")
    if trapped + partially >= 6:
        print("\nREASONING TRAP: MOST MODELS SHOW ANALYTICAL BREAKDOWN WHILE READING")
    else:
        print("\nREASONING TRAP: INSUFFICIENT — models handle reading without breakdown")


if __name__ == "__main__":
    results = run_trap_evaluation()
    print_results(results)
