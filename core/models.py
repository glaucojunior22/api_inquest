from django.db import models

class Person(models.Model):
    cpf = models.CharField('CPF', max_length=15)
    name = models.CharField('Nome', max_length=255)
    birthday = models.DateField('Data de Nascimento')


class Enterprise(models.Model):
    owner_document = models.CharField('CPF/CNPJ Proprietário', max_length=18)
    name = models.CharField('Nome', max_length=255)
    fantasy_name = models.CharField('Nome Fantasia', max_length=255)
    address = models.CharField('Endereço', max_length=255)


class Possession(models.Model):
    name = models.CharField('Nome', max_length=100)
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    description = models.TextField('Descrição', blank=True, null=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)