from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders_list),
    path('<int:pk>/', views.orders_detail),
]
