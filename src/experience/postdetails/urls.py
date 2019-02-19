from django.urls import path

from .views import ShowPostDetails

urlpatterns = [
    path('<int:post_id>/',
         ShowPostDetails.as_view(),
         name="postdetails"),
]