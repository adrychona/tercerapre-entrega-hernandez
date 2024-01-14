from django.shortcuts import render, HttpResponse
from AppMascota.models import * #from .models import Caninos 
from AppMascota.forms import *
# Create your views here.


def inicio(request):
    return render(request,'AppMascota/inicio.html')

def agregar_mascota(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Mascotaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Mascota(nombre=info["nombre"], especie=info["especie"], raza=info["raza"], edad=info["edad"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Mascotaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formmascota.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista


def agregar_vacuna(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Vacunaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Vacuna(mascota=info["mascota"], vacuna=info["vacuna"], fecha=info["fecha"])
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Vacunaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formvacuna.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista


def agregar_consulta(request):
    #Depende de darle click al boton enviar
    if request.method == "POST":
        
        nuevo_formulario = Consultaformulario(request.POST)        
        
        if nuevo_formulario.is_valid(): #Crear un objeto usando el modelo.
            
            info = nuevo_formulario.cleaned_data #Para tenerlos en modo diccionario.
            
            mascota_nueva = Consulta(paciente=info["paciente"], fecha=info["fecha"], motivo=info["motivo"], vet=info["vet"], establecimiento=info["establecimiento"] )
            
            mascota_nueva.save()
            return render(request, "AppMascota/confirmacion.html") #muestra la plantilla de inicio
        
    else: #si la persona no ha hecho click en el boton enviar
            
        nuevo_formulario = Consultaformulario() #mostraremos un formulario vacio

    return render(request,"AppMascota/formconsulta.html", {"mi_form":nuevo_formulario}) #Conexion HTML con la vista





def consultar_mascotas(request):
    
    return render(request,"AppMascota/consultaporespecie.html")


def resultadoconsultaporespecie(request):
    #return HttpResponse(f"Estoy buscando los perros de la especie {request.GET['especie']}")
    if request.method == "GET":
        
        especies = request.GET['especie']
        mascotas = Mascota.objects.filter(especie__icontains=especies)
        
        return render(request,"AppMascota/resultado.html", { "mascotas": mascotas, "especies": especies})
   
    else: #si aun no le hacer click al boton BUSCAR
        respuesta = "No enviaste datos"

    #return HttpResponse(f'Estas buscando las mascotas por la especie {request.GET["especie"]} ')
    return HttpResponse(respuesta)



