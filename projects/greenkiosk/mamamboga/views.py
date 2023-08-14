from django.shortcuts import render
from mamamboga.models import MamaMboga
from .forms import UploadMamaMbogaForm
from  django.shortcuts import redirect

# Create your views here.
def upload_mamamboga(request):
    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        form=UploadMamaMbogaForm()
    return render(request,"mamamboga/mamamboga_upload.html",{"form":form})