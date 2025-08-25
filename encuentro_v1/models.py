from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    """
    Description: usado para la informacion individual de cada usuario
    """
    user_perfil = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    bam_usuario = models.ForeignKey('Bam', on_delete=models.CASCADE, blank=True)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE, blank=True)
    puntaje = models.IntegerField(blank=True)
    
    def __str__(self):
        return str(self.user_perfil)

class Bam(models.Model):
    """
    Description: Brigadas de accion misionera
    """
    nombre_bam = models.CharField(max_length=32, unique=True)
    lider = models.OneToOneField(Perfil, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nombre_bam

class Evento(models.Model):
    """
    Description: Modelo para almacenar eventos
    """
    nombre_evento = models.CharField(max_length=63, unique=True)
    descripcion_evento = models.TextField()

    def __str__(self):
    	return self.nombre_evento

