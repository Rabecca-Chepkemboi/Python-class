from django.urls import path
from .views import upload_vendor
from django.conf import settings

urlpatterns=[
    path("vendor/upload",upload_vendor,name="vendor_upload_view"),
]