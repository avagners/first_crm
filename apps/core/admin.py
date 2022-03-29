from django.contrib import admin

from .models import Customer, Product, Order


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone_number')
    search_fields = ('last_name', 'phone_number')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'description')
    search_fields = ('name_product',)
    list_filter = ('name_product',)
    empty_value_display = '-пусто-'


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pay_date', 'customer', 'product', 'total_cost', 'comments'
    )
    search_fields = ('customer', 'product')
    list_filter = ('pay_date',)
    empty_value_display = '-пусто-'


admin.site.register(Customer, CustomersAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Order, OrdersAdmin)
