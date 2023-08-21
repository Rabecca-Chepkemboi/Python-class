from django.shortcuts import render
from payment.models import Payment
from django.shortcuts import redirect
from .forms import UploadPaymentForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def upload_payment(request):
   

    if request.method == "POST":
        form = UploadPaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment uploaded successfully!')
            return redirect('vendor_upload_view')
    else:
        form = UploadPaymentForm()
        return render(request, "payment/payment_upload.html", {"form": form})





