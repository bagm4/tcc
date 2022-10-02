from django.db import models
from django.forms.widgets import RadioSelect
from django.urls import reverse

# Create your models here.
class User (models.Model): 
    
    email = models.EmailField()
    professor = models.BooleanField()
