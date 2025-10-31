#recoleccion de datos, GUARDADO Y GESTION DE LOS CONTACTOS modelo de base de datos :)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField #importando modulo de verificacion de numeros de telefono de DJANGO
#libreria externa

# NUEVO MODELO ETIQUETA
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(
        max_length=40,
        verbose_name="Nombre Completo"#ver nombre del formulario de contacto
    )
    
    telefono = PhoneNumberField(
        unique=True,#Este modulo de django nos ayuda a evitar que se repitan los datos entre un formulario y otro
        verbose_name="Teléfono"#Evitar duplicados
    )
    
    correo = models.EmailField(
        max_length=40,
        unique=True,
        verbose_name="Correo Electrónico"
    )
    
    direccion = models.CharField(
        max_length=50,
        verbose_name="Dirección",
        blank=True#para dejar en blanco esa parte
    )
    
    # CAMPO AÑADIDO (ManyToMany)
    etiquetas = models.ManyToManyField(
        Etiqueta, 
        blank=True,
        verbose_name="Etiquetas"
    )
    
    creado = models.DateTimeField(
        auto_now_add=True, # para el registro de fecha y hora del contacto (AL FINAL NO LO USE)
        verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return self.nombre