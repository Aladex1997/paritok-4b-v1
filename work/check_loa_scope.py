import csv
ENC = 'utf-8-sig'

# LOA amendments for the 6 skip-PDF applicants and 2 cert holders
focus = {'WL-02211','WL-02618','WL-02877','WL-03044','WL-03102','WL-03390','WL-01893','WL-02401'}
print("=== LOA amendments for focus applicants (PDF + cert holders) ===")
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in focus and r['field_code']=='LOA' and r['amendment_ts']>='2022-08-01':
            print(f"  {r['applicant_id']} {r['amendment_id']} {r['amendment_ts']} {r['old_value']}->{r['new_value']} cert={r['requires_cert']} source={r['source_document']}")

# Count LOA amendments where new LOA differs from old by >1 ft AND source is empty
print("\n=== LOA amendments: empty source AND |new-old| > 1 ===")
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    count = 0
    for r in csv.DictReader(f):
        if r['field_code']=='LOA' and r['amendment_ts']>='2022-08-01':
            if r['source_document']=='' and abs(float(r['new_value'])-float(r['old_value']))>1:
                count += 1
                print(f"  {r['applicant_id']} {r['amendment_id']} {r['old_value']}->{r['new_value']}")
    print(f"Total: {count}")

# Count LOA amendments where source references a Foldview sheet NOT in our files
print("\n=== LOA amendments: Foldview sheet not in our file set ===")
our_foldview = {'2024-09-12', '2025-06-29'}
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    import re
    count = 0
    for r in csv.DictReader(f):
        if r['field_code']=='LOA' and r['amendment_ts']>='2022-08-01':
            if 'Foldview' in r['source_document']:
                m = re.search(r'(\d{4}-\d{2}-\d{2})', r['source_document'])
                if m and m.group(1) not in our_foldview:
                    count += 1
    print(f"Foldview sheets not in our files: {count}")

# Count LOA amendments where source references an MC cert NOT in our files
print("\n=== LOA amendments: MC cert not in our file set ===")
our_mcs = {'MC-2024-0062', 'MC-2024-0091'}
with open('amendment_log_2022-2026.csv', encoding=ENC) as f:
    import re
    count = 0
    for r in csv.DictReader(f):
        if r['field_code']=='LOA' and r['amendment_ts']>='2022-08-01':
            if r['source_document'].startswith('MC-'):
                m = re.search(r'(MC-\d{4}-\d{4})', r['source_document'])
                if m and m.group(1) not in our_mcs:
                    count += 1
    print(f"MC certs not in our files: {count}")
