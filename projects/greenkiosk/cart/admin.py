from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("price", "item_name", "quantity", "total_price", "item_id")

admin.site.register(Cart, CartAdmin)
