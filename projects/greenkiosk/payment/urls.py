from django.urls import path
from .views import uploadpayment
from django.conf import settings

urlpatterns=[
    path("payment/upload",uploadpayment,name="payment_upload_view")
]