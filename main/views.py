from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, 'sobre.html')

def menu(request):
    return render(request, 'menu.html')

def resumo(request):
    return render(request, 'resumo.html')

def mapa_mental(request):
    return render (request, 'mapa_mental.html')

def cadastro(request):
    return render (request, 'cadastro.html')

def entrar(request):
    return render (request, 'entrar.html')
