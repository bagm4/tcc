import email
from django.db import models

# Create your models here.

#============================================
#    POR FAVOR SEM MIGRAÇOES POR AGORA 
#============================================

class Questao (models.Model):
    pergunta = models.TextField()
    alternativaa = models.CharField(max_length=260, blank=False) #obrigatoria
    alternativab = models.CharField(max_length=160, blank=False) #obrigatoria
    alternativac = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    alternativad = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    certa = models.CharField(max_length=160, blank=False)


    

