from django.db import models

# Create your models here.
class Organizacion(models.Model):
    Nombre = models.CharField(max_length=150)
    TIPO_CHOICES = [
        ('Fundacion', 'Fundacion'),
        ('Junta de Vecinos', 'Junta de Vecinos'),
        ('Club Deportivo', 'Club Deportivo'),
    ]
    
    Tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    Direccion = models.CharField(max_length=200)
    Contacto = models.CharField(max_length=150)
    Descripcion = models.TextField()
    
    
    def __str__(self):
        return self.Nombre
    
    
