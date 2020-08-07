from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=50, verbose_name='Е-мейл')
    phone = models.CharField(max_length=50, default=None, verbose_name='Номер телефона')
    description = models.TextField(max_length=256, blank=True, verbose_name='Описание проблемы')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return 'Обращение {}'.format(self.last_name)


class Contact(models.Model):
    name = models.CharField(max_length=512, db_index=True, verbose_name='Название магазина')
    phone_1 = models.CharField(max_length=50, default=None, verbose_name='Номер телефона 1')
    phone_2 = models.CharField(max_length=50, default=None, blank=True, verbose_name='Номер телефона 2')
    email_1 = models.EmailField(max_length=50, verbose_name='Е-мейл 1')
    email_2 = models.EmailField(max_length=50, blank=True, verbose_name='Е-мейл 2')
    address_1 = models.CharField(max_length=256, verbose_name='Адрес 1')
    address_2 = models.CharField(max_length=256, blank=True, verbose_name='Адрес 2')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return '%s' % self.name
