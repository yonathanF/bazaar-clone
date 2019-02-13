from django.urls import path

from . import views
from .views import ProfileCreate, ProfileDelete, ProfileView

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name="create"),
    path('<int:profile_id>/', ProfileView.as_view(), name="change"),
    path('delete/<int:profile_id>/', ProfileDelete.as_view(), name="delete"),

]
