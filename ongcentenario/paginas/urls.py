from django.urls import path
from .views import PaginaInicial, PaginaSobre


urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
]