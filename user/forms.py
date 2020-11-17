from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class CustomAuthenticationForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))