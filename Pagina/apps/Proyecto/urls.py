from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'proyecto'

urlpatterns = [
    path('', views.index, name='principal'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('librosR/', login_required(views.crearLibro.as_view()), name='libros'),
    path('listaLibros/', login_required(views.libros1.as_view()), name="lista"),
    path('editLibros/<pk>/', login_required(views.updateLibro.as_view()), name='editar'),
    path('deleteLibros/<pk>/', login_required(views.deleteLibro.as_view()), name='eliminar'),
    path('registro/', views.registroUsuario.as_view(),name="registro"),
    path('voto/', views.votoList.as_view(),name="votos"),
    path('votar/<id_libro>/<vote>', views.votar,name="votar"),
    path('listado/', views.listado,name="listado"),
]