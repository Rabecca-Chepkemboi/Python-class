from django import forms
from .models import Vendor

class UploadVendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields="__all__"