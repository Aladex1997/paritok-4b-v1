import csv, math, zipfile, re
from collections import Counter, defaultdict

ENC = 'utf-8-sig'

slips = {}
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        slips[r['slip_id']] = r
occ = {sid: s for sid, s in slips.items() if s['status'] == 'OCCUPIED'}

def bl(s):
    return math.ceil(max(float(s['vessel_loa_ft']), float(s['slip_size_ft'])))
def ch(s):
    return bl(s) * (10.40 if s['covered']=='COVERED' else 7.55)

# August billing
aug_moorage = []
with open('billing_transactions_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['post_date'].startswith('2026-08') and r['txn_type']=='MONTHLY_MOORAGE':
            aug_moorage.append(r)
billed_ids = set(r['slip_id'] for r in aug_moorage)
missing_ids = set(occ.keys()) - billed_ids

print("=== BASELINE FLOOR candidates (317 missing slips) ===")
m_exp = sum(ch(occ[s]) for s in missing_ids)
print(f"MAX(ceil(LOA),slip) x rate: ${m_exp:,.2f}")
m_ceil_loa = sum(math.ceil(float(occ[s]['vessel_loa_ft']))*(10.40 if occ[s]['covered']=='COVERED' else 7.55) for s in missing_ids)
print(f"ceil(LOA) x rate: ${m_ceil_loa:,.2f}")
m_raw = sum(float(occ[s]['vessel_loa_ft'])*(10.40 if occ[s]['covered']=='COVERED' else 7.55) for s in missing_ids)
print(f"raw LOA x rate: ${m_raw:,.2f}")
m_slip = sum(float(occ[s]['slip_size_ft'])*(10.40 if occ[s]['covered']=='COVERED' else 7.55) for s in missing_ids)
print(f"slip_size x rate: ${m_slip:,.2f}")
# Old rate?
m_old = sum(bl(occ[s])*(9.85 if occ[s]['covered']=='COVERED' else 7.10) for s in missing_ids)
print(f"MAX x OLD rate (9.85/7.10): ${m_old:,.2f}")
m_old_ceil = sum(math.ceil(float(occ[s]['vessel_loa_ft']))*(9.85 if occ[s]['covered']=='COVERED' else 7.10) for s in missing_ids)
print(f"ceil(LOA) x OLD rate: ${m_old_ceil:,.2f}")
# covered only?
m_cov = sum(ch(occ[s]) for s in missing_ids if occ[s]['covered']=='COVERED')
m_open = sum(ch(occ[s]) for s in missing_ids if occ[s]['covered']!='COVERED')
print(f"Missing covered expected: ${m_cov:,.2f}, open: ${m_open:,.2f}")

print("\n=== Target: $99,629.80 ===")
# Try: missing slips at covered rate only, or various
for name, val in [("MAX old", m_old), ("ceil old", m_old_ceil), ("ceil loa", m_ceil_loa), ("raw", m_raw), ("slip", m_slip), ("MAX new", m_exp)]:
    print(f"  {name}: ${val:,.2f}  diff from target: ${val-99629.80:,.2f}")

# Maybe baseline floor = expected for missing using slip_size for covered, LOA for open?
def alt(s):
    if s['covered']=='COVERED':
        return float(s['slip_size_ft'])*10.40
    return math.ceil(max(float(s['vessel_loa_ft']), float(s['slip_size_ft'])))*7.55
m_alt = sum(alt(occ[s]) for s in missing_ids)
print(f"  alt (slip*10.40 cov, MAX*7.55 open): ${m_alt:,.2f}")

# Try: what's 99629.80 / 317?
print(f"  99629.80 / 317 = {99629.80/317:.2f} per slip")
print(f"  120158.25 / 317 = {120158.25/317:.2f} per slip")
