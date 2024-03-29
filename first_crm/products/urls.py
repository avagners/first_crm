from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<int:pk>/', views.products_detail, name='products_detail'),
    path('new_product/', views.NewProductView.as_view(), name='new_product'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('upload_file/', views.upload_file, name='upload_file'),
]
