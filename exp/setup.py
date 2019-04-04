import time
import requests
import json
from elasticsearch import Elasticsearch

response = requests.get('http://models-api:8000/api/v1/paintings/')
json_data = json.loads(response.text)
es = Elasticsearch(['es'])

for i in json_data:
    es.index(index='painting_index', doc_type='listing', id=i.get('id'), body=i)

es.indices.refresh(index="painting_index")

