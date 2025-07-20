from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    slot = models.IntegerField()
