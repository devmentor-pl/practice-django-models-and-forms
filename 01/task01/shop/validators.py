from django.core.exceptions import ValidationError


def price_validator(value):
    if value < 0:
        raise ValidationError("Cena nie może być mniejsza niż 0")
