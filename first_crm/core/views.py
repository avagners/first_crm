from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    template = 'core/index.html'
    title = 'Первая CRM - Главная страница'
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context)
