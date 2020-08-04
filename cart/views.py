from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product, ProductCategory
from .cart import Cart
from .forms import CartAddProductForm


# Обработчик добавления товара в корзину:
# Нужно обернуть декоратором функцию cart_add, чтобы обращаться можно было методом POST
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    # Принимаем объект товара по аргументу ID:
    product = get_object_or_404(Product, id=product_id)
    # Создается форма из form.py:
    form = CartAddProductForm(request.POST)
    # Если форма валидна:
    if form.is_valid():
        cd = form.cleaned_data
        # Добавляем товар или обновляем:
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    # Перенаправляем пользователя на URL детали корзины покупок:
    return redirect('cart:cart_detail')


# Обработчик удаления товара из корзины покупок:
def cart_remove(request, product_id):
    cart = Cart(request)
    # Принимаем объект товара по аргументу ID:
    product = get_object_or_404(Product, id=product_id)
    # Удаление товара из корзины покупок:
    cart.remove(product)
    # Перенаправляем пользователя на URL детали корзины покупок:
    return redirect('cart:cart_detail')


# Эта функция отображает данные списка товаров из request.session, добавленных в корзину:
def cart_detail(request):
    # Товары нового поступления:
    new_products = Product.objects.filter(available=True, is_active=True, as_new=True)[0:32]
    categories = ProductCategory.objects.all()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    # coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/cart_detail.html', {'cart': cart,
                                                     'categories': categories,
                                                     'new_products': new_products,
                                                     })
