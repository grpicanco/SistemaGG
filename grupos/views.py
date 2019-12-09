from django.shortcuts import render
from .models import Pessoa
from .form import Pessoa_formulario, Grupo_formulario, Funcao_formulario


# Create your views here.
def add_pessoa(request):
    form = Pessoa_formulario()
    if form.is_valid():
        form.save()
    return render(request, 'add_pessoa.html', {'form': form})


def add_grupo(request):
    form = Grupo_formulario()
    if form.is_valid():
        form.save()
    return render(request, 'add_grupo.html', {'forms': form})

def add_funcao(request):
    form : Funcao_formulario()
    if form.is_valid():
        form.save()
    return render(request, 'add_funcao.html', {'form': form})

#TODO: Fazer a exclusão, necessita trabalhar com o banco.

#TODO: Fazer listar, grupos e participantes daquele grupo.

#TODO: Adcionar por logir/criar cadastro