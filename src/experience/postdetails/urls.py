from django.urls import path

from .views import ShowPostDetails

urlpatterns = [
    path('create/',
         ShowPostDetails.as_view(),
         name="postdetails"),
]