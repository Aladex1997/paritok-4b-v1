import csv

ENC = 'utf-8-sig'
valid_docs = {'WL-01893', 'WL-02401', 'WL-03102', 'WL-02087'}

print("=== LOA amendments for valid document holders ===")
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in valid_docs and r['field_code'] == 'LOA':
            print(f"  {r['applicant_id']}: {r['amendment_id']} {r['amendment_ts']} "
                  f"{r['old_value']} -> {r['new_value']} cert={r['requires_cert']} "
                  f"source={r['source_document']}")

print()
print("=== ALL amendments (any field) for valid doc holders ===")
with open('amendment_log_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in valid_docs:
            print(f"  {r['applicant_id']}: {r['amendment_id']} {r['amendment_ts']} "
                  f"{r['field_code']} {r['old_value']} -> {r['new_value']} cert={r['requires_cert']}")

print()
print("=== WL-01893 / WL-02401 / WL-03102 / WL-02087 in slip_inventory ===")
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['tenant_id'] in valid_docs:
            print(f"  {r['slip_id']}: tenant={r['tenant_id']} name={r['tenant_name']} "
                  f"vessel={r['vessel_name']} loa={r['vessel_loa_ft']} slip={r['slip_size_ft']} "
                  f"covered={r['covered']} status={r['status']}")

print()
print("=== WL-01893 / WL-02401 / WL-03102 / WL-02087 in applicant_register ===")
with open('applicant_register_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in valid_docs:
            print(f"  {r['applicant_id']}: {r['first_name']} {r['last_name']} vessel={r['vessel_name']} "
                  f"loa={r['loa_ft']} status={r['status']}")

print()
print("=== WL-01893 / WL-02401 / WL-03102 / WL-02087 in offer_events ===")
with open('offer_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in valid_docs:
            print(f"  {r['applicant_id']}: offer={r['offer_id']} slip={r['slip_id']} "
                  f"date={r['offer_date']} outcome={r['outcome']}")