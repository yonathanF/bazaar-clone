from django.urls import path
from .views import CommentCreate, CommentUpdate 

urlpatterns = [

	#path('create/<int:post_id>/<int:user_id>', CommentCreate.as_view(), name='create'),
	path('create', CommentCreate.as_view(), name='create'),
	path('<int:comment_id>/update', CommentUpdate.as_view(), name='update'),
]