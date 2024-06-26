from django.db import models
# Create your models here.
class carrera(models.Model):
    nombre = models.CharField(max_length=128, null= False)
    
class profesor(models.Model):
    nombre = models.CharField(max_length=128, null= False)
    apellido = models.CharField(max_length=128, null= False)
    mostrar = models.TextField(max_length=256, null= False)

class materia(models.Model):
    nombre = models.CharField(max_length=128, null=False)
    cant_alumnos = models.IntegerField(default=5, null=False)
    carrera = models.ForeignKey(carrera, on_delete=models.CASCADE)
    profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)
    
class aula(models.Model):
    descripcion = models.TextField(max_length=128, null=False)
    ubicacion = models.CharField(max_length=128,null=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)
    
class reserva_aula(models.Model):
    aula = models.ForeignKey(aula, on_delete=models.CASCADE)
    fh_desde = models.TimeField()
    fh_hasta = models.TimeField()
    observaciones = models.TextField(max_length=256)
class horario_materia(models.Model):
    materia = models.ForeignKey(materia, on_delete=models.CASCADE)
    reserva = models.ForeignKey(reserva_aula, on_delete= models.CASCADE)
    fh_desde = models.TimeField()
    fh_hasta = models.TimeField()