from django import forms
from .models import Order


# Форма создания заявки:
class ContactCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    description = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'description']
        exclude = ['created', 'updated']
