from elasticsearch import Elasticsearch

INDEX_NAME = "vitoshacademy_data"
ES_HOST = "http://127.0.0.1:9200"

# SEARCH SETTINGS
    # "AUTO" allows typos (e.g. "frog" finds "from")
    # "0" means exact match only
FUZZINESS_LEVEL = "0"

# "title^2" - matches in the title are 2x more important than body text.
SEARCH_FIELDS = ["title^2", "content", "url"] 

es = Elasticsearch(ES_HOST)

def search_vitosh(query):
    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": SEARCH_FIELDS,
                    "fuzziness": FUZZINESS_LEVEL
                }
            },
            "highlight": {
                "fields": {
                    "content": {}
                }
            }
        }
    )
    return response['hits']['hits']

if __name__ == "__main__":
    print(f"--- VitoshAcademy Search Engine ---")
    print(f"Mode: Exact Match (Fuzziness: {FUZZINESS_LEVEL})")
    print("Type 'exit' to quit.")
    
    while True:
        query = input("\nEnter search term: ")
        if query.lower() == 'exit':
            break
            
        try:
            results = search_vitosh(query)
            
            if not results:
                print("No results found.")
            else:
                print(f"Found {len(results)} pages:\n")
                for hit in results[:5]: 
                    source = hit['_source']
                    score = hit['_score']
                    
                    # Highlight logic
                    if 'highlight' in hit:
                        snippet = " ".join(hit['highlight']['content'][:2])
                    else:
                        snippet = source['content'][:150]
                        
                    print(f"Title: {source['title']}")
                    print(f"Link:  {source['url']}")
                    print(f"Match: ...{snippet.strip()}...\n")
                    
        except Exception as e:
            print(f"Error: {e}")