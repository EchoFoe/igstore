from django.contrib import admin
from .models import Order, Contact


# Таблица кастомизации заказа на ремонт устройства:
@admin.register(Order)
class ContactOrderAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('first_name', 'last_name'), ('email', 'phone'), 'description', ('created', 'updated')]
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'created', 'updated']
    search_fields = ['first_name', 'phone', 'last_name']
    list_filter = ['created', 'updated']
    readonly_fields = ['created', 'updated']
    date_hierarchy = 'created'


# Таблица кастомизации контактов:
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['name', ('phone_1', 'phone_2'), ('email_1', 'email_2'), ('address_1', 'address_2'), ('created', 'updated')]
    list_display = ['name', 'phone_1', 'phone_2', 'email_1', 'email_2', 'address_1', 'address_2', 'created', 'updated']
    readonly_fields = ['created', 'updated']
