from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .forms import CreatePostForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class PostCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request):
        form = CreatePostForm()
        new_post = form.save()
        
        return JsonResponse({'a':new_post.title}) 

    def get(self, request):
        return JsonResponse({'message': 'hello world'})


class PostUpdate(View):

    def post(self, request): 
        pass
