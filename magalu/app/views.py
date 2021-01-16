from django.shortcuts import render
from app.forms import UserModelForm
from django.http import HttpResponse
from .models import Usuario

def index(request):
    return HttpResponse("OK")

def submit(request):
    nome = request.POST.get('first_name')
    sobrenome = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    usuario = Usuario.objects.create(first_name=nome, last_name=sobrenome, username=username, email=email, password=senha)
    return render(request, 'sucess.html')


def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cadastro.html', context)

