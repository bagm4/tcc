import email
from django.db import models

# Create your models here.

#============================================
#    POR FAVOR SEM MIGRAÇOES POR AGORA 
#============================================
class Usuario (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=30, blank=False)  #qual deveria ser o da senha? charfield?
    senha2 = models.CharField(max_length=30, blank=False)  #para comparar com a senha
    # um IF para ver se as senhas são iguais

class Questao (models.Model):
    titulo = models.CharField(max_length=70)
    pergunta = models.TextField()
    alternativa_certa = models.CharField(max_length=260, blank=False)
    alternativa2 = models.CharField(max_length=160, blank=False)
    alternativa3 = models.CharField(max_length=160, null=True, blank=True)#modelo desta e demais alternativas 
    # alternativas (tem que ser um numero x ou pode variar? se variar tem que descobrir como fazer)
    # tipo (ex: completar a frase(cliclar no botão), marcar alternativa) (vai ter??)

