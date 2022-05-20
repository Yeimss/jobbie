from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('perfil/<str:tipo>', views.pefil, name='perfil'),
]
