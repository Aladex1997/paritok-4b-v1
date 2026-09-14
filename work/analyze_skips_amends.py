import csv, json
from collections import Counter, defaultdict
from datetime import date

# ============================================================
# 1. SKIP EVENTS ANALYSIS
# ============================================================
print("=" * 70)
print("1. SKIP EVENTS: Jan 1, 2023 - Jul 31, 2026")
print("=" * 70)

skips = []
with open('skip_events_2022_2026.csv') as f:
    for r in csv.DictReader(f):
        if '2023-01-01' <= r['skip_date'] <= '2026-07-31':
            skips.append(r)
print(f"In-scope skips: {len(skips)}")

# Justification PDFs available
pdf_applicants = {'WL-02211', 'WL-02618', 'WL-02877', 'WL-03044', 'WL-03102', 'WL-03390'}

# Contemporaneous proof: review_date <= skip_date AND PDF exists for that applicant
def has_contemp_proof(s):
    return s['review_date'] <= s['skip_date'] and s['applicant_id'] in pdf_applicants

fails = [s for s in skips if not has_contemp_proof(s)]
passes = [s for s in skips if has_contemp_proof(s)]
print(f"Contemporaneous proof PASS: {len(passes)}")
print(f"Contemporaneous proof FAIL: {len(fails)}")

# Which applicants have PDFs and their skip dates vs review dates
print("\nPDF applicants and their in-scope skips:")
for pid in sorted(pdf_applicants):
    matching = [s for s in skips if s['applicant_id'] == pid]
    for s in matching:
        late = s['review_date'] > s['skip_date']
        print(f"  {pid}: skip {s['skip_date']} review {s['review_date']} "
              f"{'LATE' if late else 'on-time'} slip={s['slip_id']} reason={s['reason_code']} "
              f"offer={s['offer_id']}")

# Check PDF reconciliation: PDFs reference slips - do they match skip_events?
print("\nPDF slip references vs skip_events slip_id:")
for pid in sorted(pdf_applicants):
    skip_rows = [s for s in skips if s['applicant_id'] == pid]
    for s in skip_rows:
        print(f"  {pid} skip says slip={s['slip_id']}")

# Reason code distribution
print("\nReason codes in-scope:", Counter(s['reason_code'] for s in skips))

# ============================================================
# 2. LENGTH AMENDMENT ANALYSIS
# ============================================================
print()
print("=" * 70)
print("2. LENGTH AMENDMENTS (LOA) on/after 2022-08-01")
print("=" * 70)

amends = []
with open('amendment_log_2022_2026.csv') as f:
    for r in csv.DictReader(f):
        if r['amendment_ts'] >= '2022-08-01':
            amends.append(r)
print(f"Total amendments post-2022-08-01: {len(amends)}")

loa_amends = [a for a in amends if a['field_code'] == 'LOA']
print(f"LOA amendments: {len(loa_amends)}")

# Certificate holders
cert_holders = {'WL-01893', 'WL-02401'}

# Check which LOA amendments have certificate support
supported = [a for a in loa_amends if a['applicant_id'] in cert_holders]
unsupported = [a for a in loa_amends if a['applicant_id'] not in cert_holders]
print(f"LOA amendments with certificate (WL-01893/WL-02401): {len(supported)}")
print(f"LOA amendments WITHOUT certificate: {len(unsupported)}")

# Check downstream skip events for unsupported amendments
skip_applicants = set(s['applicant_id'] for s in skips)
with_downstream = [a for a in unsupported if a['applicant_id'] in skip_applicants]
without_downstream = [a for a in unsupported if a['applicant_id'] not in skip_applicants]
print(f"Unsupported LOA amendments WITH downstream skip: {len(with_downstream)}")
print(f"Unsupported LOA amendments WITHOUT downstream skip: {len(without_downstream)}")

# Unique unsupported applicants
unsup_applicants = set(a['applicant_id'] for a in unsupported)
print(f"Unique applicants with unsupported LOA amendments: {len(unsup_applicants)}")
print("Sample:", sorted(unsup_applicants)[:20])

# Check requires_cert field
print("\nrequires_cert on LOA amendments:", Counter(a['requires_cert'] for a in loa_amends))
print("requires_cert on ALL post amendments:", Counter(a['requires_cert'] for a in amends))

# Certificate details
print("\n=== Certificate details ===")
print("WL-01893: MC-2024-0062, 2024-06-03, MARBLE WING, measured LOA 31.4 ft, beam 10.2, draft 5.4")
print("WL-02401: MC-2024-0091, 2024-09-03, COHO RUN, measured LOA 31.7 ft, beam 10.8, draft 3.1")
print("Register: WL-01893 loa=36.3 (cert says 31.4 - MISMATCH)")
print("Register: WL-02401 loa=31.7 (cert says 31.7 - MATCH)")