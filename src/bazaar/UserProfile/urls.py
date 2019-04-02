from django.urls import path

from . import views
from .views import ProfileCreate, ProfileDelete, ProfileView, ProfileLogin, ProfileLogout

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name="create"),
    path('<int:profile_id>/', ProfileView.as_view(), name="change"),
    path('delete/<int:profile_id>/', ProfileDelete.as_view(), name="delete"),
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/<str:token>/', ProfileLogout_as_view(), name='logout'),
]
