from django.urls import path
from .views import add_pessoa

urlpatterns = [
 path('add_pessoa', add_pessoa, name='add_pessoa'),
]