from django.db import models

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
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
    
    def __str__(self):
        return self.departament

class Cities(models.Model):
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    departametId=models.ForeignKey(Departaments, verbose_name="Departamento", on_delete=models.PROTECT)
    class Meta:
        verbose_name='Ciudad'
        verbose_name_plural='Ciudades'
    
    def __str__(self):
        return self.city

class Neighborhoods(models.Model):
    neighborhood=models.CharField(max_length=80, verbose_name="Barrio")
    cityId=models.ForeignKey(Cities, verbose_name="Ciudad", on_delete=models.PROTECT)
    class Meta:
        verbose_name='Barrio'
        verbose_name_plural='Barrios'
    
    def __str__(self):
        return self.neighborhood

class Clients(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")    
    lastName=models.CharField(max_length=100, verbose_name="Apellido")	
    mail=models.CharField(max_length=200, verbose_name="Correo")
    bornDate=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None, verbose_name="Fecha de nacimiento")	
    password=models.CharField(max_length=200, verbose_name="Password", blank=True, null=True, default=None)	
    gender=models.OneToOneField(Genders, on_delete=models.PROTECT, blank=True, null=True, default=None)
    photo=models.ImageField(default="null", upload_to='clientes', blank=True, null=True)	
    mobile=models.IntegerField(verbose_name="Celular", blank=True, null=True, default=None)
    neighborhoodId=models.ForeignKey(Neighborhoods, verbose_name="Barrio", on_delete=models.PROTECT, blank=True, null=True, default=None)
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
    
    def __str__(self):
        return self.name


class Workeds(models.Model):	
    name=models.CharField(max_length=100, verbose_name="Nombre")    
    lastName=models.CharField(max_length=100, verbose_name="Apellido")	
    mail=models.CharField(max_length=200, verbose_name="Correo")
    bornDate=models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de nacimiento")		
    password=models.CharField(max_length=200, verbose_name="Password")	
    gender=models.OneToOneField(Genders, on_delete=models.PROTECT, blank=True, null=True, default=None)
    photo=models.ImageField(default="null", upload_to='clientes', blank=True, null=True)		
    mobile=models.IntegerField(verbose_name="Celular", blank=True, null=True, default=None)
    neighborhoodId=models.ForeignKey(Neighborhoods, verbose_name="Barrio", on_delete=models.PROTECT, blank=True, null=True, default=None)
    descripcion_personal=models.TextField(verbose_name="Descripcion", blank=True, null=True, default=None)
    class Meta:
        verbose_name='Trabajador'
        verbose_name_plural='Trabajadores'
    
    def __str__(self):
        return self.name
        