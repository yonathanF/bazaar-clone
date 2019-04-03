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


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class LoginProfile(View):
    def get(self, request, token):
        api = APIV1()
        res = api.login_logout(token)
        return JsonResponse(res, safe=False)

    def post(self, request):

        data = request.body.decode('utf-8')
        newdata = json.loads(data)
        api = APIV1()

        email = newdata['email']
        password = newdata['password']

        response_code, response_body = api.login_login(email, password)

        return JsonResponse(response_body, status=response_code)


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

        res = api.login_create(first_name, last_name, email, password)
        return JsonResponse(res, safe=False)
