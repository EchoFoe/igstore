from django.shortcuts import render
from products.models import ProductCategory, Product, ProductDetail
from instagram.models import ImageItem
from reviews.models import Review


def home(request):
    # Категории:
    category = None
    categories = ProductCategory.objects.filter(available=True, is_active=True)
    # Фотографии инстаграм:
    instagram = ImageItem.objects.filter(is_active=True)[0:6]
    # Отзывы:
    all_reviews = Review.objects.filter(is_active=True)
    # Товары:
    products = Product.objects.filter(available=True, is_active=True)[0:64]
    # Товары хиты продаж:
    hot_sales_products = Product.objects.filter(available=True, is_active=True, hot_sales=True)[0:32]
    # Товары нового поступления:
    new_products = Product.objects.filter(available=True, is_active=True, as_new=True)[0:32]
    return render(request, 'home/home.html', {'category': category,
                                              'categories': categories,
                                              'instagram': instagram,
                                              'all_reviews': all_reviews,
                                              'products': products,
                                              'hot_sales_products': hot_sales_products,
                                              'new_products': new_products,
                                              })
