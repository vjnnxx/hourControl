from django.shortcuts import render
from .models import Projeto
# Create your views here.
def home(request):

    projetos = {
        'projetos': Projeto.objects.all()
    }
    return render(request, 'projetos/home.html', projetos)

def cadastrar(request):

    projeto = Projeto()

    projeto.nome = request.POST.get('nome-projeto')
    projeto.desc = request.POST.get('descricao')

    projeto.save()

    projetos = {
        'projetos': Projeto.objects.all()
    }

    return render(request, 'projetos/home.html', projetos)

def abrir(request):

    projeto_id = request.GET.get('id_projeto')


    
    projeto = Projeto(id_projeto=projeto_id)

    projeto = {
        'projeto': projeto
    }

    

    return render(request, 'projetos/abrir.html', projeto)