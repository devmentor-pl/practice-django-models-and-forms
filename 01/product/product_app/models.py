from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.TextField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    in_stock = models.BooleanField(default=True)
    available_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.price}'


# Create your models here.
