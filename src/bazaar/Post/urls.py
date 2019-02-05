from django.urls import path

from .views import PostCreate, PostUpdate 

urlpatterns = [
    path('create/', PostCreate.as_view(), name="create"),
        path('<int:post_id>/', PostUpdate.as_view(), name="change"),
]
