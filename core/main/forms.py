from django import forms
from django.core import validators
from core.main.models import *

class Registrarse(forms.Form):

    """     
    #ciudades_list=Cities.objects.order_by('id')

    #---------------------------------------------nombre
    name=forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nombre',
                'class':'form-input'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100, 'tu nombre es muy largo'),
            validators.RegexValidator('^[A-Za-z0-9ñáéóíú ]*$', 'El nombre no puede tener caracterese especiales', 'invalid_name')
        ]
    )
    #---------------------------------------------apellido
    lastName=forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellido',
                'class':'form-input'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100, 'tu apellido es muy largo'),
            validators.RegexValidator('^[A-Za-z0-9ñáéóíú ]*$', 'El apellido no puede tener caracterese especiales', 'invalid_lastName')
        ]
    )
    #----------------------------------------------correo
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

    #---------------------------------------------departamentos
    

    #---------------------------------------------Ciudades
    #depaId=departamento(0)
    
    #---------------------------------------------Barrios
    

    #---------------------------------------------contraseña
    password=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class':'form-input',
            }
        ),
        required=True,
        validators=[
            validators.MinLengthValidator(8, 'Por favor ingrese una contraseña de más de 8 caracteres'),
        ]
    )

    rePassword=forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar contraseña',
                'class':'form-input',
            }
        ),
        validators=[
            validators.MinLengthValidator(8, 'Por favor ingrese una contraseña de más de 8 caracteres'),

        ]
    )
    
    """
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