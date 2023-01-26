from django.urls import path
from .views import PaginaAdotar




urlpatterns = [
    path('adotar', PaginaAdotar.as_view(), name='adotar'),
]