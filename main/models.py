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
    pergunta = models.TextField()
    alternativa1 = models.CharField(max_length=260, blank=False) #obrigatoria
    alternativa2 = models.CharField(max_length=160, blank=False) #obrigatoria
    alternativa3 = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    alternativa4 = models.CharField(max_length=160, null=True, blank=True)#NÃO obrigatoria
    certa = models.CharField(max_length=160, blank=False)
    

