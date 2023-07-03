from django.contrib import admin
from.models import Shipping

# Register your models here.

class ShippingAdmin(admin. ModelAdmin):
    list_display = ("name", "address", "city", "state", "phone_number", "created_at", "updated_at")

admin.site.register(Shipping, ShippingAdmin)    
