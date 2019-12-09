from django.db import models


# Create your models here.
class Pessoa(models.Model):
    fundamental = 1
    fun_incompleto = 2
    medio = 3
    med_incompleto = 4
    superior = 5
    sup_incompleto = 6

    ESCOLARIDADE_CHOICES = (
        (fundamental, 'Ensino Fundamental'),
        (fun_incompleto, 'Ensino Fundamental incompleto'),
        (medio, 'Ensino Médio'),
        (med_incompleto, 'Ensino Médio incompleto'),
        (superior, 'Ensino Superior'),
        (sup_incompleto, 'Ensino Superior incompleto')
    )


    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    escolaridade = models.PositiveSmallIntegerField(choices= ESCOLARIDADE_CHOICES)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length=50)
    def __str__(self):
        a = str(self.nome)
        return a



class Funcao(models.Model):
    nome = models.CharField(max_length=10)
    descricao = models.TextField()
    def __str__(self):
        nome = str(self.nome)
        return nome



class Projeto(models.Model):
    nome = models.CharField(max_length=45)
    objetivo = models.TextField()
    def __str__(self):
        nome = str(self.nome)
        return nome



class Grupo(models.Model):
    nome = models.CharField(max_length=45)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=30)
    grupo_responsavel = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nome)



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

class Pertence(models.Model):
    funcao = models.ForeignKey(Funcao,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    def __self__(self):
        return self.id

