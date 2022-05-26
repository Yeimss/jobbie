from django.db import models
from jobbie.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Genders(models.Model):
    gender=models.CharField(max_length=50)
    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Generos'
    
    def __str__(self):
        return self.gender

class Departaments(models.Model):
    departament=models.CharField(max_length=80, verbose_name="Departamento")
    cod_dane=models.IntegerField(primary_key=True,verbose_name="Codigo_dane", null=False, default=None)
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        db_table="Departamentos"
    
    def __str__(self):
        return self.departament


class Cities(models.Model):
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    departamet=models.ForeignKey(Departaments, verbose_name="Departamento", on_delete=models.PROTECT)
    cod_dane=models.FloatField(primary_key=True,verbose_name="Codigo_dane", null=False, default=None)
    class Meta:
        verbose_name='Ciudad'
        verbose_name_plural='Ciudades'
        db_table="Ciudades"
    
    def __str__(self):
        return self.city
    

class Neighborhoods(models.Model):
    neighborhood=models.CharField(max_length=80, verbose_name="Barrio")
    city=models.ForeignKey(Cities, verbose_name="Ciudad", on_delete=models.PROTECT)
    class Meta:
        verbose_name='Barrio'
        verbose_name_plural='Barrios'
        db_table="Barrios"
    
    def __str__(self):
        return self.neighborhood


class Types(models.Model):
    tipoUsuario=models.CharField(max_length=20)
    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'

    def __str__(self):
        return self.tipoUsuario



class Users(AbstractUser):
    email = models.EmailField('email address', unique=True)
    bornDate=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None, verbose_name="Fecha de nacimiento")	
    password=models.CharField(max_length=200, verbose_name="Password", blank=True, null=True, default=None)	
    gender=models.ForeignKey(Genders, verbose_name="Genero", on_delete=models.PROTECT, blank=True, null=True, default=None)
    photo=models.ImageField(default="user/user.png", upload_to='user/%m/%d/', blank=True, null=True)	
    mobile=models.IntegerField(verbose_name="Celular", blank=True, null=True, default=None)
    ciudad=models.ForeignKey(Cities, verbose_name="Ciudad", on_delete=models.PROTECT, blank=True, null=True, default=None)
    descripcion_personal=models.TextField(verbose_name="Descripcion", blank=True, null=True, default=None)
    type=models.ForeignKey(Types,verbose_name="Tipo", on_delete=models.PROTECT, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_image(self):
        if self.photo:
            return '{}{}'.format(MEDIA_URL,self.photo)
        return '{}{}'.format(MEDIA_URL,'user/user.png')
        
    def __str__(self):
        return self.first_name

class Skills(models.Model):
    especialidad=models.CharField(max_length=50, verbose_name="Especialidad", null=False)
    icono=models.CharField(max_length=100, verbose_name="Icono fontAwesome", null=False)
    class Meta:
        verbose_name='Especialidad'
        verbose_name_plural='Especialidades'
    def __str__(self):
        return self.especialidad


class WorkedSkills(models.Model):
    especialidad=models.ForeignKey(Skills,verbose_name="Especialidad", on_delete=models.PROTECT, blank=True, null=True, default=None)
    trabajador=models.ForeignKey(Users,verbose_name="Trabajador", on_delete=models.PROTECT, blank=True, null=True, default=None )
    class Meta:
        verbose_name='Especialidad trabajador'
        verbose_name_plural='Especialidades trabajadores'

    def __str__(self):
        return str(self.trabajador)
    
class Calificaciones(models.Model):
    cliente=models.ForeignKey(Users,verbose_name="Cliente", related_name="%(class)s_Cliente", on_delete=models.PROTECT, blank=True, null=True, default=None )
    trabajador=models.ForeignKey(Users,verbose_name="Trabajador",related_name="%(class)s_Trabajador",  on_delete=models.PROTECT, blank=True, null=True, default=None )
    calificacion=models.IntegerField(verbose_name="Calificación", blank=False, null=False)

class Comentarios(models.Model):
    cliente=models.ForeignKey(Users,verbose_name="Cliente", related_name="%(class)s_Cliente", on_delete=models.PROTECT, blank=True, null=True, default=None )
    trabajador=models.ForeignKey(Users,verbose_name="Trabajador", related_name="%(class)s_Trabajador", on_delete=models.PROTECT, blank=True, null=True, default=None )
    comentario=models.TextField(verbose_name="Comentario", blank=False, null=False)
    imagen=models.ImageField(default=None, upload_to='comentarios/%m/%d/', blank=True, null=True)
    
    