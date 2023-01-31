from django.urls import path

from djan


urlpatterns = [
    path('login', PaginaAdotar.as_view(), name='adotar'),
]