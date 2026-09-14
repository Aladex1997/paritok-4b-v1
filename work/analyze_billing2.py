import csv, math, zipfile, re
from collections import Counter, defaultdict

ENC = 'utf-8-sig'

# Load slip inventory
slips = {}
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        slips[r['slip_id']] = r
occ = {sid: s for sid, s in slips.items() if s['status'] == 'OCCUPIED'}

def billable_length(s):
    return math.ceil(max(float(s['vessel_loa_ft']), float(s['slip_size_ft'])))

def expected_charge(s):
    bl = billable_length(s)
    rate = 10.40 if s['covered'] == 'COVERED' else 7.55
    return bl * rate

expected_total = sum(expected_charge(s) for s in occ.values())
print(f"Expected monthly moorage (all {len(occ)} occupied): ${expected_total:,.2f}")

# Load August billing
aug_moorage = []
with open('billing_transactions_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['post_date'].startswith('2026-08') and r['txn_type'] == 'MONTHLY_MOORAGE':
            aug_moorage.append(r)

billed_total = sum(float(r['total_amount']) for r in aug_moorage)
amount_total = sum(float(r['amount']) for r in aug_moorage)
print(f"August moorage total_amount (before tax): ${amount_total:,.2f}")
print(f"August moorage total (with tax): ${billed_total:,.2f}")

# PAID only
paid_moorage = [r for r in aug_moorage if r['payment_status'] == 'PAID']
paid_total = sum(float(r['total_amount']) for r in paid_moorage)
paid_amount = sum(float(r['amount']) for r in paid_moorage)
print(f"August PAID moorage amount: ${paid_amount:,.2f}")
print(f"August PAID moorage total: ${paid_total:,.2f}")

# UNPAID (OPEN + LATE)
unpaid_moorage = [r for r in aug_moorage if r['payment_status'] != 'PAID']
unpaid_total = sum(float(r['total_amount']) for r in unpaid_moorage)
print(f"August UNPAID moorage total: ${unpaid_total:,.2f}")

# Check: expected - billed
print(f"\nVariance (expected - billed total): ${expected_total - billed_total:,.2f}")
print(f"Variance (expected - billed amount): ${expected_total - amount_total:,.2f}")

# Missing slips expected
billed_ids = set(r['slip_id'] for r in aug_moorage)
missing_ids = set(occ.keys()) - billed_ids
missing_expected = sum(expected_charge(occ[sid]) for sid in missing_ids)
print(f"\nMissing slips: {len(missing_ids)}, their expected: ${missing_expected:,.2f}")

# Baseline floor concept: expected for missing slips
print(f"Baseline Floor candidate (missing expected): ${missing_expected:,.2f}")

# Check golden values
print(f"\nGolden Exported Revenue: $319,760.05")
print(f"Golden Monthly Exposure: $120,158.25")
print(f"Golden Baseline Floor: $99,629.80")
print(f"Golden Expected - Golden Exported = ${439918.30 - 319760.05:,.2f}")

# What gives 319,760.05?
# Try: PAID moorage amount + something
print(f"\n319,760.05 - paid_amount({paid_amount:,.2f}) = ${319760.05 - paid_amount:,.2f}")
print(f"319,760.05 - paid_total({paid_total:,.2f}) = ${319760.05 - paid_total:,.2f}")
print(f"billed_total({billed_total:,.2f}) - 319,760.05 = ${billed_total - 319760.05:,.2f}")

# Try: amount for OPEN+LATE only
open_late = [r for r in aug_moorage if r['payment_status'] in ('OPEN','LATE')]
ol_amount = sum(float(r['amount']) for r in open_late)
ol_total = sum(float(r['total_amount']) for r in open_late)
print(f"\nOPEN+LATE moorage amount: ${ol_amount:,.2f}, total: ${ol_total:,.2f}")
print(f"billed_total - ol_total = ${billed_total - ol_total:,.2f}")

# Try PAID + OPEN (not LATE)
po = [r for r in aug_moorage if r['payment_status'] in ('PAID','OPEN')]
po_total = sum(float(r['total_amount']) for r in po)
po_amount = sum(float(r['amount']) for r in po)
print(f"PAID+OPEN moorage amount: ${po_amount:,.2f}, total: ${po_total:,.2f}")

# Maybe exported = sum of amount for all moorage rows where slip is occupied
occ_moorage = [r for r in aug_moorage if r['slip_id'] in occ]
occ_amount = sum(float(r['amount']) for r in occ_moorage)
occ_total = sum(float(r['total_amount']) for r in occ_moorage)
print(f"\nOccupied-slip moorage amount: ${occ_amount:,.2f}, total: ${occ_total:,.2f}")

# Check electricity amounts
elec = [r for r in aug_moorage if False]  # placeholder
with open('billing_transactions_2022_2026.csv', encoding=ENC) as f:
    elec_rows = [r for r in csv.DictReader(f) if r['post_date'].startswith('2026-08') and r['txn_type'] == 'ELECTRICITY']
elec_amount = sum(float(r['amount']) for r in elec_rows)
elec_total = sum(float(r['total_amount']) for r in elec_rows)
print(f"\nAugust ELECTRICITY amount: ${elec_amount:,.2f}, total: ${elec_total:,.2f}")
print(f"All August amount: ${amount_total + elec_amount:,.2f}")
print(f"All August total: ${billed_total + elec_total:,.2f}")