from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from core.main.forms import SkillsWorked, postRegistro
from core.main.models import Skills, Users, WorkedSkills
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

class updateUser(UpdateView):
    model=Users
    model_skills=WorkedSkills
    template_name='users/postRegister.html'
    form_class=postRegistro
    form_esp=SkillsWorked

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)
        especialidad=self.model_skills.objects.filter(trabajador=pk)
        if 'form' not in context:
            context['form']=self.form_class(instance=persona)
        if 'form2' not in context:
            context['form2']=self.form_esp()
        context['id']=pk
        return context

    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        form=self.form_class(request.POST,request.FILES, instance=persona)
        form2=self.form_esp(request.POST)
        if(form.is_valid() and form2.is_valid()):
            """  data=form2.cleaned_data
            especialidad=data['especialidad']
            for esp in especialidad:
                skill=WorkedSkills(
                    trabajador=(Users.objects.get(id=id_persona)),
                    especialidad=Skills.objects.get(especialidad=esp),
                )
                skill.save(commit=False) 

            """
            """ habilidades=form2.save(commit=False)
            habilidades.trabajador(persona)
            habilidades.save()"""
            form.save() 
            messages.warning(request, 'datos actualizados')
            return redirect('index')

        else:
            return HttpResponseRedirect(self.get_success_url())

