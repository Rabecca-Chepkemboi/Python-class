from django.shortcuts import render
from payment.models import Payment
from django.shortcuts import redirect
from .forms import UploadPaymentForm

# Create your views here.

def uploadpayment(request):
    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        form = UploadPaymentForm()
        return render(request,"payment/payment_upload.html",{"form":form})