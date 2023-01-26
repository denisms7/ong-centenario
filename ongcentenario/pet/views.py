from django.views.generic import TemplateView

# Create your views here.
class PaginaAdotar(TemplateView):
    template_name = 'pet/divulgar.html'

class PaginaCadastroAdotar(TemplateView):
    template_name = 'pet/divulgar_cadastro.html'