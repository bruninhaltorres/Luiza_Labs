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
def list_produtos(request):
    produtos = Produtos.objects.filter(ativo = True)
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
    return render(request, 'list_favoritos.html', {'Produtos': produtos})

def alterar(request,id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario_form = UserModelForm(request.POST or None)
    if usuario_form.is_valid():
        usuario_form.save()
    return render(request, 'alterar.html', {'usuario': usuario})

def update_usuario(request, id_usuario):
    nome = request.POST.get('first_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    last_name = request.POST.get('last_name')
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario.ativo = False
    usuario.save()
    usuario = Usuario.objects.create(first_name = nome, username = username, password = password, email = email, last_name = last_name)
    return render(request, 'index.html')

def inativar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    usuario.ativo = False
    usuario.save()
    return render(request, 'index.html', {'Usuario': usuario})

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

def submit(request):
    nome = request.POST.get('first_name')
    sobrenome = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    usuario = Usuario.objects.create(first_name=nome, last_name=sobrenome, username=username, email=email, password=senha)
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'sucess.html')


def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cadastro.html', context)

