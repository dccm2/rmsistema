from django import forms
from .models import *

class InscritoForm(forms.ModelForm):
	class Meta:
		model = Inscrito
		fields = [
			'id',
			'nombres',
			'apellidos',
			'dni',
			'e_mail',
			'telefono',
			'direccion',
			'observacion',	
		]

		labels = {
			'id':'Código',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'dni' : 'DNI',
			'e_mail': 'Correo Electrónico',
			'telefono' : 'Telefono',
			'direccion':'Direccion',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control', 'id':'inscrito'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'dni':forms.NumberInput(attrs={'class':'form-control'}),
			'e_mail': forms.EmailInput(attrs={'class':'form-control'}),	
			'telefono':forms.NumberInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
		}

class UgelForm(forms.ModelForm):
	class Meta:
		model = Ugel
		fields = [
			'id',
			'ugel',
			'director',
			'observacion',
		]

		labels = {
			'id':'Codigo',
			'ugel': 'Ugel',
			'director':'Director',
			'observacion': 'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'ugel': forms.TextInput(attrs={'class':'form-control'}),
			'director':forms.TextInput(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
		}

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = [
			'id',
			'nombre',
			'descripcion',
		]

		labels = {
			'id':'Codigo',
			'nombre': 'Curso',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'})
		}

class MatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula
		fields = [
			'id',
			'inscrito',
			'curso',
			'ugel',
			'asesora',
			'fecha_matricula',
			'fecha_diploma',
			'observacion',
		]
		labels = {
			'id':'Codigo',
			'inscrito': 'Inscrito',
			'curso':'Curso',
			'ugel' : 'Ugel',
			'asesora':'Asesora',
			'fecha_matricula':'Fecha de Matrícula',
			'fecha_diploma':'Fecha de Entrega de Diploma',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'inscrito': forms.Select(attrs={'class':'form-control'}),
			'curso':forms.Select(attrs={'class':'form-control'}),
			'ugel':forms.Select(attrs={'class':'form-control'}),
			'asesora':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_matricula':forms.SelectDateWidget(years=range(2017,2050)),
			'fecha_diploma':forms.SelectDateWidget(years=range(2017,2050)),
			'observacion': forms.Textarea(attrs={'class':'form-control'}),
		}
		

class PagoForm(forms.ModelForm):
	class Meta:
		model = Pago
		fields = [
			'id',
			'matricula',
			'descripcion',
			'fecha_pago',
			'monto',
			'mod_entregado',
			
		]

		labels = {
			'id': 'Código',
			'matricula':'Matrícula',
			'descripcion': 'Cuota',
			'fecha_pago':'Fecha de Pago',
			'monto': 'Monto',
			'mod_entregado':'Modulo Entregado',
			
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'matricula':forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_pago': forms.SelectDateWidget(years=range(2017,2050)),
			'monto':forms.TextInput(attrs={'class':'form-control'}),
			'mod_entregado':forms.TextInput(attrs={'class':'form-control'}),
			
		}


"""class RawMatriculaForm(forms.Form):
	id = forms.CharField(label='Código de Matrícula'),
	inscrito = forms.Select(),
	curso = forms.CharField(label='Curso'),
	modulos_entregados = forms.CharField(label='Módulos Entregados'),
	asesora = forms.CharField(label='Asesora'),
	beneficiario =forms.CharField(label='Beneficiario'),
	fecha_matricula =forms.DateField(label='Fecha de Matrícula' ,widget=forms.DateInput(attrs={'class':'datefield'})),
	fecha_diploma =forms.DateField(label='Fecha de Entrega de Diploma',widgets={'datefield':DateInput}),
	promocion = forms.CharField(label='Promoción'),
	descuento_actual = forms.DecimalField(label='Descuento Actual'),
	descuento_pendiente = forms.DecimalField(label='Descuento Pendiente'),
	observacion = forms.DecimalField(label='Observaciones'),


		labels = {
			'id':'Codigo',
			'inscrito': 'Inscrito',
			'curso':'Curso',
			'modulos_entregados': 'Modulos Entregados',
			'asesora':'Asesora',
			'beneficiario':'Beneficiario',
			'fecha_matricula':'Fecha de Matrícula',
			'fecha_diploma':'Fecha de Entrega de Diploma',
			'promocion':'Promoción',
			'descuento_actual':'Descuento Actual',
			'descuento_pendiente':'Descuento Pendiente',
			'observacion':'Observaciones',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'inscrito': forms.Select(attrs={'class':'form-control'}),
			'curso':forms.Select(attrs={'class':'form-control'}),
			'modulos_entregados': forms.Textarea(attrs={'class':'form-control'}),
			'asesora':forms.TextInput(attrs={'class':'form-control'}),
			'beneficiario':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_matricula':forms.DateInput(attrs={'class':'form-control'}),
			'fecha_diploma':forms.DateInput('class':'DateForm'),
			'promocion':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_actual':forms.TextInput(attrs={'class':'form-control'}),
			'descuento_pendiente':forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.Textarea(attrs={'class':'form-control'}),
		}"""

class DateInput(forms.DateInput):
	input_type= 'date'

class DateForm(forms.Form):
	datefield=forms.DateField(widget=DateInput)
