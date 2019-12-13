from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Inscrito, Ugel, Curso, Matricula, Pago
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError


def academico(request):
	return render(request, 'academico/index.html')

class cursoList(ListView):
	model = Curso
	template_name = 'academico/curso.html'

class cursoCreate(CreateView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_form.html'
	success_url = reverse_lazy('curso_listar')

class cursoUpdate(UpdateView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_form.html'
	success_url = reverse_lazy('curso_listar')

class cursoDelete(DeleteView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_del.html'
	success_url = reverse_lazy('curso_listar')

class ugelList(ListView):
	model = Ugel
	template_name = 'academico/ugel.html'

class ugelCreate(CreateView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_form.html'
	success_url = reverse_lazy('ugel_listar')

class ugelUpdate(UpdateView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_form.html'
	success_url = reverse_lazy('ugel_listar')

class ugelDelete(DeleteView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_del.html'
	success_url = reverse_lazy('ugel_listar')


class inscritoList(ListView):
	model = Inscrito
	template_name = 'academico/inscrito.html'

class inscritoCreate(CreateView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_form.html'
	success_url = reverse_lazy('inscrito_listar')

class inscritoUpdate(UpdateView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_form.html'
	success_url = reverse_lazy('inscrito_listar')

class inscritoDelete(DeleteView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_del.html'
	success_url = reverse_lazy('inscrito_listar')


class matriculaList(ListView):
	model = Matricula
	template_name = 'academico/matricula.html'

class matriculaCreate(CreateView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_form.html'	
	success_url = reverse_lazy('matricula_listar')

class matriculaUpdate(UpdateView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_form.html'
	success_url = reverse_lazy('matricula_listar')

class matriculaDelete(DeleteView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_del.html'
	success_url = reverse_lazy('matricula_listar')

class pagoList(ListView):
	model = Pago
	template_name = 'academico/pago.html'

class pagoCreate(CreateView):
	model = Pago
	form_class = PagoForm
	template_name = 'academico/pago_form.html'
	success_url = reverse_lazy('pago_listar')

class pagoUpdate(UpdateView):
	model = Pago
	form_class = PagoForm
	template_name = 'academico/pago_form.html'
	success_url = reverse_lazy('pago_listar')

class pagoDelete(DeleteView):
	model = Pago
	form_class = PagoForm
	template_name = 'academico/pago_del.html'
	success_url = reverse_lazy('pago_listar')



# def create(request):
#	context={}
#	PagoFormset = modelformset_factory(Pago, form=PagoForm)
#	form = MatriculaForm(request.POST or None, queryset=Pago.objects.none(),prefix='pagos')
#	if request.method == "POST":
#		if form.is_valid() and formset.is_valid():
#			try:
#				with transaction.atomic():
#					matricula = form.save(commit=False)
#					matricula.save()
#
#					for pago in formset:
#						data = mark.save(commit=False)
#						data.matricula = matricula
#						data.save()
#			except IntegrityError:
#				print("Error")
#			return redirect('multi_forms:list')
#	context['formset'] = formset
#	context['form'] = form
#	return render(request, 'academico/matricula_form.html')
#
#def list(request):
#	datas = Matricula.objects.all()
#	return render(request, 'academico/matricula.html', {'datas':datas})