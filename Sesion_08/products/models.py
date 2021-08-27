"""Products app models"""

from django.db import models


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="A product")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """Return product name"""
        return self.name
