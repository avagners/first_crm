from django.shortcuts import render
from .models import Customer


def customers_list(request):
    customers = Customer.objects.order_by('-pub_date')[:10]
    template = 'customers/customers_list.html'
    title = 'Список клиентов'
    context = {
        'title': title,
        'customers': customers
    }
    return render(request, template, context)


def customers_detail(request, pk):
    template = 'customers/customers_detail.html'
    title = 'Карточка клиента'
    context = {
        'title': title,
        'text': f'Карточка клиента №{pk}',
    }
    return render(request, template, context)
