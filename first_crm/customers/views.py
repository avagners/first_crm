from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'customers/index.html'
    return render(request, template)


def customers_list(request):
    return HttpResponse('Список клиентов')


def customers_detail(request, pk):
    return HttpResponse(f'Клиент номер {pk}')
