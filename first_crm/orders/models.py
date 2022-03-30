from django.db import models
from customers.models import Customer
from products.models import Product


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
