from django.db import models

from account.models import CustomAccount
from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=150)
    creator = models.ForeignKey(CustomAccount, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='images/default-image.jpg')
    desc = models.TextField()
    price = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title}'
