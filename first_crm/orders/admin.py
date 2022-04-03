from django.contrib import admin

from .models import Order


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pay_date', 'customer', 'product', 'total_cost', 'comments'
    )
    search_fields = ('customer', 'product')
    list_filter = ('pay_date',)
    empty_value_display = '-пусто-'


admin.site.register(Order, OrdersAdmin)
