from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta: 
        model = Service
        fields = ['name', 'service_type', 'price']
        labels = {
            'name': 'Service name',
            'price': 'Price (£)'
        }

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

