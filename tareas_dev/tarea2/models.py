from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=5)
    region = models.CharField(max_length=30)
    tipologia = models.CharField(max_length=4)
    titular = models.CharField(max_length=150)
    inversion = models.DecimalField(max_digits=10,decimal_places=4)
    fecha_ingreso = models.DateTimeField()
    estado = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    
    def millones_inversion_usd(self):
        return self.inversion * 1000000