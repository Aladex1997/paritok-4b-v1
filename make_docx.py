import zipfile
import os
import sys

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

CORE_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>KVL Compliance Memo</dc:title>
<dc:creator>Operations Director</dc:creator>
<cp:lastModifiedBy>Operations Director</cp:lastModifiedBy>
<dc:date>2026-07-01T00:00:00</dc:date>
</cp:coreProperties>'''

APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>KVL Compliance Memo</Application>
</Properties>'''

RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

DOC_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

STYLES_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<style w:type="paragraph" w:styleId="Normal"><w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/></w:rPr></w:pPr></style>
</styleSheet>'''

def make_docx(text_content, filename):
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', RELS)
        z.writestr('docProps/core.xml', CORE_XML)
        z.writestr('docProps/app.xml', APP_XML)
        z.writestr('word/document.xml', text_content)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('word/styles.xml', STYLES_XML)
        z.writestr('word/settings.xml', '<?xml version="1.0"?><w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"></w:settings>')
    print(f"Created {filename}")

def text_to_xml(text):
    paragraphs = text.split('\n')
    xml_parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                 '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">',
                 '<w:body>']
    for p in paragraphs:
        p = p.strip()
        if not p:
            xml_parts.append('<w:p><w:pPr><w:pStyle w:val="Normal"/></w:pPr></w:p>')
        else:
            xml_parts.append(f'<w:p><w:pPr><w:pStyle w:val="Normal"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/></w:rPr><w:t>{p}</w:t></w:r></w:p>')
    xml_parts.append('</w:body></w:document>')
    return '\n'.join(xml_parts)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: make_docx.py <text>_file output.docx")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        text = f.read()
    xml = text_to_xml(text)
    make_docx(xml, sys.argv[2])
