from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.
class Genders(models.Model):
    gender=models.CharField(max_length=50)

class Departaments(models.Model):
    departament=models.CharField(max_length=80, verbose_name="Departamento")

class Cities(models.Model):
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    departametId=models.OneToOneField(Departaments, verbose_name="DepartamentoId")

class Neighborhoods(models.Model):
    neighborhood=models.CharField(max_length=80, verbose_name="Barrio")
    cityId=models.OneToOneField(Cities, verbose_name="CiudadesId")

class Clients(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")    
    lastName=models.CharField(max_length=100, verbose_name="Apellido")	
    mail=models.CharField(max_length=200, verbose_name="Correo")
    bornDate=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de nacimiento")	
    password=models.CharField(max_length=200, verbose_name="Password")	
    gender=models.IntegerField()
    photo=models.ImageField(default="null", upload_to='clientes')	
    mobile=models.IntegerField(max_length=13, verbose_name="Celular")
    neighborhoodId=models.OneToOneField(Neighborhoods, verbose_name="Barrio")


class Workeds(models.Model):	
    name=models.CharField(max_length=100, verbose_name="Nombre")    
    lastName=models.CharField(max_length=100, verbose_name="Apellido")	
    mail=models.CharField(max_length=200, verbose_name="Correo")
    bornDate=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de nacimiento")		
    password=models.CharField(max_length=200, verbose_name="Password")	
    gender=models.IntegerField()
    photo=models.ImageField(default="null", upload_to='clientes')		
    mobile=models.IntegerField(max_length=13, verbose_name="Celular")
    neighborhoodId=models.OneToOneField(Neighborhoods, verbose_name="Barrio")
    descripcion_personal=models.TextField(verbose_name="Descripcion")
