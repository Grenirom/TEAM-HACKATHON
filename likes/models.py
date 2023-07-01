from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey('account.CustomAccount', related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'product']
