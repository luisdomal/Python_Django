"""Heroes app admin config"""

from django.contrib import admin

from .models import Hero

admin.site.register(Hero)