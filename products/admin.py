from django.contrib import admin
import mptt.admin
from django_summernote.admin import SummernoteModelAdmin
from products.models import ProductCategory, ProductStatus, Product, ProductDetail


# Детали продукции (встроенная таблица):
class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 0


# MPTT кастомизация категории товаров:
admin.site.register(ProductCategory, mptt.admin.DraggableMPTTAdmin,
                    list_display=('tree_actions', 'indented_title', 'name', 'parent', 'available', 'is_active'),
                    list_display_links=('indented_title',),
                    list_filter=(('parent', mptt.admin.TreeRelatedFieldListFilter),),
                    list_editable=('available', 'is_active'),
                    prepopulated_fields={'slug': ('name', )},
                    readonly_field=('created', 'updated'),
                    )


# Таблица кастомизации статуса товаров:
@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'available', 'is_active', ('created', 'updated')]
    list_display = ['name', 'available', 'is_active']
    search_fields = ['name']
    list_editable = ['available', 'is_active']
    list_filter = ['available', 'is_active', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


# Таблица кастомизации продукции:
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [ProductDetailInline]
    fields = ['category', ('name', 'slug'), ('code', 'vendor_code'), 'memory',
              'status', ('hot_deal', 'as_new', 'recommended', 'hot_sales'), ('price', 'discount'),
              'image', 'description', 'available', 'is_active', ('created', 'updated')]
    # summernote_fields = ('description',)
    filter_horizontal = ['category']
    list_display = ['name', 'code', 'price', 'available',
                    'is_active', 'memory', 'as_new', 'hot_sales', 'recommended', 'hot_deal']
    search_fields = ['name', 'code']
    list_editable = ['price', 'available', 'is_active', 'memory', 'hot_deal', 'as_new',
                     'recommended', 'hot_sales']
    list_filter = ['category', 'available', 'memory', 'is_active', 'as_new',
                   'hot_sales', 'recommended', 'hot_deal', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',), 'vendor_code': ('code',)}
    date_hierarchy = 'created'


# Таблица кастомизации деталей к продукции:
@admin.register(ProductDetail)
class PromotionDetailsAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['product', 'image', ('is_main', 'is_not_main'), ('created', 'updated')]
    list_display = ['product', 'is_main', 'is_not_main']
    list_filter = ['product', 'is_main', 'is_not_main']
    list_editable = ['is_main', 'is_not_main']
    readonly_fields = ['created', 'updated']
