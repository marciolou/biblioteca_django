from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    editora = models.CharField(max_length=150)        
    previa = RichTextUploadingField()
    capa = models.FileField(upload_to='capa/')
    arquivo = models.FileField(upload_to='pdf/')
    
    def __str__(self):
        return f'{self.titulo.title()}'
