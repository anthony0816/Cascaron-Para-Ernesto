from .models import Animal
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def animales(request):
    animal = Animal.objects.all()
    return render(request,"animales.html", {"anm": animal} )


def registrar(request):
    if request.method == "POST":
        nombre= request.POST.get("nombre"),
        especie = request.POST.get("especie"),
        edad = request.POST.get("edad"),
        sexo = request.POST.get("sexo"),
        disp_adopcion = request.POST.get("En adopcion")

        anm= Animal.objects.create(
            nombre,
            especie,
            edad,
            sexo,
            disp_adopcion,
        )
        
        return redirect("registrar/")
    return render(request,"crear.html")


def iniciar(request):
    nombre =  request.POST["username"]
    contraseña = request.POST["password"]
    user = authenticate(request, username=nombre, password = contraseña)
    if user is not None:
        login(request, user)
        return redirect("animales/")
    else:
        return HttpResponse("Error")
    
def desloguear(request):
    logout(request)
    return render(request, "login/")
