import csv

from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    """
    Команда 'import_csv' загружает тестовые данные в базу из csv файлов,
    которые располагаются в директории /static/data/
    """
    def handle(self, *args, **options):
        self.import_titles()
        print('Загрузка тестовых данных завершена.')

    def import_titles(self, file='products.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(reader)
                status, created = Product.objects.update_or_create(
                    name_product=row['name_product'],
                    description=row['description'],
                    price=row['price']
                )
