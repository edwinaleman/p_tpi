from django import forms
from .models import *

class FormOferta(forms.ModelForm):

	class Meta:
		model = OfertaEmpleo

		fields = [
			'empresa',
			'carrera',
			'nombre',
			'numPuestos',
			'tipoContrato',
			'nivelExperiencia',
			'genero',
			'edadMin',
			'edadMax',
			'salarioMim',
			'salarioMax',
			'depResidencia',
		]

		labels = {
			'empresa': 'Empresa',
			'carrera': 'Carrera',
			'nombre': 'Titulo de Oferta',
			'numPuestos': 'Puestos bacantes',
			'tipoContrato': 'Tipo de contrato',
			'nivelExperiencia': 'Tiempo de experiencia',
			'genero': 'Genero',
			'edadMin': 'Edad minima',
			'edadMax': 'Edad maxima',
			'salarioMim': 'Salario Base',
			'salarioMax': 'Salario maximo',
			'depResidencia': 'Departamento de residencia',
		}