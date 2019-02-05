from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from .forms import CreateCommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class CommentCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request):
        form = CreateCommentForm(request.POST)

        if form.is_valid():
        	new_comment = form.save()
        	return JsonResponse({'a':new_comment.title}) 
        else:
        	#return HttpResponse('Invalid header found.')
        	return JsonResponse(form.errors)

    def get(self, request):
        return JsonResponse({'message': 'hello world'})


class CommentUpdate(View):

    def post(self, request): 
        return "yeet not implemented yet fam"
