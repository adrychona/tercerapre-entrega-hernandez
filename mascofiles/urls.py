"""
URL configuration for mascofiles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from AppMascota.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    # URLs para crear nuevos datos usando formularios django
    path("formmascota/", agregar_mascota, name='formumascota'),
    path("formuvacuna/", agregar_vacuna, name='formuvacuna'),
    path("formuconsulta/", agregar_consulta, name='formuconsulta'),
    # URLs para buscar datos
    path("consultaporespecie/", consultar_mascotas, name='consultaporespecie'),
    path("resultado/", resultadoconsultaporespecie, name='resultado'),

    ] 
