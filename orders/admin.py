from django.contrib import admin
from .models import Order, OrderItem


# Лот товаров (встроенная таблица):
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


# Таблица кастомизации заказа:
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('first_name', 'last_name'), ('email', 'phone'), 'address',
              ('postal_code', 'city'), 'paid', 'description', 'created', 'updated']
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated']
    search_fields = ['id', 'first_name', 'last_name']
    list_editable = ['paid']
    list_filter = ['paid', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    inlines = [OrderItemInline]
    date_hierarchy = 'created'
