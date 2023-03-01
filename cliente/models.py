from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    idade = models.IntegerField('Idade')
    email = models.EmailField('Email', max_length=120)
    cpf = models.CharField('CPF', max_length=15)
    cep = models.IntegerField('CEP (Cidade, Estado, País)')

    def __str__(self):
        return self.nome.capitalize().strip()
    