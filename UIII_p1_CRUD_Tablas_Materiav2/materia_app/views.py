from django.shortcuts import render,redirect
from .models import Materia

# Create your views here.

def inicio_vistas (request):
    lasmaterias = Materia.objects.all()

    return render(request, "gestionarMaterias.html",{"lasmaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    
    guardarmateria=Materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)

    return redirect("/")