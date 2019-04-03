import json
import logging
import urllib.parse
import urllib.request

from apiwrapper.ApiWrapper import APIV1
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

logger = logging.getLogger('APPNAME')

from kafka import KafkaProducer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ShowPostDetails(View):
    def get(self, request, post_id):
        api = APIV1()
        logger.info(post_id)
        return JsonResponse(api.post_get(post_id), safe=False)

    def post(self, request, token):
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        data = request.body.decode('utf-8')
        newdata = json.loads(data)
        api = APIV1()

        title = newdata['title']
        details = newdata['details']
        category = newdata['category']
        preferred_contact = newdata['password']
        deadline = newdata['deadline']
        request_type = newdata['request_type']
        zip_code = newdata['zip_code']

        res = api.post_create(title, details, category, preferred_contact,
                              deadline, request_type, zip_code, token)
        
        prodres = producer.send('new-posts', json.dumps(res).encode('utf-8'))
        return JsonResponse({'response': res, 'send': str(prodres)}, safe=False)

