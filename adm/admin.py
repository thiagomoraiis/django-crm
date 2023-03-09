from django.contrib import admin
from .models import Receita, Solicitacoes, Gerenciador, Teste

@admin.register(Receita)
class ReceitaAdminModel(admin.ModelAdmin):
    list_display = ('tipo_receita', 'valor')

@admin.register(Solicitacoes)
class SolicitacaoModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'adm')

@admin.register(Gerenciador)
class GerenciadorModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email')

@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')