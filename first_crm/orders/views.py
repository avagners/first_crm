from django.shortcuts import render


def orders_list(request):
    template = 'orders/orders_list.html'
    title = 'Список заказов'
    context = {
        'title': title,
        'text': 'Заказы',
    }
    return render(request, template, context)


def orders_detail(request, pk):
    template = 'orders/orders_detail.html'
    title = 'Карточка заказа'
    context = {
        'title': title,
        'text': f'Заказ №{pk}',
    }
    return render(request, template, context)
