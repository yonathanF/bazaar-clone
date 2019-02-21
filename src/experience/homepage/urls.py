from django.urls import path

from .views import TopPostsPerCategory

urlpatterns = [
    path('<int:num_posts>/',
         TopPostsPerCategory.as_view(),
         name="topCategories"),
]
