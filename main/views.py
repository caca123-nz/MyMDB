from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect

from main.forms import VoteForm, MovieImageForm
from main.models import Movie, Person, Vote

class MovieList(ListView):
  context_object_name = "movies"
  model = Movie
  template_name = "main/movie-list.html"

class MovieDetail(DetailView):
  context_object_name = "movie"
  queryset = Movie.objects.all_with_related_persons_and_score()
  template_name = "main/movie-detail.html"

  def movie_image_form(self):
    if self.request.user.is_authenticated:
      return MovieImageForm()
    return None

  def get_context_data(self, **kwargs):
    # Create vote_form an passing in the context object
    ctx = super().get_context_data(**kwargs)
    ctx["image_form"] = self.movie_image_form()
    if self.request.user.is_authenticated:
      vote_data = {"user": self.request.user, "movie":self.object}
      vote = Vote.objects.get_vote_or_unsaved_blank_vote(**vote_data)
      if vote.id:
        # update vote
        vote_form_url = reverse("main:update-vote",
          kwargs={"movie_id": vote.movie.id, "pk": vote.id})
      else:
        # create vote
        vote_form_url = reverse("main:create-vote",
          kwargs={"movie_id": self.object.id})
      vote_form = VoteForm(instance=vote)
      ctx['vote_form'] = vote_form
      ctx['vote_form_url'] = vote_form_url
    return ctx

class PersonDetail(DetailView):
  context_object_name = "person"
  queryset = Person.objects.all_with_prefetch_movies()
  template_name = "main/person-detail.html"

class SuccessUrlAndRenderToResponse:

  def get_success_url(self):
    # Returning to movie detail if the form valided successfully
    # Getting movie id from self.object (vote instance)
    movie_id = self.object.movie.id
    return reverse("main:movie-detail", kwargs={"pk": movie_id})
  
  def render_to_response(self, context,  **response_kwargs):
    # Returnin a HTTP redirect instead of rendering a template
    # Getting movie id from context args if formvalidation failed
    # Errors message get losing
    movie_id = context["movie"].id
    movie_detail_url = reverse("main:movie-detail", kwargs={"pk":movie_id})
    return redirect(to=movie_detail_url)


class CreateVote(SuccessUrlAndRenderToResponse, LoginRequiredMixin, CreateView):
  form_class = VoteForm

  def get_initial(self):
    # Initializing the Form with user and movie data
    initial = super().get_initial()
    initial["user"] = self.request.user.id
    initial["movie"] = self.kwargs["movie_id"]
    return initial
  

class UpdateVote(SuccessUrlAndRenderToResponse, LoginRequiredMixin, UpdateView):
  form_class = VoteForm
  queryset = Vote.objects.all()

  def get_object(self, queryset=None):
    # Getting single vote instance using pk_url_kwarg
    vote = super().get_object(queryset)
    user = self.request.user
    if vote.user != user:
      raise PermissionDenied("Cannot change another users vote")
    return vote

class MovieImageUpload(SuccessUrlAndRenderToResponse, LoginRequiredMixin, CreateView):
  def get_initial(self):
    initial = super().get_initial()
    initial["user"]=self.request.user.id
    initial["movie"]=self.kwargs["movie_id"]
    return initial
