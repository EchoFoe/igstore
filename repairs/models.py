from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Категории устройств для услуг по ремонту:
class RepairCategory(models.Model):
    name = models.CharField(max_length=512, db_index=True, verbose_name='Подкатегория товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Уникальная строка')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        verbose_name = 'Категория устройств для услуг по ремонту'
        verbose_name_plural = 'Категории устройств для услуг по ремонту'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('repairs:repairs_list_by_category', args=[self.slug])


# Услуги по ремонту:
class Repair(models.Model):
    category = models.ForeignKey(RepairCategory, related_name='repairs', on_delete=models.CASCADE,
                                 verbose_name='Категория устройств')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование устройства',
                            help_text='Полная марка устройства')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Уникальная строка')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='repair_covers/%Y/%m/%d', blank=True, verbose_name='Обложка устройства')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('-created', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Ремонтируемое устройство'
        verbose_name_plural = 'Ремонтируемые устройства'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('repairs:repair_detail', args=[self.id, self.slug])


# Услуги, оказываемые для данного устройства:
class RepairDetail(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE,
                               verbose_name='Наименование устройства')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование услуги')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена за услугу')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.repair

    class Meta:
        verbose_name = 'Услуга по ремонту устройства'
        verbose_name_plural = 'Услуги по ремонту устройств'
