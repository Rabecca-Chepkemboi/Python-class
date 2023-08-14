from django.urls import path
from .views import upload_mamamboga
from django.conf import settings

urlpatterns=[
    path("mamamboga/upload",upload_mamamboga,name="mamamboga_upload_view")
]