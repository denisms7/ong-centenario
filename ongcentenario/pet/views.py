from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Adocao
from django.urls import reverse_lazy


class PaginaCadastroAdotar(CreateView):
    model = Adocao
    fields = [
        'nome_dono',
        'email_1',
        'email_2',
        'fone_1',
        'fone_2',
        'fone_3',
        'obs',
        'cep',
        'estado',
        'cidade',
        'bairro',
        'endereco',
        'numero',
        'complemento',
        'nome_pet',
        'idade',
        'especie',
        'raca',
        'sexo',
        'qualidades',
        'img',
        'status',
    ]

    template_name = 'pet/divulgar_cadastro.html'
    success_url = reverse_lazy('adotar')


class PaginaCadastroAdotarEdit(UpdateView):
    model = Adocao
    fields = [
        'nome_dono',
        'email_1',
        'email_2',
        'fone_1',
        'fone_2',
        'fone_3',
        'obs',
        'cep',
        'estado',
        'cidade',
        'bairro',
        'endereco',
        'numero',
        'complemento',
        'nome_pet',
        'idade',
        'especie',
        'raca',
        'sexo',
        'qualidades',
        'img',
        'status',
    ]

    template_name = 'pet/divulgar_cadastro.html'

    success_url = reverse_lazy('adotar')


class PaginaCadastroAdotarDelete(DeleteView):
    model = Adocao
    template_name = 'pet/divulgar_delete.html'
    success_url = reverse_lazy('adotar')


class PaginaAdotar(ListView):
    model = Adocao
    template_name = 'pet/divulgar.html'