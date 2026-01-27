from django.shortcuts import render
from .models import Product

# Create your views here.


def list_display(request):
    products = Product.objects.all()

    return render(
        request, "shop/products.html",
        {"products": products})
