from django.contrib import admin

from .models import Customer


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone_number',
                    'pub_date', 'status')
    search_fields = ('last_name', 'phone_number')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Customer, CustomersAdmin)
