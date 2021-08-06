"""Music app URls"""

from django.urls import path

from .views import list_songs, create_song

app_name = 'music'
urlpatterns = [
    path("", list_songs, name="list"),
    path("create", create_song, name="create"),
]