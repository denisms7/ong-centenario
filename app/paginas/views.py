from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class PaginaSobre(TemplateView):
    template_name = 'paginas/estatuto/index.html'