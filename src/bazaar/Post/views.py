import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .forms import CreatePostForm
from .models import Post
from UserProfile.models import Authenticator, Profile


def serialize_post(post_id):
    """
    Return a JSON serialized post object
    """
    try:
        post = Post.objects.filter(id=post_id)
        json_post = json.loads(serializers.serialize("json", post))
        return JsonResponse(
            {'post': json_post[0]['fields'], 'id': json_post[0]['pk']})
    except:
        return JsonResponse(
            {"Status": "Couldn't find Post ID %d." % (post_id)},
            status=404)


@method_decorator(csrf_exempt, name='dispatch')
class PostPerCategory(View):
    """
    Gets the most recent <num_posts> for the specified category
    """
    def get(self, request, num_posts, category):

        try:
            posts = Post.objects.filter(
                category=category).order_by('date_posted')[:num_posts]

            json_post = json.loads(serializers.serialize("json", posts))
            return JsonResponse({'Posts': json_post})

        except:
            return JsonResponse(
                {"Status": "Couldn't process request."})


@method_decorator(csrf_exempt, name='dispatch')
class PostViewUpdate(View):
    """
    Updates the post if the method is post
    Gets the data if the method is get
    """

    def get(self, request, post_id):
        return serialize_post(post_id)

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse(
                {'Status': "Couldn't find Post ID %d." % (post_id)},
                status=404)

        post_form = CreatePostForm(request.POST, instance=post)
        if post_form.is_valid():
            new_post = post_form.save()
            return serialize_post(new_post.pk)

        return JsonResponse({'Status': post_form.errors}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request, token):
        if(isAuthenticated(token)):
            tokenobject = Authenticator.objects.get(authenticator=token)
            userid = tokenobject.user_id
            post_form = CreatePostForm(request.POST)
            if post_form.is_valid():
                post_form.user_id = userid
                new_post = post_form.save()
                return serialize_post(new_post.pk)

            return JsonResponse({'Status': post_form.errors},
                                status=400)
        else:
            return JsonResponse({'Status': "You are not authenticated, please login"},
                                status=401)


@method_decorator(csrf_exempt, name='dispatch')
class PostDelete(View):
    def get(self, request, post_id):
        try:
            Post.objects.get(id=post_id).delete()
            return JsonResponse({'Status': "Deleted post ID %d." % (post_id)})

        except Post.DoesNotExist:
            return JsonResponse(
                {'Status': "Couldn't find post ID %d." % (post_id)},
                status=404)

def isAuthenticated(token):
    try:
        Authenticator.objects.get(authenticator=token)
        return True
    except Authenticator.DoesNotExist:
        return False