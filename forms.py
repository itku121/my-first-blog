# forms.py
from django import forms
from .models import *

class ObrazekForm(forms.ModelForm):

    class Meta:
        model = Obrazek
        fields = ['name', 'obrazek_Image'] 
