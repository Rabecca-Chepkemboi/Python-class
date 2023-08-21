from django.urls import path
from .views import upload_shipping
from django.conf import settings

urlpatterns=[
    path("shipping/upload",upload_shipping,name="shipping_upload_view"),
]