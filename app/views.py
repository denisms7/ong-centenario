from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home/index.html'


class Sobre(TemplateView):
    template_name = 'home/study.html'
