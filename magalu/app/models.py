from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    password = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.first_name
