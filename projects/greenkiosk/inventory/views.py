from django.shortcuts import render,redirect
from inventory.models import Product
from .forms import ProductUploadForm

def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm()
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html",{"form": form})


def products_list_view(request):
    products = Product.objects.all()
    return render(request,"inventory/products_list.html",{"products":products})


def product_detail_view(request,id):
    product = Product.objects.get(id = id)
    return render(request,"inventory/product_detail.html",{"product":product})




def product_update_view(request,id):
    product= Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
        return redirect("product_detail_view",id=product.id)
    else:
        form = ProductUploadForm(instance=product)
        return render(request,"inventory/edit_products.html",{"form":form})
        

def product_delete(request, id):
    product = Product.objects.get(id=id)    
    if request.method == "POST":
        product.delete()
        return redirect("products_list_view")    
    return render(request,"inventory/confirmation_page.html", {"product": product})


def edit_product_view(request,id):
    product = Product.objects.get(id = id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST,instance=product)
        if form.is_valid:
            form.save()
            return redirect("product_detail_view",id = product.id)

    else:
        form = ProductUploadForm(instance=product)
    return render(request,"inventory/edit_product.html",{"form":form})

