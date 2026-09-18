import zipfile
import xml.etree.ElementTree as ET
import os
import re
import json

base = "rep1_responses/REP 1"
docs = {
    "M1": "kvl_compliance_memo (10).docx",
    "M2": "REP 2/kvl_compliance_memo (10).docx",
    "M3": "REP3/kvl_compliance_memo (10).docx",
    "M4": "REP 4/kvl_compliance_memo (10).docx",
    "M5": "REP 5/kvl_compliance_memo (10).docx",
    "M6": "REP 6/kvl_compliance_memo (10).docx",
    "M7": "REP 7/kvl_compliance_memo (10).docx",
    "M8": "REP 8/kvl_compliance_memo (10).docx",
}

results = {}
for label, doc in docs.items():
    path = os.path.join(base, doc)
    try:
        z = zipfile.ZipFile(path)
        xml = z.read("word/document.xml")
        root = ET.fromstring(xml)
        texts = []
        for el in root.iter():
            if el.text: texts.append(el.text)
            if el.tail: texts.append(el.tail)
        full = " ".join(texts)
        full = re.sub(r'\s+', ' ', full).strip()
        results[label] = full
        print(f"{label}: {len(full)} chars")
    except Exception as e:
        print(f"{label}: ERROR {e}")

with open('rep1_responses/rep1_texts.json', 'w') as f:
    json.dump(results, f)
print(f"\nSaved {len(results)} responses")
