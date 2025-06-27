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

<<<<<<< HEAD


def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['nombre']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('listar')  
        else:
            error = 'Credenciales inválidas'
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect("/")

@login_required 
def main(request):
    return render(request,"main.html",)

@login_required 
def listar(request):
    libros = libro.objects.all()
    if libro is not None:
        return render(request,"all_elements.html", {"libros": libros} )
    return render(request,"all_elements.html")

@login_required 
def crear(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        
        libro.objects.create(
            titulo = titulo,
            descripcion = descripcion,
            precio = precio
=======
        anm= Animal.objects.create(
            nombre,
            especie,
            edad,
            sexo,
            disp_adopcion,
>>>>>>> 348ed930c90c654e826a042a0beb0438ff344381
        )
        
        return redirect("registrar/")
    return render(request,"crear.html")

<<<<<<< HEAD
@login_required 
def editar(request,id):
    if request.method == 'POST':
        
        elemento = libro.objects.get(id=id)
        elemento.titulo = request.POST.get("titulo")
        elemento.descripcion = request.POST.get("descripcion")
        elemento.precio = request.POST.get("precio")
        elemento.save()
        
        return redirect("/listar")
    elemento = libro.objects.get(id=id)
    return render(request, "editar.html", {"libro": elemento})

@login_required 
def eliminar(request,id):
    elemento = libro.objects.get(id=id)
    elemento.delete()
    return redirect("/listar")
=======

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
>>>>>>> 348ed930c90c654e826a042a0beb0438ff344381
