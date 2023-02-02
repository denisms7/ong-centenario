from django.urls import path
from .views import PaginaAdotar, PaginaCadastroAdotar, PaginaCadastroAdotarEdit, PaginaCadastroAdotarDelete, PaginaAdotarLista, PerfilPet




urlpatterns = [
    path('adocao', PaginaAdotar.as_view(), name='adotar'),
    path('adocao/added/', PaginaCadastroAdotar.as_view(), name='added-pet'),
    path('adocao/edit/<int:pk>', PaginaCadastroAdotarEdit.as_view(), name='edit-pet'),
    path('adocao/delete/<int:pk>', PaginaCadastroAdotarDelete.as_view(), name='delete-pet'),
    path('adocao/lista/', PaginaAdotarLista.as_view(), name='lista-pet'),


    path('adocao/perfil/<int:pk>', PerfilPet.as_view(), name='perfil-pet'),
]
