import csv
from collections import Counter

ENC = 'utf-8-sig'
skips = []
with open('skip_events_2022_2026.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        if '2023-01-01' <= r['skip_date'] <= '2026-07-31':
            skips.append(r)
print(f"In-scope skips: {len(skips)}")

# Distribution of review_date vs skip_date
same_day = [s for s in skips if s['review_date'] == s['skip_date']]
on_or_before = [s for s in skips if s['review_date'] <= s['skip_date']]
after = [s for s in skips if s['review_date'] > s['skip_date']]
print(f"review_date == skip_date (same day): {len(same_day)}")
print(f"review_date <= skip_date (on or before): {len(on_or_before)}")
print(f"review_date > skip_date (after): {len(after)}")

# Gap distribution
from collections import Counter
gaps = Counter()
for s in skips:
    from datetime import date
    d1 = date.fromisoformat(s['skip_date'])
    d2 = date.fromisoformat(s['review_date'])
    gaps[d2-d1] += 1
print(f"\nGap (review - skip) distribution: {sorted(gaps.items())}")

# PDF applicants
pdf_apps = {'WL-02211','WL-02618','WL-02877','WL-03044','WL-03102','WL-03390'}
# Skips with a PDF that is on-or-before
pdf_ontime = [s for s in skips if s['applicant_id'] in pdf_apps and s['review_date'] <= s['skip_date']]
print(f"\nSkips with PDF AND review<=skip: {len(pdf_ontime)}")
# Skips with a PDF but review > skip (late)
pdf_late = [s for s in skips if s['applicant_id'] in pdf_apps and s['review_date'] > s['skip_date']]
print(f"Skips with PDF but review>skip (late): {len(pdf_late)}")
for s in pdf_late:
    print(f"  {s['applicant_id']} skip={s['skip_date']} review={s['review_date']}")

# Skips with review <= skip but NO pdf
nopdf_ontime = [s for s in skips if s['review_date'] <= s['skip_date'] and s['applicant_id'] not in pdf_apps]
print(f"\nSkips review<=skip but NO pdf: {len(nopdf_ontime)}")

# What if "contemporaneous proof" = review on/before AND pdf exists, but only counting skips that have SOME pdf?
# 19 could be: skips whose applicant has a PDF file at all (regardless of date)
any_pdf = [s for s in skips if s['applicant_id'] in pdf_apps]
print(f"\nSkips whose applicant has any PDF: {len(any_pdf)}")

# Skips with review_date exactly on skip_date AND pdf
same_and_pdf = [s for s in skips if s['review_date']==s['skip_date'] and s['applicant_id'] in pdf_apps]
print(f"Same-day AND pdf: {len(same_and_pdf)}")

# Check: maybe 19 = number of distinct (skip) events that are "substantiated" some other way
# Let's check documentation_attached field
print(f"\ndocumentation_attached values: {Counter(s['documentation_attached'] for s in skips)}")
print(f"documentation_type values: {Counter(s['documentation_type'] for s in skips)}")

# Maybe skips where documentation_attached == Y AND review <= skip_date
doc_ontime = [s for s in skips if s['documentation_attached']=='Y' and s['review_date'] <= s['skip_date']]
print(f"documentation_attached=Y AND review<=skip: {len(doc_ontime)}")
