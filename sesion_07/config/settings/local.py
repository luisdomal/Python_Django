"""Development settings"""

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-pbhb_fp_cdvw9^kfxzrs!mhp=y3g9_!wvbqb!kg3450qt-7g0$'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media files

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Django extensions

INSTALLED_APPS += ['django_extensions']
