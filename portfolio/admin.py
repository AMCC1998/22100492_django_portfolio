from django.contrib import admin
from .models import *

admin.site.site_title = 'André Carvalho'
admin.site.site_header = 'André Carvalho'

# Register your models here.
admin.site.register(Blog)
admin.site.register(Projeto)
admin.site.register(CatergoriaProjeto)
admin.site.register(Foto)
admin.site.register(Video)
admin.site.register(Formacao)
admin.site.register(DadosMeteorologia)