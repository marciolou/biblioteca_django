from django.db import models

class Leitor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    nascimento = models.DateTimeField()       
    senha = models.CharField(max_length=64) # sha256 cria a senha com 64 caracteres
    
    def __str__(self):
        return self.nome
    
