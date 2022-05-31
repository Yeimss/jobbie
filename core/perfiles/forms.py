from django import forms
from django.core import validators
from core.perfiles.models import *
from core.main.models import *

from django.forms import ModelForm

class evidencias(ModelForm):
    class Meta:
        model=Evidencias
        fields=('descripcion', 'evidenciaPhoto')
        widgets = {
            'descripcion':forms.Textarea(attrs={
                'placeholder':'Descripcion',
                'class':'text-center form-input'
            }),
            'evidenciaPhoto':forms.FileInput(attrs={
                'class':'form-input-img'
            })
        }


class ComentForm(ModelForm):
    class Meta:
        model=Coments
        fields=('comentario','imagen','calificacion')
        widgets = {
            'comentario':forms.Textarea(attrs={
                'placeholder':'Añada su comentario',
                'class':'text-start form-input'
            }),
            'imagen':forms.FileInput(attrs={
                'class':'form-input-img form-control',
                'style':'background:transparent; color:white;'
            }),
            'calificacion':forms.RadioSelect(attrs={
                'class':'',
                'style':'color:white;'
            },
            choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
        }
    