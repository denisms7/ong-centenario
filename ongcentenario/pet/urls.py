from django.urls import path
from .views import PaginaAdotar, PaginaCadastroAdotar




urlpatterns = [
    path('adotar', PaginaAdotar.as_view(), name='adotar'),
    path('adotar/cadastro', PaginaCadastroAdotar.as_view(), name='adotarcadastro'),
]
