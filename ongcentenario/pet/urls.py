from django.urls import path
from .views import PaginaAdotar, PaginaCadastroAdotar, PaginaCadastroAdotarEdit




urlpatterns = [
    path('adotar', PaginaAdotar.as_view(), name='adotar'),

    path('adocao/added/', PaginaCadastroAdotar.as_view(), name='added-pet'),
    path('adocao/edit/<int:pk>', PaginaCadastroAdotarEdit.as_view(), name='editar-pet'),
]
