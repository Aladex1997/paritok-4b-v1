import zipfile
import xml.etree.ElementTree as ET
import os
import re

base = "eval_responses/RESPONSE 7"
docs = [
    "RESPONSE 2/kvl_compliance_memo.docx",
    "RESPONSE 3/kvl_compliance_memo.docx",
    "RESPONSE 4/kvl_compliance_memo (1).docx",
    "Response 5/kvl_compliance_memo (2).docx",
    "RESPONSE 6/kvl_compliance_memo (3).docx",
    "RESPONSE 7/kvl_compliance_memo (5).docx",
    "RESPONSE 8/kvl_compliance_memo (5).docx",
]

for doc in docs:
    path = os.path.join(base, doc)
    print(f"\n{'='*80}")
    print(f"MODEL: {doc}")
    print(f"{'='*80}")
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
        print(full[:8000])
    except Exception as e:
        print(f"ERROR: {e}")
