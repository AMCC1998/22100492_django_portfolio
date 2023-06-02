from django.shortcuts import render
from .models import *


# Create your views here.

#  hello/views.py


def home_page_view(request):
    projetos = Projeto.objects.all()[:3]
    videos = Video.objects.all()[:2]
    return render(request, 'portfolio/home.html', {'projetos': projetos, 'videos': videos})


def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def videos_view(request):
    videos = Video.objects.all()
    return render(request, 'portfolio/videos.html', {'videos': videos})
