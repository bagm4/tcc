import email
from django.db import models

# Create your models here.

#============================================
#    POR FAVOR SEM MIGRAÇOES POR AGORA 
#============================================

class Questao (models.Model):
    pergunta = models.TextField()
    alternativa1 = models.CharField(max_length=260, blank=False) #obrigatoria
    alternativa2 = models.CharField(max_length=160, blank=False) #obrigatoria
    alternativa3 = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    alternativa4 = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    certa = models.CharField(max_length=160, blank=False)
    

