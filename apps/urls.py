from django.urls import path, include
from django.conf.urls import url
from apps import views
from .views import * 

urlpatterns = [
	path('',academico, name = 'academico'),
	#path('nuevoinscrito/',inscrito_view, name = 'nuevoinscrito'),
	path('listarinscrito',inscritoList.as_view(), name = 'inscrito_listar'),
	path('nuevoinscrito',inscritoCreate.as_view(), name= 'inscrito_crear'),
	path('editarinscrito/<pk>',inscritoUpdate.as_view(), name='inscrito_editar'),
	path('eliminarinscrito/<pk>',inscritoDelete.as_view(), name='inscrito_eliminar'),
	path('listarmatricula',matriculaList.as_view(), name='matricula_listar'),
	path('nuevomatricula',matriculaCreate.as_view(), name= 'matricula_crear'),
	path('editarmatricula/<pk>',matriculaUpdate.as_view(), name='matricula_editar'),
	path('eliminarmatricula/<pk>',matriculaDelete.as_view(), name='matricula_eliminar'),
	path('listarpago',pagoList.as_view(), name='pago_listar'),
	path('nuevopago',pagoCreate.as_view(), name= 'pago_crear'),
	path('editarpago/<pk>',pagoUpdate.as_view(), name='pago_editar'),
	path('eliminarpago/<pk>',pagoDelete.as_view(), name='pago_eliminar'),
	path('listarcurso',cursoList.as_view(), name='curso_listar'),
	path('nuevocurso',cursoCreate.as_view(), name= 'curso_crear'),
	path('editarcurso/<pk>',cursoUpdate.as_view(), name='curso_editar'),
	path('eliminarcurso/<pk>',cursoDelete.as_view(), name='curso_eliminar'),
	path('listarugel',ugelList.as_view(), name='ugel_listar'),
	path('nuevougel',ugelCreate.as_view(), name= 'ugel_crear'),
	path('editarugel/<pk>',ugelUpdate.as_view(), name='ugel_editar'),
	path('eliminarugel/<pk>',ugelDelete.as_view(), name='ugel_eliminar'),
	#url(r'^create/$', views.create, name="create"),
    #url(r'^list/$', views.list, name="list"),
	]