from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


def products_list(request):
    template = 'products/products_list.html'
    title = 'Список услуг'
    products = Product.objects.all()
    context = {
        'title': title,
        'text': 'Услуги',
        'products': products
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


class NewProductView(CreateView):
    form_class = ProductForm
    template_name = 'products/new_product_form.html'
    success_url = reverse_lazy('products:products_list')
