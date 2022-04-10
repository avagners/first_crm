import csv

from django.core.management.base import BaseCommand
from products.models import Product
from customers.models import Customer
from orders.models import Order


class Command(BaseCommand):
    """
    Команда 'import_csv' загружает тестовые данные в базу из csv файлов,
    которые располагаются в директории /static/data/
    """
    def handle(self, *args, **options):
        self.import_products()
        self.import_customers()
        self.import_orders()
        print('Загрузка тестовых данных завершена.')

    def import_products(self, file='products.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Product.objects.update_or_create(
                    name_product=row['Наименование услуги'],
                    description=row['Описание'],
                    price=row['Цена']
                )

    def import_customers(self, file='customers.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Customer.objects.update_or_create(
                    last_name=row['Фамилия'],
                    first_name=row['Имя'],
                    email=row['email'],
                    phone_number=row['Телефон']
                )

    def import_orders(self, file='orders.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Order.objects.update_or_create(
                    customer_id=row['id_клиента'],
                    product_id=row['id_услуги'],
                    total_cost=row['Стоимость'],
                    comments=row['Комметарий']
                )
