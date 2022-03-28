from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'core/index.html'
    title = 'Первая CRM'
    context = {
        'title': title,
        'text': 'Главная страница'
    }
    return render(request, template, context)


def customers_list(request):
    return HttpResponse('Список клиентов')


def customers_detail(request, pk):
    return HttpResponse(f'Клиент номер {pk}')
