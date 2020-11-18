from django.urls import re_path, path

from main import views

app_name = "main"

urlpatterns = [
  re_path(r"^movies/$", views.MovieList.as_view(), name="movie-list"),
  re_path(r"^top-10-movies/$", views.TopMovies.as_view(), name="top-movies"),
  re_path(r"^movie/(?P<pk>[0-9]+)/$", views.MovieDetail.as_view(), name="movie-detail"),
  re_path(r"^movie/(?P<movie_id>[0-9]+)/vote/$", views.CreateVote.as_view(), name="create-vote"),
  re_path(r"^movie/(?P<movie_id>[0-9]+)/vote/(?P<pk>[0-9]+)/$", views.UpdateVote.as_view(), name="update-vote"),
  re_path(r"^movie/(?P<movie_id>[0-9]+)/image/upload/$", views.MovieImageUpload.as_view(), name="movie-image-upload")
]