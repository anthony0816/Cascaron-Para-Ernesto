from django.db import models
from  django.contrib.auth.models import User


# Create your models here.
class libro (models.Model):
    titulo = models.TextField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    