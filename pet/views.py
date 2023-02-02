from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Adocao
from django.db.models import Q

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator

class PaginaCadastroAdotar(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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
    success_url = reverse_lazy('lista-pet')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        
        url = super().form_valid(form)
        
        return url

class PaginaCadastroAdotarEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
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
    success_url = reverse_lazy('lista-pet')

class PaginaCadastroAdotarDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Adocao
    template_name = 'pet/divulgar_delete.html'
    success_url = reverse_lazy('lista-pet')

class PaginaAdotarLista(LoginRequiredMixin, ListView):
    paginate_by = 20
    login_url = reverse_lazy('login')
    model = Adocao
    template_name = 'pet/divulgar_lista.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nome_dono__icontains=query) | Q(nome_pet__icontains=query)
            )
        return queryset


class PaginaAdotar(ListView):
    paginate_by = 10
    model = Adocao
    template_name = 'pet/divulgar.html'
    def get_queryset(self):
        self.object_list = Adocao.objects.filter(status='d')
        return self.object_list

class PerfilPet(ListView):
    model = Adocao
    template_name = 'pet/pet_perfil.html'

    def get_queryset(self):
        self.object_list = Adocao.objects.filter(pk=self.kwargs['pk'])
        return self.object_list
