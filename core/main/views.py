import email
from django.shortcuts import render, redirect, HttpResponse
from core.main.models import *
from .forms import Login
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def register_page(request):

    return render(request, 'users/register.html',{
        'title':'Registrarse',
    })

def index(request):
    
    return render(request, 'index/index.html',{
        'Titulo':'Inicio',
    })


def login_page(request):
    if request.method=='POST':
        formulario=Login(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            correo=data['correo']
            contraseña=data['password']
            user=authenticate(request ,username=correo,password=contraseña)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request,f'no te has identificado correctamente!!')
            
    else:
        formulario=Login()

    return render(request, 'users/login.html', {
        'titulo':'Inicio de sesión',
        'form':formulario,
    })

def save_client(request):
    if request.method=='POST':
        name=request.POST['name']
        lastName=request.POST['lastName']
        correo=request.POST['correo']
        password=request.POST['password']
        confirmar=request.POST['rePassword']
        city=request.POST['municipio']
        city=int(city.replace(".",""))
        tipo=int(request.POST['tipo'])

        if password==confirmar:
            client = Users(
                first_name=name,
                last_name=lastName,
                email=correo,
                ciudad=Cities.objects.get(cod_dane=city),
                type=Types.objects.get(id=tipo)
            )
            client.set_password(password)
            client.save()
            messages.success(request, f"Cliente registrado correctamente")
            return redirect('login')

        else:
            messages.success(request, f"las contraseñas debens ser iguales")
            return redirect('registrarse')
    

def logout_user(request):
    logout(request)
    return redirect('login')

        
        

    
