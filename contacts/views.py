from django.shortcuts import render
from .models import Contact
from .forms import ContactCreateForm
from products.models import ProductCategory


# Обработчик страницы "контакты":
def contact(request):
    # Вывод категорий магазина для покупок смартфонов:
    category = None
    categories = ProductCategory.objects.all()
    contacts = Contact.objects.filter(is_active=True)
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            # Записываем данные в БД
            order = form.save()
            return render(request, 'contacts/contact_created.html', {'category': category,
                                                                     'categories': categories,
                                                                     'order': order,
                                                                     'contacts': contacts,
                                                                     })
    else:
        form = ContactCreateForm()
    return render(request, 'contacts/contacts.html', {'categories': categories,
                                                      'category': category,
                                                      'form': form,
                                                      'contacts': contacts,
                                                      })
