"""Products app tests for helpers"""

from unittest import TestCase, mock

from ..helpers.stripe import checkout


class StripeHelperTestCase(TestCase):
    """Test stripe module"""

    @mock.patch("products.helpers.stripe.print")
    def test_checkout(self, mock_print):
        """Test that checkout works"""
        result = checkout(20)

        mock_print.assert_called_once_with("PROCESSING WITH STRIPE")
        self.assertEqual(result, 30)
