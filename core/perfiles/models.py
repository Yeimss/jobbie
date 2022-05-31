from django.db import models
from jobbie.settings import MEDIA_URL, STATIC_URL
from core.main.models import *
# Create your models here.

class Evidencias(models.Model):
    descripcion=models.TextField(verbose_name="Descripcion", blank=False, null=False, default=None)
    evidenciaPhoto=models.ImageField(default=None, upload_to='evidencias/%m/%d/', blank=False, null=False)
    trabajador=models.ForeignKey(Users, verbose_name="Trabajador", on_delete=models.PROTECT, blank=True, default=None)
    def get_image(self):
        if self.evidenciaPhoto:
            return '{}{}'.format(MEDIA_URL,self.evidenciaPhoto)
        
    class Meta:
        verbose_name='Evidencia trabajador'
        verbose_name_plural='Evidencias trabajadores'
        db_table="Evidencias"

    def __str__(self):
        return str(self.trabajador)

class Coments(models.Model):
    cliente=models.ForeignKey(Users,verbose_name="Cliente", related_name="%(class)s_Cliente", on_delete=models.PROTECT, blank=True, null=True, default=None )
    trabajador=models.ForeignKey(Users,verbose_name="Trabajador", related_name="%(class)s_Trabajador", on_delete=models.PROTECT, blank=True, null=True, default=None )
    calificacion=models.IntegerField(verbose_name="Calificación", blank=False, null=False)
    comentario=models.TextField(verbose_name="Comentario", blank=False, null=False)
    imagen=models.ImageField(default="", upload_to='comentarios/%m/%d/', blank=True, null=True)
    class Meta:
        verbose_name='Comentario'
        verbose_name_plural='Comentarios'
        db_table="comentarios"


    def __str__(self):
        return str(self.comentario)
    
class Skills(models.Model):
    especialidad=models.CharField(max_length=50, verbose_name="Especialidad", null=False)
    icono=models.CharField(max_length=100, verbose_name="Icono fontAwesome", null=False)
    class Meta:
        verbose_name='Especialidad'
        verbose_name_plural='Especialidades'
        db_table="especialidades"
        

    def __str__(self):
        return self.especialidad


class WorkedSkills(models.Model):
    especialidad=models.ForeignKey(Skills,verbose_name="Especialidad", on_delete=models.PROTECT, blank=True, null=True, default=None)
    trabajador=models.ForeignKey(Users,verbose_name="Trabajador", on_delete=models.PROTECT, blank=True, null=True, default=None )
    class Meta:
        verbose_name='Especialidad trabajador'
        verbose_name_plural='Especialidades trabajadores'
        db_table="especialidades_trabajadores"


    def __str__(self):
        return str(self.trabajador)
    