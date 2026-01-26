# Elasticsearch with Python

## Chrome
```
http://127.0.0.1:9200/vitosh_data/_search?pretty=true&size=2
http://127.0.0.1:9200/_cat/indices?v
http://127.0.0.1:9200/vitosh_data/_search?q=title:vba&pretty=true
http://127.0.0.1:9200/vitosh_data/_search?q=title:Python+or+VBA+content:PYTHON+VBA&pretty=true
http://127.0.0.1:9200/vitosh_data/_search?q=content:C%2B%2B&pretty=true
```

## Docker:
```
docker run --name kib01 --net elastic -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01:9200" docker.elastic.co/kibana/kibana:8.11.1
```

## YouTube:
https://youtu.be/Wucy4jbAi5g?si=pWFJ13wfUfBFW2mF

## VitoshAcademy:
https://www.vitoshacademy.com/elastic-search-simple-introduction-and-web-app/