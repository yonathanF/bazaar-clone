from django.urls import path

from .views import PostCreate, PostDelete, PostPerCategory, PostViewUpdate

urlpatterns = [
    path('byCategory/<str:category>/<int:num_posts>/', PostPerCategory.as_view(),
         name="topPosts"),
    path('<int:post_id>/', PostViewUpdate.as_view(), name="viewPost"),
    path('create/', PostCreate.as_view(), name="createPost"),
    path('delete/<int:post_id>/', PostDelete.as_view(), name="deletePost"),
]
