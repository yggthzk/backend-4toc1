from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):#crea un formulario usando los datos heredados de modelos, validaciones
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #bucle de recorrido de los campos del formulario nombre tlfn etc
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contacto #creacion del formulario y los campos a rellenar(Segun caso de estudio solo son estos 4)
        fields = ['nombre', 'telefono', 'correo', 'direccion']