from django.db import models






class Animal(models.Model):
    ANIMAL_CHOICES = [
    ("perro","Perro"),
    ("gato","Gato"),
    ("hamster","Hámster"),
    ("ave","Ave"),
]

    SEX_CHOICES = [
    ("M","Macho"),
    ("H", "Hembra"),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=30, choices=ANIMAL_CHOICES)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=2 ,choices=SEX_CHOICES)
    disp_adopcion = models.BooleanField(default= True)


class AtencionMedica(models.Model):
    
    TIPO_CHOICES = [
    ("consulta", "Consulta"),
    ("vacunacion","Vacunacion"),
]
    
    VETERINARIOS_CHOICE = [
    ("dr_andres_herrera","Dr. Andrés Herrera"),
    ("dra_clara_nuñez","Dra. Clara Núñez"),
    ("dra_sofia_mena","Dra. Sofía Mena"),
    ("dr_luis_torres","Dr. Luis Torres"),
]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    animal= models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinario = models.CharField(max_length=30, choices=VETERINARIOS_CHOICE)
    fecha = models.DateTimeField()
    
class Consulta(AtencionMedica):
    atención_medica = models.OneToOneField(AtencionMedica, on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)


class Vacunacion(AtencionMedica):
    VACUNAS_CHOICES = [
    ("anti-rabia","Anti-Rabia"),
    ("anti-leucemia_felina","Anti-leucemia_felina"),
    ("anti-tifoidea","Anti-tifoidea"),
    ("anti-viruela","Anti-viruela"),
    ]
    atención_medica = models.OneToOneField(AtencionMedica, on_delete=models.CASCADE)
    vacuna = models.CharField(max_length=100, choices=VACUNAS_CHOICES)