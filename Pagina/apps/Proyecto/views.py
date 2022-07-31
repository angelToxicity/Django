from asyncio.log import logger
from itertools import product
import logging
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from apps.Proyecto.forms import registroLibro, registroProducto, registroIngresoProducto, detalleIngresoProducto
from apps.Proyecto.models import registro, productos, registro_producto
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
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
	
class insertProduct(CreateView):
	model = productos
	form_class = registroProducto
	success_url = reverse_lazy('proyecto:success')
	
	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super(insertProduct, self).form_valid(form)

def formReceptionProduct(request, pk):
	form = registroIngresoProducto(request.POST)
	if form.is_valid():
		form.instance.usuario = request.user
		form.instance.producto = productos.objects.get(id=pk)
		form.save()
		return redirect('proyecto:success-insert', pk=pk)
	return render(request, 'Proyecto/registro_form.html', {"form": form})

class detail_prod(ListView):
	model = registro_producto
	template_name = "Proyecto/productos_list.html"
	form_class = detalleIngresoProducto
	def get_queryset(self):
		r = registro_producto.objects.raw("SELECT pp.*, prp.* FROM Proyecto_productos pp LEFT JOIN Proyecto_registro_producto prp ON pp.id = prp.producto_id WHERE pp.id = %s;", [self.kwargs['id_p']])
		return r

class lista_prod(ListView):
	model = productos
	template_name = "Proyecto/lista_productos.html"
	def get_queryset(self):
		queryset = productos.objects.raw("SELECT pp.*, (SELECT SUM(prp.cantidad) AS cantidad FROM Proyecto_registro_producto AS prp WHERE prp.producto_id = pp.id) AS cantidad FROM Proyecto_productos pp;")
		return queryset

def success_prod(request):
	elem = productos.objects.latest('titulo')
	template_name = "Proyecto/success_product.html"
	return render(request, 'Proyecto/success_product.html', {"product": elem})

def success_insert(request, pk):
	template_name = "Proyecto/success_insert.html"
	return render(request, 'Proyecto/success_insert.html', {'id': pk})

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