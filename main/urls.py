from django.urls import re_path, path

from main import views

app_name = "main"

urlpatterns = [
  re_path(r"^movies/$", views.MovieList.as_view(), name="movie-list"),
  re_path(r"^movie/(?P<pk>[0-9])/$", views.MovieDetail.as_view(), name="movie-detail"),
]