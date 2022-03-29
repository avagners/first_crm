from django.db import models


class Customer(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=254,
        blank=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Телефон',
        unique=True
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Product(models.Model):
    name_product = models.CharField(
        max_length=254,
        verbose_name='Наименование услуги'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание услуги'
    )
    price = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name_product


class Order(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID заказа')
    pay_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        related_name='orders'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Услуга',
        related_name='orders'
    )
    total_cost = models.IntegerField(
        null=True,
        verbose_name='Стоимость'
    )
    comments = models.TextField(
        blank=True,
        verbose_name='Комментарии'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
