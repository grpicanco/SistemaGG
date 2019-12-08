from django.forms import ModelForm
from .models import Pessoa, Projeto, Grupo, Funcao, Trabalha, Participa

class Pessoa_formulario(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','cpf', 'escolaridade', 'data_nascimento', 'profissao']



class Funcao_formulario(ModelForm):
    class Meta:
        model = Funcao
        fields = ['nome', 'descricao']



class Projeto_formulario(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'objetivo']



class Grupo_formulario(ModelForm):
    class Meta:
        grupo = Grupo
        fields = ['nome', 'cidade', 'bairro', 'logradouro']



# class Trabalha_formulario(ModelForm):
#     class Meta:
