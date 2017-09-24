from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Fuser1(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Usuario',
			'first_name': 'Nombres',
		}

class Fuser(UserCreationForm):

	class Meta:
		model = Empresa

		fields = [
			'username',
			#'first_name',
			#'last_name',
			'email',
			'nombreEmpresa',
			'telefono',
			'ubicacion',
			
		]

		labels = {
			'username': 'Usuario',
			#'first_name': 'Nombres',
			#'last_name': 'Apellidos',
			'email': 'Email',
			'nombreEmpresa': 'Nombre de empresa',
			'telefono':'tel',
			'ubicacion':'ub',
		}