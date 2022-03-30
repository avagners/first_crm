from django.shortcuts import render
from .models import Product


def products_list(request):
    template = 'orders/orders_list.html'
    title = 'Список услуг'
    context = {
        'title': title,
        'text': 'Услуги',
    }
    return render(request, template, context)


def products_detail(request, pk):
    template = 'orders/orders_detail.html'
    product = Product.objects.get(pk=pk)
    title = 'Карточка услуги'
    context = {
        'title': title,
        'text': product.name_product,
    }
    return render(request, template, context)
