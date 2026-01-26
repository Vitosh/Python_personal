from elasticsearch import Elasticsearch

es = Elasticsearch("http://127.0.0.1:9200")

def search(query):
    resp = es.search(
        index="vitosh_data_txt",
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["content", "title"],
                    "fuzziness": "AUTO"
                }
            },
            "highlight": {
                "fields": {"content": {}},
                "pre_tags": ["<b>"],
                "post_tags": ["</b>"]
            }
        }
    )
    return resp['hits']['hits']

if __name__ == "__main__":
    while True:
        q = input("\n🔍 Search (or 'exit'): ")
        if q == "exit": break
        
        hits = search(q)
        print(f"Found {len(hits)} results:")
        for hit in hits[:3]:
            title = hit['_source']['title']
            snippet = hit['highlight']['content'][0] if 'highlight' in hit else hit['_source']['content'][:100]
            print(f"📄 {title} \n   ...{snippet}...\n")