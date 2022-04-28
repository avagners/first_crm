from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from customers.models import Customer

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

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='Man_X')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_unexisting_page(self):
        """Запрос к несуществующей странице вернёт ошибку 404."""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_urls_httpstatus_for_authorized_client(self):
        """Страницы доступны авторизованному автору"""
        urls_list = [
            '/customers/',
            f'/customers/{self.customer.pk}/',
            '/customers/new_customer/',
            f'/customers/{self.customer.pk}/edit/',
            '/customers/upload_file/'
        ]
        for url in urls_list:
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirects_for_guest_user(self):
        """Проверяем редиректы для неавторизованного автора"""
        dict_url_redirect = {
            '/customers/': reverse('users:login') + '?next='
            + reverse('customers:customers_list'),
            f'/customers/{self.customer.pk}/':
            reverse('users:login') + '?next='
            + reverse('customers:customers_detail', args=[self.customer.pk]),
            f'/customers/{self.customer.pk}/edit/':
            reverse('users:login') + '?next=' + reverse(
                'customers:customer_edit', args=[self.customer.pk]
            ),
            '/customers/new_customer/': reverse('users:login') + '?next='
            + reverse('customers:new_customer')
        }
        for url, redirect in dict_url_redirect.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertRedirects(response, redirect)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/customers/': 'customers/customers_list.html',
            f'/customers/{self.customer.pk}/': 'customers/customers_detail.html',
            f'/customers/{self.customer.pk}/edit/': 'customers/customer_form.html',
            '/customers/new_customer/': 'customers/customer_form.html',
            '/customers/upload_file/': 'customers/upload.html'
        }
        for template, adress in templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(template)
                self.assertTemplateUsed(response, adress)
