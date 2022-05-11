from django.shortcuts import render, redirect, HttpResponse
from main.models import *
from .forms import Registrarse, Login
from django.contrib import messages
# Create your views here.

def register_page(request):

    return render(request, 'users/register.html',{
        'title':'Registrarse',
    })

def index(request, id=None, name=None, lastName=None):
    
    return render(request, 'index/index.html',{
        'Titulo':'Inicio',
    })


def login_page(request):
    mensaje=False
    if request.method=='POST':
        formulario=Login(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            correo=data['correo']
            contraseña=data['password']
            usuarios=Clients.objects.filter(mail__iexact=correo)
            user=[]
            for usuario in usuarios:
                user.append(usuario)
            if len(user)!= 0:
                if user[0].password==contraseña:
                    messages.success(request, f"Bienvenido, {user[0].name}")
                    return redirect('index')
                else:
                    mensaje="la contraseña es incorrecta"
            else:
                mensaje="el usuario no existe, por favor registrese"
            
    else:
        formulario=Login()

    return render(request, 'users/login.html', {
        'titulo':'Inicio de sesión',
        'form':formulario,
        'mensaje':mensaje
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
            if tipo==1:
                client = Clients(
                    name=name,
                    lastName=lastName,
                    mail=correo,
                    password=password,
                    ciudad=Cities.objects.get(cod_dane=city),

                )
                client.save()
                messages.success(request, f"Cliente registrado correctamente")
                return redirect('login')

            elif tipo==2:
                worked = Workeds(
                    name=name,
                    lastName=lastName,
                    mail=correo,
                    password=password,
                    ciudad=Cities.objects.get(cod_dane=city),
                )
                worked.save()
                messages.success(request, f"Treabajador registrado correctamente")
                return redirect('login')
        else:
            messages.success(request, f"las contraseñas debens ser iguales")
            return redirect('registrarse')
    

        
        
        

    
