from django.shortcuts import render


def index(request):
    template = 'core/index.html'
    title = 'Первая CRM - Главная страница'
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context)
