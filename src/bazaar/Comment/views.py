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


def serialize_post(post):
    """
    Return a JSON serialized post object
    """
    return json.dumps({
    	'id': post.pk,
		'title' : post.title,
		'details' : post.details,
		'stars' : post.get_stars_display(),
		'date_posted' : str(post.date_posted)
	})


@method_decorator(csrf_exempt, name='dispatch')
class CommentView(View):

    def get(self, request, comment_id):
         try:
             comment = Comment.objects.filter(id=comment_id)
             json_comment = json.loads(serializers.serialize("json", comment))
             return JsonResponse({'comment': json_comment[0]['fields']})
         except:
            return JsonResponse({'status':"Error. Couldn't find comment"})


@method_decorator(csrf_exempt, name='dispatch')
class CommentCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request, post_id, user_id):
    #def post(self, request):

		form = CreateCommentForm(request.POST)

		if form.is_valid():
			new_comment = form.save(commit= False)
			new_comment.post = Post.objects.get(pk=post_id)
			new_comment.user = Profile.objects.get(pk=user_id)
			new_comment.save()

			return JsonResponse({'created':serialize_post(new_comment)}) 
		else:
        	#return HttpResponse('Invalid header found.')
			return JsonResponse({'error':form.errors})


@method_decorator(csrf_exempt, name='dispatch')
class CommentUpdate(View):

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_form = CreateCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            new_comment = comment_form.save()
            return JsonResponse({'created': serialize_post(new_comment)})
        return JsonResponse({'error':comment_form.errors})


@method_decorator(csrf_exempt, name='dispatch')
class commentDelete(View):
    def get(self, request, comment_id):
         try:
             Comment.objects.get(id=comment_id).delete()
             return JsonResponse({'status': "deleted comment."})
         except:
            return JsonResponse({'status':"Error. Couldn't find comment"})



