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

    def request_type_to_human(self, request_type):
        Type = (
            ("OF", "Offering"),
            ("AS", "Asking"),
        )
        if request_type == Type[0][0]:
            return Type[0][1]

        return Type[1][1]


    def get(self, request, num_posts):
        categories = (
            ("LI", "Lifestyle"),
            ("IT", "IT Consultation"),
            ("EV", "Events"),
            ("TU", "Tutoring"),
            ("AR", "Art"),
            ("HO", "Household"),
            ("LB", "Labor"),
            ("OT", "Other"),
        )
        posts = {}
        api = APIV1()

        for category in categories:
            result = api.post_top_n(category[0], num_posts)
            posts_in_category = {}
            for post in result['Posts']:
                fields = {'request_type': self.request_type_to_human(post['fields']['request_type']),
                          'deadline': post['fields']['deadline'],
                          'title': post['fields']['title'],
                          'zip_code': post['fields']['zip_code'],
                          'id':post['pk']}

                posts_in_category[post['pk']] = fields


            posts[category[1]] = posts_in_category

        return JsonResponse(posts)
