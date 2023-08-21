from django.urls import path
from .views import upload_reviews
from django.conf import settings

urlpatterns=[
    path("reviews/upload",upload_reviews,name="reviews_upload_view"),
]