import csv

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomerForm, UploadFileForm
from .models import Customer


def paginate(request, customers):
    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def customers_list(request):
    customers = Customer.objects.order_by('-pub_date')
    page_obj = paginate(request, customers)
    template = 'customers/customers_list.html'
    title = 'Список клиентов'
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def customers_detail(request, pk):
    template = 'customers/customers_detail.html'
    title = 'Карточка клиента'
    context = {
        'title': title,
        'text': f'Карточка клиента №{pk}',
    }
    return render(request, template, context)


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


class NewCustomerView(CreateView):
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:customers_list')


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
