from django.urls import path
from.views import product_upload_view
from.views import products_list_view
from.views import product_detail_view
from.views import edit_product_view
from.views import product_delete

# from.views import product_update_view


urlpatterns=[
    path("product/upload/",product_upload_view,name="product_upload_view"),
    path("products/list/",products_list_view,name="products_list_view"),
    path("product/detail<int:id>/",product_detail_view,name="product_detail_view"),
    path("product/edit/<int:id>/", edit_product_view, name="edit_product_view"),
    path("products/delete/<int:id>/",product_delete,name="product_delete"),

    # path("product/update",product_update_view, name = "product_update_view"),

]