from django.contrib import admin
from instagram.models import ImageItem


# Таблица кастомизации инстаграма:
@admin.register(ImageItem)
class ImageItemAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['image', 'is_active', ('created', 'updated')]
    list_display = ['id', 'image', 'is_active', 'created']
    list_editable = ['is_active']
    list_filter = ['is_active']
    readonly_fields = ['created', 'updated']
