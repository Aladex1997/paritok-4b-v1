import csv
from collections import Counter
ENC = 'utf-8-sig'

loa = []
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['field_code'] == 'LOA' and r['amendment_ts'] >= '2022-08-01':
            loa.append(r)

print(f"Total LOA amendments post-2022-08-01: {len(loa)}")
print(f"source_document empty: {sum(1 for a in loa if a['source_document']=='')}")
print(f"source_document non-empty: {sum(1 for a in loa if a['source_document']!='')}")

# Check source_document patterns
sd = Counter(a['source_document'] for a in loa if a['source_document'])
print(f"\nDistinct source_documents: {len(sd)}")
for k,v in list(sd.items())[:20]:
    print(f"  {v}: {k[:80]}")

# Check: LOA amendments where new_value differs from old by material amount
# Or where the amendment is "recent" (after certificates?)
print(f"\nLOA amendments after 2024-06-03 (first cert date): {sum(1 for a in loa if a['amendment_ts'] >= '2024-06-03')}")
print(f"LOA amendments after 2024-09-03 (second cert date): {sum(1 for a in loa if a['amendment_ts'] >= '2024-09-03')}")

# Check: LOA amendments for applicants who are currently OCCUPIED
slips = {}
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        slips[r['slip_id']] = r
occ_tenants = set(s['tenant_id'] for s in slips.values() if s['status']=='OCCUPIED')
loa_occ = [a for a in loa if a['applicant_id'] in occ_tenants]
print(f"\nLOA amendments for currently-occupied tenants: {len(loa_occ)}")
loa_occ_unsup = [a for a in loa_occ if a['applicant_id'] not in {'WL-01893','WL-02401'}]
print(f"  of those, unsupported (no cert): {len(loa_occ_unsup)}")

# Check: LOA amendments where new_value > slip_size (vessel too big)
# Need to join to slip inventory by tenant
print(f"\n=== LOA amendments where new LOA > current slip size ===")
count = 0
for a in loa:
    if a['applicant_id'] in occ_tenants:
        # find tenant's slip
        for sid, s in slips.items():
            if s['tenant_id'] == a['applicant_id']:
                new_loa = float(a['new_value'])
                slip_size = float(s['slip_size_ft'])
                if new_loa > slip_size:
                    count += 1
                    if count <= 15:
                        print(f"  {a['applicant_id']} {a['amendment_id']} {a['amendment_ts']} "
                              f"{a['old_value']}->{a['new_value']} slip={sid}({slip_size}ft)")
                break
print(f"Total LOA amendments where new LOA > slip size: {count}")
