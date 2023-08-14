from django.db import models

# Create your models here.
class Cart(models.Model):
    item_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    item_name = models.CharField(max_length=40)
    quantity = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=5, decimal_places=1)
    date_added = models.DateField()
    product_image = models.ImageField(upload_to='cart_images/',null=True)
