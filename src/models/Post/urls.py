from django.urls import path

from .views import (PostCreate, PostDelete, PostPerCategory, PostRec,
                    PostViewUpdate)

urlpatterns = [
    path('byCategory/<str:category>/<int:num_posts>/',
         PostPerCategory.as_view(),
         name="topPosts"),
    path('<int:post_id>/', PostViewUpdate.as_view(), name="viewPost"),
    path('create/<str:token>', PostCreate.as_view(), name="createPost"),
    path('rec/', PostRec.as_view(), name="updatedRec"),
    path('delete/<int:post_id>/', PostDelete.as_view(), name="deletePost"),
]
