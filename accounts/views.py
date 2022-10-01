from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #igual ao redirect(?) mas pra ca se usa ele
from django.views.generic.edit import CreateView
from .forms import UsuarioForm



# Create your views here.
class signUp(CreateView):
    template_name = 'registration/register.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
