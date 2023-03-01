from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def cliente(request):
    template = loader.get_template('detalhe_produto.html')
    return HttpResponse(template.render())