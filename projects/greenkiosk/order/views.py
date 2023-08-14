from django.shortcuts import render
from order.models import Order
from django.shortcuts import redirect
from .forms import UploadOrderForm

# Create your views here.

def upload_order(request):
    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        form=UploadOrderForm()
    return render(request,"order/order_upload.html",{"form":form})
