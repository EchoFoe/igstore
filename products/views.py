from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product, ProductDetail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm


# Обработчик категорий и сабкатегорий товаров (в набаре):
def category_menu(request):
    category = None
    categories = ProductCategory.objects.filter(available=True, is_active=True)
    return render(request, 'navbar/navbar.html', {'category': category,
                                                  'categories': categories,
                                                  })


# Обработчик категорий и сабкатегорий товаров (в набаре):
def category_footer(request):
    category = None
    categories = ProductCategory.objects.filter(available=True, is_active=True)
    return render(request, 'footer/footer.html', {'category': category,
                                                  'categories': categories,
                                                  })


# Обработчик страницы товаров с фильтрацией по категориям
def product_list(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.filter(available=True, is_active=True)
    object_list = Product.objects.filter(available=True, is_active=True)
    recommended_products = Product.objects.filter(available=True, is_active=True, recommended=True)[0:32]
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        object_list = object_list.filter(category=category)
    paginator = Paginator(object_list, 42)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product_list.html', {'category': category,
                                                      'categories': categories,
                                                      'page': page,
                                                      'products': products,
                                                      'recommended_products': recommended_products,
                                                      })


# Обработчик страницы товара с его подробным описанием
def product_detail(request, id, slug, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.filter(available=True)
    products_images = ProductDetail.objects.filter(is_not_main=True, product__available=True)
    # Товары специального предложения:
    special_products = Product.objects.filter(available=True, is_active=True, hot_deal=True)[0:32]
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product_detail.html', {'product': product,
                                                        'products': products,
                                                        'categories': categories,
                                                        'products_images': products_images,
                                                        'category': category,
                                                        'special_products': special_products,
                                                        'cart_product_form': cart_product_form,
                                                        })
