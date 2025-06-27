from django.urls import path
from pepe import views


urlpatterns = [
    path("animales/",views.animales ,name="animales"),
    path("registrar/",views.registrar,name="registrar"),
    path("login/", views.iniciar, name="iniciar"),
]
