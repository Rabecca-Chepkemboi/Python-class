from django.shortcuts import render
from order.models import Order
from django.shortcuts import redirect
from .forms import UploadOrderForm
from django.contrib import messages

# Create your views here.
def upload_order(request):
    form = None  

    if request.method == "POST":
        form = UploadOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order uploaded successfully!')
            return redirect('order_upload_view')
    else:
        form = UploadOrderForm()
        return render(request, "order/order_upload.html", {"form": form})
    
    