from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Questao
from .forms import CadastroForm, QuestaoForm

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

def mapaPrincipal(request):
    return render (request, 'mapa_principal.html')

def atividade (request):
    questoes = Questao.objects.all()
    context = {
        'questoes': questoes,
    }
    return render (request, 'atividade.html',context)

def addquestao (request):
    if request.method == 'POST':
        form = QuestaoForm(request.POST)
        if form.is_valid():
            questao = form.save(commit=False) #para esperar a gente mandar salvar
            questao.done = 'doing'
            questao.save()
            return redirect('/')
    else:
        form = QuestaoForm()

    questao = Questao.objects.all()
    context = {'form': form , 'questoes':questao}

    return render (request, 'addquestao.html', context)

def editquestao (request, id):
    questao = get_object_or_404(Questao, pk=id)
    form = QuestaoForm(instance=questao) #formulario pre populado para editar
    if(request.method == 'POST'):
        form = QuestaoForm(request.POST, instance=questao)
        if(form.is_valid()):
            questao.save()
            return redirect('/')
        else:
            return render (request, 'editquestao.html', {'form':form, 'questao':questao})
    else:
        return render (request, 'editquestao.html', {'form':form, 'quustao':questao})
