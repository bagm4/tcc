from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from main.models import Questao
from .forms import  QuestaoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

def mapaPrincipal(request):
    return render (request, 'mapa_principal.html')

@login_required
def atividade (request):
    questoes = Questao.objects.all()
    context = {
        'questoes': questoes,
    }
    return render (request, 'atividade.html',context)

@login_required
def addquestao (request):
    #cadastro da questao
    if request.method == 'POST':
        form = QuestaoForm(request.POST)
        if form.is_valid():
            questao = form.save(commit=False) #para esperar a gente mandar salvar
            questao.done = 'doing'
            questao.save()
            return redirect('/addquestao/')
    else:
        form = QuestaoForm()

    #exibir questão
    questaolist = Questao.objects.all()
    paginator = Paginator(questaolist, 6)
    page = request.GET.get('page')
    questao = paginator.get_page(page)

    context = {'form': form , 'questoes':questao}

    return render (request, 'addquestao.html', context)

@login_required
def editquestao (request, id):
    questao = get_object_or_404(Questao, pk=id)
    form = QuestaoForm(instance=questao) #formulario pre populado para editar
    if(request.method == 'POST'):
        form = QuestaoForm(request.POST, instance=questao)
        if(form.is_valid()):
            questao.save()
            return redirect('/addquestao/')
        else:
            return render (request, 'editquestao.html', {'form':form, 'questao':questao})
    else:
        return render (request, 'editquestao.html', {'form':form, 'quustao':questao})

@login_required
def deletequestao (request, id):
    questao = get_object_or_404(Questao, pk=id)
    questao.delete()
    messages.info(request, 'tarefa deletada com sucesso ;)')
    return redirect('/addquestao/')
