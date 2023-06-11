from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models import TextField
from django.utils.html import format_html
from django import forms

from django.db import models


# Create your models here.
class Blog(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class CatergoriaProjeto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricaoResumida = models.CharField(max_length=255)
    descricao = models.TextField(max_length=5000)
    OPÇÕES = (
        ('1', 'Sim'),
        ('0', 'Não'),
    )
    destaqueHome = models.CharField(max_length=10, choices=OPÇÕES, default='1')
    categoria = models.ManyToManyField(
        CatergoriaProjeto,
        related_name='projetos'
    )
    fotos = models.ManyToManyField('Foto', related_name='projetos')

    def __str__(self):
        return self.nome


class Foto(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    alt = models.CharField(max_length=255, default='')
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        imagem_url = "/imagens/" + self.imagem.name
        return format_html(self.nome + '<img src="{}" height="60" alt="{}">', imagem_url, self.alt)


class Area_Site(models.Model):
    nome = models.CharField(max_length=50)
    nomeItemMenu = models.CharField(max_length=50, default='')
    seoTitle = models.CharField(max_length=50, default='')
    seoDescription = TextField(max_length=70, default='')
    html = models.TextField(default='')
    posicao = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} (Posição: {self.posicao})"


class Video(models.Model):
    nome = models.CharField(max_length=50)
    iframe = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    titulo = models.CharField(max_length=255)
    dataInicio = models.DateField(null=True, default=None)
    dataFim = models.DateField(null=True, default=None)
    detalhes = models.TextField(max_length=5000, default='')
    pdfFile = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.titulo