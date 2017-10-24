# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..usuario.models import Empresa #Importacion de models.py de la app usuario

# Create your models here.

class Facultad(models.Model):
	nombreFacultad=models.CharField(max_length=70)

	class Meta:
		verbose_name='Facultad'
		verbose_name_plural='Facultades'
	def __str__(self):
		return '%s' %(self.nombreFacultad)

class Carrera(models.Model):
	facultad=models.ForeignKey(Facultad)
	nombreCarrera=models.CharField(max_length=70)

	class Meta:
		verbose_name='Carrera'
		verbose_name_plural='Carreras'
	def __str__(self):
		return '%s' %(self.nombreCarrera)

class OfertaEmpleo(models.Model):
	empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
	carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)
	#area=models.CharField(max_length=50)
	numPuestos=models.IntegerField()
	tipoContrato=models.CharField(max_length=50)
	nivelExperiencia=models.CharField(max_length=25)
	genero=models.CharField(max_length=15)
	edadMin=models.IntegerField()
	edadMax=models.IntegerField()
	salarioMax=models.IntegerField()
	salarioMim=models.IntegerField()
	depResidencia=models.CharField(max_length=50)
