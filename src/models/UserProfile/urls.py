from django.urls import path

from .views import (ProfileCreate, ProfileDelete, ProfileLogin, ProfileLogout,
                    ProfileToTokenView, ProfileView)

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name="create"),
    path('<int:profile_id>/', ProfileView.as_view(), name="change"),
    path('authProfile/<str:token>/',
         ProfileToTokenView.as_view(),
         name="tokenProfile"),
    path('delete/<int:profile_id>/', ProfileDelete.as_view(), name="delete"),
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/<str:token>/', ProfileLogout.as_view(), name='logout'),
]
