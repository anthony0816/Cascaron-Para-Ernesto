from django.shortcuts import render
from django.http import HttpResponse
from  django.contrib.auth.models import User
from .models import libro
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




# Create your models here.



def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['nombre']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('main')  
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

def listar(request):
    libros = libro.objects.all()
    if libro is not None:
        return render(request,"all_elements.html", {"libros": libros} )
    return render(request,"all_elements.html")


def crear(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        
        libro.objects.create(
            titulo = titulo,
            descripcion = descripcion,
            precio = precio
        )
        return redirect("/listar")
    return render(request, "crear.html")

def editar(request,id):
    elemento = libro.objects.get(id=id)
    return render(request, "editar.html", {"libro": elemento})

def eliminar(request,id):
    elemento = libro.objects.get(id=id)
    elemento.delete()
    return redirect("/listar")