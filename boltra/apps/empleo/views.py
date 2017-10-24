# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from ..usuario.models import Empresa
from .models import *
from .forms import *
# Create your views here.

def pagInicial(request):
	facultad=Facultad.objects.all()
	empresa=Empresa.objects.all()
	return render(request, 'inicio.html', {'facultad':facultad}, {'empresa':empresa})

def regOferta(request):
	if request.method =='POST':
		form = FormOferta(request.POST)
		if form.is_valid():
			form.save()
		return redirect('empleo:pag_inicio')
	else:
		form=FormOferta()
	return render(request, 'oferta/regOferta.html', {'form': form})

def conOferta(request):
	ofertas=OfertaEmpleo.objects.all
	return render(request, 'oferta/conOferta.html', {'ofertas':ofertas})

def desOferta(request, id_ofertaempleo):
	oferta=OfertaEmpleo.objects.get(id=id_ofertaempleo)
	return render(request, 'oferta/desOferta.html', {'oferta':oferta})

def edtOferta(request, id_ofertaempleo):
	oferta=OfertaEmpleo.objects.get(id=id_ofertaempleo)
	if request.method =='GET':
		form = FormOferta(instance=oferta)
	else:
		form = FormOferta(request.POST, instance=oferta)
		if form.is_valid():
			form.save()
		return redirect('empleo:con_oferta')
	return render(request, 'oferta/regOferta.html', {'form': form})

def elmOferta(request, id_ofertaempleo):
	oferta = OfertaEmpleo.objects.get(id=id_ofertaempleo)
	if request.method == 'POST':
		oferta.delete()
		return redirect('empleo:con_oferta')
	return render(request, 'oferta/elmOferta.html', {'oferta': oferta})

def lstCarrera(request, id_facultad):
	facultad=Facultad.objects.all()
	facultad_select = Facultad.objects.get(id=id_facultad)
	atrib = facultad_select.id
	carreras = Carrera.objects.filter(facultad_id=atrib)
	return render(request, 'carrera/lstCarrera.html', {'carreras':carreras}, {'facultad':facultad})

def conOfertaStd(request, id_carrera): #
	facultad=Facultad.objects.all()
	empresas=Empresa.objects.all()
	carrera=Carrera.objects.get(id=id_carrera)
	atrib = carrera.id
	ofertas = OfertaEmpleo.objects.filter(carrera_id=atrib)
	return render(request, 'carrera/conOfertasStd.html', {'ofertas':ofertas}, {'empresas':empresas})