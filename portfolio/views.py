from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

#  hello/views.py


def home_page_view(request):
    projetos = Projeto.objects.all().filter(destaqueHome='1')[:3]
    videos = Video.objects.all()[:2]
    context = {
        'projetos': projetos,
        'videos': videos,
        'seoTitle': 'Home | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'portfolio/home.html', context)


def projetos_view(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos,
        'seoTitle': 'Projetos | André Carvalho',
        'seoDescription': 'Os meus projetos, em diversas áreas.',
    }
    return render(request, 'portfolio/projetos.html', context)


def videos_view(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
        'seoTitle': 'Projetos | André Carvalho',
        'seoDescription': 'O meu canal de YouTube.',
    }
    return render(request, 'portfolio/videos.html', context)


def labs_view(request):
    context = {
        'seoTitle': 'Labs | André Carvalho',
        'seoDescription': 'Labs desenvolvidos na cadeira de Programação Web.',
    }
    return render(request, 'portfolio/labs.html', context)


def contactos_view(request):
    context = {
        'seoTitle': 'Contactos | André Carvalho',
        'seoDescription': 'Contactos.',
    }
    return render(request, 'portfolio/contactos.html', context)


def sobre_view(request):
    context = {
        'seoTitle': 'Sobre | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'portfolio/sobre_mim.html', context)
