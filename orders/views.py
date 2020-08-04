from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .task import order_created
from products.models import ProductCategory
from utils.emails import SendingEmail


# Обработчик будет получать данные из запроса, инициировать, валидировать форму и создавать заказ:
def order_create(request):
    # Категории:
    category = None
    categories = ProductCategory.objects.filter(available=True, is_active=True)
    # Получаем объект корзины:
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Записываем данные в БД
            order = form.save()
            # Проходим по всем товарам корзины и создаем для каждого объект OrderItem:
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            email = SendingEmail()
            email.sending_email(type_id=1, order=order)
            email.sending_email(type_id=2, email=order.email, order=order)
            # Очищаем форму из сессии и формируем ответ на страницу order_created:
            cart.clear()
            # Вызов запуска асинхронной задачи:
            # order_created.delay(order.id)
            return render(request, 'orders/order_created.html', {'order': order,
                                                                 'category': category,
                                                                 'categories': categories,
                                                                 })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'cart': cart,
                                                        'form': form,
                                                        'category': category,
                                                        'categories': categories,
                                                        })
