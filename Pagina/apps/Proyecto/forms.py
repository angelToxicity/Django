from django import forms
from apps.Proyecto.models import registro
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