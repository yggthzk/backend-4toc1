from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q
from django.contrib import messages#importando modulo de mensajes para errores o inserciones exitosass
from django.db import IntegrityError
#importaciones

def lista_contactos(request):#obtenemos el valor de la url, si no existe regresa un string vacio
    query = request.GET.get('busqueda', '')
    if query:
        contactos = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        )#filtramos los contactos segun el nombre o correo del contacto usando q
    else:
        contactos = Contacto.objects.all()
    contexto = {'contactos': contactos}
    return render(request, 'Agendapersonal/lista_contactos.html', contexto)

def crear_contacto(request):
    if request.method == 'POST':#
        form = ContactoForm(request.POST)
        if form.is_valid():
            try: #error al obtener el id SOLUCIONADOOO
                form.save()
                messages.success(request, '¡Contacto creado exitosamente!')
                return redirect('lista_contactos')
            except IntegrityError as e:
                if 'telefono' in str(e): #Si ocurre un error de integridad o manejo de exepciones nos dara aviso 
                    messages.error(request, 'Error: Ya existe un contacto con ese número de teléfono.')
                elif 'correo' in str(e):
                    messages.error(request, 'Error: Ya existe un contacto con ese correo electrónico.')
                else:
                    messages.error(request, 'Error: Ocurrió un problema al guardar el contacto.')
    else:
        form = ContactoForm()
    return render(request, 'Agendapersonal/crear_contacto.html', {'form': form})#crear_contacto. NO SIRVEEE AAAAA 

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    #busco el contacto por el ID del post que tiene
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'El Contacto se ha guardado. Nuevo Contacto añadido a la Agenda')
                return redirect('lista_contactos')
            except IntegrityError as e:
                if 'telefono' in str(e):
                    messages.error(request, 'Erroor: Ya existe un contacto con ese numero de teléfono.')
                elif 'correo' in str(e):
                    messages.error(request, 'Error: Ya existe un contacto con ese correo. impostor.')
                else:
                    messages.error(request, 'Error: no se pudo guardar el contacto.')
    else:
        form = ContactoForm(instance=contacto)#Al ingresar se mostratra la lista de contactos vacia. no hay contactos
    return render(request, 'Agendapersonal/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        messages.success(request, 'Contacto eliminado')#confirmar eliminacion de contacto shi o no pasa na??
        return redirect('lista_contactos')
    
    contexto = {'contacto': contacto}
    return render(request, 'Agendapersonal/eliminar_contacto.html', contexto)