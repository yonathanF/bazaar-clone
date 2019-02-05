from django.urls import path

from .views import PostCreate, PostDelete, PostViewUpdate 

urlpatterns = [
    path('<int:post_id>/', PostViewUpdate.as_view(), name="viewPost"),
    path('create/', PostCreate.as_view(), name="createPost"),
    path('delete/<int:post_id>/', PostDelete.as_view(), name="deletePost"),
]
