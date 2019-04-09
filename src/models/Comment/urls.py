from django.urls import path

from .views import CommentCreate, CommentDelete, CommentView

urlpatterns = [
    path('<int:comment_id>/', CommentView.as_view(), name="viewComment"),
    path('create/<int:post_id>/<int:user_id>', CommentCreate.as_view(), name='createComment'),
    path('delete/<int:comment_id>/', CommentDelete.as_view(), name="deleteComment"),
]
