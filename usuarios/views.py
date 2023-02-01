from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

class PaginaPerfil(ListView):
    model = User
    template_name = 'usuarios/perfil.html'
