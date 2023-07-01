from django.db import models

from hackathon import settings
from products.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite_product')

    class Meta:
        unique_together = ['user', 'product']
