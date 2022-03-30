from django.shortcuts import render


def customers_list(request):
    template = 'customers/customers_list.html'
    title = 'Список клиентов'
    context = {
        'title': title,
        'text': 'Список клиентов',
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
