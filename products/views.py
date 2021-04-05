from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view to return all products
    """
    template = 'products/all.html'
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, template, context)
