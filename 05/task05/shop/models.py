from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def price_validator(value):
    if value < 0:
        raise ValidationError("Cena nie może być mniejsza niż 0")


class Product(models.Model):
    name = models.TextField(null=False)
    price = models.FloatField(null=False, validators=[price_validator])
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
