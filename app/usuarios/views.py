from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User




class PaginaPerfil(ListView):
    model = User
    template_name = 'usuarios/perfil.html'
    def get_queryset(self):
        var_id = self.request.user.pk
        self.object_list = User.objects.filter(id=var_id)
        return self.object_list