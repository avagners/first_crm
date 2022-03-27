from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def customers_list(request):
    return HttpResponse('Список клиентов')


def customers_detail(request, pk):
    return HttpResponse(f'Клиент номер {pk}')
