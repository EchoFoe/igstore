from django.db import models
from django.template.defaultfilters import truncatechars
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Категории товаров:
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=512, db_index=True, verbose_name='Подкатегория товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Уникальная строка')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Категория товара')
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True, verbose_name='Обложка категории')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    available = models.BooleanField(default=True, verbose_name='Наличие в магазине')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('products:products_list_by_category', args=[self.slug])


# Статус товаров:
class ProductStatus(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name='Статус товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Уникальная строка')
    available = models.BooleanField(default=True, verbose_name='Наличие в магазине')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    class Meta:
        verbose_name = 'Статус товара'
        verbose_name_plural = 'Статус товаров'

    def __str__(self):
        return '%s' % self.name


# Товары:
class Product(models.Model):
    # category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE,
    #                              verbose_name='Категория товара')
    category = TreeManyToManyField(ProductCategory, blank=True, symmetrical=False, related_name='products',
                                   verbose_name='Категория')
    status = models.ForeignKey(ProductStatus, default=None, null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='Статус')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Уникальная строка')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    code = models.CharField(max_length=6, db_index=True, default=None, blank=True, verbose_name='Код товара',
                            help_text='Код товара должен быть 6-значным')
    vendor_code = models.CharField(max_length=6, db_index=True, blank=True, default=None, verbose_name='Артикул')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=None, null=True,
                                   blank=True, verbose_name='Скидка на товар в %')
    memory = models.IntegerField(default=None, null=True, blank=True, verbose_name='Память уст-ва',
                                 help_text='Память устройства в Гб')
    image = models.ImageField(upload_to='product_covers/%Y/%m/%d', blank=True, verbose_name='Обложка товара')
    hot_deal = models.BooleanField(default=None, verbose_name='Товар спец. предложения')
    hot_sales = models.BooleanField(default=None, verbose_name='Хит продаж')
    as_new = models.BooleanField(default=None, verbose_name='Новое поступление')
    recommended = models.BooleanField(default=None, verbose_name='Рекомендуемые магазином')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('-created', 'name', '-memory')
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])


# Фотографии товаров:
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                verbose_name='Товар')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Основная фотография')
    is_not_main = models.BooleanField(default=False, verbose_name='Доп. фотография')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.product

    class Meta:
        verbose_name = 'Подробная информация к товару'
        verbose_name_plural = 'Подробная информация к товарам'
