# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .forms import *

# Create your views here.

#vista de prueba
def pagInicial(request):
	empresa=Empresa.objects.all()
	return render(request, 'usuario/paginaInicial.html', {'empresa':empresa})

class Vuser(CreateView):
	model = User
	template_name = "usuario/regEstudiante.html"
	form_class = Fuser1
	success_url = reverse_lazy('usuario:pag_inicial')

def add_user(request):
	if request.method=="POST":
		perfil_form=Fuser(request.POST)
		if perfil_form.is_valid():
			perfil_form.save()
			return redirect('usuario:pag_inicial')
	else:
		perfil_form=Fuser()
	return render(request, 'usuario/regEmpresa.html', {'perfil_form': perfil_form})