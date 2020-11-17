from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Movie, Person

class MovieList(ListView):
  context_object_name = "movies"
  model = Movie
  template_name = "main/movie-list.html"

class MovieDetail(DetailView):
  context_object_name = "movie"
  queryset = Movie.objects.all_with_related_persons()
  template_name = "main/movie-detail.html"

class PersonDetail(DetailView):
  context_object_name = "person"
  queryset = Person.objects.all_with_prefetch_movies()
  template_name = "main/person-detail.html"