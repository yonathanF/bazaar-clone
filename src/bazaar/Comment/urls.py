from django.urls import path
from .views import CommentCreate, CommentViewUpdate, CommentDelete

urlpatterns = [

    path('<int:comment_id>/', CommentViewUpdate.as_view(), name="viewComment"),
	path('create/<int:post_id>/<int:user_id>', CommentCreate.as_view(), name='createComment'),
	path('delete/<int:comment_id>/', CommentDelete.as_view(), name="deleteComment"),


]
