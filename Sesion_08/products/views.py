"""Products app views"""

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Product
from .helpers import stripe


class ProductListView(ListView):
    """Show all products"""
    template_name = "products/list.html"
    queryset = Product.objects.all().order_by("name")


class ProductCreateView(CreateView):
    """Create a product"""
    template_name = "products/create.html"
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("products:list")


def checkout(request, pk):
    """A view for pay a product"""
    product = get_object_or_404(Product, pk=pk)
    checkout_price = stripe.checkout(product.price)
    return render(request, "products/checkout.html", {"checkout_price": checkout_price})
