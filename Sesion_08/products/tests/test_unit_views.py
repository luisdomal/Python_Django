"""Unit test product app views"""

from unittest import mock

from django.urls import reverse
from django.test import SimpleTestCase, RequestFactory

from ..models import Product
from ..views import checkout


class ProductsUnitViewsTestCase(SimpleTestCase):
    """Unit tests for product views"""

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    @mock.patch("products.views.get_object_or_404")
    @mock.patch("products.views.stripe")
    def test_checkout(self, mock_stripe, mock_get_object_or_404):
        """Test checkout view"""
        product = mock.Mock()
        product.pk = 1
        mock_get_object_or_404.return_value = product

        checkout_price = 10.99
        mock_stripe.checkout.return_value = checkout_price

        checkout_url = reverse("products:checkout", args=[product.pk])
        request = self.factory.get(checkout_url)
        response = checkout(request, product.pk)

        mock_get_object_or_404.assert_called_once_with(Product, pk=product.pk)
        mock_stripe.checkout.assert_called_once_with(product.price)
        self.assertContains(response, f"Debes pagar ${checkout_price}")
