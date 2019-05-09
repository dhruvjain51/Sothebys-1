from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time


es = Elasticsearch(['es'])
consumer = KafkaConsumer('painting-topic', group_id='painting-indexer', bootstrap_servers=['kafka:9092'])
for message in consumer:
    json_data = (json.loads((message.value).decode('utf-8')))
    painting = json_data[0]
    es.index(index='painting_index', doc_type='listing', id=painting.get('id'), body=painting)
    es.indices.refresh(index="painting_index")
    