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
            createdProfile = Profile.objects.filter(id=new_profile.pk)
            data = json.loads(serializers.serialize('json', createdProfile))
            return JsonResponse({'allinfo': data[0]['fields'], 'id': data[0]['pk']})

        return JsonResponse({'error':profile_form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class ProfileUpdate(View):
    def get(self, request, profile_id):
        getRequestProfile = Profile.objects.filter(id=profile_id)
        if getRequestProfile.count() != 0:
            data = json.loads(serializers.serialize('json', getRequestProfile))
            return JsonResponse({'allinfo': data[0]['fields'], 'id': data[0]['pk']})
        return JsonResponse({'Notfound': 'Requested Object is not found'})

    def post(self, request, profile_id): 
        try:
            profileModel = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return JsonResponse({'Notfound': 'Requested Object is not found'})
        profile_form = ProfileForm(request.POST, instance=profileModel)
        if profile_form.is_valid():
            new_profile = profile_form.save()
            profileset = Profile.objects.filter(id=profile_id)
            data = json.loads(serializers.serialize('json', profileset))
            return JsonResponse({'updated': data[0]['fields']})
        return JsonResponse({'error': profile_form.errors})
        

@method_decorator(csrf_exempt, name='dispatch')
def deleting(request, profile_id):
    profileToDelete = Profile.objects.filter(id=profile_id)
    if profileToDelete.count() != 0:
        profileToDelete.delete()
        return JsonResponse({'deleted': 'sucessfully deleted'})
    return JsonResponse({'Notfound': 'Requested Object is not found'})
