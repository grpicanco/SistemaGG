from django.db import models


# Create your models here.
class Pessoa(models.Model):
    fundamental = 1
    medio = 2
    superior = 3

    ESCOLARIDADE_CHOICES = (
        (fundamental, 'Ensino Fundamental'),
        (medio, 'Ensino Médio'),
        (superior, 'Ensino Superior')
    )


    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    escolaridade = models.PositiveSmallIntegerField(choices= ESCOLARIDADE_CHOICES)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length=50)
    def __self__(self):
        return self.nome



class Funcao(models.Model):
    nome = models.CharField(max_length=10)
    descricao = models.TextField()
    def __self__(self):
        return self.nome



class Projeto(models.Model):
    nome = models.CharField(max_length=45)
    objetivo = models.TextField()
    def __self__(self):
        return self.nome



class Grupo(models.Model):
    nome = models.CharField(max_length=45)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=20)
    grupo_responsavel = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    def __self__(self):
        return self.nome



class Trabalha(models.Model):
    grupo =  models.ForeignKey(Grupo, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)
    def __self__(self):
        return self.projeto + ' ' + self.grupo



class Participa(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)
    def __self__(self):
        return self.id


