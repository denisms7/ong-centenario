from django.db import models


class Especie(models.Model):
    nome = models.CharField(
        max_length=150, verbose_name='Nome', unique=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class Raca(models.Model):
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, verbose_name='Especie')
    raca = models.CharField(max_length=150, verbose_name='Raça')

    def __str__(self):
        return f"{self.especie.nome} - {self.raca}"


class Idade(models.Model):
    idade = models.CharField(
        max_length=10, verbose_name='Idade', unique=True, null=False)

    def __str__(self):
        return f"{self.idade}"


class Adocao(models.Model):
    VAR_SEXO = [
        ('Indefinido', 'Indefinido'),
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]

    VAR_STATUS = [
        ('d', 'Disponível'),
        ('a', 'Adotado'),
        ('c', 'Adoção Cancelada'),
    ]

    # Sistema
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    # Dados Pessoais
    nome_dono = models.CharField(
        max_length=200, verbose_name='Nome Completo do Dono')
    # Contato
    email_1 = models.CharField(
        max_length=150, verbose_name='E-mail 01', null=True, blank=True)
    email_2 = models.CharField(
        max_length=150, verbose_name='E-mail 02', null=True, blank=True)
    fone_1 = models.CharField(max_length=15, verbose_name='Fone 01')
    fone_2 = models.CharField(
        max_length=15, verbose_name='Fone 02', null=True, blank=True)
    fone_3 = models.CharField(
        max_length=15, verbose_name='Fone 03', null=True, blank=True)
    obs = models.TextField(
        max_length=2000, verbose_name='Observações', null=True, blank=True)
    # Endereço
    cep = models.CharField(
        max_length=8, verbose_name='CEP', null=True, blank=True)
    estado = models.CharField(
        max_length=2, verbose_name='Estado', null=True, blank=True)
    cidade = models.CharField(
        max_length=200, verbose_name='Cidade', null=True, blank=True)
    bairro = models.CharField(
        max_length=200, verbose_name='Bairro', null=True, blank=True)
    endereco = models.CharField(
        max_length=250, verbose_name='Endereço', null=True, blank=True)
    numero = models.IntegerField(
        default=0, verbose_name='Número', null=True, blank=True)
    complemento = models.TextField(
        max_length=2000, verbose_name='Complemento', null=True, blank=True)
    # Dados do Pet
    nome_pet = models.CharField(max_length=200, verbose_name='Nome do Pet')
    idade = models.ForeignKey(
        Idade, on_delete=models.PROTECT, verbose_name='Idade')
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, verbose_name='Especie')
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, verbose_name='Raça')
    sexo = models.CharField(max_length=10, choices=VAR_SEXO)
    qualidades = models.CharField(max_length=2000, verbose_name='Qualidades')
    img = models.ImageField(upload_to='Adocao_fotos/', verbose_name='Foto')
    # Status
    status = models.CharField(max_length=1, choices=VAR_STATUS)

    def __str__(self):
        return f"Dono: {self.nome_dono} Pet: {self.nome_pet} Raça: {self.raca}"
