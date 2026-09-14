import zipfile, re, os, json

base = "/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output/model_responses/New 3"

# 15 critical components - check if model ADDRESSED each (not exact values)
# Each component maps to a regex pattern that indicates the model addressed the ask
components = [
    ("C01", "Skip audit performed", [
        r"skip_events", r"skip.*audit", r"contemporaneous", r"review_date.*skip_date|skip_date.*review_date"
    ]),
    ("C02", "Contemporaneous proof logic", [
        r"review_date", r"skip_date", r"cover sheet", r"Standing Order.*15-3|15-3.*s\.3\.2"
    ]),
    ("C03", "PDF reconciliation", [
        r"justification.*PDF|PDF.*justification", r"offer_events.*skip|skip.*offer_events",
        r"cross.check.*justification|justification.*cross.check", r"supporting record"
    ]),
    ("C04", "Amendment verification (certificate)", [
        r"measurement certificate|yard haul-out|amendment.*certificate|certificate.*amendment"
    ]),
    ("C05", "Post-adoption cutoff (Aug 1, 2022)", [
        r"Aug\.? 1,? 2022|August 1,? 2022|2022-06.*s\.4\.3|Resolution.*2022.*4\.3"
    ]),
    ("C06", "Amendment reconciliation", [
        r"applicant_id", r"skip_events.*amendment|amendment.*skip_events",
        r"unsubstantiated|unsupported"
    ]),
    ("C07", "Covered vs open determination", [
        r"covered.*open|open.*covered", r"OCCUPIED", r"check-in.*LOA|LOA.*check-in"
    ]),
    ("C08", "Expected monthly charges", [
        r"expected.*monthly|monthly.*expected", r"billing_transaction"
    ]),
    ("C09", "Rates from Resolution 2022-06", [
        r"Resolution.*2022.*06|2022-06.*rate|rate.*2022"
    ]),
    ("C10", "Variance in dollars", [
        r"variance.*dollar|dollar.*variance", r"billing.*reconcil", r"actual.*expected|expected.*actual"
    ]),
    ("C11", "Aging buckets (91-120, 120+)", [
        r"91-120|120\+|120\+", r"aging"
    ]),
    ("C12", "Slip ID join (AC-LP-0122)", [
        r"AC-LP.*LP|slip.*ID.*embedded|embedded.*slip.*ID|account.*number.*slip"
    ]),
    ("C13", "OCCUPIED status confirmation", [
        r"status.*OCCUPIED|OCCUPIED.*status", r"confirm.*occup"
    ]),
    ("C14", "Delinquent balance computed", [
        r"delinquent.*balance|balance.*delinquent", r"total.*delinquent"
    ]),
    ("C15", "Priority classification", [
        r"Priority 1", r"Priority 2", r"Priority 3", r"downstream skip"
    ]),
]

# Scoring function
results = {}
for d in sorted(os.listdir(base)):
    wb_dir = os.path.join(base, d)
    if not os.path.isdir(wb_dir): continue
    xlsx = [f for f in os.listdir(wb_dir) if f.endswith('.xlsx')]
    docx = [f for f in os.listdir(wb_dir) if f.endswith('.docx')]
    if not xlsx: continue

    all_text = ""
    try:
        z3 = zipfile.ZipFile(os.path.join(wb_dir, xlsx[0]))
        ss = []
        if 'xl/sharedStrings.xml' in z3.namelist():
            sxml = z3.read('xl/sharedStrings.xml').decode('utf-8')
            sis = re.findall(r'<si>(.*?)</si>', sxml, re.DOTALL)
            for si in sis:
                ts = re.findall(r'<t[^>]*>(.*?)</t>', si, re.DOTALL)
                ss.append(''.join(ts))
        xml_files = sorted([n for n in z3.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')])
        for xf in xml_files:
            xcontent = z3.read(xf).decode('utf-8')
            cells = re.findall(r'<c[^>]*>(.*?)</c>', xcontent)
            for cell in cells:
                v_match = re.search(r'<v>([^<]+)</v>', cell)
                is_str = 't="s"' in cell
                if v_match and is_str:
                    idx = int(v_match.group(1))
                    if idx < len(ss):
                        all_text += ss[idx] + " "
                else:
                    t_match = re.search(r'<t[^>]*>([^<]*)</t>', cell)
                    if t_match:
                        all_text += t_match.group(1) + " "
        z3.close()
    except Exception as e:
        all_text = f"ERROR: {e}"

    memo_text = ""
    if docx:
        try:
            z4 = zipfile.ZipFile(os.path.join(wb_dir, docx[0]))
            if 'word/document.xml' in z4.namelist():
                dxml = z4.read('word/document.xml').decode('utf-8')
                paras = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', dxml)
                memo_text = ' '.join(paras)
            z4.close()
        except:
            memo_text = "ERROR"

    full_text = all_text + " " + memo_text

    # Check each component
    model_results = []
    for comp_id, comp_name, patterns in components:
        matches = sum(1 for p in patterns if re.search(p, full_text, re.IGNORECASE))
        # Require at least 2 patterns to match for a component to "pass"
        passed = matches >= 2
        model_results.append({'id': comp_id, 'name': comp_name, 'matches': matches, 'pass': passed})

    passed_count = sum(1 for m in model_results if m['pass'])
    total = len(model_results)
    fail_count = total - passed_count
    fail_pct = (fail_count / total * 100) if total > 0 else 0

    results[d] = {'passed': passed_count, 'total': total, 'failed': fail_count, 'fail_pct': round(fail_pct, 1), 'results': model_results}

    print(f"\n{d}: {passed_count}/{total} passed ({fail_count} failed = {fail_pct:.1f}%)")
    failed = [m for m in model_results if not m['pass']]
    if failed:
        print(f"  Failed: {[(m['id'], m['name'], m['matches']) for m in failed]}")
    passed = [m for m in model_results if m['pass']]
    if passed:
        print(f"  Passed: {[(m['id'], m['name']) for m in passed]}")

# Threshold check
print(f"\n\n{'='*60}")
print("THRESHOLD CHECK (15 critical components)")
for d in sorted(results.keys()):
    r = results[d]
    num = int(''.join(filter(str.isdigit, d)))
    group = "1-4" if num <= 4 else "5-8"
    threshold = 50 if group == "1-4" else 80
    status = "PASS" if r['fail_pct'] >= threshold else "FAIL"
    print(f"  {d} [Group {group}]: {r['failed']}/{r['total']} failed ({r['fail_pct']}%) — threshold ≥{threshold}%: {status}")

os.makedirs("/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output", exist_ok=True)
with open('/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output/new3_compliance.json', 'w') as f:
    json.dump(results, f, indent=2)
print("\nSaved: output/new3_compliance.json")
