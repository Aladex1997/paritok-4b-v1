import zipfile
import xml.etree.ElementTree as ET
import os
import re
import json

base = "eval_responses/RESPONSE 7"
docs = {
    "R1": "RESPNSE 1/kvl_compliance_memo.docx",
    "R2": "RESPONSE 2/kvl_compliance_memo.docx",
    "R3": "RESPONSE 3/kvl_compliance_memo.docx",
    "R4": "RESPONSE 4/kvl_compliance_memo (1).docx",
    "R5": "Response 5/kvl_compliance_memo (2).docx",
    "R6": "RESPONSE 6/kvl_compliance_memo (3).docx",
    "R7": "kvl_compliance_memo (4).docx",
    "R8": "RESPONSE 8/kvl_compliance_memo (5).docx",
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
            if el.text:
                texts.append(el.text)
            if el.tail:
                texts.append(el.tail)
        full = " ".join(texts)
        full = re.sub(r'\s+', ' ', full).strip()
        results[label] = full
        print(f"{label}: {len(full)} chars")
    except Exception as e:
        print(f"{label}: ERROR {e}")

with open('eval_responses/response_texts.json', 'w') as f:
    json.dump(results, f)
print(f"\nSaved {len(results)} responses")
