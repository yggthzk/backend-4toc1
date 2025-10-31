from django.contrib import admin
from .models import Contacto, Etiqueta
import csv
from django.http import HttpResponse

def exportar_a_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contactos.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['nombre', 'telefono', 'correo', 'direccion'])
    
    for contacto in queryset:
        writer.writerow([contacto.nombre, contacto.telefono, contacto.correo, contacto.direccion])
        
    return response

exportar_a_csv.short_description = "Exportar seleccionados a CSV"

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo')
    search_fields = ('nombre', 'correo')
    actions = [exportar_a_csv]
    filter_horizontal = ('etiquetas',)

admin.site.register(Etiqueta)
admin.site.register(Contacto, ContactoAdmin)