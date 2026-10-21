from django.db import models
from .validators import validate_greater_than_zero


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        validators=[validate_greater_than_zero]
    )
    in_stock = models.BooleanField(default=True)
    available_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price} zł"
