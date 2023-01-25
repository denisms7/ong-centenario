from django.urls import path
from .views import PaginaAdotar


app_name = 'inicio'

urlpatterns = [
    path('adotar', PaginaAdotar.as_view(), name='inicio'),
]