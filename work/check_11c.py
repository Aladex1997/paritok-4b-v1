import csv
from collections import Counter
ENC = 'utf-8-sig'

loa = []
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['field_code'] == 'LOA' and r['amendment_ts'] >= '2022-08-01':
            loa.append(r)

# 12 empty source_documents
empty = [a for a in loa if a['source_document']=='']
print(f"LOA amendments with EMPTY source_document: {len(empty)}")
for a in empty:
    print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} {a['old_value']}->{a['new_value']}")

# Check: LOA amendments where source_document references our 4 actual files
our_files = ['MC-2024-0062', 'MC-2024-0091', '2024-09-12', '2025-06-29']
print(f"\nLOA amendments referencing our 4 actual files:")
for a in loa:
    for f in our_files:
        if f in a['source_document']:
            print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} source={a['source_document']}")

# Check: LOA amendments where source_document references a Foldview sheet we HAVE (2024-09-12, 2025-06-29)
print(f"\nLOA amendments referencing Foldview 2024-09-12 or 2025-06-29:")
for a in loa:
    if '2024-09-12' in a['source_document'] or '2025-06-29' in a['source_document']:
        print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} source={a['source_document']}")

# Check: LOA amendments where source_document references MC-2024-0062 or MC-2024-0091
print(f"\nLOA amendments referencing MC-2024-0062 or MC-2024-0091:")
for a in loa:
    if 'MC-2024-0062' in a['source_document'] or 'MC-2024-0091' in a['source_document']:
        print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} source={a['source_document']}")

# Total supported by our 4 files
supported = [a for a in loa if any(f in a['source_document'] for f in our_files)]
print(f"\nTotal LOA amendments supported by our 4 actual files: {len(supported)}")
print(f"Unsupported (no verifiable file): {len(loa) - len(supported)}")

# What about LOA amendments referencing MC-XXXX certificates (any)?
mcs = [a for a in loa if a['source_document'].startswith('MC-')]
print(f"\nLOA amendments referencing an MC- certificate: {len(mcs)}")
# Of those, how many are MC-2024-0062 or MC-2024-0091?
our_mcs = [a for a in mcs if 'MC-2024-0062' in a['source_document'] or 'MC-2024-0091' in a['source_document']]
print(f"  of those, our 2 certs: {len(our_mcs)}")
