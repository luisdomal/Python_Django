"""Music app URls"""

from django.urls import path

from .views import list_songs, create_song, song_detail, division_by_zero

app_name = 'music'
urlpatterns = [
    path("", list_songs, name="list"),  # music:list
    path("create", create_song, name="create"),  # music:create
    path("detail/<int:pk>", song_detail, name="detail"),  # music:detail
    path("error", division_by_zero, name="division_by_zero"),  # music:division_by_zero
]
