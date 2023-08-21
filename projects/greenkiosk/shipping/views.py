from django.shortcuts import render
from shipping.models import Shipping
from django.shortcuts import redirect
from .forms import UploadShippingForm
from django.contrib import messages

# Create your views here.
def upload_shipping(request):
    form = None  

    if request.method == "POST":
        form = UploadShippingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shipping uploaded successfully!')
            return redirect('shipping_upload_view')
    else:
        form = UploadShippingForm()
        return render(request, "shipping/shipping_upload.html", {"form": form})
    
    
