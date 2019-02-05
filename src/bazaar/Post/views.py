from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .forms import CreatePostForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

@method_decorator(csrf_exempt, name='dispatch')
class PostCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request):
        post_form = CreatePostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return JsonResponse({'a':new_post.zip_code, 'b': new_post.deadline})
        return JsonResponse({'error':post_form.errors})
    
class PostUpdate(View):
    def get(self, request, post_id):
        return JsonResponse({'a':'test'})

    def post(self, request, post_id): 
        pass

    def delete(self, request, post_id):
        pass
