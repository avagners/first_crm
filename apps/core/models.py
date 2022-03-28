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
    email = models.EmailField(max_length=254, blank=True, unique=True)
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Телефон',
        unique=True
    )
