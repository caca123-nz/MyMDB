from django.urls import re_path

from main import views

app_name = "main"

urlpatterns = [
  re_path(r"^movies/$", views.MovieList.as_view(), name="movie-list")
]