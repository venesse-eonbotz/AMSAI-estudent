from django import forms
from .models import Soa


class FileForm(forms.ModelForm):
    class Meta:
        model= Soa
        fields= ["soano", "file"]