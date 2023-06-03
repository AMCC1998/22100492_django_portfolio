from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

#  hello/views.py


def home_page_view(request):
    areas = Area_Site.objects.all().order_by('posicao')
    projetos = Projeto.objects.all().filter(destaqueHome='1')[:3]
    videos = Video.objects.all()[:2]
    context = {
        'projetos': projetos,
        'videos': videos,
        'areas': areas,
        'seoTitle': 'Home | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'portfolio/home.html', context)


def projetos_view(request):
    areas = Area_Site.objects.all().order_by('posicao')
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos,
        'areas': areas,
        'seoTitle': 'Projetos | André Carvalho',
        'seoDescription': 'Os meus projetos, em diversas áreas.',
    }
    return render(request, 'portfolio/projetos.html', context)


def videos_view(request):
    areas = Area_Site.objects.all().order_by('posicao')
    videos = Video.objects.all()
    context = {
        'videos': videos,
        'areas': areas,
        'seoTitle': 'Projetos | André Carvalho',
        'seoDescription': 'O meu canal de YouTube.',
    }
    return render(request, 'portfolio/videos.html', context)


def area_detail_view(request, area_id):
    areas = Area_Site.objects.all().order_by('posicao')
    area = get_object_or_404(Area_Site, id=area_id)
    context = {
        'area': area,
        'areas': areas,
        'seoTitle': area.seoTitle,
        'seoDescription': area.seoDescription,
    }
    return render(request, 'portfolio/area_detail.html', context)
