#  hello/urls.py

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('projetos', views.projetos_view, name='projetos'),
    path('videos', views.videos_view, name='videos'),
    path('area/<int:area_id>/', views.area_detail_view, name='area_detail'),
]

# Adicione esta linha para configurar a rota para arquivos de mídia estáticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
