import email
from django.db import models

# Create your models here.

#============================================
#    POR FAVOR SEM MIGRAÇOES POR AGORA 
#============================================

class Questao (models.Model):
    pergunta = models.TextField()
    alternativaa = models.CharField(max_length=260, blank=False, verbose_name='Alternativa A') #obrigatoria
    alternativab = models.CharField(max_length=160, blank=False, verbose_name='Alternativa B') #obrigatoria
    alternativac = models.CharField(max_length=160, null=True, blank=True, verbose_name='Alternativa C')#NÃO obrigatoria
    alternativad = models.CharField(max_length=160, null=True, blank=True, verbose_name='Alternativa D')#NÃO obrigatoria
    certa = models.CharField(max_length=160, blank=False, verbose_name='Resposta correta')


    

