from django.db import models
from django.contrib.auth.models import User
from hackathon import settings


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=150, unique=True)
    # category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images/', default='default-image.jpg')
    desc = models.TextField()
    price = models.SmallIntegerField(null=True)


