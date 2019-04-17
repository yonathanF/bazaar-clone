#!/bin/bash
docker-compose -f ../docker-compose-prod.yml build
echo "Pi3.1415926535" | docker login -u "yonathanf" --password-stdin
docker push yonathanf/isa_2019_bazaar
