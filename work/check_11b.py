import csv, re
from collections import Counter
ENC = 'utf-8-sig'

loa = []
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['field_code'] == 'LOA' and r['amendment_ts'] >= '2022-08-01':
            loa.append(r)

# Categorize source_document
def categorize(sd):
    if not sd: return 'EMPTY'
    if sd.startswith('MC-'): return 'CERT:' + re.search(r'MC-\d{4}-\d{4}', sd).group(0) if re.search(r'MC-\d{4}-\d{4}', sd) else 'CERT_OTHER'
    if 'Foldview' in sd or 'haul-out' in sd.lower(): 
        m = re.search(r'(\d{4}-\d{2}-\d{2})', sd)
        return 'HAULOUT:' + (m.group(1) if m else 'HAULOUT_OTHER')
    return 'OTHER:' + sd[:40]

cats = Counter(categorize(a['source_document']) for a in loa)
print("Source document categories:")
for k,v in sorted(cats.items(), key=lambda x:-x[1]):
    print(f"  {v}: {k}")

# Our actual files:
# MC-2024-0062 (WL-01893), MC-2024-0091 (WL-02401)
# Foldview 2024-09-12 (WL-02087), Foldview 2025-06-29 (WL-03102)
print("\n=== LOA amendments referencing our actual files ===")
our_refs = {'MC-2024-0062', 'MC-2024-0091', '2024-09-12', '2025-06-29'}
for a in loa:
    sd = a['source_document']
    if any(ref in sd for ref in our_refs):
        print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} source={sd}")

# Check: LOA amendments where source_document references a Foldview sheet dated 2022 or 2023
# (i.e., a haul-out sheet that would have been done BEFORE the certs we have)
print("\n=== LOA amendments with Foldview haul-out sheets (all dates) ===")
foldview = [a for a in loa if 'Foldview' in a['source_document']]
print(f"Total Foldview references: {len(foldview)}")
dates = Counter(re.search(r'(\d{4}-\d{2}-\d{2})', a['source_document']).group(1) if re.search(r'(\d{4}-\d{2}-\d{2})', a['source_document']) else 'N/A' for a in foldview)
for d,v in sorted(dates.items()):
    print(f"  {d}: {v}")

# Maybe 11 = LOA amendments where the source_document is a Foldview sheet from 2022 (before our files)?
foldview_2022 = [a for a in foldview if '2022' in a['source_document']]
print(f"\nFoldview 2022 sheets: {len(foldview_2022)}")
