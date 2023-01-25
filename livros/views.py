from django.shortcuts import render
from . models import Livro
from django.shortcuts import redirect       # método de redirecionamento
from usuarios.models import Leitor


# Create your views here.
def index(request):
      
    livros = Livro.objects.all()
    
    if request.session['usuario'] :
        
        objeto = {
        'livros': livros,
        'leitor': Leitor.objects.get(pk = request.session['usuario'])
        }
    
        return render(request, 'index.html', objeto)
    
    else:
        
        objeto = {
        'livros': livros,
        }
    
        return render(request, 'index.html', objeto)


    
    