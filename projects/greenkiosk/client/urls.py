from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_client

urlpatterns=[
    path("client/upload",upload_client, name="clientuploadview"),
 
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)