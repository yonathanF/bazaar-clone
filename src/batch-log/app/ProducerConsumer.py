import json

from kafka import KafkaConsumer

consumer = KafkaConsumer('post-log',
                         group_id='accessing-posts',
                         bootstrap_servers=['kafka:9092'])

log_file_name = "data/access_log.log"
log_file = open(log_file_name, 'a')

while (True):
    for message in consumer:
        message_json = json.loads((message.value).decode('utf-8'))
        log_file.write(message_json)
