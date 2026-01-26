import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch, helpers
from urllib.parse import urljoin, urlparse

# CONFIG
SEED_URL = "https://www.vitoshacademy.com/"
INDEX_NAME = "vitoshacademy_data"
ES_HOST = "http://127.0.0.1:9200"

def run_crawler():
    es = Elasticsearch(ES_HOST)
    
    # 1. Clean Slate: Delete old index if exists
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
    es.indices.create(index=INDEX_NAME)

    visited = set()
    queue = [SEED_URL]
    docs_buffer = []

    print(f"🕷️ Crawling {SEED_URL}...")

    while queue and len(visited) < 40: # Limit to 40 pages
        url = queue.pop(0)
        if url in visited: 
            continue
        try:
            # 2. Fetch Page
            resp = requests.get(url, timeout=3)
            if resp.status_code != 200: 
                continue
            
            # 3. Parse HTML
            soup = BeautifulSoup(resp.content, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            title = soup.title.string if soup.title else url

            # 4. Prepare Document (JSON)
            docs_buffer.append({
                "_index": INDEX_NAME,
                "_source": {"title": title, "url": url, "content": text}
            })
            visited.add(url)
            print(f"[{len(visited)}] Indexed: {title[:40]}...")

            # 5. Find new links
            for link in soup.find_all('a', href=True):
                full_link = urljoin(url, link['href'])
                if "vitoshacademy.com" in urlparse(full_link).netloc:
                    if full_link not in visited:
                        queue.append(full_link)
                else: 
                    print(f"Skipping external link: {full_link}")

        except Exception as e:
            print(f"Error: {e}")

    # 6. Bulk Upload to Elasticsearch
    if docs_buffer:
        helpers.bulk(es, docs_buffer)
        print(f"✅ Successfully uploaded {len(docs_buffer)} pages!")

if __name__ == "__main__":
    run_crawler()