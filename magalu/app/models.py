from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default=None)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='app')
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_produto)
