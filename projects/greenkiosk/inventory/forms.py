from django import forms
from.models import Productclass ProductUploadForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= "__all__"