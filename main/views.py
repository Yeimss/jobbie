from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register_page(request):
    register_form=UserCreationForm()

    return render(request, 'users/registers.html',{
        'title':'Registrarse',
        'register_form':register_form
    })

