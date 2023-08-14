from django.urls import path
from .views import upload_order
from django.conf import settings

urlpatterns=[
    path("order/upload",upload_order,name="order_upload_view"),
]