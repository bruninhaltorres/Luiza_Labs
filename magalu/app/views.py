from django.shortcuts import render, redirect
from app.forms import UserModelForm
from django.http import HttpResponse
from .models import Usuario, Produtos
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    produtos = Produtos.objects.filter(favorito = False)
    return render(request, 'list_produtos.html', {'Produtos': produtos})

@login_required(login_url='/login/')
def perfil(request):
    usuario = Usuario.objects.filter(ativo = True)
    return render(request, 'perfil.html', {'Usuario': usuario})

@login_required(login_url='/login/')
def perfil_id(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    return render(request, 'detail.html', {'Usuario': usuario})

@login_required(login_url='/login/')
def detail_produto(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    return render(request, 'detail_produtos.html', {'Produtos': produtos})

@login_required(login_url='/login/')
def detail_produto_favoritado(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    return render(request, 'detail_produtos_favoritados.html', {'Produtos': produtos})

@login_required(login_url='/login/')
def list_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'list_produtos.html', {'Produtos': produtos})

@login_required(login_url='/login/')
def favoritar(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    produtos.favorito = True
    produtos.save()
    return redirect('/favoritos/')

@login_required(login_url='/login/')
def favoritos(request):
    produtos = Produtos.objects.filter(favorito=True)
    return render(request, 'list_favoritos.html', {'Produtos': produtos})

@login_required(login_url='/login/')
def desfavoritar(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    produtos.favorito = False
    produtos.save()
    produtos = Produtos.objects.filter(favorito=True)
    return redirect('/favoritos/')

def alterar(request,id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    return render(request, 'alterar.html', {'usuario': usuario})

def update_usuario(request, id_usuario):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario.delete()
    usuario = Usuario.objects.create(name = nome, email = email)
    return render(request, 'detail.html', {'Usuario': usuario})

def inativar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario.delete()
    usuario = Usuario.objects.all()
    return redirect('/perfil/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cadastro.html', context)

def submit(request):
    nome = request.POST.get('name')
    nome = request.POST.get('first_name')
    email = request.POST.get('email')
    usuario = Usuario.objects.create(name=nome, email=email)
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'sucess.html')

def cadastro_cliente(request):
    return render(request, 'cadastro_cliente.html')

def cliente_submit(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    usuario = Usuario.objects.filter(ativo = True)
    igual = 0
    for u in usuario:
        if email == u.email:
            igual = 1
            
    if igual != 1:
        print('email', email)
        print('u.email', u.email)
        print('IGUAL:', igual)
        usuario = Usuario.objects.create(name=nome, email=email)
        return redirect('/perfil/')
    else:
        return render(request, 'fail.html')

def pesquisar(request):
    title = request.POST.get('title')    
    existe = 0
    produto = Produtos.objects.filter(favorito=False)
    for p in produto:
        if title == p.title:
            existe = 1
    
    if existe == 1:
        produtos = Produtos.objects.get(title = title)
        return render(request, 'detail_produtos.html', {'Produtos': produtos})
    else:
        return render(request, 'pesquisa_erro.html')

