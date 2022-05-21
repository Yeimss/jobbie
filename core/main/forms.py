from urllib import request
from django import forms
from django.core import validators
from core.main.models import *
from django.forms import ModelForm

generos=Genders.objects.all()
g=[(0, 'seleccione un genero')]
for genero in generos:
    a=(genero.id,genero.gender)
    g.append(a)

skills=Skills.objects.all()
especialidad=[]
for skill in skills:
    a=(skill.id,skill.especialidad)
    especialidad.append(a)


class SkillsWorked(ModelForm):
    class Meta:
        model=WorkedSkills
        fields=('especialidad',)
        
        widgets = {
            'especialidad':forms.CheckboxSelectMultiple()
        } 
    """ especialidad=forms.MultipleChoiceField(
        label="Especialidades",
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class':''
            }
        ),
        choices=especialidad,
    )
 """
class postRegistro(ModelForm):
    class Meta:
        model=Users
        fields=('first_name', 'last_name', 'email','gender', 'photo', 'bornDate', 'mobile', 'descripcion_personal')
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-input',
                'placeholder':'Nombre'           
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-input',
                'placeholder':'Apellido'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-input',
                'placeholder':'Email'
            }),
            'bornDate': forms.DateInput(attrs={
                'class': 'form-input',
                'type':'date'
                }),
            'mobile':forms.NumberInput(attrs={
                'class':'form-input',
                'placeholder':'Numero de celular'
            }),
            'descripcion_personal':forms.Textarea(attrs={
                'placeholder':'Descripcion personal',
                'class':'text-center form-input'
            }),
            'photo':forms.FileInput(attrs={
                'class':'form-input-img'
            })
        }
        input_formats={'bornDate':["%Y-%m-%d"]}

class Login(forms.Form):
    correo=forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class':'form-input',
                'placeholder':'example@example.com'
            }
        ),
        required=True,
        validators=[
            validators.MaxLengthValidator(200, 'El correo es demasiado largo'),
            validators.EmailValidator('Por favor ingrese un correo valido')
        ]
    )

    password=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class':'form-input',
            }
        ),
        required=True
    )
