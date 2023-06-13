from django.contrib.admin import site
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User

from portfolio.models import *
from portfolio.forms import *


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


# *********************************************************************************************
@login_required
def adiciona_projeto(request):
    if request.method == 'POST':
        form = AdicionarProjetoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricaoResumida = form.cleaned_data['descricaoResumida']
            descricao = form.cleaned_data['descricao']
            destaqueHome = form.cleaned_data['destaqueHome']
            categoria = form.cleaned_data['categoria']
            fotos = form.cleaned_data['fotos']

            projeto = Projeto.objects.create(nome=nome, descricaoResumida=descricaoResumida, descricao=descricao, destaqueHome=destaqueHome)
            projeto.categoria.set(categoria)
            projeto.fotos.set(fotos)

            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('users:lista_projetos')
    else:
        form = AdicionarProjetoForm()

    return render(request, 'users/form_adicionar.html', {'form': form})


@login_required
def editar_projeto(request, objeto_id):
    projeto = get_object_or_404(Projeto, id=objeto_id)
    model_admin = site._registry[Projeto]
    form_class = EditarProjetoForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricaoResumida = form.cleaned_data['descricaoResumida']
            descricao = form.cleaned_data['descricao']
            destaqueHome = form.cleaned_data['destaqueHome']
            categoria = form.cleaned_data['categoria']
            fotos = form.cleaned_data['fotos']

            projeto.nome = nome
            projeto.descricaoResumida = descricaoResumida
            projeto.descricao = descricao
            projeto.destaqueHome = destaqueHome
            projeto.save()
            projeto.categoria.set(categoria)
            projeto.fotos.set(fotos)

            # Redirecionar para a página de detalhes do projeto ou outra página desejada
            return redirect('users:lista_projetos')
    else:
        form = form_class(initial={
            'nome': projeto.nome,
            'descricaoResumida': projeto.descricaoResumida,
            'descricao': projeto.descricao,
            'destaqueHome': projeto.destaqueHome,
            'categoria': projeto.categoria.all(),
            'fotos': projeto.fotos.all()
        })

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


# *********************************************************************************************
@login_required
def adiciona_video(request):
    if request.method == 'POST':
        form = AdicionarVideoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            iframe = form.cleaned_data['iframe']
            video = Video.objects.create(nome=nome, iframe=iframe)
            return redirect('users:lista_videos')
    else:
        form = AdicionarVideoForm()

    return render(request, 'users/form_adicionar.html', {'form': form})


@login_required
def editar_video(request, objeto_id):
    video = get_object_or_404(Video, id=objeto_id)

    if request.method == 'POST':
        form = EditarVideoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            iframe = form.cleaned_data['iframe']
            # Atualizar os dados no modelo Video
            video.nome = nome
            video.iframe = iframe
            video.save()
            # Redirecionar para a página de detalhes do vídeo ou outra página desejada
            return redirect('users:lista_videos')
    else:
        form = EditarVideoForm(initial={'nome': video.nome, 'iframe': video.iframe})

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


# *********************************************************************************************
def adiciona_user(request):
    if request.method == 'POST':
        form = AdicionarUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create_user(username=username, email=email, password=password)

            return redirect('users:lista_utilizadores')
    else:
        form = AdicionarUserForm()

    return render(request, 'users/form_adicionar.html', {'form': form})


def edita_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = EditarUserForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()

            # Redirecionar para a página desejada após editar o usuário
            return redirect('users:lista_utilizadores')
    else:
        form = EditarUserForm(initial={'username': user.username, 'email': user.email})

    return render(request, 'users/form_editar.html', {'form': form})


@login_required
def lista_utilizadores(request):
    objs = User.objects.all()

    campos_a_listar = ['username', 'email', 'id']
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
        'titulo': 'Utilizadores',
        'campos_a_listar': campos_a_listar,
        'objs': projetos_array,
        'endereco_edicao': 'users:edita_user',
        'endereco_adicao': 'users:adiciona_user',
        'endereco_eliminar': 'users:eliminar_user',
        'seoTitle': 'Listar Videos | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'users/lista_objs.html', context)


# *********************************************************************************************
def adiciona_formacao(request):
    if request.method == 'POST':
        form = AdicionarFormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            dataInicio = form.cleaned_data['dataInicio']
            dataFim = form.cleaned_data['dataFim']
            detalhes = form.cleaned_data['detalhes']
            pdfFile = form.cleaned_data['pdfFile']

            formacao = Formacao.objects.create(titulo=titulo, dataInicio=dataInicio, dataFim=dataFim,
                                               detalhes=detalhes, pdfFile=pdfFile)
            return redirect('users:lista_formacoes')
    else:
        form = AdicionarFormacaoForm()

    return render(request, 'users/form_adicionar.html', {'form': form})


def edita_formacao(request, objeto_id):
    formacao = get_object_or_404(Formacao, id=objeto_id)

    if request.method == 'POST':
        form = EditarFormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            dataInicio = form.cleaned_data['dataInicio']
            dataFim = form.cleaned_data['dataFim']
            detalhes = form.cleaned_data['detalhes']
            pdfFile = form.cleaned_data['pdfFile']

            formacao.titulo = titulo
            formacao.dataInicio = dataInicio
            formacao.dataFim = dataFim
            formacao.detalhes = detalhes
            formacao.pdfFile = pdfFile
            formacao.save()

            # Redirecionar para a página desejada após editar a formação
            return redirect('users:lista_formacoes')
    else:
        form = EditarFormacaoForm(initial={
            'titulo': formacao.titulo,
            'dataInicio': formacao.dataInicio,
            'dataFim': formacao.dataFim,
            'detalhes': formacao.detalhes,
            'pdfFile': formacao.pdfFile
        })

    return render(request, 'users/form_editar.html', {'form': form})


@login_required
def lista_formacoes(request):
    objs = Formacao.objects.all()

    campos_a_listar = ['titulo', 'id']
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
        'titulo': 'Formação \ Experiência',
        'campos_a_listar': campos_a_listar,
        'objs': projetos_array,
        'endereco_edicao': 'users:edita_formacao',
        'endereco_adicao': 'users:adiciona_formacao',
        'endereco_eliminar': 'users:eliminar_formacao',
        'seoTitle': 'Listar Videos | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'users/lista_objs.html', context)


# *********************************************************************************************
def adiciona_categoria_projeto(request):
    if request.method == 'POST':
        form = AdicionarCategoriaProjetoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']

            categoria_projeto = CatergoriaProjeto.objects.create(nome=nome)
            # Redirecionar para a página desejada após adicionar a categoria do projeto
            return redirect('users:lista_categoria_projeto')
    else:
        form = AdicionarCategoriaProjetoForm()

    return render(request, 'users/form_adicionar.html', {'form': form})


def edita_categoria_projeto(request, objeto_id):
    categoria_projeto = get_object_or_404(CatergoriaProjeto, id=objeto_id)

    if request.method == 'POST':
        form = EditarCategoriaProjetoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']

            categoria_projeto.nome = nome
            categoria_projeto.save()

            return redirect('users:lista_categoria_projeto')
    else:
        form = EditarCategoriaProjetoForm(initial={'nome': categoria_projeto.nome})

    return render(request, 'users/form_editar.html', {'form': form})


@login_required
def lista_categoria_projeto(request):
    objs = CatergoriaProjeto.objects.all()

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
        'titulo': 'Categorias de Projeto',
        'campos_a_listar': campos_a_listar,
        'objs': projetos_array,
        'endereco_edicao': 'users:edita_categoria_projeto',
        'endereco_adicao': 'users:adiciona_categoria_projeto',
        'endereco_eliminar': 'users:eliminar_categoria_projeto',
        'seoTitle': 'Listar Categorais de Projetos | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'users/lista_objs.html', context)


# **************************************************************************************************


@login_required
def eliminar_objeto(request, objeto_id, model, end):
    objeto = get_object_or_404(model, id=objeto_id)
    objeto.delete()
    return redirect(end)
