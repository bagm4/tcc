from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect



class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
  