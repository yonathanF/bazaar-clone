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
        f = open('tmp.txt', "w+")
        f.write("WErwlkrwehjqiuerhbqlrj3fh34j")
        f.close()
        data = request.POST
        api = APIV1()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        rating = data.get('rating')
        description = data.get('description')
        education = data.get('education')
        zip_code = data.get('zip_code')
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email':  email,
            'password': password,
            'rating':  rating,
            'description': description,
            'education': education,
            'zip_code': zip_code,
        }
        
        res = api.user_create(first_name,last_name,email, password, rating, description, education, zip_code)
        return JsonResponse(res, safe=False)