from django.urls import path

from .views import LoginProfile

urlpatterns = [
    path('/login/',
         LoginProfile.as_view(),
         name="loginuser"),
    path('/logout/<str:token>', LoginProfile.as_view(), name="logoutuser"),
]