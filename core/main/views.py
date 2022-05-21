from django.shortcuts import render, redirect
from core.main.models import *
from .forms import Login, postRegistro
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.


##-----------------pagina de registro
def register_page(request):

    return render(request, 'users/register.html',{
        'title':'Registrarse',
    })




##-------------------pagina para completar la info del trabajador
def postRegister(request):
    if request.method=='POST':
        Worked = Users.objects.get(id=request.user.id)
        formulario=postRegistro(request.POST, request.FILES, instance=Worked)
        if formulario.is_valid():
            formulario.save()
            
            messages.warning(request, 'datos actualizados')
            return redirect('index')
    else:
        formulario=postRegistro()

    return render(request, 'users/postRegister.html', {
        'titulo':'Registro',
        'form':formulario,
    })


###------------------login page
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
                messages.warning(request, 'no te has identificado correctamente!!')
            
    else:
        formulario=Login()

    return render(request, 'users/login.html', {
        'titulo':'Inicio de sesión',
        'form':formulario,
    })


##---------------metodo para registrar un cliente
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

            user=authenticate(request ,username=correo,password=password)
            login(request, user)

            if tipo==2:
                return redirect('postRegister')
            else:
                return redirect('index')
                
    
        else:
            messages.success(request, f"las contraseñas debens ser iguales")
    

##-------------------cerrar sesion

def logout_user(request):
    logout(request)
    return redirect('login')



        
        

    

""" especialidad=data['especialidad']

            for esp in especialidad:
                skill=WorkedSkills(
                    especialidad=Skills.objects.get(id=int(esp)),
                )
                skill.save() 

Worked.photo=photo
Worked.get_image
Worked.bornDate=bornDate
Worked.mobile=mobile
Worked.descripcion_personal=descripcion
Worked.gender=Genders.objects.get(id=gender)
Worked.save() """