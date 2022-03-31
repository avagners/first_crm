from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm


def customers_list(request):
    customers = Customer.objects.order_by('-pub_date')[:10]
    template = 'customers/customers_list.html'
    title = 'Список клиентов'
    context = {
        'title': title,
        'customers': customers
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


class NewCustomerView(CreateView):
    form_class = CustomerForm
    template_name = 'customers/new_customer_form.html'
    success_url = reverse_lazy('customers:customers_list')
