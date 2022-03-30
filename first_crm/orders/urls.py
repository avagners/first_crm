from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_list),
    path('<int:pk>/', views.orders_detail),
]
