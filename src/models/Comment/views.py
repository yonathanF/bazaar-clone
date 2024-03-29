import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from Post.models import Post
from UserProfile.models import Profile

from .forms import CreateCommentForm
from .models import Comment


def serialize_post(comment_id):
    """
    Return a JSON serialized post object
    """
    try:
        comment = Comment.objects.filter(id=comment_id)
        comment_json = json.loads(serializers.serialize("json", comment))
        return JsonResponse({'comment': comment_json[0]['fields'],
                             'id': comment_json[0]['pk']})
    except:
        return JsonResponse(
            {'Status': "Couldn't find Comment ID %d." % (comment_id)},
            status=404)

@method_decorator(csrf_exempt, name='dispatch')
class CommentView(View):
    """
    Get and Update endpoint for comment
    """
    def get(self, request, comment_id):
        return serialize_post(comment_id)

    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return JsonResponse(
            {'Status': "Couldn't find Comment ID %d." % (comment_id)},
            status=404)        
        comment_form = CreateCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            new_comment = comment_form.save()
            return serialize_post(new_comment.id)
        return JsonResponse({'Status': comment_form.errors}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class CommentCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request, post_id, user_id):

        form = CreateCommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            try:
                new_comment.post = Post.objects.get(pk=post_id)
            except Post.DoesNotExist:
                return JsonResponse({'Status': comment_form.errors},
                    status=400)
            try:
                new_comment.user = Profile.objects.get(pk=user_id)
            except Profile.DoesNotExist:
                return JsonResponse({'Status': comment_form.errors},
                                    status=400)

            new_comment.save()

            return serialize_post(new_comment.pk)
        else:
            return JsonResponse({'Status': comment_form.errors},
                            status=400)


@method_decorator(csrf_exempt, name='dispatch')
class CommentDelete(View):
    """
    DELETE endpoint for comment
    """
    def get(self, request, comment_id):
        try:
            Comment.objects.get(id=comment_id).delete()
            return JsonResponse({'Status': "Deleted comment ID %d." % (comment_id)})
        except Comment.DoesNotExist:
            return JsonResponse({'Status': "Couldn't find comment ID %d." % (comment_id)},
                status=404)
