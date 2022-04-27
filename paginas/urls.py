from django.urls import path
# o ponto é pq estou pegando algo dentro do diretorio do projeto
from .views import PaginaInicial, SobreView

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('', PaginaInicial.as_view(), name = 'inicio'),
    path('sobre/', SobreView.as_view(), name = 'sobre'),
]