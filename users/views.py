from django.contrib.admin import site
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect

from portfolio.models import *


@login_required
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:home"))
        else:
            return render(request, 'users/login.html', {
                "message": "Credenciais inválidas."
            })
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })


@login_required
def adiciona_projeto(request):
    model_admin = site._registry[Projeto]
    form_class = model_admin.get_form(request)

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:lista_projetos')
    else:
        form = form_class()

    return render(request, 'users/form_adicionar.html', {'form': form})


@login_required
def editar_projeto(request, objeto_id):
    projeto = get_object_or_404(Projeto, id=objeto_id)
    model_admin = site._registry[Projeto]
    form_class = model_admin.get_form(request)

    if request.method == 'POST':
        form = form_class(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('users:lista_projetos')
    else:
        form = form_class(instance=projeto)

    return render(request, 'users/form_editar.html', {'form': form})


@login_required
def lista_projetos(request):
    projetos = Projeto.objects.all()

    campos_a_listar = ['nome', 'id']
    projetos_array = []

    for projeto in projetos:
        projeto_lista = []
        for campo in campos_a_listar:
            try:
                valor = getattr(projeto, campo)
                campo_verbose = projeto._meta.get_field(campo).verbose_name
                projeto_lista.append({'Campo': campo_verbose, 'Valor': valor})
            except AttributeError:
                continue
        projetos_array.append(projeto_lista)

    context = {
        'titulo': 'Projetos',
        'campos_a_listar': campos_a_listar,
        'objs': projetos_array,
        'endereco_edicao': 'users:editar_projeto',
        'endereco_adicao': 'users:adiciona_projeto',
        'endereco_eliminar': 'users:eliminar_projeto',
        'seoTitle': 'Listar Projetos | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'users/lista_objs.html', context)


@login_required
def adiciona_video(request):
    model_admin = site._registry[Video]
    form_class = model_admin.get_form(request)

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:lista_videos')
    else:
        form = form_class()

    return render(request, 'users/form_adicionar.html', {'form': form})


@login_required
def editar_video(request, objeto_id):
    obj = get_object_or_404(Video, id=objeto_id)
    model_admin = site._registry[Video]
    form_class = model_admin.get_form(request)

    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('users:lista_videos')
    else:
        form = form_class(instance=obj)

    return render(request, 'users/form_editar.html', {'form': form})


@login_required
def lista_videos(request):
    objs = Video.objects.all()

    campos_a_listar = ['nome', 'id']
    projetos_array = []

    for obj in objs:
        projeto_lista = []
        for campo in campos_a_listar:
            try:
                valor = getattr(obj, campo)
                campo_verbose = obj._meta.get_field(campo).verbose_name
                projeto_lista.append({'Campo': campo_verbose, 'Valor': valor})
            except AttributeError:
                continue
        projetos_array.append(projeto_lista)

    context = {
        'titulo': 'Videos',
        'campos_a_listar': campos_a_listar,
        'objs': projetos_array,
        'endereco_edicao': 'users:editar_video',
        'endereco_adicao': 'users:adiciona_video',
        'endereco_eliminar': 'users:eliminar_video',
        'seoTitle': 'Listar Videos | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'users/lista_objs.html', context)


def eliminar_objeto(request, objeto_id, model, end):
    objeto = get_object_or_404(model, id=objeto_id)
    objeto.delete()
    return redirect(end)
