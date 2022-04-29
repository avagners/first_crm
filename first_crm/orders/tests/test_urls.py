from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from orders.models import Order
from customers.models import Customer
from products.models import Product

User = get_user_model()


class CustomersURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.customer = Customer.objects.create(
            first_name='Анастасия',
            last_name='Иванова',
            phone_number='+19001111223'
        )
        cls.order = Order.objects.create(
            customer=cls.customer,
            product=Product.objects.create(name_product='Услуга1'),
            total_cost=1500
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='Man_X')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_httpstatus_for_authorized_client(self):
        """Страницы '/orders/' доступны авторизованному автору"""
        urls_list = [
            '/orders/',
            f'/orders/{self.order.pk}/',
            '/orders/new_order/',
            f'/orders/{self.order.pk}/edit/',
        ]
        for url in urls_list:
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirects_for_guest_user(self):
        """Проверяем редиректы для неавторизованного автора"""
        dict_url_redirect = {
            '/orders/': reverse('users:login') + '?next='
            + reverse('orders:orders_list'),
            f'/orders/{self.order.pk}/': reverse('users:login') + '?next='
            + reverse('orders:orders_detail', args=[self.order.pk]),
            f'/orders/{self.order.pk}/edit/': reverse('users:login') + '?next='
            + reverse('orders:order_edit', args=[self.order.pk]),
            '/orders/new_order/': reverse('users:login') + '?next='
            + reverse('orders:new_order'),
        }
        for url, redirect in dict_url_redirect.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertRedirects(response, redirect)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/orders/': 'orders/orders_list.html',
            f'/orders/{self.order.pk}/': 'orders/orders_detail.html',
            f'/orders/{self.order.pk}/edit/': 'orders/order_form.html',
            '/orders/new_order/': 'orders/order_form.html',
        }
        for template, adress in templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(template)
                self.assertTemplateUsed(response, adress)
