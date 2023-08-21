from django.shortcuts import render
from vendor.models import Vendor
from django.shortcuts import redirect
from .forms import UploadVendorForm
from django.contrib import messages

# Create your views here.
def upload_vendor(request):
    form = None  

    if request.method == "POST":
        form = UploadVendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor uploaded successfully!')
            return redirect('vendor_upload_view')
    else:
        form = UploadVendorForm()
        return render(request, "vendor/vendor_upload.html", {"form": form})