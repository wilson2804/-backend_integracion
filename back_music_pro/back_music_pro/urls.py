"""back_music_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from django.conf.urls import url
from api_music.ViewSets.vw_UserProfile import UserProfileViewSet
from api_music.ViewSets.login import Login, Logout
from api_music.ViewSets.vw_marca import MarcaViewSet
from api_music.ViewSets.vw_modelo import ModeloViewSet
from api_music.ViewSets.vw_categoria import CategoriaViewSet
from api_music.ViewSets.vw_producto import ProductoViewSet


app_name= 'back_music_pro'

rt = routers.SimpleRouter(trailing_slash=True)
rt.register("usuarios",UserProfileViewSet , basename="usuarios")
rt.register("marcas",MarcaViewSet , basename="marcas")
rt.register("modelos",ModeloViewSet , basename="modelos")
rt.register("categorias",CategoriaViewSet , basename="categorias")
rt.register("productos",ProductoViewSet , basename="productos")



urlpatterns = [
    url(r"", include(rt.urls)),
    path('admin/', admin.site.urls),
    path(r"login", Login.as_view(), name="login"),
    path(r"logout", Logout.as_view(), name="logout")

    
]