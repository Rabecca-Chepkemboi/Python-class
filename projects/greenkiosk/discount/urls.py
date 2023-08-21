from django.urls import path
from .views import upload_discount
from django.conf import settings

urlpatterns=[
    path("discount/upload",upload_discount,name="discount_upload_view"),
]