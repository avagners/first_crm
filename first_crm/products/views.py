import csv

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ProductForm, UploadFileForm
from .models import Product


def paginate(request, products):
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def products_list(request):
    template = 'products/products_list.html'
    title = 'Список услуг'
    products = Product.objects.all()
    page_obj = paginate(request, products)
    context = {
        'title': title,
        'text': 'Услуги',
        'page_obj': page_obj
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


def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        status, created = Product.objects.update_or_create(
            name_product=row['Наименование услуги'],
            description=row['Описание'],
            price=row['Цена']
        )


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse_lazy('products:products_list'))
    else:
        form = UploadFileForm()
    return render(request, 'products/upload.html', {'form': form})
