import csv, re, zlib

def pdf_text(path):
    data = open(path, 'rb').read()
    out = []
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.DOTALL):
        try:
            dec = zlib.decompress(m.group(1))
            text = re.sub(rb'[^\x20-\x7E\n\t]', b' ', dec)
            text = re.sub(rb'\s+', b' ', text).decode('latin-1')
            out.append(text)
        except Exception:
            pass
    return ' '.join(out)

for f in ['2025-06-29_haul_out_WL-03102_foldview.pdf', '2024-09-12_haul_out_WL-02087_foldview.pdf']:
    print(f'=== {f} ===')
    print(pdf_text(f)[1800:5000])
    print()

print("=== WL-03102 LOA amendments ===")
with open('amendment_log_2022_2026.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] == 'WL-03102' and r['field_code'] == 'LOA':
            print(r)

print()
print("=== WL-02087 LOA amendments ===")
with open('amendment_log_2022_2026.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        if r['applicant_id'] == 'WL-02087' and r['field_code'] == 'LOA':
            print(r)