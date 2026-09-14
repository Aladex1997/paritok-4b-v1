import zipfile, re, os, json

base = "/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output/model_responses/New 3"
rubric_path = "/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output/audit_rubric.xlsx"

# === Read rubric expected values ===
z = zipfile.ZipFile(rubric_path)
ss_xml = z.read('xl/sharedStrings.xml').decode('utf-8')
shared = re.findall(r'<si>(.*?)</si>', ss_xml, re.DOTALL)
strings = []
for si in shared:
    ts = re.findall(r'<t[^>]*>(.*?)</t>', si, re.DOTALL)
    strings.append(''.join(ts))

content = z.read('xl/worksheets/sheet1.xml').decode('utf-8')
row_matches = re.findall(r'<row[^>]*r="(?:\d+)"[^>]*>(.*?)</row>', content, re.DOTALL)
print(f"Rubric rows: {len(row_matches)}")

rubric_entries = []
for row_data in row_matches:
    cells = re.findall(r'<c([^>]*?)>(.*?)</c>', row_data, re.DOTALL)
    vals = []
    for attrs, cell_data in cells:
        v_match = re.search(r'<v>(\d+)</v>', cell_data)
        t_match = re.search(r'<t[^>]*>(.*?)</t>', cell_data, re.DOTALL)
        is_str = 't="s"' in attrs
        is_inline = '<is>' in attrs
        if v_match and is_str:
            idx = int(v_match.group(1))
            vals.append(strings[idx] if idx < len(strings) else f"[{idx}]")
        elif is_inline and t_match:
            vals.append(t_match.group(1))
        elif v_match:
            vals.append(v_match.group(1))
        elif t_match:
            vals.append(t_match.group(1))
    if len(vals) >= 4:
        rid = vals[0]
        criterion = vals[1]
        expected = vals[2]
        rtype = vals[3]
        if rid.startswith('R-'):
            rubric_entries.append({'id': rid, 'criterion': criterion, 'expected': expected, 'type': rtype})

print(f"Rubric entries: {len(rubric_entries)}")
for r in rubric_entries:
    print(f"  {r['id']}: {r['criterion']} = {r['expected']} ({r['type']})")

# === Define leak values ===
leak_values = []
for r in rubric_entries:
    exp = r['expected']
    if r['type'] not in ['Yes', 'No', 'Text', 'Numeric']:
        leak_values.append(exp)
leak_values.extend(['$439,918.30', '$319,760.05', '$120,158.25', '$1,441,899.00', '$99,629.80',
                     '317 slips', '19 skips', '11 items', '6 accounts', '$4,368.00', '826 slips',
                     '39 errors', '$17,108.00', '$147,836.00', '$10.40/$7.55',
                     '7 Priority 1 / 16 Priority 2 / 9 Priority 3', 'WL-02085',
                     '$10.40/foot-month', '$7.55/foot-month',
                     'Standing Order 15-3 ss.3.2-3.3', 'Appeal 2018-3 pp.2-3',
                     'Resolution 2022-06 ss.1-2, 4.3', 'Flagged as unresolved',
                     '4 tabs with formulas', 'All buckets checked', '39 errors with source rows',
                     'Stated in memo', 'Specific Board actions', 'Missing export rows explained'])
leak_values = list(set(leak_values))

# === Score each model ===
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

    model_results = []
    for r in rubric_entries:
        expected = r['expected']
        passed = expected in full_text
        model_results.append({'id': r['id'], 'criterion': r['criterion'], 'expected': expected, 'type': r['type'], 'pass': passed})

    passed_count = sum(1 for m in model_results if m['pass'])
    total = len(model_results)
    fail_count = total - passed_count
    fail_pct = (fail_count / total * 100) if total > 0 else 0

    leaked = [lv for lv in leak_values if lv in full_text]

    results[d] = {'passed': passed_count, 'total': total, 'failed': fail_count, 'fail_pct': round(fail_pct, 1), 'leaked': leaked}

    print(f"\n{'='*60}")
    print(f"{d}: {passed_count}/{total} passed ({fail_count} failed = {fail_pct:.1f}%)")
    if leaked:
        print(f"  LEAKED: {leaked}")
    failed = [m for m in model_results if not m['pass']]
    if failed:
        print(f"  Failed IDs: {[m['id'] for m in failed]}")

# Threshold check
print(f"\n\n{'='*60}")
print("THRESHOLD CHECK")
for d in sorted(results.keys()):
    r = results[d]
    num = int(''.join(filter(str.isdigit, d)))
    group = "1-4" if num <= 4 else "5-8"
    threshold = 50 if group == "1-4" else 80
    status = "PASS" if r['fail_pct'] >= threshold else "FAIL"
    print(f"  {d} [Group {group}]: {r['failed']}/{r['total']} failed ({r['fail_pct']}%) — threshold ≥{threshold}%: {status}")

os.makedirs("/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output", exist_ok=True)
with open('/workspace/e8b477d3-d111-404c-9fae-fc593b39c679/sessions/agent_e8b79be5-f3c7-44ef-a1a5-6db56bfe9c1f/output/new3_scoring.json', 'w') as f:
    json.dump(results, f, indent=2)
print("\nSaved: output/new3_scoring.json")
