from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomerForm
from .models import Customer


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
