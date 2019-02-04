from django.urls import path
from . import views

urlpatterns = [

	path('api/v1/comments/<int:db_id>/', views.detail, name='detail'), 
	path('api/v1/comments/create', views.create, name='create'),
	path('api/v1/comments/<int:db_id>/update', views.update, name='update'),
	path('api/v1/comments/<int:db_id>/delete', views.delete, name='delete'),

]