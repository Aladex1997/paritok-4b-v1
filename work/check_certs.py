import csv

print("=== Certificate holders in applicant_register ===")
with open('applicant_register_2026-08.csv') as f:
    for r in csv.DictReader(f):
        if r.get('applicant_id') in ('WL-01893', 'WL-02401'):
            print(r)

print()
print("=== Vessel names MARBLE WING / COHO RUN in slip_inventory ===")
with open('slip_inventory_2026-08.csv') as f:
    for r in csv.DictReader(f):
        if r['vessel_name'] in ('MARBLE WING', 'COHO RUN'):
            print(r)

print()
print("=== slip_inventory columns ===")
with open('slip_inventory_2026-08.csv') as f:
    r = next(csv.DictReader(f))
    print(list(r.keys()))
    print(r)