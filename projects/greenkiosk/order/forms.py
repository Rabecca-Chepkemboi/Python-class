from django import forms
from .models import Order

class UploadOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"