from django.shortcuts import render
from .forms import UploadClientForm
from client.models import Client
from django.shortcuts import redirect

# Create your views here.

def upload_client(request):
    if request.method=="POST":
        form=UploadClientForm(request.POST,request.Files)
        if form.is_valid():
            forms.save()
    else:
        form = UploadClientForm()
        return render(request,"client/client_upload.html",{"form":form})