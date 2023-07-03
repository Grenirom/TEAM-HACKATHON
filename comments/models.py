from django.contrib.auth import get_user_model
from django.db import models

from hackathon import settings
from products.models import Product


User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    content = models.TextField()





