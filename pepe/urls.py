from pepe import views
from django.urls import path

urlpatterns= [
    path("main/", views.main, name = "main" ),
    path("", views.iniciar_sesion, name= "iniciar_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
    path('listar/', views.listar, name='listar'),
    path("crear/", views.crear, name = "crear"),
    path("editar/<int:id>/" , views.editar, name = "editar"),
    path("eliminar/<int:id>/", views.eliminar, name ="eliminar")
]