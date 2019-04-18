#!/bin/sh
pip install elasticsearch -U
pip install kafka-python -U
curl -XDELETE elasticsearch:9200
python ProducerConsumer.py
#etc.
