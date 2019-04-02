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
        res = api.user_logout(token)
        return JsonResponse(res, safe=False)

    def post(self, request):

        data = request.body.decode('utf-8')
        newdata = json.loads(data)
        api = APIV1()

        email = newdata['email']
        password = newdata['password']

        res = api.user_login(email, password)
        return JsonResponse(res, safe=False)