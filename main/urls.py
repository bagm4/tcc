from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name="index"),
    path('sobre/', sobre, name="sobre"),
    path('menu/', menu, name="menu"),
    path('resumo/', resumo, name="resumo"),
    path('mapa_mental/', mapa_mental, name="mapa_mental"),
    path('cadastro/', cadastro, name="cadastro"),
    path('mapaPrincipal/', mapaPrincipal, name="mapa_principal"),
    path('addquestao/', addquestao, name="addquestao"),
    path('editquestao/<int:id>', editquestao, name="editquestao"),
    path('delet/<int:id>', deletequestao, name= 'deletequestao'),
    path('atividade/', atividade, name="atividade"),
]