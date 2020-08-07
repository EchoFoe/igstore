from django.shortcuts import render, get_object_or_404
from .models import RepairCategory, Repair, RepairDetail
from .forms import RepairCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.emails import SendingRepairEmail
from products.models import ProductCategory


# Обработчик категорий для ремонта (в набаре):
def r_category_menu(request):
    r_category = None
    r_categories = RepairCategory.objects.filter(is_active=True)
    return render(request, 'navbar/navbar.html', {'r_category': r_category,
                                                  'r_categories': r_categories,
                                                  })


# Обработчик категорий для ремонта (в футере):
def r_category_footer(request):
    r_category = None
    r_categories = RepairCategory.objects.filter(is_active=True)
    return render(request, 'footer/footer.html', {'r_category': r_category,
                                                  'r_categories': r_categories,
                                                  })


# Обработчик страницы по ремонту с фильтрацией по категориям:
def repair_list(request, r_category_slug=None):
    # Вывод категорий магазина для покупок смартфонов:
    category = None
    categories = ProductCategory.objects.all()
    # Вывод категорий для устройств по услуге ромента:
    r_category = None
    r_categories = RepairCategory.objects.all()
    object_list = Repair.objects.filter(is_active=True)
    if r_category_slug:
        r_category = get_object_or_404(RepairCategory, slug=r_category_slug)
        object_list = object_list.filter(category=r_category)
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
                                                       'r_category': r_category,
                                                       'r_categories': r_categories,
                                                       'page': page,
                                                       'repairs': repairs,
                                                       })


# Обработчик страницы услуг по ремонту с его подробным описанием:
def repair_detail(request, id, slug, r_category_slug=None):
    # Вывод категорий магазина для покупок смартфонов:
    category = None
    categories = ProductCategory.objects.all()
    # Вывод категорий для устройств по услуге ромента:
    r_category = None
    r_categories = RepairCategory.objects.all()
    repair = get_object_or_404(Repair, id=id, slug=slug, is_active=True)
    repairs = Repair.objects.filter(is_active=True)
    repairs_details = RepairDetail.objects.filter(is_active=True, repair__is_active=True)
    if r_category_slug:
        r_category = get_object_or_404(RepairCategory, slug=r_category_slug)
        repairs = repairs.filter(category=r_category)
    if request.method == 'POST':
        form = RepairCreateForm(request.POST)
        if form.is_valid():
            # Записываем данные в БД
            order = form.save()
            email = SendingRepairEmail()
            email.sending_email(type_id=1, order=order)
            email.sending_email(type_id=2, email=order.email, order=order)
            return render(request, 'repair/repair_created.html', {'order': order,
                                                                  'category': category,
                                                                  'categories': categories,
                                                                  'r_category': r_category,
                                                                  'r_categories': r_categories,
                                                                  })
    else:
        form = RepairCreateForm()
    return render(request, 'repair/repair_detail.html', {'repair': repair,
                                                         'repairs': repairs,
                                                         'categories': categories,
                                                         'repairs_details': repairs_details,
                                                         'category': category,
                                                         'r_category': r_category,
                                                         'r_categories': r_categories,
                                                         'form': form,
                                                         })
