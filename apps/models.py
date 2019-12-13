from django.db import models


class Curso(models.Model):
	id = models.AutoField(primary_key= True)
	nombre = models.CharField(max_length=100, unique=True)
	descripcion= models.TextField(max_length=200, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Ugel(models.Model):
	id= models.AutoField(primary_key= True)
	ugel = models.CharField(max_length=100,unique=True)
	director = models.CharField(max_length=100, blank=True, null=True)
	observacion = models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.ugel)

	class Meta:
		ordering = ['ugel']


class Inscrito(models.Model):
	id = models.AutoField(max_length=30, primary_key = True, unique=True)
	nombres = models.CharField(max_length=70)
	apellidos = models.CharField(max_length=70)
	dni= models.IntegerField(unique=True)
	e_mail= models.EmailField(blank=True)
	telefono = models.IntegerField(blank=True)
	direccion = models.CharField(null=True,max_length=150)
	observacion = models.TextField(max_length=1000, null=True, blank=True)
	

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	class Meta:
		ordering = ['id']

class Matricula(models.Model):

	id = models.CharField(primary_key= True,max_length=20, null=False, unique=True)
	inscrito = models.ForeignKey(Inscrito,on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	ugel = models.ForeignKey(Ugel, null=True, blank=True, on_delete=models.CASCADE)
	asesora = models.CharField(null=True,max_length=50)
	fecha_matricula = models.DateField(null=True)
	fecha_diploma = models.DateField(null=True)
	observacion = models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.id)


class Pago(models.Model):
	id = models.AutoField(max_length=30, primary_key = True, unique=True)
	matricula= models.ForeignKey(Matricula, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=50, null=True)
	fecha_pago= models.DateField()
	monto = models.DecimalField(max_digits=5, decimal_places=2)
	mod_entregado= models.CharField(max_length=50)
	