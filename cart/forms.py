from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 1000)]


# Форма добавления товара в корзину покупателем:
class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
