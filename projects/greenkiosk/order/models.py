from django.db import models

# Create your models here.
class Order(models.Model):
   order_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=40)
   ordered_items = models.TextField()
   total_cost = models.DecimalField(max_digits=8,decimal_places=1)
   delivery_address = models.CharField(max_length=90)
   delivery_date = models.DateField()
   status = models.CharField(max_length=40)

