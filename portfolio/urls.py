#  hello/urls.py

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('projetos', views.projetos_view, name='projetos'),
    path('videos', views.videos_view, name='videos'),
    path('labs', views.labs_view, name='labs'),
    path('contactos', views.contactos_view, name='contactos'),
    path('sobre', views.sobre_view, name='sobre'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
