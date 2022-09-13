import email
from django.db import models

# Create your models here.

#============================================
#    POR FAVOR SEM MIGRAÇOES POR AGORA 
#============================================
class Usuario (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=30)  #qual deveria ser o da senha? charfield?
    senha2 = models.CharField(max_length=30)  #para comparar com a senha
    # um IF para ver se as senhas são iguais

class Questao (models.Model):
    titulo = models.CharField(max_length=70)
    # pergunta
    # alternativas (tem que ser um numero x ou pode variar? se variar tem que descobrir como fazer)
    # tipo (ex: completar a frase(cliclar no botão), marcar alternativa) (vai ter??)

