from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('customers/', views.customers_list),
    path('customers/<int:pk>/', views.customers_detail),
]
