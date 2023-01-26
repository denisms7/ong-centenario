from django.db import models

# Create your models here.

class Especie(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome', unique=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class Raca(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, verbose_name='Especie')
    raca = models.CharField(max_length=150, verbose_name='Raça')

    def __str__(self):
        return f"{self.especie.nome} - {self.raca}"

