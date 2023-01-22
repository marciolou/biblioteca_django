from django.shortcuts import render
from . models import Livro
from django.shortcuts import redirect       # método de redirecionamento
from usuarios.models import Leitor
from django.http import HttpResponse


# Create your views here.
def index(request):
    
    if request.session.get('usuario'):
        leitor = Leitor.objects.get(pk = request.session['usuario'])
        #return HttpResponse(f'Index {leitor}')
        
        livros = Livro.objects.all()
    
        livros = {
        'objeto': livros
    }
        
        return render(request, 'livros/index.html', livros)
    
    else:
        return redirect('/login')


    
    
    