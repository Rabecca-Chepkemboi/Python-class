from django.contrib import admin
from.models import Stock

# Register your models here.
class StockAdmin (admin.ModelAdmin):
    list_display = ("product_id", "product_name", "price", "quantity", "category", "store_name", "store_location")

admin.site.register(Stock, StockAdmin) 
