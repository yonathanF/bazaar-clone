from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .forms import CreatePostForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .models import Post
from django.core import serializers

def serialize_post(post):
    """
    Return a JSON serialized post object
    """

    return json.dumps({
      'id':post.pk,
      'title': post.title,
      'details':post.details,
      'category':post.get_category_display(),
      'preferred_contact':post.get_preferred_contact_display(),
      'date_posted':str(post.date_posted),
      'deadline':str(post.deadline),
      'zip_code':post.zip_code,
      'request_type':str(post.request_type)
    })

@method_decorator(csrf_exempt, name='dispatch')
class PostView(View):
    """
    Creates a post through the Post HTTP method
    """

    def get(self, request, post_id):
         try:
             post = Post.objects.filter(id=post_id)
             json_post = json.loads(serializers.serialize("json", post))
             return JsonResponse({'post': json_post[0]['fields']})
         except:
            return JsonResponse({'status':"Error. Couldn't find post"})


@method_decorator(csrf_exempt, name='dispatch')
class PostCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request):
        post_form = CreatePostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return JsonResponse({'created': serialize_post(new_post)})
        return JsonResponse({'error':post_form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class PostUpdate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post_form = CreatePostForm(request.POST, instance=post)
        if post_form.is_valid():
            new_post = post_form.save()
            return JsonResponse({'created': serialize_post(new_post)})
        return JsonResponse({'error':post_form.errors})


@method_decorator(csrf_exempt, name='dispatch')
class PostDelete(View):
    def get(self, request, post_id):
         try:
             Post.objects.get(id=post_id).delete()
             return JsonResponse({'status': "deleted post."})
         except:
            return JsonResponse({'status':"Error. Couldn't find post"})

