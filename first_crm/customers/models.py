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
        max_length=16,
        verbose_name='Телефон',
        unique=True
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата',)
    status = models.BooleanField(default=True, verbose_name='Статус')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-id']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
