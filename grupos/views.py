from django.shortcuts import render
from .models import Pessoa
from .form import Pessoa_formulario, Grupo_formulario


# Create your views here.
def add_pessoa(request):
    form = Pessoa_formulario()
    if form.is_valid():
        form.save()
    return render(request, 'add_pessoa.html', {'form': form})


def add_grupo(request):
    form_grup = Grupo_formulario()
    if form_grup.is_valid():
        form_grup.save()
    return render(request, 'add_grupo.html', {'form': form_grup})
