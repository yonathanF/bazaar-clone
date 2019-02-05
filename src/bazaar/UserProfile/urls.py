from django.urls import path

from .views import ProfileCreate, ProfileUpdate
from . import views

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name="create"),
    path('<int:profile_id>/', ProfileUpdate.as_view(), name="change"),
    path('delete/<int:profile_id>/', views.deleting, name="delete"),
    path('update/<int:profile_id>/', ProfileUpdate.as_view(), name="update")

]
