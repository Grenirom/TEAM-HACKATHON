from django.db import models

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey('account.CustomAccount', on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.SmallIntegerField()

