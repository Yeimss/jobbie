from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('perfil/<str:tipo>', views.pefil, name='perfil'),
    path('editarPerfil/<int:pk>', views.updateUser.as_view(), name='perfilUpdate'),
]
