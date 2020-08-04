from django.db import models
from django.utils import timezone
from products.models import Product, ProductCategory
from django.db.models.signals import post_save
from utils.main import disable_for_loaddata


# Модель для сведений об покупаемых товарах:
class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя покупатея')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия покупателя')
    email = models.EmailField(max_length=50, verbose_name='Е-мейл покупателя')
    phone = models.CharField(max_length=50, default=None, verbose_name='Номер телефона покупателя')
    address = models.CharField(max_length=256, verbose_name='Адрес покупателя')
    postal_code = models.CharField(max_length=9, blank=True, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    paid = models.BooleanField(default=False, verbose_name='Заказ оплачен')
    description = models.TextField(max_length=256, blank=True, verbose_name='Пожелание к заказу')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return 'Заказ № {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


@disable_for_loaddata
def order_post_save(sender, instance, created, **kwargs):
    pass


post_save.connect(order_post_save, sender=Order)


# Модель для связи заказа с покупаемым товаром с указаниями их стоимости и количества:
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Лот заказа'
        verbose_name_plural = 'Лот заказа'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


@disable_for_loaddata
def order_item_post_save(sender, instance, created, **kwargs):

    order = instance.order
    all_orders_item = OrderItem.objects.filter(order=order)


post_save.connect(order_item_post_save, sender=OrderItem)
