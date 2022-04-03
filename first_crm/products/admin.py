from django.contrib import admin

from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'description')
    search_fields = ('name_product',)
    list_filter = ('name_product',)
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductsAdmin)
