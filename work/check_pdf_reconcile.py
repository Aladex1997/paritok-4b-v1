import csv

ENC = 'utf-8-sig'

pdf_applicants = {'WL-02211', 'WL-02618', 'WL-02877', 'WL-03044', 'WL-03102', 'WL-03390'}
pdf_slips = {'EW-0414', 'GW-0702', 'EW-0603', 'EW-0620', 'VB-0144', 'LP-0307'}
skip_slips = {'GW-0610', 'GW-1012', 'VB-0904', 'LP-0806', 'SB-0302', 'SB-0120'}

print("=== PDF applicants in offer_events ===")
with open('offer_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in pdf_applicants:
            print(f"  {r['applicant_id']}: offer={r['offer_id']} slip={r['slip_id']} date={r['offer_date']} outcome={r['outcome']} skip_reason={r['skip_reason_code']}")

print()
print("=== PDF slips in offer_events ===")
with open('offer_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['slip_id'] in pdf_slips:
            print(f"  {r['slip_id']}: offer={r['offer_id']} applicant={r['applicant_id']} date={r['offer_date']} outcome={r['outcome']}")

print()
print("=== PDF slips in slip_inventory ===")
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['slip_id'] in pdf_slips:
            print(f"  {r['slip_id']}: basin={r['basin']} covered={r['covered']} status={r['status']} tenant={r['tenant_id']}")

print()
print("=== skip_events slips in slip_inventory ===")
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['slip_id'] in skip_slips:
            print(f"  {r['slip_id']}: basin={r['basin']} covered={r['covered']} status={r['status']} tenant={r['tenant_id']}")

print()
print("=== WL-02211 all skips ===")
with open('skip_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] == 'WL-02211':
            print(f"  skip {r['skip_date']} review {r['review_date']} slip={r['slip_id']} reason={r['reason_code']}")