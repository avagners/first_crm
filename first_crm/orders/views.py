from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import OrderForm
from .models import Order


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


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(
        request.POST or None,
        files=request.FILES or None,
        instance=order
    )
    if form.is_valid():
        form.save()
        return redirect('orders:orders_list')
    context = {
        'form': form,
        'order': order}
    return render(request, 'orders/order_form.html', context)


class NewOrderView(CreateView):
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('orders:orders_list')
