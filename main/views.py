from django import forms
from django.shortcuts import render, redirect
from main.models import *
from .forms import Registrarse, Login
from django.contrib import messages
# Create your views here.

def register_page(request):
    if request.method=='POST':
        
        formulario = Registrarse(request.POST)
        if formulario.is_valid():
            data_form= formulario.cleaned_data
            name=data_form.get('name')
            lastName=data_form['lastName']
            correo=data_form['correo']
            password=data_form['password']
            confirmar=data_form['rePassword']
            barrio=data_form['barrio']

            if password==confirmar:
                client = Clients(
                    name=name,
                    lastName=lastName,
                    mail=correo,
                    password=password,
                    neighborhoodId_id=barrio,
                )
                client.save()
                messages.success(request, f"Usuario registrado correctamente")
                return redirect('login')
                
    else:
        formulario=Registrarse()

    return render(request, 'users/register.html',{
        'title':'Registrarse',
        'form':formulario
    })

def index(request):
    return render(request, 'index/index.html',{
        'Titulo':'Inicio'
    })

def login_page(request):
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
            if user[0].password==contraseña:
                messages.success(request, f"Bienvenido, {user[0].name}")
                return redirect('index')
    else:
        formulario=Login()


    return render(request, 'users/login.html', {
        'titulo':'Inicio de sesión',
        'form':formulario,
    })

    
