#  hello/urls.py

from django.urls import path

from django.urls import path

from portfolio.models import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User

app_name = "users"

urlpatterns = [
    path('', views.login_view, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    # Projetos
    path('adiciona_projeto', views.adiciona_projeto, name='adiciona_projeto'),
    path('editar_projeto/<int:objeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('eliminar_projeto/<int:objeto_id>/', views.eliminar_objeto, {'model': Projeto, 'end': 'users:lista_projetos'}, name='eliminar_projeto'),
    path('lista_projetos', views.lista_projetos, name='lista_projetos'),

    # Categorias de Projeto
    path('adiciona_categoria_projeto', views.adiciona_categoria_projeto, name='adiciona_categoria_projeto'),
    path('edita_categoria_projeto/<int:objeto_id>/', views.edita_categoria_projeto, name='edita_categoria_projeto'),
    path('eliminar_categoria_projeto/<int:objeto_id>/', views.eliminar_objeto, {'model': CatergoriaProjeto, 'end': 'users:lista_categoria_projeto'}, name='eliminar_categoria_projeto'),
    path('lista_categoria_projeto', views.lista_categoria_projeto, name='lista_categoria_projeto'),


    # Videos
    path('adiciona_video', views.adiciona_video, name='adiciona_video'),
    path('editar_video/<int:objeto_id>/', views.editar_video, name='editar_video'),
    path('eliminar_video/<int:objeto_id>/', views.eliminar_objeto, {'model': Video, 'end': 'users:lista_videos'}, name='eliminar_video'),
    path('lista_videos', views.lista_videos, name='lista_videos'),

    # Users
    path('adiciona_user', views.adiciona_user, name='adiciona_user'),
    path('edita_user/<int:user_id>/', views.edita_user, name='edita_user'),
    path('lista_utilizadores', views.lista_utilizadores, name='lista_utilizadores'),
    path('eliminar_user/<int:objeto_id>/', views.eliminar_objeto, {'model': User, 'end': 'users:lista_utilizadores'}, name='eliminar_user'),

    # Formações
    path('adiciona_formacao', views.adiciona_formacao, name='adiciona_formacao'),
    path('edita_formacao/<int:objeto_id>/', views.edita_formacao, name='edita_formacao'),
    path('eliminar_formacao/<int:objeto_id>/', views.eliminar_objeto, {'model': Formacao, 'end': 'users:lista_formacoes'}, name='eliminar_formacao'),
    path('lista_formacoes', views.lista_formacoes, name='lista_formacoes'),

    # Fotos
    path('adiciona_foto', views.adiciona_foto, name='adiciona_foto'),
    path('edita_foto/<int:objeto_id>/', views.edita_foto, name='edita_foto'),
    path('eliminar_foto/<int:objeto_id>/', views.eliminar_objeto, {'model': Foto, 'end': 'users:lista_fotos'}, name='eliminar_foto'),
    path('lista_fotos', views.lista_fotos, name='lista_fotos'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
