from django.shortcuts import render, redirect
from app.forms import UserModelForm
from django.http import HttpResponse
from .models import Cliente, Produtos
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
    cliente = Cliente.objects.filter(ativo = True)
    return render(request, 'perfil.html', {'Cliente': cliente})

@login_required(login_url='/login/')
def perfil_id(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    return render(request, 'detail.html', {'Cliente': cliente})

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
    fav = 0
    for p in produtos:
        fav += 1
    if fav != 0:
        return render(request, 'list_favoritos.html', {'Produtos': produtos})
    else:
        return render(request, 'not_fav.html')

@login_required(login_url='/login/')
def desfavoritar(request, id_produto):
    produtos = Produtos.objects.get(id_produto = id_produto)
    produtos.favorito = False
    produtos.save()
    produtos = Produtos.objects.filter(favorito=True)
    return redirect('/favoritos/')

def alterar(request,id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    return render(request, 'alterar.html', {'Cliente': cliente})

def update_cliente(request, id_cliente):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    cliente.delete()
    cliente = Cliente.objects.create(name = nome, email = email)
    return render(request, 'detail.html', {'Cliente': cliente})

def deletar(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    cliente.delete()
    cliente = Cliente.objects.all()
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
    cliente = Cliente.objects.filter(ativo = True)
    igual = 0
    for c in cliente:
        if email == c.email:
            igual = 1
            
    if igual != 1:
        cliente = Cliente.objects.create(name=nome, email=email)
        return redirect('/perfil/')
    else:
        return render(request, 'fail.html')

def pesquisar(request):
    title = request.POST.get('title')    
    produto_false = Produtos.objects.filter(favorito=False)
    produto_true = Produtos.objects.filter(favorito=True)
    for p in produto_false:
        if title == p.title:
            produtos = Produtos.objects.get(title = title)
            return render(request, 'detail_produtos.html', {'Produtos': produtos})
    for p in produto_true:
        if title == p.title:
            produtos = Produtos.objects.get(title = title)
            return render(request, 'detail_produtos_favoritados.html', {'Produtos': produtos})

    return render(request, 'pesquisa_erro.html')

