from django.core.exceptions import ValidationError


def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError("Wartość musi być większa od zera.")
