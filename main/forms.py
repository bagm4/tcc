from django import forms
from .models import *

class CadastroForm(forms.ModelForm):
   
    class Meta:
        model = Usuario
        fields = '__all__'


class QuestaoForm(forms.ModelForm):
   
    class Meta:
        model = Questao
        fields = '__all__'