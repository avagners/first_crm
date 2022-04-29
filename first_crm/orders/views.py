from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import Order


def paginate(request, orders):
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required
def orders_list(request):
    template = 'orders/orders_list.html'
    title = 'Список заказов'
    orders = Order.objects.order_by('-pay_date')
    page_obj = paginate(request, orders)
    context = {
        'title': title,
        'text': 'Заказы',
        'page_obj': page_obj
    }
    return render(request, template, context)


@login_required
def orders_detail(request, pk):
    template = 'orders/orders_detail.html'
    title = 'Карточка заказа'
    context = {
        'title': title,
        'text': f'Заказ №{pk}',
    }
    return render(request, template, context)


@login_required
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
        'order': order
    }
    return render(request, 'orders/order_form.html', context)


@login_required
def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders:orders_list')
    return render(request, 'orders/order_form.html', {'form': form})
