from django.db import models

# Create your models here.

class Discount(models.Model):
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=100)
    items_bought = models.IntegerField()
    active = models.BooleanField()
    date = models.DateField()
