import json
import re

with open('rep1_responses/rep1_texts.json', 'r') as f:
    responses = json.load(f)

def score_response(text):
    """Score a model response against V6 rubric."""
    scores = {}
    penalties = 0.0
    details = []

    # ---- SECTION A: FORMAT (1.0) ----
    a = 0.0
    a += 0.25  # docx
    a += 0.25  # no external attachments
    has_memo_header = bool(re.search(r'(TO|FROM|DATE|RE|MEMORANDUM|memo)', text, re.IGNORECASE))
    a += 0.125 if has_memo_header else 0.0
    has_abs_dates = bool(re.search(r'(July \d+, 2026|August \d+, 2026|June \d+, 2026)', text))
    a += 0.125 if has_abs_dates else 0.0
    scores['A'] = round(min(a, 1.0), 2)

    # ---- SECTION B: SITE BREAKDOWN (1.0) ----
    b = 0.0
    has_passed = bool(re.search(r'Passed', text, re.IGNORECASE))
    has_never = bool(re.search(r'Never Examined|never-examined|never examined', text, re.IGNORECASE))
    has_corrigwell = 'Corrigwell' in text
    has_loon = 'Loon Hollow' in text
    site_class = sum(1 for s in ['Corrigwell', 'Loon Hollow', 'Tamarack Ridge', 'Bluegill Point', 'Heron Landing', 'Otter Run'] if s in text)
    b1 = 0.0
    if site_class >= 5 and has_passed and has_never:
        b1 = 0.50
    elif site_class >= 3:
        b1 = 0.25
    b += b1
    has_unauthorized = bool(re.search(r'unauthorized|Unauthorized', text))
    b2 = 0.25 if has_unauthorized and has_corrigwell else 0.0
    b += b2
    has_never_qualifier = bool(re.search(r'not.*compliant|cannot.*classified|ineligible|default.*ineligible|segregated', text, re.IGNORECASE))
    b3 = 0.25 if has_never_qualifier and has_never else 0.0
    b += b3
    scores['B'] = round(min(b, 1.0), 2)

    # ---- SECTION C: SCOPE ISOLATION (1.0) ----
    c = 0.0
    has_water = bool(re.search(r'water quality|Water Quality|chlorine', text, re.IGNORECASE))
    has_ratio = bool(re.search(r'1:25|ratio|buddy.?board', text, re.IGNORECASE))
    has_incident = bool(re.search(r'incident|first.?aid', text, re.IGNORECASE))
    c += 0.083 if has_water else 0.0
    c += 0.083 if has_ratio else 0.0
    c += 0.083 if has_incident else 0.0
    has_separation = bool(re.search(r'regulatory.*internal|filing.*draft|\.pdf.*\.md|separated.*draft', text, re.IGNORECASE))
    c += 0.25 if has_separation else 0.0
    scores['C'] = round(min(c, 1.0), 2)

    # ---- SECTION D: RE-ASSESSMENT WORKLOAD (1.5 + penalties) ----
    d = 0.0
    camper_489 = bool(re.search(r'\b489\b', text))
    camper_568 = bool(re.search(r'\b568\b', text))
    camper_800 = bool(re.search(r'\b800\b', text))
    d1 = 0.0
    if camper_489:
        d1 = 0.30
    elif camper_568 or camper_800:
        d1 = 0.0
        penalties += 1.5
        details.append(f"P1: Incorrect camper count (reported {568 if camper_568 else 800}, expected 489)")
    else:
        d1 = 0.0
        penalties += 1.5
        details.append("P1: No clear camper count reported (P1 triggered)")
    d += d1

    has_session = bool(re.search(r'Session\s*1.*Session\s*2|Session 1.*280|280.*288', text))
    d2 = 0.15 if has_session else 0.0
    d += d2

    wristband_489 = bool(re.search(r'\b489\b.*wristband|wristband.*489', text, re.IGNORECASE))
    wristband_0 = bool(re.search(r'(zero|0)\s*(?:wristband|wristbands)', text, re.IGNORECASE))
    d3 = 0.0
    if wristband_489:
        d3 = 0.30
    elif wristband_0:
        d3 = 0.0
        penalties += 1.0
        details.append("P2: Missing wristband count (reported 0, expected 489)")
    else:
        d3 = 0.0
        penalties += 1.0
        details.append("P2: No clear wristband count (P2 triggered)")
    d += d3

    staff_37 = bool(re.search(r'\b37\b', text))
    staff_wsi = 'WSI' in text
    has_aqs = 'AQS' in text
    d4 = 0.0
    if staff_37 and staff_wsi and has_aqs:
        d4 = 0.30
    elif staff_37:
        d4 = 0.15
    elif has_aqs:
        staff_numbers = re.findall(r'(\d+)\s*(?:staff|people|person|individuals)', text, re.IGNORECASE)
        if any(s != 37 for s in staff_numbers):
            d4 = 0.0
            penalties += 0.5
            details.append(f"P3: Staff count includes AQS (wrong count)")
        else:
            d4 = 0.15
    else:
        d4 = 0.0
        penalties += 0.5
        details.append("P3: Staff calculation error")
    d += d4

    has_copus_gap = '[CORPUS GAP]' in text
    d5 = 0.30 if has_copus_gap else 0.0
    d += d5
    scores['D'] = round(min(d, 1.5), 2)

    # ---- SECTION E: DEADLINE RECONCILIATION (1.5) ----
    e = 0.0
    has_july2 = bool(re.search(r'July\s*2|July 2', text))
    has_july15 = bool(re.search(r'July\s*15|July 15', text))
    has_july30 = bool(re.search(r'July\s*30|July 30', text))
    has_great_pines = 'Great Pines' in text
    has_cap = bool(re.search(r'CAP|Corrective Action Plan', text, re.IGNORECASE))
    has_feasibility = bool(re.search(r'feasible|CANNOT|cannot.*completed|unlikely|mathematically', text, re.IGNORECASE))
    e += 0.133 if has_july2 else 0.0
    e += 0.133 if has_july15 else 0.0
    e += 0.133 if has_july30 else 0.0
    e += 0.30 if has_great_pines else 0.0
    e += 0.30 if has_cap else 0.0
    e += 0.30 if has_feasibility else 0.0
    e += 0.201 if has_july2 and has_july15 and has_july30 else 0.0
    scores['E'] = round(min(e, 1.5), 2)

    # ---- SECTION F: TRACEABILITY (0.5) ----
    f = 0.0
    citations = re.findall(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+/\S+\.(?:docx|xlsx|csv|pdf|md)', text)
    f = 0.25 if len(citations) >= 5 else (0.125 if len(citations) >= 2 else 0.0)
    scores['F'] = round(min(f, 0.5), 2)

    # ---- SECTION G: CONSTRAINTS (0.5) ----
    g = 0.0
    has_regional_exclusion = bool(re.search(r'NYC|Chicago|regional.*excluded|exclude.*regional', text, re.IGNORECASE))
    g += 0.25 if has_regional_exclusion else 0.0
    has_pipeline = bool(re.search(r'Site Audit|Scope Check|Re-Assessment|Deadline', text, re.IGNORECASE))
    g += 0.25 if has_pipeline else 0.0
    scores['G'] = round(min(g, 0.5), 2)

    base_total = sum(scores.values())
    final = max(base_total - penalties, 0)
    pct = round(final / 7.0 * 100, 1)

    return {
        'scores': scores,
        'penalties': round(penalties, 2),
        'final': round(final, 2),
        'pct': pct,
        'penalty_details': details,
        'base_total': round(base_total, 2),
    }

results = {}
for label in sorted(responses.keys()):
    text = responses[label]
    result = score_response(text)
    results[label] = result

    model_type = 'STRONG' if label in ['M1', 'M2', 'M3', 'M4'] else 'WEAK'
    threshold = '50%' if model_type == 'STRONG' else '80%'
    status = 'PASS' if result['pct'] >= float(threshold.replace('%','')) else 'FAIL'

    print(f"\n{label} ({model_type}) — {result['base_total']} base, {result['penalties']} penalties → {result['final']} final ({result['pct']}%) [threshold {threshold}] {status}")
    print(f"  Sections: A={result['scores']['A']}, B={result['scores']['B']}, C={result['scores']['C']}, D={result['scores']['D']}, E={result['scores']['E']}, F={result['scores']['F']}, G={result['scores']['G']}")
    for pd in result['penalty_details']:
        print(f"  PENALTY: {pd}")

strong_pcts = [results[r]['pct'] for r in ['M1', 'M2', 'M3', 'M4']]
weak_pcts = [results[r]['pct'] for r in ['M5', 'M6', 'M7', 'M8']]
strong_fail = sum(1 for p in strong_pcts if p < 50)
weak_fail = sum(1 for p in weak_pcts if p < 80)

print(f"\n{'='*60}")
print(f"V6 EVALUATION SUMMARY — REP 1 ALL.zip")
print(f"{'='*60}")
print(f"Strong: avg={sum(strong_pcts)/len(strong_pcts):.1f}%, fail={strong_fail}/4 (need ≥3 for ≥60%)")
print(f"Weak: avg={sum(weak_pcts)/len(weak_pcts):.1f}%, fail={weak_fail}/4 (need ≥4 for ≥90%)")
print(f"Penalties triggered across all models:")
all_penalties = {}
for r in results:
    for pd in results[r]['penalty_details']:
        key = pd.split(':')[0]
        all_penalties[key] = all_penalties.get(key, 0) + 1
for k in sorted(all_penalties):
    print(f"  {k}: {all_penalties[k]} models")
