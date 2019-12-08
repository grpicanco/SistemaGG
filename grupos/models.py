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
    cpf = models.CharField(11)
    escolaridade = models.PositiveSmallIntegerField(choices= ESCOLARIDADE_CHOICES)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length=50)



class Funcao(models.Model):
    nome = models.CharField(max_length=10)
    descricao = models.TextField()



class Projeto(models.Model):
    nome = models.CharField(45)
    objetivo = models.TextField()



class Grupo(models.Model):
    nome = models.CharField(max_length=45)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField()
    cidade = models.CharField(20)
    bairro = models.CharField(20)
    logradouro = models.CharField(20)
    grupo_responsavel = models.ForeignKey('self', on_delete=models.CASCADE)



class Trabalha(models.Model):
    grupo =  models.ForeignKey(Grupo, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()



class Participa(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()


