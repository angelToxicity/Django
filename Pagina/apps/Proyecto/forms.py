from itertools import product
from django import forms
from apps.Proyecto.models import registro, productos, registro_producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registroLibro(forms.ModelForm):
	class Meta:
		model = registro
		fields = [
			'titulo',
			'autor',
			'sexo',
			'fecha_publicacion',
			'resumen',
		]
		labels = {
			'titulo': 'Titulo',
			'autor': 'Autor',
			'sexo': 'Sexo',
			'fecha_publicacion': 'Fecha Publicacion',
			'resumen': 'Reseña'
		}
		widgets ={
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'autor': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.Select(attrs={'class':'form-control'}),
			'fecha_publicacion': forms.DateInput(attrs={'class':'form-control'}),
			'resumen': forms.Textarea(attrs={'class':'form-control'})
		}

class registroProducto(forms.ModelForm):
	class Meta:
		model = productos
		fields = [
			'titulo',
			'codigo',
			'descripcion'
		]
		labels = {
			'titulo': 'Titulo',
			'codigo': 'Codigo de Producto',
			'descripcion': 'Descripción'
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'})
		}

class registroIngresoProducto(forms.ModelForm):
	class Meta:
		model = registro_producto
		fields = [
			'lote',
			'fecha_recepcion',
			'fecha_vencimiento',
			'cantidad',
			'ubicacion',
			'proveedor'
		]
		labels = {
			'lote': 'N° de Lote',
			'fecha_recepcion': 'Fecha de Recepción',
			'fecha_vencimiento': 'Fecha de Vencimiento',
			'cantidad': 'Cantidad',
			'ubicacion': 'Ubicación',
			'proveedor': 'Proveedor (Interno/Externo)'
		}
		widgets = {
			'lote': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_recepcion': forms.DateInput(attrs={'class':'form-control', 'placeholder':'dd/MM/YYYY', 'type': 'date'}, format=('%d/%m/%Y')),
			'fecha_vencimiento': forms.DateInput(attrs={'class':'form-control', 'placeholder':'dd/MM/YYYY', 'type': 'date'}, format=('%d/%m/%Y')),
			'cantidad': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
			'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
			'proveedor': forms.TextInput(attrs={'class':'form-control'})
		}

class detalleIngresoProducto(forms.ModelForm):
	class Meta:
		model = productos
		fields = [
			'titulo',
			'codigo',
			'descripcion'
		]
		labels = {
			'titulo': 'Titulo',
			'codigo': 'Codigo de Producto',
			'descripcion': 'Descripción'
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control col-xs-6', 'disabled':''}),
			'codigo': forms.TextInput(attrs={'class':'form-control col-xs-6', 'disabled':''}),
			'descripcion': forms.Textarea(attrs={'class':'form-control col-xs-4', 'disabled':''})
		}