from django.shortcuts import render
from discount.models import Discount
from django.shortcuts import redirect
from .forms import UploadDiscountForm
from django.contrib import messages

# Create your views here.
def upload_discount(request):
    form = None  

    if request.method == "POST":
        form = UploadDiscountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Discount uploaded successfully!')
            return redirect('discount_upload_view')
    else:
        form = UploadDiscountForm()
        return render(request, "discount/discount_upload.html", {"form": form})
    
