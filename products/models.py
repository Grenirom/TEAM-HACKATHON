from django.db import models
from django.contrib.auth.models import User
from hackathon import settings


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True, default='no title was added')
    # category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images/', default='default-image.jpg')
    desc = models.TextField(null=True)
    price = models.SmallIntegerField(null=True)
