from django.db import models
from jobbie.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Genders(models.Model):
    gender=models.CharField(max_length=50)
    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Generos'
        db_table='Generos'

    
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
        db_table="TypeUser"


    def __str__(self):
        return self.tipoUsuario



class Users(AbstractUser):
    email = models.EmailField('email address', unique=True)
    bornDate=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None, verbose_name="Fecha de nacimiento")	
    password=models.CharField(max_length=200, verbose_name="Password", blank=True, null=True, default=None)	
    gender=models.ForeignKey(Genders, verbose_name="Genero", on_delete=models.PROTECT, blank=True, null=True, default=None)
    photo=models.ImageField(default="", upload_to='user/%m/%d/', blank=True, null=True)	
    mobile=models.IntegerField(verbose_name="Celular", blank=True, null=True, default=None)
    ciudad=models.ForeignKey(Cities, verbose_name="Ciudad", on_delete=models.PROTECT, blank=True, null=True, default=None)
    descripcion_personal=models.TextField(verbose_name="Descripcion", blank=True, null=True, default=None)
    type=models.ForeignKey(Types,verbose_name="Tipo", on_delete=models.PROTECT, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_image(self):
        if self.photo and self.photo!= "":
            return '{}{}'.format(MEDIA_URL,self.photo)
        else:
            if self.type.id=="1":
                return '{}{}'.format(MEDIA_URL,'user/client-user.png')
            return '{}{}'.format(MEDIA_URL,'user/user.png')
        
    def __str__(self):
        return self.first_name

