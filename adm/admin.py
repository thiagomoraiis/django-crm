from django.contrib import admin
from .models import Receita, Solicitacoes, Gerenciador, CategoriaProduto, Venda, Produto
from .models import Produto

@admin.register(Receita)
class ReceitaAdminModel(admin.ModelAdmin):
    list_display = ('tipo_receita', 'valor')

@admin.register(Solicitacoes)
class SolicitacaoModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'adm', 'concluido')

@admin.register(Gerenciador)
class GerenciadorModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email')

@admin.register(Produto)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco_unitario', 'estoque', 'postado_por')

@admin.register(CategoriaProduto)
class CategoriaModelAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria',)

@admin.register(Venda)
class VendaModelAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_venda')