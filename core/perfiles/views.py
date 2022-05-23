from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, CreateView
from core.main.forms import SkillsWorked, postRegistro
from core.main.models import Skills, Users, WorkedSkills
from .models import *
from .forms import *

from django.contrib import messages

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

def index(request):
    
    return render(request, 'index/index.html',{
        'Titulo':'Inicio',
    })

class updateUser(CreateView, DetailView):
    model=Users
    model_skills=WorkedSkills
    template_name='users/postRegister.html'
    form_class=postRegistro
    form_esp=SkillsWorked

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form']=self.form_class(instance=persona)
        if 'form2' not in context:
            context['form2']=self.form_esp()
        if 'especialidad' not in context:
            context['especialidad']=self.model_skills.objects.filter(trabajador=pk)
        context['title']='Perfil'
        context['id']=pk
        
        return context

    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        if request.method=='POST':
            form=self.form_class(request.POST,request.FILES, instance=persona)
            form2=self.form_esp(request.POST)
            if(form.is_valid()):
                form.save() 
                messages.warning(request, 'datos actualizados')
                if form2.is_valid():
                    data=form2.cleaned_data
                    especiality=data['especialidad']

                for esp in especiality:
                    existe=WorkedSkills.objects.filter(trabajador=persona, especialidad=int(esp)).exists()
                    if not existe:
                        skill=WorkedSkills(
                            trabajador=persona,
                            especialidad=Skills.objects.get(id=int(esp))
                        )
                        skill.save()

                return redirect('perfilUpdate', pk=request.user.id)

        else:
            messages.warning(request, 'Hay algun error en el formulario')
            return redirect('perfilUpdate', pk=request.user.id)

class evidenciasTrabajadores(UpdateView, DetailView):
    model=Users
    model_evidencias=Evidencias
    template_name='users/evidencias.html'
    form_class=evidencias

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form']=self.form_class()
        if 'evidencias' not in context:
            context['evidencias']=self.model_evidencias.objects.filter(trabajador=pk)
        context['title']='Galeria'
        context['id']=pk
        
        return context
    
    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        if request.method=='POST':
            form=self.form_class(request.POST,request.FILES)
            if(form.is_valid()):
                data=form.cleaned_data
                descripcion=data['descripcion']
                evidenciaPhoto=data['evidenciaPhoto']
                evidence=Evidencias(
                    descripcion=descripcion,
                    evidenciaPhoto=evidenciaPhoto,
                    trabajador=persona
                )
                evidence.save() 
                
                messages.warning(request, 'datos actualizados')

                return redirect('perfilUpdate', pk=request.user.id)

        else:
            messages.warning(request, 'Hay algun error en el formulario')
            return redirect('perfilUpdate', pk=request.user.id)

