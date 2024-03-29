import csv

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm, UploadFileForm
from .models import Customer
from orders.models import Order


def paginate(request, customers):
    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required
def customers_list(request):
    sort = request.GET.getlist('sort')
    if sort:
        customers = Customer.objects.get_queryset().order_by(*sort)
    else:
        customers = Customer.objects.all()
    page_obj = paginate(request, customers)
    template = 'customers/customers_list.html'
    title = 'Список клиентов'
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def customers_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    order_history = Order.objects.filter(customer=customer)
    template = 'customers/customers_detail.html'
    title = 'Карточка клиента'
    context = {
        'title': title,
        'text': f'Карточка клиента №{pk}',
        'customer': customer,
        'order_history': order_history
    }
    return render(request, template, context)


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(
        request.POST or None,
        files=request.FILES or None,
        instance=customer
    )
    if form.is_valid():
        form.save()
        return redirect('customers:customers_list')
    context = {
        'form': form,
        'customer': customer}
    return render(request, 'customers/customer_form.html', context)


@login_required
def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customers:customers_list')
    return render(request, 'customers/customer_form.html', {'form': form})


def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        status, created = Customer.objects.update_or_create(
            last_name=row['Фамилия'],
            first_name=row['Имя'],
            email=row['email'],
            phone_number=row['Телефон']
        )


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(
                reverse_lazy('customers:customers_list')
            )
    else:
        form = UploadFileForm()
    return render(request, 'customers/upload.html', {'form': form})
