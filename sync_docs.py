import os
import html2text
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Caminho do arquivo de chave do serviço
SERVICE_ACCOUNT_FILE = 'docstomarkdownsync.json' 
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

def load_credentials():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError(f"❌ Arquivo de credencial não encontrado: {SERVICE_ACCOUNT_FILE}")
    return service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def extract_markdown(service, doc_id):
    try:
        doc = service.documents().get(documentId=doc_id).execute()
        content = doc.get('body', {}).get('content', [])
        html = ""
        for e in content:
            if 'paragraph' in e:
                for run in e['paragraph'].get('elements', []):
                    html += run.get('textRun', {}).get('content', '') + '\n'
        return html2text.html2text(html)
    except Exception as e:
        print(f"⚠️ Erro ao extrair conteúdo do documento {doc_id}: {e}")
        return ""

def main():
    credentials = load_credentials()
    service = build('docs', 'v1', credentials=credentials)

    for doc in documents:
        print(f"🔄 Sincronizando {doc['id']} -> {doc['output']}...")
        markdown = extract_markdown(service, doc["id"])
        if markdown:
            os.makedirs(os.path.dirname(doc["output"]), exist_ok=True)
            with open(doc["output"], 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"✅ Documento sincronizado: {doc['output']}")
        else:
            print(f"❌ Falha ao sincronizar: {doc['output']}")

if __name__ == "__main__":
    main()
