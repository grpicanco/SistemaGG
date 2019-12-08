from django.shortcuts import render
from .models import Pessoa
from .form import Pessoa_formulario


# Create your views here.
def add_pessoa(request):
    form = Pessoa_formulario()
    if form.is_valid():
        form.save()
    return render(request, 'add_pessoa.html', {'form': form})