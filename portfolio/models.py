from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html


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


class Area(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='areas'
    )

    def __str__(self):
        return self.nome


class Video(models.Model):
    nome = models.CharField(max_length=50)
    iframe = models.TextField(max_length=2000)
    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    areas = models.ManyToManyField(
        Area,
        related_name='autores'
    )

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    data_criacao = models.CharField
    autor = models.ManyToManyField(
        Autor,
        related_name='autores'
    )
    areas = models.ManyToManyField(
        Area,
        related_name='artigos'
    )

    def __str__(self):
        return self.titulo
