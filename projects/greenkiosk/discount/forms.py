from django import forms
from .models import Discount

class UploadDiscountForm(forms.ModelForm):
    class Meta:
        model=Discount
        fields="__all__"