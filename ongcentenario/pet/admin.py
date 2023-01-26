from django.contrib import admin
from .models import Especie, Raca, Sexo, Idade

# Register your models here.
admin.site.register(Especie)
admin.site.register(Raca)
admin.site.register(Idade)
admin.site.register(Sexo)