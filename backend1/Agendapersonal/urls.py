from django.urls import path#path para definir rutas
from . import views#vistas

urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),#Ruta principal de la lisyta de contactos
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>/', views.eliminar_contacto, name='eliminar_contacto'),#usando el ID para el CRUD en el enrutamiento
]