from pepe import views
from django.urls import path

urlpatterns= [
    path("main/", views.main, name = "main" ),
    path("login/", views.iniciar_sesion, name= "iniciar_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion")
]