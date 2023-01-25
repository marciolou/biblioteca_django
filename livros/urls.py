from django.contrib import admin
from django.urls import path
from . import views

# (Arquivo settings da configuração do Dajngo (core/settings.py))
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
