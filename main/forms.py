from django import forms
from django.core import validators

from main.models import *

class Registrarse(forms.Form):

    
    #ciudades_list=Cities.objects.order_by('id')

    #---------------------------------------------nombre
    name=forms.CharField(
        label='Nombre',
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
        label='Apellido',
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
        label="Correo",
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
    departamentos=Departaments.objects.all().order_by('departament')
    departamentos_list=[(None,'Departamento')]
    for departamento in departamentos:
        depa=(departamento.id,departamento.departament)
        departamentos_list.append(depa)
    departamento=forms.TypedChoiceField(
        label = "Departamento",
        widget=forms.Select(
            attrs={
                'class':'form-input-select',
            },
        ),
        choices = departamentos_list
    )

    #---------------------------------------------Ciudades
    #depaId=departamento(0)
    ciudades=Cities.objects.order_by('city')#.filter(departametId__exacts=depaId).
    ciudades_list=[(None,'Ciudades')]
    for ciudad in ciudades:
        ciu=(ciudad.id,ciudad.city)
        ciudades_list.append(ciu)
    ciudad=forms.TypedChoiceField(
        label = "Ciudad",
        widget=forms.Select(
            attrs={
                'class':'form-input-select',
            },
        ),
        choices = ciudades_list,
    )

    #---------------------------------------------Barrios
    barrios=Neighborhoods.objects.order_by('neighborhood')#.filter(departametId__exacts=depaId).
    barrios_list=[(None,'Barrios')]
    for barrio in barrios:
        bar=(barrio.id, barrio.neighborhood)
        barrios_list.append(bar)
    barrio=forms.TypedChoiceField(
        label = "Barrio",
        widget=forms.Select(
            attrs={
                'class':'form-input-select',
            },
        ),
        choices = barrios_list,
    )

    #---------------------------------------------contraseña
    password=forms.CharField(
        label="Contraseña",
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
        label="Confirmar Contraseña",
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
    

class Login(forms.Form):
    correo=forms.CharField(
        label="Correo",
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
        label="Contraseña",
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