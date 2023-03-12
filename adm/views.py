from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Receita, Solicitacoes
from .forms import ReceitaModelForm, SolicitacaoModelForm
from django.contrib import messages
from django.db.models import Sum

def dashboard(request):
    template = loader.get_template('dashboard.html')
    soma = Receita.objects.aggregate(soma=Sum('valor'))['soma']
    soma = round(soma, 2)
    ano = soma * 12
    count_false = Solicitacoes.objects.filter(concluido=False).count()
    count_true = Solicitacoes.objects.filter(concluido=True).count()
    tudo = Solicitacoes.objects.values('concluido').count()
    porcent = (count_true*100) / tudo
    porcent = round(porcent, 2)
    context = {
        'soma':soma,
        'ano': ano,
        'count_false':count_false,
        'porcentagem':porcent,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

# def error404(request, exception):
#     template = loader.get_template('404.html')
#     return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404)

# def error500(request):
#     template = loader.get_template('500.html')
#     return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=500)

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

def solicitacoes(request):
    template = loader.get_template('solicitacoes.html')
    solicita = Solicitacoes.objects.all()
    context = {
        'solicita':solicita
    }
    return HttpResponse(template.render(context, request))

def solicitar(request):
    if request.method == 'POST':
        form = SolicitacaoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitacoes')
    else:
        form = SolicitacaoModelForm()
    context={
        'form':form
    }
    return render(request, 'solicitacoes_criar.html', context)

def edit_solicitar(request, id):
    template = loader.get_template('edit_solicitar.html')
    sol = get_object_or_404(Solicitacoes, id=id)
    if request.method == 'POST':
        form = SolicitacaoModelForm(request.POST, instance=sol)
        if form.is_valid():
            form.save()
            return redirect('solicitacoes')
    else:
        form = SolicitacaoModelForm(instance=sol)
    context = {
        'form':form
    }
    return HttpResponse(template.render(context, request))

def del_solicitar(request, id):
    template = loader.get_template('del_solicitar.html')
    de = get_object_or_404(Solicitacoes, id=id)
    if request.method == 'POST':
        de.delete()
        return redirect('solicitacoes')
    context={
        'de':de
    }
    return HttpResponse(template.render(context, request))

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(template.render())