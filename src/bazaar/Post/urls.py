from django.urls import path

from .views import PostCreate, PostDelete, PostView, PostUpdate

urlpatterns = [
    path('<int:post_id>/', PostView.as_view(), name="viewPost"),
    path('create/', PostCreate.as_view(), name="createPost"),
    path('delete/<int:post_id>/', PostDelete.as_view(), name="deletePost"),
    path('update/<int:post_id>/', PostUpdate.as_view(), name="updatePost"),
]
