from django import forms
from django.core import validators
from core.perfiles.models import *
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

