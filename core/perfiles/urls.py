from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('perfil/<str:tipo>', views.pefil, name='perfil'),
    path('editarPerfil/<int:pk>', views.updateUser.as_view(), name='perfilUpdate'),
    path('galeria/<int:pk>', views.evidenciasTrabajadores.as_view(), name='galeriaPropia'),
]
