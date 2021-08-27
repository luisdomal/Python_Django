"""Products app admin site config"""

from django.contrib import admin

from .models import Product

admin.site.register(Product)
