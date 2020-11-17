from django.urls import reverse
from django.views.generic import ListView, DetailView

from main.forms import VoteForm
from main.models import Movie, Person, Vote

class MovieList(ListView):
  context_object_name = "movies"
  model = Movie
  template_name = "main/movie-list.html"

class MovieDetail(DetailView):
  context_object_name = "movie"
  queryset = Movie.objects.all_with_related_persons()
  template_name = "main/movie-detail.html"

  def get_context_data(self, **kwargs):
    # Create vote_form an passing in the context object
    ctx = super().get_context_data(**kwargs)
    if self.request.user.is_authenticated:
      vote_data = {"user": self.request.user, "movie":self.object}
      vote = Vote.objects.get_vote_or_unsaved_blank_vote(**vote_data)
      if vote.id:
        # update vote
        vote_form_url = reverse(
          "main:update-vote",
          kwargs={
            "movie_id": vote.movie.id,
            "pk": vote.id
          }
        )
      else:
        # create vote
        vote_form_url = reverse(
          "main:create-vote",
          kwargs={"movie_id": self.object.id}
        )
      vote_form = VoteForm(instance=vote)
      ctx['vote_form'] = vote_form
      ctx['vote_form_url'] = vote_form_url
    return ctx

class PersonDetail(DetailView):
  context_object_name = "person"
  queryset = Person.objects.all_with_prefetch_movies()
  template_name = "main/person-detail.html"