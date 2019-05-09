from data.kafka import KafkaConsumer
import json

consumer = KafkaConsumer('recommendation-topic', group_id='recommendation-indexer', bootstrap_servers=['kafka:9092'])
for message in consumer:
    json_data = (json.loads((message.value).decode('utf-8')))
    painting = json_data['painting_id']
    user = json_data['user_id']
    f = open("access.log", "a+")
    f.write(user + "\t" + painting)