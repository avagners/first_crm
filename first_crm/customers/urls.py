from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customers_list, name='customers_list'),
    path('<int:pk>/', views.customers_detail,
         name='customers_detail'),
    path('new_customer/', views.NewCustomerView.as_view(),
         name='new_customer'),
    path('<int:pk>/edit/', views.customer_edit, name='customer_edit'),
]
