import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .forms import ProfileForm
from .models import Profile


def serialize_profile(profile_id):
    """
    Serializes a profile object into a json string
    """
    try:
        profile = Profile.objects.filter(pk=profile_id)
        profile_json = json.loads(serializers.serialize('json', profile))
        return JsonResponse({'profile': profile_json[0]['fields'],
                             'id': profile_json[0]['pk']})
    except:
        return JsonResponse({'Status': 'Profile is not found'})


@method_decorator(csrf_exempt, name='dispatch')
class ProfileCreate(View):
    """
    Creates a Profile through the Post HTTP method
    """

    def post(self, request):
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save()
            return serialize_profile(new_profile.pk)

        return JsonResponse({'Status': 'Couldn\'t create profile.'})


@method_decorator(csrf_exempt, name='dispatch')
class ProfileView(View):
    """
    Returns the profiel data for GET requests
    Updates the specified profile for POST requests
    """

    def get(self, request, profile_id):
        return serialize_profile(profile_id)

    def post(self, request, profile_id):
        try:
            current_profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return JsonResponse({'Status': 'Profile is not found'})

        profile_form = ProfileForm(request.POST, instance=current_profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return serialize_profile(updated_profile.pk)
        return JsonResponse({'Stats': profile_form.errors})


@method_decorator(csrf_exempt, name='dispatch')
class ProfileDelete(View):
    def get(self, request, profile_id):
        try:
            Profile.objects.get(id=profile_id).delete()
            return JsonResponse({'Status': "Deleted Profile."})
        except:
            return JsonResponse({'Status': 'Profile is not found'})
