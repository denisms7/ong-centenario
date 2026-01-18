from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import default_storage

class Especie(models.Model):
    nome = models.CharField(
        max_length=150, verbose_name=_('Nome da Espécie'), unique=True, null=False)
    def __str__(self):
        return f"{self.nome}"


class Raca(models.Model):
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, verbose_name=_('Espécie'))
    raca = models.CharField(max_length=150, verbose_name=_('Raça'))
    def __str__(self):
        return f"{self.especie.nome} - {self.raca}"


class Adocao(models.Model):
    SEXO_CHOICES = [
        ('I', _('Indefinido')),
        ('M', _('Macho')),
        ('F', _('Fêmea')),
    ]

    STATUS_CHOICES = [
        ('d', _('Disponível')),
        ('a', _('Adotado')),
        ('c', _('Adoção Cancelada')),
    ]

    IDADE_CHOICES = [
        ('Desconhecida', _('Desconhecida')),

        ('01 Mês', _('01 Mês')),
        ('02 Mêses', _('02 Mêses')),
        ('03 Mêses', _('03 Mêses')),
        ('04 Mêses', _('04 Mêses')),
        ('05 Mêses', _('05 Mêses')),
        ('06 Mêses', _('06 Mêses')),
        ('07 Mêses', _('07 Mêses')),
        ('08 Mêses', _('08 Mêses')),
        ('09 Mêses', _('09 Mêses')),
        ('10 Mêses', _('10 Mêses')),
        ('11 Mêses', _('11 Mêses')),


        ('01 Ano', _('01 Ano')),
        ('02 Anos', _('02 Anos')),
        ('03 Anos', _('03 Anos')),
        ('04 Anos', _('04 Anos')),
        ('05 Anos', _('05 Anos')),
        ('06 Anos', _('06 Anos')),
        ('07 Anos', _('07 Anos')),
        ('08 Anos', _('08 Anos')),
        ('09 Anos', _('09 Anos')),

        ('10 Anos', _('10 Anos')),
        ('11 Anos', _('11 Anos')),
        ('12 Anos', _('12 Anos')),
        ('13 Anos', _('13 Anos')),
        ('14 Anos', _('14 Anos')),
        ('15 Anos', _('15 Anos')),
        ('16 Anos', _('16 Anos')),
        ('17 Anos', _('17 Anos')),
        ('18 Anos', _('18 Anos')),
        ('19 Anos', _('19 Anos')),

        ('20 Anos', _('20 Anos')),
        ('21 Anos', _('21 Anos')),
        ('22 Anos', _('22 Anos')),
        ('23 Anos', _('23 Anos')),
        ('24 Anos', _('24 Anos')),
        ('25 Anos', _('25 Anos')),
        ('26 Anos', _('26 Anos')),
        ('27 Anos', _('27 Anos')),
        ('28 Anos', _('28 Anos')),
        ('29 Anos', _('29 Anos')),

        ('30 Anos', _('30 Anos')),
    ]

    # Sistema
    cadastrado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de Cadastro'))
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Cadastrante'))

    # Dados Pessoais
    nome_dono = models.CharField(
        max_length=200, verbose_name=_('Nome Completo do Dono'))
    # Contato
    email_1 = models.EmailField(
        max_length=150, verbose_name=_('E-mail 01'), null=True, blank=True)
    email_2 = models.EmailField(
        max_length=150, verbose_name=_('E-mail 02'), null=True, blank=True)
    fone_1 = models.CharField(max_length=15, verbose_name=_('Fone 01'))
    fone_2 = models.CharField(
        max_length=15, verbose_name=_('Fone 02'), null=True, blank=True)
    fone_3 = models.CharField(
        max_length=15, verbose_name=_('Fone 03'), null=True, blank=True)
    obs = models.TextField(
        max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # Endereço
    cep = models.CharField(
        max_length=8, verbose_name='CEP', null=True, blank=True)
    estado = models.CharField(
        max_length=2, verbose_name=_('Estado'), null=True, blank=True)
    cidade = models.CharField(
        max_length=200, verbose_name=_('Cidade'), null=True, blank=True)
    bairro = models.CharField(
        max_length=200, verbose_name=_('Bairro'), null=True, blank=True)
    endereco = models.CharField(
        max_length=250, verbose_name=_('Endereço'), null=True, blank=True)
    numero = models.IntegerField(
        default=0, verbose_name=_('Número'), null=True, blank=True)
    complemento = models.TextField(
        max_length=2000, verbose_name=_('Complemento'), null=True, blank=True)
    # Dados do Pet
    nome_pet = models.CharField(max_length=200, verbose_name=_('Nome do Pet'))
    idade = models.CharField(max_length=15, choices=IDADE_CHOICES)
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, verbose_name=_('Especie'))
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, verbose_name=_('Raça'))
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    qualidades = models.CharField(max_length=2000, verbose_name=_('Qualidades do Pet'))
    img = models.ImageField(upload_to='Adocao_fotos/', verbose_name=_('Foto'))
    # Status
    status = models.CharField(max_length=1, choices=STATUS_CHOICES , verbose_name=_('Status'))


    def __str__(self):
        return f"Dono: {self.nome_dono} || Pet: {self.nome_pet} - {self.raca}"
    
    def delete(self, *args, **kwargs):
        if self.img:
            default_storage.delete(self.img.path)
        super().delete(*args, **kwargs)
