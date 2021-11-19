from django import forms
from .models import csvmodel

class csvModelForm(forms.ModelForm):
    class Meta: 
        model = csvmodel
        fields = "__all__"