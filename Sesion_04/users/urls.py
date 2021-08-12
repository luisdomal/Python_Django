"""Users app URLS"""

from django.urls import path
from .views import users_login
from django.views.generic.base import TemplateView


app_name = "users"
urlpatterns = [
    path("login", users_login, name="login"),
    path("home", TemplateView.as_view(template_name='home.html'), name='home')
]