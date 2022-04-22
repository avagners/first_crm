from django.db import models


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
        ordering = ['id']

    def __str__(self):
        return self.name_product
