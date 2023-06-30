from django.db import models
from django.contrib.auth.models import User
from hackathon import settings


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    # category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images/', default='default-image.jpg')
    desc = models.TextField()
    price = models.SmallIntegerField(null=True)


