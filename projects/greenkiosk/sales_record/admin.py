from django.contrib import admin
from.models import Sales

# Register your models here.
class SalesAdmin(admin.ModelAdmin):
    list_display = ("sales_id", "date", "customer_name", "products", "total_price", "payment_method")

admin.site.register(Sales, SalesAdmin)    
 
 