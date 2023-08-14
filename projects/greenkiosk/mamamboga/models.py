from django.db import models

# Create your models here.
# from products.models import Products
class MamaMboga(models.Model):
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    phonenumber=models.CharField(max_length=32)
    location=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

    def __str__(self):
        return self.name