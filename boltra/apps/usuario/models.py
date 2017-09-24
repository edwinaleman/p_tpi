# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empresa(User):
	nombreEmpresa=models.CharField(max_length=100)
	telefono=models.CharField(max_length=8)
	ubicacion=models.CharField(max_length=150)

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural='Empresas'
	def __str__(self):
		return '%s' %(self.nombreEmpresa)