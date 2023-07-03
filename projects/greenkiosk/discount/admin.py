from django.contrib import admin
from.models import Discount

# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ("discount", "name", "items_bought", "active", "date")

admin.site.register(Discount, DiscountAdmin)    