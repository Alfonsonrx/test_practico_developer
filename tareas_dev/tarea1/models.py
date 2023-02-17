from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Station(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    latitude = models.DecimalField(decimal_places=6, max_digits=20)
    longitude = models.DecimalField(decimal_places=6, max_digits=20)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
class Extra(models.Model):
    uid = models.CharField(max_length=100, primary_key=True, unique=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    altitude = models.DecimalField(decimal_places=1, max_digits=10)
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField(default=True)
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = ArrayField(
        models.CharField(max_length=20, blank=False),
        size=5
    )
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=10, blank=True)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    
    def __str__(self):
        return self.uid