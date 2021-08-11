"""Users app URLS"""

from django.urls import path

from .views import users_login


app_name = "users"
urlpatterns = [
    path("login", users_login, name="login"),
]