import json

from elasticsearch import Elasticsearch
from kafka import KafkaConsumer

consumer = KafkaConsumer('new-posts',
                         group_id='creating-posts',
                         bootstrap_servers=['kafka:9092'])

esbody = {
    "mappings": {
        "post": {
            "properties": {
                "title": {
                    "type": "text"
                },
                "details": {
                    "type": "text"
                },
                "zip_code": {
                    "type": "integer"
                },
                "user": {
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
                "category": {
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
x = es.indices.create(index="models", body=esbody, ignore=[400, 404])
# print(str(x))

while (True):

    for message in consumer:
        tmp = json.loads((message.value).decode('utf-8'))
        post_id = tmp['id']
        post = tmp['post']
        es.index(index="models", id=post_id, body=post, doc_type="post")
        es.indices.refresh(index="models")
