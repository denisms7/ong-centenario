from django.db import models



class Especie(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome', unique=True, null=False)
    
    def __str__(self):
        return f"{self.nome}"


class Raca(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, verbose_name='Especie')
    raca = models.CharField(max_length=150, verbose_name='Raça')

    def __str__(self):
        return f"{self.especie.nome} - {self.raca}"


class Idade(models.Model):
    idade = models.CharField(max_length=10, verbose_name='Idade', unique=True, null=False)

    def __str__(self):
        return f"{self.idade}"


class Sexo(models.Model):
    sexo = models.CharField(max_length=10, verbose_name='Sexo', unique=True, null=False)

    def __str__(self):
        return f"{self.sexo}"


class Adocao(models.Model):
    # Dados Pessoais
    nome_dono = models.CharField(max_length=200, verbose_name='Nome Completo do Dono', null=False)
    #Contato
    email_1 = models.CharField(max_length=150, verbose_name='E-mail 01', null=True)
    email_2 = models.CharField(max_length=150, verbose_name='E-mail 02', null=True)
    fone_1 = models.CharField(max_length=15, verbose_name='Fone 01', null=True)
    fone_2 = models.CharField(max_length=15, verbose_name='Fone 02', null=True)
    fone_3 = models.CharField(max_length=15, verbose_name='Fone 03', null=True)
    obs = models.CharField(max_length=2000, verbose_name='Observações', null=True)
    # Endereço
    cep = models.CharField(max_length=8, verbose_name='CEP', null=True)
    estado = models.CharField(max_length=2, verbose_name='Estado', null=True)
    cidade = models.CharField(max_length=200, verbose_name='Cidade', null=True)
    bairro = models.CharField(max_length=200, verbose_name='Bairro', null=True)
    endereco = models.CharField(max_length=250, verbose_name='Endereço', null=True)
    numero = models.IntegerField(default=0, verbose_name='Número', null=True)
    complemento = models.CharField(max_length=2000, verbose_name='Complemento', null=True)
    # Dados do Pet
    nome_pet = models.CharField(max_length=200, verbose_name='Nome do Pet', null=False)
    idade = models.ForeignKey(Idade, on_delete=models.PROTECT, verbose_name='Idade', null=False)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, verbose_name='Especie', null=False)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name='Raça', null=False)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, verbose_name='Sexo', null=False)
    qualidades = models.CharField(max_length=2000, verbose_name='Qualidades', null=False)

    def __str__(self):
        return f"Dono: {self.nome_dono} Pet: {self.nome_pet} Raça: {self.raca}"
