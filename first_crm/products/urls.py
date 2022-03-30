from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list),
    path('<int:pk>/', views.products_detail),
]
