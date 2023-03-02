from django.db import models

class Gerenciador(models.Model):
    nome = models.CharField('Nome', max_length=150)
    idade = models.IntegerField('Idade')
    email = models.EmailField('Email', max_length=120)
    cpf = models.CharField('CPF', max_length=15)

    def __str__(self):
        return self.nome.capitalize().strip()

class Receita(models.Model):
    tipo_receita = models.CharField('Informe qual o tipo de receita', max_length=8)
    valor = models.DecimalField('Informe o valor', max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.tipo_receita.title().strip()} R${self.valor}'
    
class Teste(models.Model):
    tipo_receita = models.CharField('Informe qual o tipo de receita', max_length=8)
    valor = models.DecimalField('Informe o valor', max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.tipo_receita.title().strip()} R${self.valor}'