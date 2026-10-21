from decimal import Decimal
from django.contrib import admin
from .models import Product


@admin.action(description="Obniż cenę o 10%%")
def discount_10_percent(modeladmin, request, queryset):
    for product in queryset:
        product.price = round(product.price * Decimal("0.9"), 2)
        product.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    actions = [discount_10_percent]
