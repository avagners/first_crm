from django.db import models


class Customer(models.Model):
    first_name = models.TextField(max_length=150)
    last_name = models.TextField(max_length=150)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.TextField(max_length=15)
