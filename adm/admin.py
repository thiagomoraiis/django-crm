from django.contrib import admin
from .models import Receita, Teste

@admin.register(Receita)
class ReceitaAdminModel(admin.ModelAdmin):
    list_display = ('tipo_receita', 'valor')

@admin.register(Teste)
class TesteAdminModel(admin.ModelAdmin):
    list_display = ('tipo_receita', 'valor')