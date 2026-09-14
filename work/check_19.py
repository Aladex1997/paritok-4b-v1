import csv
from collections import Counter
ENC = 'utf-8-sig'

skips = []
with open('skip_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if '2023-01-01' <= r['skip_date'] <= '2026-07-31':
            skips.append(r)

# 19 skips with documentation_attached = N
no_doc = [s for s in skips if s['documentation_attached'] == 'N']
print(f"Skips with documentation_attached='N': {len(no_doc)}")
for s in no_doc:
    print(f"  {s['skip_id']} {s['applicant_id']} skip={s['skip_date']} review={s['review_date']} "
          f"reason={s['reason_code']} doc_type='{s['documentation_type']}' rank={s['rank_at_offer']}")

# Check: of the 45 with review<=skip, how many have doc_attached=Y
ontime = [s for s in skips if s['review_date'] <= s['skip_date']]
print(f"\nreview<=skip: {len(ontime)}")
print(f"  of those, doc_attached=Y: {sum(1 for s in ontime if s['documentation_attached']=='Y')}")
print(f"  of those, doc_attached=N: {sum(1 for s in ontime if s['documentation_attached']=='N')}")

# The 6 PDF applicants - check their skips
pdf_apps = {'WL-02211','WL-02618','WL-02877','WL-03044','WL-03102','WL-03390'}
print(f"\n=== PDF applicant skips (all, including out of scope) ===")
with open('skip_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] in pdf_apps:
            print(f"  {r['applicant_id']} {r['skip_id']} skip={r['skip_date']} review={r['review_date']} "
                  f"reason={r['reason_code']} slip={r['slip_id']} offer={r['offer_id']} doc_attached={r['documentation_attached']}")

# Triage: what gives 7/16/9 = 32?
# Hypothesis: 19 no-doc skips + 11 unsupported LOA + ... 
# Let's see: 19 + 11 = 30. Need 32. 
# Maybe 19 skips + 13 something = 32? Or the 19 includes some LOA-related?
print(f"\n=== Triage math check ===")
print(f"19 (no-doc skips) + 11 (unsupported LOA) = 30")
print(f"7 + 16 + 9 = 32")
print(f"Difference: 2")

# Check: unsupported LOA amendments with downstream skip = 23 (from earlier)
# unsupported without downstream = 176
# Unique unsupported applicants = 196
