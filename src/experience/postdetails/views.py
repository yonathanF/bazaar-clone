from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from apiwrapper.ApiWrapper import APIV1

import json

import urllib.request
import urllib.parse

from django.core import serializers
from django.http import JsonResponse

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ShowPostDetails(View):
    

    def get(self, request, post_id):
        api = APIV1()
        return JsonResponse(api.post_get(post_id))