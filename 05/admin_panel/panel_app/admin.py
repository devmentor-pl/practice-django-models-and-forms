from django.contrib import admin
from .models import Product
from decimal import Decimal


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
                    'in_stock']

    def in_stock(self, obj):
        return "Dostępna" if obj.is_available else "Brak w magazynie"
    in_stock.short_description = "Dostępność"

    @admin.action(description='Obniz cene o 10 procent')
    def discount_10_percent(self, request, queryset):
        for product in queryset:
            product.price = product.price * Decimal('0.9')
            product.save()

    actions = ['discount_10_percent']

# Register your models here.
