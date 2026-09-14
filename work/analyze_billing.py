import csv
from collections import Counter, defaultdict

ENC = 'utf-8-sig'

# Load slip inventory
slips = {}
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        slips[r['slip_id']] = r

occ = {sid: s for sid, s in slips.items() if s['status'] == 'OCCUPIED'}
print(f"Total slips: {len(slips)}, OCCUPIED: {len(occ)}")
print(f"Covered occupied: {sum(1 for s in occ.values() if s['covered']=='COVERED')}")
print(f"Open occupied: {sum(1 for s in occ.values() if s['covered']!='COVERED')}")

# Load August 2026 billing
aug_rows = []
with open('billing_transactions_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['post_date'].startswith('2026-08'):
            aug_rows.append(r)
print(f"\nAugust 2026 billing rows: {len(aug_rows)}")
print(f"By txn_type: {dict(Counter(r['txn_type'] for r in aug_rows))}")

# Monthly moorage only
moorage_rows = [r for r in aug_rows if r['txn_type'] == 'MONTHLY_MOORAGE']
print(f"August MONTHLY_MOORAGE rows: {len(moorage_rows)}")
aug_moorage_total = sum(float(r['total_amount']) for r in moorage_rows)
print(f"August MONTHLY_MOORAGE total: ${aug_moorage_total:,.2f}")

# Unique occupied slips billed
billed_occ = set(r['slip_id'] for r in moorage_rows if r['slip_id'] in occ)
print(f"Unique OCCUPIED slips with August moorage billing: {len(billed_occ)}")
missing = set(occ.keys()) - billed_occ
print(f"OCCUPIED slips MISSING August moorage billing: {len(missing)}")

# By basin
by_basin = Counter()
for sid in missing:
    by_basin[slips[sid]['basin']] += 1
print(f"Missing by basin: {dict(by_basin)}")

# Expected charges per Resolution 2022-06: covered=$10.40, open=$7.55
# Billable length per Res 2019-14 s.1(4): MAX(LOA rounded up, nominal slip length)
def billable_length(s):
    import math
    loa = float(s['vessel_loa_ft'])
    slip = float(s['slip_size_ft'])
    return math.ceil(max(loa, slip))

def expected_charge(s):
    bl = billable_length(s)
    rate = 10.40 if s['covered'] == 'COVERED' else 7.55
    return bl * rate

expected_total = sum(expected_charge(s) for s in occ.values())
print(f"\nExpected monthly moorage (all occupied, MAX(ceil(LOA),slip) x rate): ${expected_total:,.2f}")

# What about just ceil(LOA)?
def expected_ceil_loa(s):
    import math
    bl = math.ceil(float(s['vessel_loa_ft']))
    rate = 10.40 if s['covered'] == 'COVERED' else 7.55
    return bl * rate
exp_ceil_loa = sum(expected_ceil_loa(s) for s in occ.values())
print(f"Expected (ceil(LOA) only): ${exp_ceil_loa:,.2f}")

# What about raw LOA?
def expected_raw_loa(s):
    bl = float(s['vessel_loa_ft'])
    rate = 10.40 if s['covered'] == 'COVERED' else 7.55
    return bl * rate
exp_raw = sum(expected_raw_loa(s) for s in occ.values())
print(f"Expected (raw LOA): ${exp_raw:,.2f}")

# Variance
print(f"\nVariance (MAX formula): ${expected_total - aug_moorage_total:,.2f}")
print(f"Annualized: ${(expected_total - aug_moorage_total)*12:,.2f}")

# Check billed vs expected per slip for billed slips
print("\n=== Sample billed slips: billed amount vs expected ===")
count = 0
for sid in sorted(billed_occ):
    s = occ[sid]
    billed = sum(float(r['total_amount']) for r in moorage_rows if r['slip_id'] == sid)
    exp = expected_charge(s)
    if abs(billed - exp) > 0.01:
        if count < 15:
            print(f"  {sid}: billed=${billed:.2f} expected=${exp:.2f} diff=${billed-exp:.2f} "
                  f"loa={s['vessel_loa_ft']} slip={s['slip_size_ft']} covered={s['covered']}")
        count += 1
print(f"Total billed slips with variance: {count}")
