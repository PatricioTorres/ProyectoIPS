from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class Empresa(models.Model):
    ESTADO = (('A', 'Activo'),('I', 'Inactivo'))
    nombre = models.CharField(max_length=50, blank=False,unique=True)
    razon_social = models.CharField(max_length=100, blank=False)
    nombre_comercial = models.CharField(max_length=50, blank=False)
    ruc = models.IntegerField()
    estado = models.CharField(max_length=1,choices=ESTADO)
    fecha_inicio = models.CharField(max_length=10)

class PersonalizadoBaseUserManager(BaseUserManager):
    def create_user(self,usuario,password):
        user = self.model(usuario=usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,usuario,password):
        user = self.create_user(usuario,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser,PermissionsMixin,models.Model):
    PERMISOS = (('0', 'Visitante'), ('1', 'Usuario'), ('2','Admin'))
    nombre = models.CharField(max_length=50, blank=False)
    usuario = models.CharField(max_length=50, blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    permisos = models.CharField(max_length=1, choices=PERMISOS,default='0')
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'usuario'
    objects = PersonalizadoBaseUserManager()

class Trafico_linea(models.Model):
    TRIMESTRE = (('I','Uno'),('II','Dos'),('III','Tercer'),('IV','Cuarto'))
    temporada  = models.IntegerField()
    trimestre = models.CharField(max_length=3, choices=TRIMESTRE)
    equipo = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=50)
    lineas = models.BigIntegerField()
    t_cursado = models.BigIntegerField()
    usuario = models.ForeignKey(Usuario,null=False,blank=False, on_delete=models.CASCADE)



