from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import CreateCommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Post.models import Post
from UserProfile.models import Profile
from Comment.models import Comment
import json

# class CommentEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Comment):
#             return { "title" : obj.title,
#                     "details" : obj.details,
#                     "stars" : obj.get_stars_display(),
#                     "date_posted" : obj.date_posted.isoformat()
#                     }
#         return json.JSONEncoder.default(self, obj)

def serializable(post):

	json_input = {
		'title' : post.title,
		'details' : post.details,
		'stars' : post.get_stars_display(),
		'date_posted' : post.date_posted.isoformat()
	}

	return json.dumps(json_input)

@method_decorator(csrf_exempt, name='dispatch')
class CommentCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    #def post(self, request, post_id, user_id):
    def post(self, request):

    	return serializable(request)

		# form = CreateCommentForm(request.POST)

		# if form.is_valid():
		# 	new_comment = form.save(commit= False)
		# 	new_comment.post = Post.objects.get(pk=post_id)
		# 	new_comment.user = Profile.objects.get(pk=user_id)

		# 	new_comment.save()

		# 	return JsonResponse({'a':new_comment.title}) 
		# else:
  #       	#return HttpResponse('Invalid header found.')
		# 	return JsonResponse(form.errors)

    def get(self, request):
        return JsonResponse({'message': 'hello world'})


class CommentUpdate(View):

    def post(self, request): 
        return "yeet not implemented yet fam"
