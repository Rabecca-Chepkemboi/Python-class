from django import forms
from .models import MamaMboga

class UploadMamaMbogaForm(forms.ModelForm):
    class Meta:
        model=MamaMboga
        fields= "__all__"