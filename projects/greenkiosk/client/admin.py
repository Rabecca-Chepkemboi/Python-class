from django.contrib import admin
from.models import Client

# Register your models here.
class ClientAdmin (admin.ModelAdmin):
    list_display = ("customer_id", "name", "phone_number", "email", "loyalty_points")

admin.site.register(Client, ClientAdmin)
