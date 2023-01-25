from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validacao_cadastro/', views.validacao_cadastro, name='validacao_cadastro'),
    path('autenticar/', views.autenticar, name='autenticar'),
    path('logout/', views.logout, name='logout'),
]