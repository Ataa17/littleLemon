from django.db import models

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

class booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    no_of_guests = models.IntegerField(max_length=5)
   