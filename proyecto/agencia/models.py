from tabnanny import verbose
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    mail = models.EmailField()
    pagina = models.URLField()
    telefono = PhoneNumberField()

    def __str__(self):
        return self.nombre

class Viaje(models.Model):
    destino = models.CharField(max_length=30)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='imagenes')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    TIP_VIA = (
        ('Aire','Aire'),
        ('Tierra','Tierra'),
        ('Mar','Mar'),
    )
    tipo = models.CharField(max_length=6, choices=TIP_VIA,default='tierra')

    def __str__(self):
        return self.destino

    class Meta:
        verbose_name_plural = 'Viajes'
