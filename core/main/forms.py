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


class postRegistro(ModelForm):
    class Meta:
        model=Users
        fields=('gender', 'photo', 'bornDate', 'mobile', 'descripcion_personal')
        widgets = {
            'bornDate': forms.DateInput(attrs={
                'class': 'form-input',
                'type':'date'
                }),
            'mobile':forms.NumberInput(
            attrs={
                'class':'form-input',
                'placeholder':'Numero de celular'
            }),
            'descripcion_personal':forms.Textarea(
            attrs={
                'placeholder':'Descripcion personal',
                'class':'text-center'
            }
        ),
        }
        input_formats={'bornDate':["%Y-%m-%d"]}

    """
    photo = forms.ImageField(
        label='Foto de perfil',
        required=False, 
        error_messages = {'invalid':("solamente se aceptan imagenes")}, 
        widget=forms.FileInput(
            attrs={
                'class':'form-input-img',
            }
        ))
        
    bornDate = forms.DateField(
        label='Fecha de nacimiento', 
        label_suffix=" : ",
        required=True, 
        disabled=False, 
        widget=forms.DateInput(
            attrs={
                'class': 'form-input',
                'type':'date'
                }),
            error_messages={'required': "This field is required."})

    mobile=forms.CharField(
        label="",
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-input',
                'placeholder':'Numero de celular'
            }
        ),
        validators=[
            validators.MaxLengthValidator(10, 'El nuemro telefonico debe tener 10 caracteres'),
            validators.MinLengthValidator(10, 'El nuemro telefonico debe tener 10 caracteres'),
        ]
    )
    descripcion=forms.CharField(
        label="Descripcion personal",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Descripcion personal'
            }
        ),
        required=True
    )

    especialidad=forms.MultipleChoiceField(
        label="Especialidades",
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class':''
            }
        ),
        choices=especialidad,
    ) """

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
