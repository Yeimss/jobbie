from django.urls import path
from . import views

urlpatterns = [
    path('perfil/<str:tipo>', views.pefil, name='perfil'),
]
