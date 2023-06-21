from django.db import models

# Create your models here.
class Client(models.Model):
      customer_id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=50)
      phone_number = models.CharField(max_length=50)
      email = models.EmailField()
    #   orders = models.ManyToManyField(Order)
      loyalty_points = models.IntegerField()
