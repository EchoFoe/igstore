from django.shortcuts import render, get_object_or_404
from .models import RepairCategory, Repair, RepairDetail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Обработчик страницы по ремонту с фильтрацией по категориям:
def repair_list(request, category_slug=None):
    category = None
    categories = RepairCategory.objects.all()
    object_list = Repair.objects.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(RepairCategory, slug=category_slug)
        object_list = object_list.filter(category=category)
    paginator = Paginator(object_list, 42)
    page = request.GET.get('page')
    try:
        repairs = paginator.page(page)
    except PageNotAnInteger:
        repairs = paginator.page(1)
    except EmptyPage:
        repairs = paginator.page(paginator.num_pages)
    return render(request, 'repair/repair_list.html', {'category': category,
                                                       'categories': categories,
                                                       'page': page,
                                                       'repairs': repairs,
                                                       })


# Обработчик страницы услуг по ремонту с его подробным описанием:
def repair_detail(request, id, slug, category_slug=None):
    category = None
    categories = RepairCategory.objects.all()
    repair = get_object_or_404(Repair, id=id, slug=slug, is_active=True)
    repairs = Repair.objects.filter(is_active=True)
    repairs_details = RepairDetail.objects.filter(is_active=True, repair__is_active=True)
    if category_slug:
        category = get_object_or_404(RepairCategory, slug=category_slug)
        repairs = repairs.filter(category=category)
    return render(request, 'repair/repair_detail.html', {'repair': repair,
                                                         'repairs': repairs,
                                                         'categories': categories,
                                                         'repairs_details': repairs_details,
                                                         'category': category,
                                                         })
