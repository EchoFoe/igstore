from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from repairs.models import RepairCategory, Repair, RepairDetail


# Детали продукции (встроенная таблица):
class RepairDetailInline(admin.TabularInline):
    model = RepairDetail
    raw_id_fields = ['repair']
    extra = 0


# Таблица кастомизации категории устройств по ремонту:
@admin.register(RepairCategory)
class RepairCategoryAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'is_active', ('created', 'updated')]
    list_display = ['name', 'is_active']
    search_fields = ['name']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


# Таблица кастомизации продукции:
@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [RepairDetailInline]
    fields = ['category', ('name', 'slug'), 'image', 'description', 'is_active', ('created', 'updated')]
    # summernote_fields = ('description',)
    list_display = ['name', 'category', 'is_active', 'created', 'updated']
    search_fields = ['name']
    list_editable = ['category', 'is_active']
    list_filter = ['category', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'


# Таблица кастомизации услуг по ремонту:
@admin.register(RepairDetail)
class RepairDetailsAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['repair', 'name', 'price', 'is_active', ('created', 'updated')]
    list_display = ['repair', 'name', 'price', 'is_active', 'created', 'updated']
    list_filter = ['repair', 'is_active']
    list_editable = ['is_active', 'price']
    readonly_fields = ['created', 'updated']
    date_hierarchy = 'created'
