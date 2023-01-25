from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'index.html'

class PaginaSobre(TemplateView):
    template_name = 'sobre.html'