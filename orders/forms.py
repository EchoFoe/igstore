from django import forms
from .models import Order


# Форма создания заказа:
class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    postal_code = forms.CharField(required=False)
    city = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone']
        exclude = ['created', 'updated']
