from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from apiwrapper.ApiWrapper import APIV1

import logging

import json

import urllib.request
import urllib.parse

from django.core import serializers
from django.http import JsonResponse

logger = logging.getLogger('APPNAME')

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class UserProfiles(View):
     
    def post(self, request): 
        
        data = request.body.decode('utf-8')
        newdata = json.loads(data)
        api = APIV1()
        first_name = newdata['first_name']
        last_name = newdata['last_name']
        email = newdata['email']
        password = newdata['password']
        rating = float(newdata['rating'])
        description = newdata['description']
        education = newdata['education']
        zip_code = int(newdata['zip_code'])
        # data2 = {
        #     'first_name': first_name,
        #     'last_name': last_name,
        #     'email':  email,
        #     'password': password,
        #     'rating':  rating,
        #     'description': description,
        #     'education': education,
        #     'zip_code': zip_code,
        # }
        
        
        res = api.user_create(first_name,last_name,email, password, description, education)
        return JsonResponse(res, safe=False)