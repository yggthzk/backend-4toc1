from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator

def lista_contactos(request):
    query = request.GET.get('busqueda', '')
    if query:
        contactos_lista = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        ).order_by('nombre')
    else:
        contactos_lista = Contacto.objects.all().order_by('nombre')
    
    paginator = Paginator(contactos_lista, 6) 
    page_number = request.GET.get('page')
    contactos = paginator.get_page(page_number)

    contexto = {'contactos': contactos, 'query': query}
    return render(request, 'Agendapersonal/lista_contactos.html', contexto)

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            try: 
                form.save()
                messages.success(request, '¡Contacto creado exitosamente!')
                return redirect('lista_contactos')
            except IntegrityError as e:
                if 'telefono' in str(e): 
                    messages.error(request, 'Error: Ya existe un contacto con ese número de teléfono.')
                elif 'correo' in str(e):
                    messages.error(request, 'Error: Ya existe un contacto con ese correo electrónico.')
                else:
                    messages.error(request, 'Error: Ocurrió un problema al guardar el contacto.')
    else:
        form = ContactoForm()
    return render(request, 'Agendapersonal/crear_contacto.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
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
        form = ContactoForm(instance=contacto)
    return render(request, 'Agendapersonal/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        messages.success(request, 'Contacto eliminado')
        return redirect('lista_contactos')
    
    contexto = {'contacto': contacto}
    return render(request, 'Agendapersonal/eliminar_contacto.html', contexto)