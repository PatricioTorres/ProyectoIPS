from django.db import models

# Create your models here.
class Empresa(models.Model):
    ESTADO = (('A', 'Activo'),('I', 'Inactivo'))
    nombre = models.CharField(max_length=50, blank=False)
    razon_social = models.CharField(max_length=50, blank=False)
    nombre_comercial = models.CharField(max_length=50, blank=False)
    ruc = models.IntegerField()
    estado = models.CharField(max_length=1,choices=ESTADO)
    fecha_inicio = models.DateField()

class Usuario(models.Model):
    ESTADO = (('A', 'Activo'),('I', 'Inactivo'))
    PERMISOS = (('0', 'Visitante'), ('1', 'Usuario'), ('2','Admin'))
    nombre = models.CharField(max_length=50, blank=False)
    clave = models.CharField(max_length=50, blank=False)
    estado = models.CharField(max_length=1,choices=ESTADO)
    permisos = models.CharField(max_length=1, choices=ESTADO,default='0')
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)

