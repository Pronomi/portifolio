from google.oauth2 import service_account
from googleapiclient.discovery import build
import html2text
import os

SERVICE_ACCOUNT_FILE = 'docstomarkdownsync-ebfb3ef29999.json'
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# Lista de documentos e destinos
documents = [
    {
        "id": "I14V_goCmIv11WLZJd-MpHo2M6v_0qDtw198dFgXT64Eg",
        "output": "pages/anotacao1.md"
    },
    {
        "id": "1Q4gd0-dn8wQqYQFRa7hUzLRdgSHUj7lh-lwMd7Vj04k",
        "output": "pages/anotacao2.md"
    },
    {
        "id": "1UdQlSk2lgv5tQxxQtkGsRgSCXtW681ogF3th-Z3Psvo",
        "output": "pages/anotacao3.md"
    }
]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('docs', 'v1', credentials=credentials)

def extract_markdown(doc_id):
    doc = service.documents().get(documentId=doc_id).execute()
    content = doc.get('body').get('content')
    
    html = ""
    for e in content:
        if 'paragraph' in e:
            for run in e['paragraph'].get('elements', []):
                html += run.get('textRun', {}).get('content', '') + '\n'
    
    return html2text.html2text(html)

for doc in documents:
    markdown = extract_markdown(doc["id"])
    os.makedirs(os.path.dirname(doc["output"]), exist_ok=True)
    with open(doc["output"], 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"✔ Documento sincronizado: {doc['output']}")
