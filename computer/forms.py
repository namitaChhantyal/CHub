from django import forms
from django.forms import ModelForm
from computer.models import Computer

class ComputerForm(ModelForm):
    class Meta:
        model=Computer
        fields=('computercode','brandname','quantity','unitrate','computer')

        widgets = {
            'computercode': forms.NumberInput(attrs={'class': 'form-control'}),
            'brandname': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unitrate': forms.NumberInput(attrs={'class': 'form-control'}),  
        }
    