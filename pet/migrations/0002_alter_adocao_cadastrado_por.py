# Generated by Django 4.1.5 on 2023-02-01 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adocao',
            name='cadastrado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Cadastrante'),
        ),
    ]
