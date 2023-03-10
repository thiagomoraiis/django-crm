from django import forms
from .models import Receita,Solicitacoes, Teste

class ReceitaModelForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'

class SolicitacaoModelForm(forms.ModelForm):
    class Meta:
        model = Solicitacoes
        fields = '__all__'

class TesteModelForm(forms.ModelForm):
    # nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # ativo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    ativo = forms.BooleanField(widget=forms.RadioSelect(choices=[(True, 'Concluído'), (False, 'Não concluído')]))

    class Meta:
        model = Teste
        fields = ['nome', 'sobrenome', 'email', 'ativo']