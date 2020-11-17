from django import forms
from django.contrib.auth import get_user_model

from main.models import Movie, Vote

class VoteForm(forms.ModelForm):
  '''Provide a form to let user votes for a film'''
  user = forms.ModelChoiceField(
    widget=forms.HiddenInput,
    queryset=get_user_model().objects.all(),
    disabled=True
  )
  
  movie = forms.ModelChoiceField(
    widget=forms.HiddenInput,
    queryset=Movie.objects.all(),
    disabled=True
  )

  value = forms.ChoiceField(
    label="Vote",
    widget=forms.RadioSelect(attrs={"class": "form-control-input"}),
    choices=Vote.VALUE_CHOICES
  )

  class Meta:
    model = Vote
    fields = ("value", "user", "movie")
