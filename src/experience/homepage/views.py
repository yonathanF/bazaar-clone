from apiwrapper.ApiWrapper import APIV1
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


@method_decorator(csrf_exempt, name='dispatch')
class TopPostsPerCategory(View):
    """
    Returns the top <num_per_cat> from each
    category of posts
    """

    def get(self, request, num_posts):
        categories = (
            "Lifestyle",
            "IT Consultation",
            "Events",
            "Tutoring",
            "Art",
            "Household",
            "Labor",
            "Other",
        )
        posts = {}
        api = APIV1()

        for category in categories:
            result = api.post_top_n(category, num_posts)

            posts_in_category = {}
            for post in result['Posts']:
                fields = {
                    'request_type': post['fields']['request_type'],
                    'deadline': post['fields']['deadline'],
                    'title': post['fields']['title'],
                    'zip_code': post['fields']['zip_code'],
                    'id': post['pk']
                }

                posts_in_category[post['pk']] = fields

            posts[category] = posts_in_category
        return JsonResponse({'data': posts}, status=200)
