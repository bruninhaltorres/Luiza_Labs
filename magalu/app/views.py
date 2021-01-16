from django.shortcuts import render, redirect
from app.forms import UserModelForm
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

def index(request):
    return HttpResponse("OK")

def login_user(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['user_name'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'sucess.html')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')

@csrf_protect
@require_POST
def submit_login(request):
    if request.POST:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(user_name=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')

def submit_cadastro(request):
    return render(request, 'sucess.html', context)

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cadastro.html', context)

