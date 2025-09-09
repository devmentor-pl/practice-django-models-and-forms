from django.db import models


class Product(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField()

    def __str__(self):
        return f'{self.name}, {self.price}, {self.in_stock}'

# Create your models here.
