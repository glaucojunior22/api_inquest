# Generated by Django 3.1.3 on 2020-11-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_document', models.CharField(max_length=18, verbose_name='CPF/CNPJ Proprietário')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('fantasy_name', models.CharField(max_length=255, verbose_name='Nome Fantasia')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('birthday', models.DateField(verbose_name='Data de Nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
        ),
    ]