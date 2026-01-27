from django.contrib import admin
from .models import Product
from django.db.models import F


def discount_10_percent(modeladmin, request, queryset):
    queryset.update(price=F("price") * 0.9)


discount_10_percent.short_description = "Przecena o 10 procent"


def raise_10_percent(modeladmin, request, queryset):
    queryset.update(price=F("price") * 1.1)


raise_10_percent.short_description = "Podniesienie ceny o 10 procent"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    actions = [discount_10_percent, raise_10_percent]