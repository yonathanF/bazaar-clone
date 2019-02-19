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
        Categories = (
            ("LI", "Lifestyle"),
            ("IT", "IT Consultation"),
            ("EV", "Events"),
            ("TU", "Tutoring"),
            ("AR", "Art"),
            ("HO", "Household"),
            ("LB", "Labor"),
            ("OT", "Other"),
        )


        api = APIV1()
        return JsonResponse(api.post_top_n("LI", num_posts))
