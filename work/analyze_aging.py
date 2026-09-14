import zipfile, re, csv, math
from collections import Counter, defaultdict

ENC = 'utf-8-sig'

# Load slip inventory
slips = {}
with open('slip_inventory_2026-08.csv', encoding=ENC) as f:
    for r in csv.DictReader(f):
        slips[r['slip_id']] = r
occ = {sid: s for sid, s in slips.items() if s['status'] == 'OCCUPIED'}

# Read ar_aging
z = zipfile.ZipFile('ar_aging_2026-07-31.xlsx')
content = z.read('xl/worksheets/sheet1.xml').decode('utf-8')
rows = re.findall(r'<row[^>]*>(.*?)</row>', content, re.DOTALL)

aging = []
for row_data in rows[1:]:
    cells = re.findall(r'<c([^>]*?)>(.*?)</c>', row_data, re.DOTALL)
    vals = []
    for attrs, cell_data in cells:
        v_match = re.search(r'<v>([^<]+)</v>', cell_data)
        t_match = re.search(r'<t[^>]*>(.*?)</t>', cell_data, re.DOTALL)
        is_str = 't="s"' in attrs
        if v_match and is_str:
            vals.append(v_match.group(1))
        elif t_match:
            vals.append(t_match.group(1))
        elif v_match:
            vals.append(v_match.group(1))
    if len(vals) >= 11 and vals[0].startswith('AC-'):
        aging.append(vals)

print(f"AR aging accounts: {len(aging)}")

# Over 90 days: days_90 + days_120_plus > 0
over90 = [a for a in aging if float(a[7]) + float(a[8]) > 0]
print(f"Accounts over 90 days (90+120+ > 0): {len(over90)}")
for a in over90:
    print(f"  {a[0]} {a[1]} slip={a[2]} 90={a[7]} 120+={a[8]} total={a[10]} status={a[12]}")

# Occupied over-90 accounts
occ_over90 = [a for a in over90 if a[2] in occ]
print(f"\nOver-90 accounts with OCCUPIED slip: {len(occ_over90)}")
for a in occ_over90:
    print(f"  {a[0]} {a[1]} slip={a[2]} basin={a[3]} 90={a[7]} 120+={a[8]} total={a[10]}")

# The 6 from the golden memo
six_ids = ['AC-LP-0122','AC-LP-0402','AC-LP-0602','AC-LP-0605','AC-LP-0713','AC-LP-0801']
print(f"\n=== The 6 memo accounts ===")
six = [a for a in aging if a[0] in six_ids]
for a in six:
    s = occ.get(a[2], {})
    print(f"  {a[0]} {a[1]} slip={a[2]} basin={a[3]} cur={a[5]} 30={a[6]} 60={a[7]} 90={a[8]} 120+={a[9]} total={a[10]} status={a[12]} slip_status={s.get('status','N/A')}")

# Sum of 90+120+ for the 6
sum_90_120 = sum(float(a[8]) + float(a[9]) for a in six)
print(f"\nSum of 90+120+ buckets for 6 accounts: ${sum_90_120:,.2f}")
sum_total = sum(float(a[10]) for a in six)
print(f"Sum of total_due for 6 accounts: ${sum_total:,.2f}")

# All over-90 occupied: sum of 90+120+
all_90_120 = sum(float(a[8]) + float(a[9]) for a in occ_over90)
print(f"\nAll occupied over-90: 90+120+ sum = ${all_90_120:,.2f}")

# Bucket sums
buck = {'Current':0,'30':0,'60':0,'90':0,'120+':0}
for a in aging:
    buck['Current'] += float(a[5]); buck['30'] += float(a[6]); buck['60'] += float(a[7]); buck['90'] += float(a[8]); buck['120+'] += float(a[9])
print(f"\nBucket sums: { {k: round(v,2) for k,v in buck.items()} }")
print(f"Total (all buckets): ${sum(buck.values()):,.2f}")
print(f"90+120+: ${buck['90']+buck['120+']:,.2f}")

# Ledger total
ledger = sum(float(a[10]) for a in aging)
print(f"Ledger total_due sum: ${ledger:,.2f}")
print(f"True bucket total - Ledger: ${sum(buck.values()) - ledger:,.2f}")

# Subledger errors
errors = [a for a in aging if abs(sum(float(a[i]) for i in range(5,10)) - float(a[10])) > 0.001]
print(f"\nSubledger errors (sum buckets != total_due): {len(errors)}")
err_total = sum(float(a[10]) for a in errors)
print(f"Sum of total_due for error rows: ${err_total:,.2f}")

# Missing from aging
aging_slips = set(a[2] for a in aging)
missing_from_aging = set(occ.keys()) - aging_slips
print(f"\nOccupied slips missing from aging: {len(missing_from_aging)}")

# Check sheet2
content2 = z.read('xl/worksheets/sheet2.xml').decode('utf-8')
rows2 = re.findall(r'<row[^>]*>(.*?)</row>', content2, re.DOTALL)
print("\n=== Sheet2 (summary) ===")
for row_data in rows2:
    cells = re.findall(r'<c([^>]*?)>(.*?)</c>', row_data, re.DOTALL)
    vals = []
    for attrs, cell_data in cells:
        v_match = re.search(r'<v>([^<]+)</v>', cell_data)
        t_match = re.search(r'<t[^>]*>(.*?)</t>', cell_data, re.DOTALL)
        is_str = 't="s"' in attrs
        if v_match and is_str:
            vals.append(v_match.group(1))
        elif t_match:
            vals.append(t_match.group(1))
        elif v_match:
            vals.append(v_match.group(1))
    print(' | '.join(vals))
