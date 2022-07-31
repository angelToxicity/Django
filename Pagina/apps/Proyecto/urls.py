from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'proyecto'

urlpatterns = [
    path('', views.index, name='principal'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('librosR/', login_required(views.crearLibro.as_view()), name='libros'),
    path('listaLibros/', login_required(views.libros1.as_view()), name="lista-libros"),
    path('editLibros/<pk>/', login_required(views.updateLibro.as_view()), name='editar'),
    path('deleteLibros/<pk>/', login_required(views.deleteLibro.as_view()), name='eliminar'),
    path('registro/', views.registroUsuario.as_view(),name="registro"),
    path('voto/', views.votoList.as_view(),name="votos"),
    path('votar/<id_libro>/<vote>', views.votar,name="votar"),
    path('reporte/', login_required(views.lista_prod.as_view()), name="lista"),
    path('registro-prod/', login_required(views.insertProduct.as_view()), name='new-productos'),
    path('recepcion-prod/<pk>/', login_required(views.formReceptionProduct), name='new-input'),
    path('detail/<int:id_p>/', login_required(views.detail_prod.as_view()), name='detalle'),
    path('success/', login_required(views.success_prod), name='success'),
    path('success-registro/<int:pk>/', login_required(views.success_insert), name='success-insert'),
]