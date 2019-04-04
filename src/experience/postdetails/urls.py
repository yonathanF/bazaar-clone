from django.urls import path

from .views import ShowPostDetails, SearchPosts

urlpatterns = [
    path('create/<str:token>/', ShowPostDetails.as_view(), name="createpost"),
    path('<int:post_id>/', ShowPostDetails.as_view(), name="getpost"),
    path('search/<str:keywords>', SearchPosts.as_view(), name="searchposts")
]
