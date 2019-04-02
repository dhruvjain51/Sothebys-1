from kafka import KafkaProducer
import requests
import json

producer = KafkaProducer(bootstrap_servers='kafka:9092')
response = requests.get('http://models-api:8000/api/v1/paintings/')
json_data = json.loads(response.text)
producer.send('painting-load', json.dumps(json_data).encode('utf-8'))