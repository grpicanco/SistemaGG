from django.contrib import admin

# Register your models here.
from grupos.models import Pessoa, Grupo, Funcao, Projeto, Trabalha, Participa,Pertence

admin.site.register(Pessoa)
admin.site.register(Grupo)
admin.site.register(Funcao)
admin.site.register(Projeto)
admin.site.register(Trabalha)
admin.site.register(Participa)
admin.site.register(Pertence)
