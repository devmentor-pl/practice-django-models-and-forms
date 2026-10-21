from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} – {self.price}"
