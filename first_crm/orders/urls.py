from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('<int:pk>/', views.orders_detail, name='orders_detail'),
    path('new_order/', views.NewOrderView.as_view(), name='new_order'),
    path('<int:pk>/edit/', views.order_edit, name='order_edit'),
]
