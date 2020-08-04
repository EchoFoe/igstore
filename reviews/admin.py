from django.contrib import admin
from reviews.models import Review


# Таблица кастомизации инстаграма:
@admin.register(Review)
class ImageItemAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['first_name', 'last_name', 'message', 'image', 'is_active', ('created', 'updated')]
    list_display = ['first_name', 'last_name', 'is_active', 'created']
    list_editable = ['is_active']
    list_filter = ['is_active']
    readonly_fields = ['created', 'updated']
