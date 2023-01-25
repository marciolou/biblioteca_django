from django.shortcuts import render
from . models import Leitor
from django.shortcuts import redirect       # método de redirecionamento
from hashlib import sha256                  # criptografia


def login(request):
    
    validacao = request.GET.get('validacao')
    
    confirme = {
        'validacao': validacao
    }
    
    return render(request, 'login.html', confirme)


def autenticar(request):
    
    email = request.POST.get('email')
    senha = sha256(request.POST.get('senha').encode()).hexdigest()
    
    usuario = Leitor.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) != 0:
        request.session['usuario'] = usuario[0].id
        return redirect('index')
        
    else:
        return redirect('/login?validacao=00')
        
    
def logout(request):
    
    request.session['usuario'] = None
    
    return render(request, 'login.html')
    

def cadastro(request):      # Cadastro de usuário novo (leitor)
    
    validacao = request.GET.get('validacao')
    
    confirme = {
        'validacao': validacao
    }
    
    if validacao == 10:
        return redirect('index')
    
    return render(request, 'cadastro.html', confirme)


def validacao_cadastro(request):
    
    nome = request.POST.get('nome')
    senha = sha256(request.POST.get('senha').encode()).hexdigest()
    email = request.POST.get('email')
    nascimento = request.POST.get('nascimento')
    confirmar_senha = sha256(request.POST.get('confirmar_senha').encode()).hexdigest()
    
    usuario = Leitor.objects.filter(email = email)
    
    if len(usuario) > 0:
        return redirect('/cadastro/?validacao=10')
    
    if confirmar_senha != senha:
        return redirect('/cadastro/?validacao=20')
    
    try:
        usuario = Leitor(
            nome = nome ,
            senha = senha,
            email = email ,
            nascimento = nascimento ,
            )
        usuario.save()
    
        return redirect('login')
            
    except:
        return redirect('/cadastro/?validacao=30')
