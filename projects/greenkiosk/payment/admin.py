from django.contrib import admin
from.models import Payment

# Register your models here.
class PaymentAdmin (admin.ModelAdmin):
    list_display = ("transaction_id", "amount", "date", "payment_method", "status", "currency")

admin.site.register(Payment, PaymentAdmin) 
