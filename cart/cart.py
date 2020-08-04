from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):
    # Инициализация объекта корзины:
    def __init__(self, request):
        self.session = request.session
        # Получаем данные корзины:
        cart = self.session.get(settings.CART_SESSION_ID)
        # Если не получаем объект корзины, то создаем пустой словарь в сессии:
        if not cart:
            # Сохраняем в сессии пустую корзину (СЛОВАРЬ)
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину или обновление его количества:
    def add(self, product, quantity=1, update_quantity=False):
        # product_id использует ID товара как ключ в словаре корзины, но нужно преобразовать его в строку,
        # потому что для сериализации данных в сессии Django юзает формат JSON (а в JSON ключи могут быть только СТРОКИ)
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Помечаем сессию как измененную:
    def save(self):
        # Если данные сессии редактировлись, то нужно сохранить с помощью атрибута modified:
        self.session.modified = True

    # Удаление товара из корзины покупок и сохранение изменений:
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Проходим (цикл) по товарам корзины и получаем соответствующие объекты товаров Product:
    def __iter__(self):
        product_ids = self.cart.keys()
        # Получаем объекты модели Product и передаем их в корзину:
        products = Product.objects.filter(id__in=product_ids)
        # Создается копия объекта корзины покупок:
        cart = self.cart.copy()
        # Далее получаем данные товаров, которые лежат в корзине:
        for product in products:
            cart[str(product.id)]['product'] = product
        # Для каждого товара преобразуем цену из строки в Decimal с фиксированной точностью:
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            # Вычисляется общая стоимость с учетом товара и количества, вложенного в форму:
            item['total_price'] = item['price'] * item['quantity']
            # Yield — это ключевое слово которое используется так же, как и return, но функция при этом возвращает генератор вместо значения:
            yield item

    # Для адекватного отображения корзины выводим кол-во товаров в корзине:
    def __len__(self):
        # Возвращает общее количество товаров в корзине:
        return sum(item['quantity'] for item in self.cart.values())

    # Функция вычисления ОБЩЕЙ СТОИМОСТИ КОРЗИНЫ (цена * количество):
    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    # Функция очищения корзины (полезная на самом деле функция):
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
