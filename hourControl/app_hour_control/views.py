from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'projetos/home.html')

def cadastrar(request):
    return render(request, 'projetos/home.html')