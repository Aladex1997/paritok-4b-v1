import re, zlib, glob

for f in ['resolution_2022-06.pdf', 'standing_order_15-3.pdf', 'tariff_resolution_2019-14.pdf', 'appeal_2018-3_decision.pdf']:
    data = open(f, 'rb').read()
    out = []
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.DOTALL):
        try:
            dec = zlib.decompress(m.group(1))
            text = re.sub(rb'[^\x20-\x7E\n\t]', b' ', dec)
            text = re.sub(rb'\s+', b' ', text).decode('latin-1')
            out.append(text)
        except Exception:
            pass
    full = ' '.join(out)
    print(f'========== {f} ==========')
    # Print the whole thing in chunks
    for i in range(0, len(full), 1200):
        print(full[i:i+1200])
    print()
    print('===============================')