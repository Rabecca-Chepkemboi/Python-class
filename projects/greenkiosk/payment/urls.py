from django.urls import path
from .views import upload_payment
from django.conf import settings

urlpatterns=[
    path("payment/upload",upload_payment,name="payment_upload_view"),
]