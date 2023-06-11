#  hello/urls.py

from django.urls import path

from django.urls import path

from portfolio.models import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

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

    # Videos
    path('adiciona_video', views.adiciona_video, name='adiciona_video'),
    path('editar_video/<int:objeto_id>/', views.editar_video, name='editar_video'),
    path('eliminar_video/<int:objeto_id>/', views.eliminar_objeto, {'model': Video, 'end': 'users:lista_videos'}, name='eliminar_video'),
    path('lista_videos', views.lista_videos, name='lista_videos'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
