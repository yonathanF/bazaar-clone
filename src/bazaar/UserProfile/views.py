from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .forms import ProfileForm
from .models import Profile
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers


@method_decorator(csrf_exempt, name='dispatch')
class ProfileCreate(View):
    """
    Creates a post through the Post HTTP method
    """

    def post(self, request):
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save()
        
            return JsonResponse({'a':new_profile.first_name, 'b': new_profile.description})

        return JsonResponse({'error':profile_form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class ProfileUpdate(View):
    def get(self, request, profile_id):
        obj = Profile.objects.filter(id=profile_id)
        if obj.count() != 0:
            data = json.loads(serializers.serialize('json', obj))
            return JsonResponse({'allinfo': data[0]['fields'], 'id': data[0]['pk']})
        return JsonResponse({'Notfound': 'Requested Object is not found'})

    def post(self, request, profile_id): 
        profileModel = Profile.objects.get(id=profile_id)
        profile_form = ProfileForm(request.POST, instance=profileModel)
        if profile_form.is_valid():
            new_profile = profile_form.save()
            profileset = Profile.objects.filter(id=profile_id)
            data = json.loads(serializers.serialize('json', profileset))
            return JsonResponse({'updated': data[0]['fields']})
        return JsonResponse({'error': profile_form.errors})

@method_decorator(csrf_exempt, name='dispatch')
def deleting(request, profile_id):
    Profile.objects.filter(id=profile_id).delete()
    return JsonResponse({'deleted': 'sucessfully deleted'})
