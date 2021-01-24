from django.contrib import admin
from .models import Cliente, Produtos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produtos)