from django import forms
from .models import Order


# Форма создания заявки на ремонт:
class RepairCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False)
    phone = forms.CharField(required=True)
    description = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'description']
        exclude = ['created', 'updated']
