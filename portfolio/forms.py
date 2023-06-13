from django import forms
from .models import *


# ********************************** PROJETOS **********************************
class EditarProjetoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    descricaoResumida = forms.CharField(max_length=255)
    descricao = forms.CharField(widget=forms.Textarea)
    destaqueHome = forms.ChoiceField(choices=(('1', 'Sim'), ('0', 'Não')))
    categoria = forms.ModelMultipleChoiceField(
        queryset=CatergoriaProjeto.objects.all(),
        widget=forms.SelectMultiple
    )
    fotos = forms.ModelMultipleChoiceField(
        queryset=Foto.objects.all(),
        widget=forms.SelectMultiple
    )


class AdicionarProjetoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    descricaoResumida = forms.CharField(max_length=255)
    descricao = forms.CharField(widget=forms.Textarea)
    destaqueHome = forms.ChoiceField(choices=(('1', 'Sim'), ('0', 'Não')))
    categoria = forms.ModelMultipleChoiceField(
        queryset=CatergoriaProjeto.objects.all(),
        widget=forms.SelectMultiple
    )
    fotos = forms.ModelMultipleChoiceField(
        queryset=Foto.objects.all(),
        widget=forms.SelectMultiple
    )


# *******************************************************************************

# ********************************** Categorias Projetos *************************************

class AdicionarCategoriaProjetoForm(forms.Form):
    nome = forms.CharField(max_length=50)


class EditarCategoriaProjetoForm(forms.Form):
    nome = forms.CharField(max_length=50)


# *******************************************************************************

# ********************************** Videos *************************************

class AdicionarVideoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    iframe = forms.CharField(widget=forms.Textarea)


class EditarVideoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    iframe = forms.CharField(widget=forms.Textarea)


# *******************************************************************************


# ********************************** Utilizadores *************************************

class AdicionarUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class EditarUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()


# *******************************************************************************

# ********************************** Formações *************************************

class AdicionarFormacaoForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    dataInicio = forms.DateField(required=False)
    dataFim = forms.DateField(required=False)
    detalhes = forms.CharField(widget=forms.Textarea, max_length=5000)
    pdfFile = forms.FileField(required=False)


class EditarFormacaoForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    dataInicio = forms.DateField(required=False)
    dataFim = forms.DateField(required=False)
    detalhes = forms.CharField(widget=forms.Textarea, max_length=5000)
    pdfFile = forms.FileField(required=False)

# *******************************************************************************
