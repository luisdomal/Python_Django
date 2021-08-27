"""Products app models tests"""

from django.test import TestCase

from products.models import Product


# 1. Unitarias: Prueban unidades
# 2. Integración: Prueban cómo se integran los componentes
# 3. End-to-End: Prueban el comportamiento completo de la aplicación


# Test-driven development
# 1. Crear la prueba
# 2. Correrla y esperar que falle
# 3. Crear el código
# 4. Esperar que pase

# TransactionTestCase: Por cada prueba mata la base de datos y vuelve a crear todas las tablas
# TestCase: Va a crear todas las tablas al principio, y por cada prueba va a hacer un rollback de la transacción


class ProductModelTestCase(TestCase):

    def test_product_description_can_be_blank(self):
        """Test that product has a description even if is not speecified"""
        description = "Un pan"
        product = Product.objects.create(name="Pan", price=2.50, description=description)
        self.assertEqual(product.description, description)

        product = Product.objects.create(name="Leche", price=9.50)
        self.assertEqual(product.description, "A product")

    def test_product_str_method(self):
        """Test that product has a proper __str__ method"""
        product = Product.objects.create(name="Pan", price=2.50)
        self.assertEqual(str(product), "Pan")
