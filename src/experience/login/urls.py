from django.urls import path

from .views import LoginProfile

urlpatterns = [
    path('/login',
         LoginProfile.as_view(),
         name="loginuser"),
]