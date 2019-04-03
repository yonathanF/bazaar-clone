from django.urls import path

from .views import UserProfiles

urlpatterns = [
    path('create/',
         UserProfiles.as_view(),
         name="creatinguser"),
]