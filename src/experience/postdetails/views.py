import json

from apiwrapper.ApiWrapper import APIV1
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ShowPostDetails(View):
    def get(self, request, post_id):

        api = APIV1()

        if 'HTTP_AUTHORIZATION' in request.META:
            token = str(request.META['HTTP_AUTHORIZATION']).split()[1]
            profile = api.profile_get_with_token(token)
            user_id = profile[1]['id']
            return JsonResponse(api.post_get_and_log(post_id, user_id),
                                safe=False)
        else:
            return JsonResponse(api.post_get(post_id), safe=False)

    def post(self, request, token):

        data = request.body.decode('utf-8')
        newdata = json.loads(data)
        api = APIV1()

        title = newdata['title']
        details = newdata['details']
        category = newdata['category']
        preferred_contact = newdata['preferred_contact']
        deadline = newdata['deadline']
        request_type = newdata['request_type']
        zip_code = newdata['zip_code']
        res = api.post_create(title, details, category, preferred_contact,
                              deadline, request_type, zip_code, token)

        return JsonResponse(res, safe=False)


class SearchPosts(View):
    def get(self, request, keywords):
        api = APIV1()
        results = api.post_search(keywords)
        return JsonResponse({"posts": results})
