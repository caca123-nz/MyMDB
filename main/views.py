from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Movie

class MovieList(ListView):
  context_object_name = "movies"
  model = Movie
  template_name = "main/movie-list.html"

class MovieDetail(DetailView):
  context_object_name = "movie"
  model = Movie
  template_name = "main/movie-detail.html"


