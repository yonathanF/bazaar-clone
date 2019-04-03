from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

consumer = KafkaConsumer('new-posts', group_id='creating-posts', bootstrap_servers=['kafka:9092'], auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

esbody = {
    "mappings": {
        "post": {
            "properties":{
                "title": {
                    "type": "text"
                },
                "details": {
                    "type": "text"
                },
                "zip_code": {
                    "type": "integer"
                },
                "user":{
                    "type": "integer"
                },
                "date_created": {
                    "type": "date"
                },
                "deadline": {
                    "type": "date"
                },
                "preferred_contact": {
                    "type": "text"
                },
                "category":{
                    "type": "text"
                },
                "request_type": {
                    "type": "text"
                }
            }
        }
    }
}

es = Elasticsearch(['elasticsearch'])
es.indices.create(index="bazaar", body=esbody, ignore=[400, 404])

while(1):
    for message in consumer:
        post_id = message.value['id']
        post = message.value['post']
        es.index(index="bazaar", id=post_id, body = post, doc_type = "post")
        es.indices.refresh(index="bazaar")
        