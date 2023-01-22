from django.contrib import admin
from . import models
from usuarios.models import Leitor



@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'nascimento', 'senha')
    # Inpossibilita o administrador do site de fazer/criar usuários(leitores) via Django admin
    
    