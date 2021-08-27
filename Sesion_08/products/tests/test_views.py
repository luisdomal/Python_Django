"""Test views from products app"""

from django.test import TestCase, Client
from django.urls import reverse

from ..models import Product


class ProductViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_product_list_view(self):
        Product.objects.create(name="Pizza", price=5)
        Product.objects.create(name="Leche", price=7)

        url = reverse("products:list")
        response = self.client.get(url)

        self.assertContains(response, f"Pizza - $5")
        self.assertContains(response, f"Leche - $7")

    def test_product_create_view(self):
        product_count = Product.objects.count()
        self.assertEqual(product_count, 0)

        name = "Cheetos"
        description = "Una bolsa de Cheetos"
        price = 9.99

        body = {
            "name": name,
            "description": description,
            "price": price
        }

        url = reverse("products:create")
        response = self.client.post(url, body, follow=True)

        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

        product = Product.objects.first()
        self.assertEqual(product.name, name)
        self.assertEqual(product.description, description)
        self.assertEqual(float(product.price), price)

        self.assertContains(response, f"{name} - ${price}")
