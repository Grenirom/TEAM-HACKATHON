from django.db import models
from django.contrib.auth.models import User

from hackathon import settings


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True, default='No title')
    # category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images/', blank=True, default='default-image.jpg')
    desc = models.TextField(blank=True)
    price = models.SmallIntegerField(null=True)



# поля модели Product






