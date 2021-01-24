"""magalu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from . import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('pesquisar/', views.pesquisar),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('cadastro/submit/', views.submit, name = 'submit'),
    path('cadastro_cliente/', views.cadastro_cliente),
    path('cadastro_cliente/submit/', views.cliente_submit),
    path('login/', views.login_user),
    path('login/submit/', views.submit_login),
    path('logout/', views.logout_user),
    path('perfil/', views.perfil),
    path('perfil/<id_cliente>/', views.perfil_id),
    path('alterar/<int:id_cliente>/', views.alterar),
    path('alterar/<int:id_cliente>/submit/', views.update_cliente),
    path('deletar/<id_cliente>/', views.deletar),
    path('produto/', views.list_produtos),
    path('produto/<id_produto>/', views.detail_produto),
    path('produtos_favoritado/<id_produto>/', views.detail_produto_favoritado),
    path('favoritar/<id_produto>/', views.favoritar),
    path('desfavoritar/<id_produto>/', views.desfavoritar),
    path('favoritos/', views.favoritos)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)