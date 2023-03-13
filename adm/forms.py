from django import forms
from .models import *

class ReceitaModelForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco_unitario', 'imagem', 'categoria', 'estoque', 'postado_por']


class SolicitacaoModelForm(forms.ModelForm):

    class Meta:
        model = Solicitacoes
        fields = ('titulo', 'conteudo', 'adm', 'concluido')




        # widgets = {
        #     'concluido': forms.CheckboxInput
        # }

# class TesteModelForm(forms.ModelForm):
    # nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # ativo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    # ativo = forms.BooleanField(widget=forms.RadioSelect(choices=[(True, 'Concluído'), (False, 'Não concluído')]))

    # class Meta:
    #     model = Teste
    #     fields = ['nome', 'sobrenome', 'email', 'ativo']
