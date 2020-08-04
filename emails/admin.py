from django.contrib import admin
from .models import EmailType, EmailSendingFact


@admin.register(EmailType)
class EmailTypeAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['name', 'is_active', 'created', 'updated']
    list_display = ['name', 'is_active', 'created', 'updated']
    list_filter = ['is_active']
    readonly_fields = ['created', 'updated']


@admin.register(EmailSendingFact)
class EmailSendingFactAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('order', 'email'), 'type', ('created', 'updated')]
    list_display = ['order', 'email', 'type']
    list_filter = ['email', 'type__name']
    search_fields = ['email', 'type__name']
    readonly_fields = ['created', 'updated']
