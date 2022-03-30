from django.shortcuts import render


def index(request):
    template = 'customers/index.html'
    return render(request, template)
