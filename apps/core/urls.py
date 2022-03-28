from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('customers/', views.customers_list, name='customers_list'),
    path('customers/<int:pk>/', views.customers_detail,
         name='customers_detail'),
]
