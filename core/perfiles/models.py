from django.db import models
from jobbie.settings import MEDIA_URL, STATIC_URL
from core.main.models import Users
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

    def __str__(self):
        return str(self.trabajador)