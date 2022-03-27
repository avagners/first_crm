from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def customers_list(request):
    return HttpResponse('Список клиентов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def customers_detail(request, pk):
    return HttpResponse(f'Клиент номер {pk}')
