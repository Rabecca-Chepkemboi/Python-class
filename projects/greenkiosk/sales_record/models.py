from django.db import models

# Create your models here.
class Sales (models.Model):
    sales_id = models.AutoField(primary_key=True)
    date = date = models.DateField()
    customer_name = models.CharField(max_length=100)
    products =  models.TextField()
    total_price = models.DecimalField(max_digits=8,decimal_places=2)
    payment_method = models.CharField(max_length=50)