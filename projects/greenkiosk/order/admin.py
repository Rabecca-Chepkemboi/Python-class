from django.contrib import admin
from.models import Order

# Register your models here.
class OrderAdmin (admin.ModelAdmin):
    list_display = ("order_id", "name", "ordered_items", "total_cost", "delivery_address", "delivery_date", "status")

admin.site.register(Order, OrderAdmin) 
