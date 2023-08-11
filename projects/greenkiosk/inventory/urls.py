
from django.urls import path
from .views import product_upload
from .views import product_list
from .views import product_details

urlpatterns=[
    path("products/upload/",product_upload,name = "product_uploadview"),
    path("products/list/", products_list,name = "products_list"),
    path("products/<int:id>", product_details,name = "product_detail"),
]

# urlpatterns=[
#     path("products/upload/",product_upload_view, name="product_upload_view"),    
#     path("products/list/", products_list, name="product_list_view"),    
#     path("products/<int:id>/", product_detail, name="product_description_view"),
# ]