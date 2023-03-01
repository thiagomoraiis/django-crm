from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdminModel(admin.ModelAdmin):
    list_display = ('tipo_receita', 'valor')
