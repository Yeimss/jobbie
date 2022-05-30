from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('error/',views.error, name="error"),
    path('perfil/<str:tipo>', views.pefil, name='perfil'),
    path('editarPerfil/<int:pk>', views.updateUser.as_view(), name='perfilUpdate'),
    path('galeria/<int:pk>', views.evidenciasTrabajadores.as_view(), name='galeriaPropia'),
    path('borrarEvidencia/<int:id>', views.borrarEvidencia, name="borrarEvidencia"),
    path('editarEvidencia/<int:id>', views.editarEvidencia, name="editarEvidencia"),
    path('categorias/<int:id>', views.categorias, name="categorias"),
]
