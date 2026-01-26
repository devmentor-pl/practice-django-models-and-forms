from django.db import models
from .validators import price_validator
# Create your models here.


class Product(models.Model):
    name = models.TextField(blank=False, null=False)
    price = models.FloatField(validators=[price_validator])
    in_stock = models.BooleanField(default=True)
    available_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
