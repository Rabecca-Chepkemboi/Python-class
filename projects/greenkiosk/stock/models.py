from django.db import models

# Create your models here.
class Stock(models.Model):
   product_id = models.AutoField(primary_key=True)
   product_name = models.CharField(max_length=40)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   quantity = models.PositiveBigIntegerField()
   category = models.CharField(max_length=50)
   store_name = models.CharField(max_length=40)
   store_location = models.CharField(max_length=60) 
