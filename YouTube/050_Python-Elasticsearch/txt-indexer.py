import os
from elasticsearch import Elasticsearch, helpers

DATA_DIR = os.path.join("dox", "EN", "raw-documents") 
INDEX_NAME = "vitosh_data_txt"
es = Elasticsearch("http://127.0.0.1:9200")

def run_indexer():
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
    es.indices.create(index=INDEX_NAME)

    documents = []
    
    if not os.path.exists(DATA_DIR):
        print("❌ Error: Folder not found!")
        return

    print(f"📂 Reading files from {DATA_DIR}...")
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(DATA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                
            documents.append({
                "_index": INDEX_NAME,
                "_source": {"title": filename, "content": text}
            })

    helpers.bulk(es, documents)
    print(f"✅ Indexed {len(documents)} text files!")

if __name__ == "__main__":
    run_indexer()