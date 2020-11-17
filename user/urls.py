from django.contrib.auth import views as auth_views
from django.urls import re_path

from user.forms import CustomAuthenticationForm
from user import views

app_name="user"
urlpatterns = [
  re_path(r"^register/$", views.RegisterView.as_view(), name="register"),
  re_path(r"^login/$", auth_views.LoginView.as_view(authentication_form = CustomAuthenticationForm ), name="login"),
  re_path(r"^logout/$", auth_views.LogoutView.as_view(), name="logout")
]