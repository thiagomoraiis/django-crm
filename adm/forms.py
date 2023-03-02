from django import forms
from .models import Receita, Teste

# RECEITA_NAME_CHOICES = [
#     ('receita', 'receita'),
#     ('despesa', 'despesa'),  
# ]
class ReceitaModelForm(forms.ModelForm):
    # tipo_receita = forms.ChoiceField(
    #     widget=forms.Select,
    #     choices=RECEITA_NAME_CHOICES 
    # ).capitalize()
    class Meta:
        model = Receita
        fields = '__all__'

class TesteModelForm(forms.ModelForm):
    class Meta:
        model = Teste
        fields = '__all__'