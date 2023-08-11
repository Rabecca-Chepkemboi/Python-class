from django.shortcuts import render
from.forms import ProductUploadForm
from .models import Product

# from.views import products_upload_view


# Create your views here.
# Create your views here.def product_upload_view(request):

def product_upload_view(request):
    form =ProductUploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})

def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html",{"products": products})    

def product_detail_view(request, id):
    product = Product.objects.get(id = id)
    return render(request, "inventory/product_details.html", {"product: product"})




# def products_list(request):
#     products = Product.objects.all()
#     return render(request, "inventory/product_list.html", {"products":products})

# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     return render(request, "inventory/product_description.html", {"product":product})    