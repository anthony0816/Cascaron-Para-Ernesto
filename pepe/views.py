from django.shortcuts import render
from django.http import HttpResponse
from  django.contrib.auth.models import User
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
    return redirect("/pepe/login")

@login_required 
def main(request):
    return render(request,"main.html",)

