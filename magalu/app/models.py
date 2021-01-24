from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='app')
    favorito = models.BooleanField(default=False)
    reviewScore = models.FloatField(null=True)

    def __str__(self):
        return str(self.title)
