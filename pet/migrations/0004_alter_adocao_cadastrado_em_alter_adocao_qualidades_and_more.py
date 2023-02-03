# Generated by Django 4.1.5 on 2023-02-03 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_alter_adocao_email_1_alter_adocao_email_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adocao',
            name='cadastrado_em',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro'),
        ),
        migrations.AlterField(
            model_name='adocao',
            name='qualidades',
            field=models.CharField(max_length=2000, verbose_name='Qualidades do Pet'),
        ),
        migrations.AlterField(
            model_name='adocao',
            name='status',
            field=models.CharField(choices=[('d', 'Disponível'), ('a', 'Adotado'), ('c', 'Adoção Cancelada')], max_length=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nome',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nome da Espécie'),
        ),
        migrations.AlterField(
            model_name='raca',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pet.especie', verbose_name='Espécie'),
        ),
    ]
