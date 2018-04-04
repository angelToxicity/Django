from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from apps.Proyecto.forms import registroLibro
from apps.Proyecto.models import registro

def index(request):
	return render(request, 'Proyecto/index.html')

def listado(request):
	lista = serializers.serialize('json', registro.objects.filter(pk=2), fields=['titulo', 'autor', 'votos'])
	return HttpResponse(lista, content_type='application/json')

class libros1(ListView):
    model = registro
    template_name = "Proyecto/lista_libros.html"

class crearLibro(CreateView):
	model = registro
	form_class = registroLibro

class updateLibro(UpdateView):
	model = registro
	form_class = registroLibro
	success_url = reverse_lazy('proyecto:lista')

class deleteLibro(DeleteView):
	model = registro
	template_name = "Proyecto/delete_libro.html"
	success_url = reverse_lazy('proyecto:lista')

class registroUsuario(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'Proyecto/registro_usuario.html'
	success_url = reverse_lazy('proyecto:principal')

class votoList(ListView):
    model = registro
    template_name = "Proyecto/votos.html"

def votar(request, id_libro, vote):
	libro = registro.objects.get(id=id_libro)
	if vote == 'None':
		vote = 0
		libro.votos = int(vote) + 1
		libro.save()
	else:
		libro.votos = int(vote) + 1
		libro.save()
	return render(request, 'Proyecto/success.html', {"libro": libro})
	
# def registrarLibro(request):
# 	if request.method == 'POST':
# 		form = registroLibro(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('proyecto:lista')
# 	else:
# 		form = registroLibro()
# 	return render(request, 'Proyecto/registro_libros.html', {"form": form})

# def listarLibros(request):
# 	libro = registro.objects.all().order_by('id')
# 	contexto = {"book": libro}
# 	return render(request, 'Proyecto/lista_libros.html', contexto)

# def editarLibro(request, id_libro):
# 	libro = registro.objects.get(id=id_libro)
# 	if request.method == 'GET':
# 		form = registroLibro(instance=libro)
# 	else:
# 		form = registroLibro(request.POST, instance=libro)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('proyecto:lista')
# 	return render(request, 'Proyecto/registro_form.html', {"form": form})

# def libroDelete(request, id_libro):
# 	libro = registro.objects.get(id=id_libro)
# 	if request.method == 'POST':
# 		libro.delete()
# 		return redirect('proyecto:lista')
# 	return render(request, 'Proyecto/delete_libro.html', {"libro": libro})