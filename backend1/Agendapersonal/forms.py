from django import forms
from .models import Contacto 

class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'etiquetas':
                field.widget.attrs.update({'class': 'form-select', 'size': '5'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion', 'etiquetas']
        widgets = {
            'etiquetas': forms.SelectMultiple(attrs={'class': 'form-control'})
        }