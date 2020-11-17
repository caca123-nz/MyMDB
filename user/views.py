from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
  template_name = "user/register.html"
  form_class = CustomUserCreationForm
  success_url = reverse_lazy("main:movie-list")