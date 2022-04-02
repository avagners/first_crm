from django.shortcuts import render
from .models import Order
from django.urls import reverse_lazy
from .forms import OrderForm
from django.views.generic.edit import CreateView


def orders_list(request):
    template = 'orders/orders_list.html'
    title = 'Список заказов'
    orders = Order.objects.order_by('-pay_date')
    context = {
        'title': title,
        'text': 'Заказы',
        'orders': orders
    }
    return render(request, template, context)


def orders_detail(request, pk):
    template = 'orders/orders_detail.html'
    title = 'Карточка заказа'
    context = {
        'title': title,
        'text': f'Заказ №{pk}',
    }
    return render(request, template, context)


class NewOrderView(CreateView):
    form_class = OrderForm
    template_name = 'orders/new_order_form.html'
    success_url = reverse_lazy('orders:orders_list')
