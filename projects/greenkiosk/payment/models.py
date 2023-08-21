from django.db import models

# Create your models here.
class Payment(models.Model):
   transaction_id = models.AutoField(primary_key=True)
   amount = models.DecimalField(max_digits=8, decimal_places=2)  
   date = models.DateTimeField()  
   payment_method = models.CharField(max_length=50)
   status = models.CharField(max_length=20)
   currency = models.CharField(max_length=100)
