# Save as app.py
import os
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch("http://127.0.0.1:9200")

# Point this to your text files folder so we can open them!
DATA_DIR = os.path.join("dox", "EN", "raw-documents")

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""
    
    if request.method == "POST":
        query = request.form["search_term"]
        
        # Searching BOTH indices (Web + Txt) at the same time
        resp = es.search(
            index="vitosh_data_txt, vitosh_data", 
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
                    "pre_tags": ["<mark>"],
                    "post_tags": ["</mark>"],
                    "fragment_size": 300,   # <--- Shows ~3 lines of text
                    "number_of_fragments": 1
                }
            }
        )
        results = resp['hits']['hits']

    return render_template("index.html", results=results, query=query)

# NEW: A route to actually read the file when clicked
@app.route("/view/<filename>")
def view_document(filename):
    try:
        path = os.path.join(DATA_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"<pre style='white-space: pre-wrap; font-family: sans-serif; padding: 20px;'>{content}</pre>"
    except FileNotFoundError:
        return "<h3>File not found on server disk.</h3>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)