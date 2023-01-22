from django.shortcuts import render
from . models import Leitor
from django.shortcuts import redirect       # método de redirecionamento
from hashlib import sha256                  # criptografia
from django.http import HttpResponse


# Create your views here.

def login(request):         # ok porem o template não ficou como o esperado
    
    validacao = request.GET.get('validacao')
    
    confirme = {
        'validacao': validacao
    }
    
    return render(request, 'usuarios/login.html', confirme)


def autenticar(request):            # ok
    
    email = request.POST.get('email')
    senha = sha256(request.POST.get('senha').encode()).hexdigest()
    
    
    usuario = Leitor.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) != 0:
        request.session['usuario'] = usuario[0].id   # ok
        return redirect('index')
        
    else:
        return redirect('/login?validacao=00')            # ajustar para fazer a mensagem de erro 
        
    
def logout(request):            # ok
    
    request.session['usuario'] = None
    
    return render(request, 'usuarios/login.html')
    


def cadastro(request):      # cadastrar usuário novo (leitor)
    
    validacao = request.GET.get('validacao')
    
    confirme = {
        'validacao': validacao
    }
    
    return render(request, 'usuarios/cadastro.html', confirme)


def validacao_cadastro(request):            # ok    está com uma falha na senha 
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    nascimento = request.POST.get('nascimento')
    senha = request.POST.get('senha')
    
    usuario = Leitor.objects.filter(email = email)
    
    if len(usuario) > 0:
        return redirect('/cadastro/?validacao=10')
    
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/cadastro/?validacao=20')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Leitor(
            nome = nome ,
            email = email ,
            nascimento = nascimento ,
            senha = senha
            )
        usuario.save()
       
        #return redirect('/cadastro/?validacao=00')     Criar uma mensagem em JavaScrypt com temporizador e logo após fazer o redirecionamento
        return redirect('index')
        
    except:
        return redirect('/cadastro/?validacao=30')

