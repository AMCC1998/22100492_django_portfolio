from django.shortcuts import render, get_object_or_404
from .models import *

from bs4 import BeautifulSoup
import requests
import time, threading
import json

import time
from datetime import datetime


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
        'seoTitle': 'Videos | André Carvalho',
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
    formacoes = Formacao.objects.all()
    context = {
        'formacoes': formacoes,
        'seoTitle': 'Sobre | André Carvalho',
        'seoDescription': 'O meu interesse pela programação web começou há 5 anos quando ingressei no meu primeiro emprego.',
    }
    return render(request, 'portfolio/sobre_mim.html', context)


def metreologia_web_scraping():
    url = '//weather.com/pt-PT/clima/hoje/l/f0d93b551dcc5b4eeee581ecbbc1eec1306bf6c27ea78e3c64d846a3a34969a3'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    dados = []
    localidade = soup.find('div', {'data-cq-observe': True})

    cidade = localidade.find('h1').text
    temperatura_element = soup.find('span', {'data-testid': 'TemperatureValue'})
    temperatura_text = temperatura_element.text if temperatura_element else ''
    temperatura_text = temperatura_text.replace('°', '')
    temperatura = float(temperatura_text) if temperatura_text.isdigit() else 0

    descricao = localidade.find('div', {'data-testid': 'wxPhrase'}).text
    data_hora = datetime.now()
    dados.append({'cidade': cidade, 'temperatura': temperatura, 'descricao': descricao, 'data_hora': data_hora})

    for dado in dados:
        novo_dado = DadosMeteorologia(cidade=dado['cidade'], temperatura=dado['temperatura'], descricao=dado['descricao'], data_hora=dado['data_hora'])
        novo_dado.save()


def consulta_metreologia(request):
    dados = DadosMeteorologia.objects.all()[:60]
    dados_grafico = []
    for dado in dados:
        dado_grafico = {
            'data_hora': dado.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
            'temperatura': dado.temperatura
        }
        dados_grafico.append(dado_grafico)

    context = {
        'dados_grafico': json.dumps(dados_grafico)
    }

    return render(request, 'portfolio/meteorologia.html', context)


def cidades(request):
    dados = Cidade.objects.all()

    context = {
        'cidades': dados
    }

    return render(request, 'portfolio/cidades.html', context)


def agendar_metreologia_web_scraping():
    # metreologia_web_scraping()
    # intervalo_segundos = 5
    intervalo_segundos = 6 * 60 * 60  # Intervalo de 6 horas em segundos
    while True:
        time.sleep(intervalo_segundos)
        metreologia_web_scraping()


t = threading.Thread(target=agendar_metreologia_web_scraping)
t.start()
