from django.urls import path
from .views import add_pessoa, add_grupo,add_funcao

urlpatterns = [
 path('add_pessoa/', add_pessoa, name='add_pessoa'),
 path('add_grupo/', add_grupo, name='add_grupo'),
 path('add_função/', add_funcao, name='add_funcao')
]