"""Production settings"""

from .base import *

import os

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = ['deploy-dw-pt-21-01.herokuapp.com',]

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# Database

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Settings

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True

# Django Storages

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = os.getenv("DROPBOX_OAUTH2_TOKEN")


# Sentry

sentry_sdk.init(
    dsn="https://63282604b6264ae59ef748079bdb39d0@o973476.ingest.sentry.io/5924985",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
