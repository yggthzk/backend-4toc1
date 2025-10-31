from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre 

class Contacto(models.Model):
    nombre = models.CharField(
        max_length=40,
        verbose_name="Nombre Completo"#verssss
    )
    
    telefono = PhoneNumberField(
        unique=True,
        verbose_name="Telefono"
    )
    
    correo = models.EmailField(
        max_length=40,
        unique=True,
        verbose_name="Correo Electronico"
    )
    
    direccion = models.CharField(
        max_length=50,
        verbose_name="Direccion", 
        blank=True
    )
    
    etiquetas = models.ManyToManyField(
        Etiqueta, 
        blank=True,
        verbose_name="Etiquetas"
    )
    
    creado = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creacion"
    )
#arreglao
    def __str__(self):
        return self.nombre