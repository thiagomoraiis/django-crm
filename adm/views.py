from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Receita
from .forms import ReceitaModelForm, TesteModelForm
from django.contrib import messages

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def error404(request):
    template = loader.get_template('error404.html')
    return HttpResponse(template.render())

def forgot_password(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())

def blank(request):
    template = loader.get_template('blank.html')
    return HttpResponse(template.render())

def form(request):
    template = loader.get_template('form.html')
    if request.method == 'POST':
        form = ReceitaModelForm(request.POST or None)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.tipo_receita = form.cleaned_data['tipo_receita']
            receita.valor = form.cleaned_data['valor']
            receita.save()
            form = ReceitaModelForm()
            messages.success(request, 'Formulario salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar o formulario')
    else:
        form = ReceitaModelForm()
        # messages.success(request, 'Erro ao salvar o formulario')
    context = {
        'form':form
    }
    return HttpResponse(template.render(context, request))

def registros(request):
    # receita = Receita.objects.values('')
    template = loader.get_template('registros.html')
    return HttpResponse(template.request)

def teste(request):
    template = loader.get_template('teste.html')
    if request.method == 'POST':
        teste = TesteModelForm(request.POST or None)
        if teste.is_valid():
            r = teste.save(commit=False)
            r.tipo_receita = teste.cleaned_data['tipo_receita']
            r.valor = teste.cleaned_data['valor']
            r.save()
            teste = TesteModelForm()
            messages.success(request, 'Formulario salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar o formulario')
    else:
        teste = TesteModelForm()
    context = {
        'teste':teste
    }
    return HttpResponse(template.render(context, request))