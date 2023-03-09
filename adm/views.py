from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Receita, Teste
from .forms import ReceitaModelForm, TesteModelForm
from django.contrib import messages
from django.db.models import Sum

def dashboard(request):
    template = loader.get_template('dashboard.html')
    soma = Receita.objects.aggregate(soma=Sum('valor'))['soma']
    soma = round(soma, 2)
    ano = soma * 12
    context = {
        'soma':soma,
        'ano': ano
    }
    return HttpResponse(template.render(context, request))

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
    template = loader.get_template('registros.html')
    # receita = Receita.objects.filter(tipo_receita='receita')
    receita = Receita.objects.all()
    context = {
        'receita':receita
    }
    return HttpResponse(template.render(context, request))

def edit(request, id):
    template = loader.get_template('edit.html')
    ed = Receita.objects.get(id=id)
    if request.method == 'POST':
        ed.tipo_receita = request.POST['tipo_receita']
        ed.valor = request.POST['valor']
        ed.save()
        return redirect('registros')
    context = {
        'ed':ed
    }
    return HttpResponse(template.render(context, request))

def deletar(request, id):
    template = loader.get_template('deletar.html')
    de = Receita.objects.get(id=id)
    if request.method == 'POST':
        de.delete()
        return redirect('registros')
    context = {
        'de':de
    }
    return HttpResponse(template.render(context, request))