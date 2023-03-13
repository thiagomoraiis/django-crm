from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from adm.models import Venda, Produto

def index(request):
    template = loader.get_template('index.html')
    p = Produto.objects.all()
    context = {
        'p':p
    }
    return HttpResponse(template.render(context, request))

def produto(request):
    template = loader.get_template('produto.html')
    return HttpResponse(template.render())

def carrinho(request):
    template = loader.get_template('carrinho.html')
    p = Produto.objects.all()
    carrin = Venda.objects.count()
    context = {
        'carrin':carrin,
        'p':p,
    }
    return HttpResponse(template.render(context, request))

def base(request):
    template = loader.get_template('basep.html')
    carrin = Venda.objects.count()
    context = {
        'carrin':carrin,
    }
    return HttpResponse(template.render(context, request))