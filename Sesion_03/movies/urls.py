"""Movies app URls"""

from django.urls import path

from .views import list_movies, add_movie

app_name = 'movies'
urlpatterns = [
    path("", list_movies, name="list"),
    path("add", add_movie, name="add"),
]