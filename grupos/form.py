from django.forms import ModelForm
from .models import Pessoa, Projeto, Grupo, Funcao  # Trabalha, Participa


class Pessoa_formulario(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'profissao', 'data_nascimento', 'escolaridade']


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
        model = Grupo
        fields = ['nome', 'cidade', 'bairro', 'logradouro']

    def clear_data_fim(self):
        return self.data_fim['Null']

# class Trabalha_formulario(ModelForm):
#     class Meta:
