from django.urls import path
from .views import CommentCreate, CommentUpdate 

urlpatterns = [

    path('<int:comment_id>/', CommentView.as_view(), name="viewComment"),
	path('create/<int:post_id>/<int:user_id>', CommentCreate.as_view(), name='createComment'),
	#path('create/', CommentCreate.as_view(), name='create'),
	path('update/<int:comment_id>', CommentUpdate.as_view(), name='updateComment'),
	path('delete/<int:comment_id>/', CommentDelete.as_view(), name="deleteComment"),


]