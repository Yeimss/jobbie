from django.shortcuts import render, redirect
from core.main.models import *
from core.perfiles.models import *
from .forms import Login, postRegistro
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.


##-----------------pagina de registro
def register_page(request):
    categorias=Skills.objects.all()
    return render(request, 'users/register.html',{
        'title':'Registrarse',
        'especialidades':categorias
    })


###------------------login page
def login_page(request):
    categorias=Skills.objects.all()
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
                messages.warning(request, 'no te has identificado correctamente!!')
            
    else:
        formulario=Login()

    return render(request, 'users/login.html', {
        'titulo':'Inicio de sesión',
        'form':formulario,
        'especialidades':categorias
    })


##---------------metodo para registrar un cliente
def save_client(request):
    try:
        if request.method=='POST':
            name=request.POST['name']
            lastName=request.POST['lastName']
            correo=request.POST['correo']
            password=request.POST['password']
            confirmar=request.POST['rePassword']
            city=request.POST['municipio']
            #city=int(city.replace(".",""))
            tipo=int(request.POST['tipo'])

            if password==confirmar and city != 0:
                correo_existente=Users.objects.filter(email=correo).exists()
                if correo_existente:
                    messages.success(request, f"El correo ya existe, por favor inicie sesion")
                    return redirect('login')

                client = Users(
                    first_name=name,
                    last_name=lastName,
                    email=correo,
                    ciudad=Cities.objects.get(cod_dane=city),
                    type=Types.objects.get(id=tipo)
                )
                client.set_password(password)
                client.save()

                user=authenticate(request ,username=correo,password=password)
                login(request, user)

                if tipo==2:
                    messages.success(request, f"Por favor complete su perfil")
                    return redirect('perfilUpdate', pk=request.user.id)
                else:
                    return redirect('perfilUpdate',  pk=request.user.id)

            elif city == 0:
                messages.success(request, f"Por favor elija una ciudad")
            else:
                messages.success(request, f"las contraseñas debens ser iguales")
    except:
        return redirect('error')

##-------------------cerrar sesion

def logout_user(request):
    logout(request)
    return redirect('login')
