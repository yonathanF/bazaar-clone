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
        pass
