from django.shortcuts import render, redirect

# Create your views here.
def pefil(request, tipo):
    if(tipo=='Oficial'):
        return render(request, 'users/perfilWorked.html',{
            'title':'Perfil',
        })
    else:
        return render(request, 'users/perfilClient.html',{
            'title':'Perfil',
        })
