from django.urls import path

from .views import TopPostsPerCategory

urlpatterns = [
    path('<int:num_per_cat>/',
         TopPostsPerCategory.as_view(),
         name="topCategories"),
]
