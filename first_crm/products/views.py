from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
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
    template = 'products/products_detail.html'
    product = Product.objects.get(pk=pk)
    title = 'Карточка услуги'
    context = {
        'title': title,
        'text': product.name_product,
    }
    return render(request, template, context)


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
        instance=product
    )
    if form.is_valid():
        form.save()
        return redirect('products:products_list')
    context = {
        'form': form,
        'product': product}
    return render(request, 'products/product_form.html', context)


class NewProductView(CreateView):
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:products_list')
